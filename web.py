from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
import time
from googlesearch import search

companies = []
driver = webdriver.Chrome()

def scrape_images_on_page():
    img_elements = driver.find_elements(By.CLASS_NAME, "your-correct-class-name")

    for img in img_elements:
        try:
            img_alt = img.find_element(By.TAG_NAME, "img").get_attribute("alt")
            companies.append(img_alt)
            print(img_alt)
        except StaleElementReferenceException:
            print("StaleElementReferenceException: Element is no longer attached to the DOM.")

url = "https://aws.amazon.com/solutions/case-studies/browse-customer-success-stories/page/{}"
for page_number in range(1, 15):
    driver.get(url.format(page_number))
    time.sleep(5)
    scrape_images_on_page()

driver.quit()

def get_website_link(company):
    try:
        for result in search(f"{company} official website", num=1, stop=1):
            return result
        time.sleep(2)
    except Exception as e:
        print(f"Error: {e}")

    return None

for company in companies:
    website_link = get_website_link(company)
    if website_link:
        print(f"{company}: {website_link}")
    else:
        print(f"Unable to retrieve website link for {company}")
