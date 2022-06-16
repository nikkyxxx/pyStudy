import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import lxml


def get_source_html(url):
    driver = webdriver.Chrome(
        executable_path=r"D:\project\pythonStudy\Chrome\chromedriver.exe"
    )
    driver.maximize_window()
    try:
        driver.get(url=url)
        driver.implicitly_wait(5)
        with open(f"source.html", "w", encoding="utf-8") as file:
            file.write(driver.page_source)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


def get_items(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")
    items = soup.find_all("div", class_="start-search")

    for item in items:
        print(item)


def main():
    get_source_html("https://spb.zoon.ru")
    get_items("source.html")


if __name__ == '__main__':
    main()
