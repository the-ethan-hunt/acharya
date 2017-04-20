from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request
import pickle
import re
from reverse.items import ReverseItem
name="reverse"
allowed_domains = ["www.gcet.ac.in"]
proflinks = open("proflinks.pkl", 'rb')
start_urls = pickle.dump(proflinks)
items = []
def parse(self, response):
	sel = Selector(response)
	titles = sel.xpath('//*[@id="contents"]/fieldset')
        items = []
        item["link"] = response.url
        item["field"] = titles[2].xpath('.//ul/li/text()').extract()
	header_txt = titles[0].xpath("string((.//table/tr/td[2]))")[0].extract()
        re_dept = re.compile('Professor,[\s\w&]*')
        item["dept"] = re_dept.findall(header_txt)[0].split('\n')[0].lstrip('Professor,').lstrip().rstrip()
	name = str((titles[0].xpath("string((.//table/tr/td[2]//text())[1])").extract())[0])
        item["name"] = name.lstrip().rstrip()
        items.append(item)
	item["image_src"] = "http://gcet.ac.in" + sel.xpath('//table//img/@src').extract_first()
	info_items = titles[1].xpath('//td/text()').extract()
        if "email" in info_items:
            item["email"] = info_items[info_items.index('email')+1].strip().replace(' ', '')
        else:
            item["email"] = ""
	return items
