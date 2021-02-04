
def open_web_page_bs4(url):
    import requests
    from bs4 import BeautifulSoup
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }
    req = requests.get(url, headers) #, headers
    soup = BeautifulSoup(req.content, 'html.parser')
    print(soup.prettify())


def open_page_selenium(url):
    from selenium import webdriver
    from bs4 import BeautifulSoup
    import time

    browser = webdriver.Chrome()
    browser.get(url)
    time.sleep(3)
    doc = browser.find_element_by_name('Submit')
    doc.click()
    page_source = browser.page_source
    time.sleep(1)
    try:
        soup = BeautifulSoup(page_source, 'html.parser')
        print(soup.prettify())

        gdp_table = soup.find("table", attrs={"class": "table-border"})
        gdp_table_data = gdp_table.tbody.find_all("tr")  # contains 2 rows

        # Get all the headings of Lists
        headings = []
        for td in gdp_table_data[0].find_all("td"):
            # remove any newlines and extra spaces from left and right
            headings.append(td.text)
            print(td.text)

        # print(headings)
    except Exception as e:
        print(e)
        browser.quit()


if __name__ == '__main__':
    url = "https://ec.europa.eu/growth/tools-databases/cosing/index.cfm?fuseaction=search.simple"#"http://example.com"
    # open_web_page_bs4(url)
    open_page_selenium(url)

