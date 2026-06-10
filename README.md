# check-data-pipeline-urls
This Python script demonstrates how to create a lean, single-running broken URL tracker for data pipelines. It iterates through a predefined list of URLs, making HTTP requests to each and reporting its status. The script identifies URLs as 'broken' if they return HTTP error codes (4xx, 5xx) or if network/DNS resolution fails, simulating a check for
