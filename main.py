import logging
from WebCrawler import WebCrawler
from CNNContentHandler import CNNContentHandler


logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(message)s',
    level=logging.INFO)

if __name__ == '__main__':
    content_handler = CNNContentHandler()
    _urls = [
                   "https://edition.cnn.com/article/sitemap-2023-01.html",
                #    "https://edition.cnn.com/article/sitemap-2023-02.html",
                #    "https://edition.cnn.com/article/sitemap-2023-03.html",
                #    "https://edition.cnn.com/article/sitemap-2023-04.html",
                #    "https://edition.cnn.com/article/sitemap-2023-05.html",
                #    "https://edition.cnn.com/article/sitemap-2023-06.html",
                #    "https://edition.cnn.com/article/sitemap-2023-07.html",
                #    "https://edition.cnn.com/article/sitemap-2023-08.html",
                #    "https://edition.cnn.com/article/sitemap-2023-09.html",
                #    "https://edition.cnn.com/article/sitemap-2023-10.html",
                #    "https://edition.cnn.com/article/sitemap-2023-11.html",
                #    "https://edition.cnn.com/article/sitemap-2023-12.html",
               ]
    WebCrawler(content_handler,
               urls=_urls,
               stop_depth=1,
               save_file="CNN_Articles.json").run()
