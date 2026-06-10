# Check Data Pipeline URLs

This Python script demonstrates how to create a lean, single-running broken URL tracker for data pipelines. It iterates through a predefined list of URLs, making HTTP requests to each and reporting its status. The script identifies URLs as 'broken' if they return HTTP error codes (4xx, 5xx) or if network/DNS resolution fails, simulating a check for external dependencies that could impact data pipeline integrity.

## Language

`python`

## How to Run

Save the code as `main.py`.
Run from your terminal: `python main.py`

## Original Article

This example accompanies the Turkish article: [Veri Boru Hatları İçin Yalın ve Tekil Çalışan Kırık URL İzleyici Nasıl Oluşturulur?](https://fatihsoysal.com/blog/veri-boru-hatlari-icin-yalin-ve-tekil-calisan-kirik-url-izleyici-nasil-olusturulur/).

## License

MIT — see [LICENSE](LICENSE).
