from proxy import Proxy
from .basespider import BaseSpider
from scrapy import Selector


class IPJiangXianLiSpider(BaseSpider):
    name = 'ipjiangxinanli'

    def __init__(self, *a, **kwargs):
        super(IPJiangXianLiSpider, self).__init__(*a, **kwargs)
        # self.urls = ['https://ip.jiangxianli.com/?page=1']
        self.urls = [f'https://ip.jiangxianli.com/?page={i}' for i in range(1, 4)]
        self.headers = {
            "Accept": "image / avif, image / webp, image / apng, image / svg + xml, image / *, * / *;q = 0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh - CN, zh; q = 0.9",
            "User-Agent": "Mozilla / 5.0(Windows NT 10.0; Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / "
                          "89.0.4389.90Safari / 537.36 "
        }
        self.init()

    def parse_page(self, response):
        html = Selector(response)
        ip_list = [
            html.xpath(f"/html/body/div[1]/div[2]/div[1]/div[1]/table/tbody/tr[{i}]/td[1]/text()").extract_first()
            for i in range(1, 16)]
        port_list = [
            html.xpath(f"/html/body/div[1]/div[2]/div[1]/div[1]/table/tbody/tr[{i}]/td[2]/text()").extract_first()
            for i in range(1, 16)]
        country_list = [
            html.xpath(f"/html/body/div[1]/div[2]/div[1]/div[1]/table/tbody/tr[{i}]/td[5]/text()").extract_first()
            for i in range(1, 16)]
        anonymity_list = [
            html.xpath(f"/html/body/div[1]/div[2]/div[1]/div[1]/table/tbody/tr[{i}]/td[3]/text()").extract_first()
            for i in range(1, 16)]

        for new_ip, new_port, new_country, new_anonymity in zip(ip_list, port_list, country_list, anonymity_list):
            proxy = Proxy()
            if new_ip is not None:
                proxy.set_value(
                    ip=new_ip,
                    port=new_port,
                    country=new_country,
                    anonymity=new_anonymity,
                    source=self.name
                )
                self.add_proxy(proxy)



if __name__ == '__main__':
    pass
