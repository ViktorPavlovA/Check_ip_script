import requests
from bs4 import BeautifulSoup

class my_ip_is:
    def check_ip(self):
        responce = requests.get(link_on_website).text
        bs = BeautifulSoup(responce, 'html.parser')
        block = bs.find("div", id="main")
        # print(block)
        find_block_ip = block.find_all('strong')[0].text
        print(f"Your ip is {find_block_ip}")
if __name__ =='__main__':
    link_on_website = "https://whoer.net/ru"
    x = my_ip_is
    x.check_ip(None)

