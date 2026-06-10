import urllib.request
import urllib.error
import ssl

# Disable SSL certificate verification for simplicity in this example.
# In a production environment, you should properly handle SSL certificates
# and not disable verification globally.
ssl._create_default_https_context = ssl._create_unverified_context

def check_url_status(url):
    """
    Checks the HTTP status of a given URL.
    Returns a tuple (status_code, message) indicating health or broken status.
    """
    try:
        # Attempt to open the URL with a timeout to prevent hanging.
        with urllib.request.urlopen(url, timeout=10) as response:
            # If successful (status 2xx, 3xx), return the status code and 'OK'.
            # This signifies a healthy external dependency for the data pipeline.
            return response.getcode(), "OK"
    except urllib.error.HTTPError as e:
        # Catches HTTP errors (e.g., 404 Not Found, 500 Internal Server Error).
        # These are considered 'broken' URLs, indicating a problem with the external resource.
        return e.code, f"BROKEN (HTTP Error: {e.code})"
    except urllib.error.URLError as e:
        # Catches URL errors (e.g., network issues, invalid domain, connection refused).
        # These also indicate a 'broken' URL dependency that could halt a data pipeline.
        return None, f"BROKEN (URL Error: {e.reason})"
    except Exception as e:
        # Catch any other unexpected errors during the request.
        return None, f"BROKEN (Unexpected Error: {e})"

if __name__ == "__main__":
    # Simulate a list of URLs that a data pipeline might depend on.
    # These could be external APIs, web services, or data sources.
    urls_to_monitor = [
        "https://www.google.com",
        "https://httpbin.org/status/200",  # A known good URL
        "https://httpbin.org/status/404",  # A known broken URL (Not Found)
        "https://httpbin.org/status/500",  # A known broken URL (Server Error)
        "https://this-domain-does-not-exist-12345.com", # A URL that should cause a DNS error
        "https://www.example.com/non-existent-path", # Another 404 example
    ]

    print("--- Data Pipeline URL Health Check ---")
    print("Monitoring the following URLs for broken links:\n")

    for url in urls_to_monitor:
        status_code, message = check_url_status(url)
        # The core of the 'tracker': reporting the status of each URL.
        # This output helps identify which data pipeline dependencies are failing.
        if status_code and 200 <= status_code < 400:
            print(f"[HEALTHY] {url} (Status: {status_code})")
        else:
            print(f"[BROKEN]  {url} ({message})")
    
    print("\n--- Check Complete ---")
    print("Broken URLs indicate potential issues for data pipeline integrity.")
