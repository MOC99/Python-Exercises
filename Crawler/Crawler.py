import re
import pandas as pd
import requests
from bs4 import BeautifulSoup

shop_goods = {'good_num':[], 'shop_name': [], 'price_old': [], 'price_new': [], 'sale_ticket': []}
headers = {"user-agent": "Mozilla/5.0"}

class getURLdetails():
    def Saleticket(self):
        good_url = self + good_num
        good_geturl = requests.get(good_url, headers=headers)
        good_geturl.encoding = "utf-8"
        soup_good = BeautifulSoup(good_geturl.text, "lxml")
        SaleTicket = soup_good.find("a", class_="title")
        tmp = re.search("https://uland.taobao.com/coupon/edetail\?e=.*?\"", str(SaleTicket))
        print(tmp)
        try:
            tmp = tmp.group()
            tmp1 = tmp[:-1]
            URLData = TranslateDWZ(tmp1)
            if URLData != 1:
                shop_goods['sale_ticket'].append(URLData)
        except Exception as err:
            print(err)
            good_geturl = requests.get(good_url, headers=headers)
            good_geturl.encoding = "utf-8"
            soup_good = BeautifulSoup(good_geturl.text,"lxml")
            SaleTicket = soup_good.find("a", class_="title")
            tmp = re.search("https://uland.taobao.com/coupon/edetail.*?\"", str(SaleTicket))
            print(tmp)
            if tmp == None:
                tmp = re.search("https://s.click.taobao.com/.*?\"",str(SaleTicket))
            
            tmp = tmp.group()
            tmp1 = tmp[:-1]
            URLData = TranslateDWZ(tmp1)
            if URLData != 1:
                shop_goods['sale_ticket'].append(URLData)


def TranslateDWZ(x):        # 短网址转换
    api = "http://dwz.cn/admin/create"
    url_json = {"url": x}
    DWZResponse = requests.post(api, json=url_json)
    if DWZResponse.status_code != 200:
        return 1
    result = DWZResponse.json()
    if result.get("Code") != 0:
        return 1
    else:
        return result.get("ShortUrl")


rul = requests.get("http://www.laoaigou.com/index.php?r=l&cid=8", headers=headers)
rul.encoding = "urf-8"
print(rul.status_code)
soup = BeautifulSoup(rul.text, "lxml")

goods_pattern = soup.find_all('div', 'title')
price_old = soup.find_all('span', 'old-price')
price_new = soup.find_all('span', 'price theme-color-8')

for item in goods_pattern:   # good_num
    print(item.a)
    item_tmp = re.search("1\d{7}", str(item.a))
    good_num = item_tmp.group()
    shop_goods['good_num'].append(good_num)
    good_url = "http://www.laoaigou.com/index.php?r=l/d&id="
    getURLdetails.Saleticket(good_url)

for item in goods_pattern:  # 商品
    item_re = item.a.string
    p = re.compile("^\s+|\s+$")
    item_re1 = re.sub(p, "", item_re)
    shop_goods['shop_name'].append(item_re1)

for item in price_old:  # 优惠前的价格
    item_re = item.contents[1]
    shop_goods['price_old'].append(item_re)

for item in price_new:  # 优惠后的价格
    item_re = item.b.contents[1]
    shop_goods['price_new'].append(item_re)

length = len(goods_pattern)
print(len(shop_goods['sale_ticket']))
goods_data = pd.DataFrame(shop_goods, index=range(1, length+1))
goods_data.to_csv("d://shop_goods.csv", sep=",", header=True, index=True, encoding="utf_8_sig")
goods_data.to_html("d://DHT.html")
