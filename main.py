

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
    # time.sleep(2)
    doc = browser.find_element_by_name('Submit')
    doc.click()
    page_source = browser.page_source
    # time.sleep(500)
    try:
        soup = BeautifulSoup(page_source, 'html.parser')
        print(soup.prettify())
        # reviews = []
        # reviews_selector = soup.find_all('div', class_='reviewSelector')
        # for review_selector in reviews_selector:
        #     review_div = review_selector.find('div', class_='dyn_full_review')
        #     if review_div is None:
        #         review_div = review_selector.find('div', class_='basic_review')
        #     review = review_div.find('div', class_='entry').find('p').get_text()
        #     review = review.strip()
        #     reviews.append(review)

    except Exception as e:
        print(e)
        browser.quit()

if __name__ == '__main__':
    url = "https://ec.europa.eu/growth/tools-databases/cosing/index.cfm?fuseaction=search.simple"#"http://example.com"
    # open_web_page_bs4(url)
    open_page_selenium(url)

