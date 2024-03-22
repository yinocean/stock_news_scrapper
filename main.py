import requests
import csv
from datetime import datetime
from bs4 import BeautifulSoup

all_infos = []

class Stock_News_Scrapper():
    def scrape_page(url):
        response = requests.get(url = url, headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
})
        soup = BeautifulSoup(response.content, "html.parser")
        infos = soup.find("div", class_="sub_n_list_cont").find_all("li")

        for info in infos:
            title = info.find("div", class_ = "cluster_text_headline21 t_reduce").text
            article = info.find("div", class_ = "cluster_text_lede21 link_text2").text
            time = info.find("div", class_ = "cluster_text_press21").text
            info_data = {
                "title" : title.replace("\n", ""),
                "article" : article, 
                "time" : time
            }
            all_infos.append(info_data)

        return all_infos
# def get_pages(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, "html.parser")
#     return len(soup.find("div", class_="pagination").find_all("span", class_="page"))

# total_pages = get_pages("https://www.etoday.co.kr/news/section/subsection?MID=1202&page=1")

# for x in range(total_pages):
#     url = f"https://www.etoday.co.kr/news/section/subsection?MID=1202&page={x+1}"
#     print(url)
#     scrape_page(url)


    def save_to_file(all_infos):
        now = ''.join(filter(lambda x: x.isdigit(), str(datetime.now())))
        file = open(file=f"{now}.csv", mode="w", encoding="utf-8")
        writer = csv.writer(file)
        writer.writerow(
            [
            "title"
            "article"
            "time"
            ]
        )
        for info in all_infos:
            writer.writerow(info.values())

        file.close()
if __name__ == "__main__":
    total_pages = Stock_News_Scrapper.scrape_page(
        "https://www.etoday.co.kr/news/section/subsection?MID=1202&page=1")
    
    Stock_News_Scrapper.save_to_file(total_pages)
