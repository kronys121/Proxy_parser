from bs4 import BeautifulSoup
import requests


proxylist = []


headers = {
    "Accept": "*/*",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}


def hideme():
    url = 'https://hidemy.name/ru/proxy-list/?type=s&anon=4#list'
    req = requests.get(url, headers=headers)
    src = req.text

    soup = BeautifulSoup(src, "lxml")

    proxy = soup.find(class_="table_block").find("tbody")

    for i in proxy.find_all("tr"):
        proxyTemp = i.find_all()
        ip = proxyTemp[0].text
        port = proxyTemp[1].text
        proxylist.append(f'{ip}:{port}')



def write():
    with open("proxy_HTTP.txt","w",encoding="utf-8") as file:
        for i in proxylist:
            file.write(str(i + "\n"))




def main():
    hideme()
    write()
    print("hello")
    print(f"Всего прокси - {len(proxylist)}")

if __name__ == "__main__":
    main()



