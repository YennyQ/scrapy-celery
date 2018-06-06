from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
from spd import MeijuSpider
from billiard import Process, freeze_support
from celery import Celery

app = Celery('test', broker='amqp://admin:123@abcd@10.10.17.51//')
app.conf.task_default_queue = 'test'

import sys, os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

def a():
    settings = get_project_settings()
    settings.set('ITEM_PIPELINES', {'pipl.MoviePipeline': 100})
    crawler = CrawlerProcess(settings)
    crawler.crawl(MeijuSpider)
    crawler.start()
    crawler.join()


@app.task(name='crawl')
def crawl():
    p = Process(target=a, args=[])
    p.start()
    p.join()


