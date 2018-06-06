
class MoviePipeline(object):
    def process_item(self, item, spider):
        with open("meiju.txt", 'a', encoding='utf-8') as fp:
            fp.write(item['name'] + '\n')

    def open_spider(self, spider):
        print('Open Spider')