from bs4 import BeautifulSoup
import requests

proxylist = []

headers = {
    "Accept": "*/*",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
}

#Parsing hideme func
def hideme():
    url = "https://hidemy.name/ru/proxy-list/?type=h&anon=34#list"
    urls = ["https://hidemy.name/ru/proxy-list/?type=h&anon=34&start=0#list"]
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.text, "lxml")
    pagination = soup.find("div", class_="pagination")

    urlMax = int(pagination.find_all("li")[-2].find("a")["href"][37:-5])
    for i in range(64, urlMax + 64, 64):
        urls.append(f"https://hidemy.name/ru/proxy-list/?type=h&anon=34&start={i}#list")

    for url in urls:

        req = requests.get(url, headers=headers)
        soup = BeautifulSoup(req.text, "lxml")
        proxy = soup.find(class_="table_block").find("tbody")

        for i in proxy.find_all("tr"):
            proxyTemp = i.find_all()
            ip = proxyTemp[0].text
            port = proxyTemp[1].text
            proxylist.append(f'{ip}:{port}')





#Add and write in .txt file all proxies
def write():
    with open("proxy_HTTP.txt","w",encoding="utf-8") as file:
        for i in proxylist:
            file.write(str(i + "\n"))



#All call func
def main():
    hideme()
    write()
    print(f"Всего прокси - {len(proxylist)}")

if __name__ == "__main__":
    main()



