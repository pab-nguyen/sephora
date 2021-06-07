from selenium import webdriver
from selenium.webdriver.chrome.options import Options

### This is a script for getting the urls of the brand pages at sephora. 
### This should be run first

# Setting up the webdriver with a user agent and attempting to diable pop-ups
opts = Options()
opts.add_argument("user-agent=['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36']")
opts.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=opts)

# start at the page listing brands
start_url = "https://www.sephora.com/brands-list"
driver.get(start_url)

## getting the urls by their xpath
# brands = driver.find_elements_by_xpath('//div//ul/li/a')
brands = driver.find_elements_by_xpath('//a[@data-at="brand_link"]')
brands = [a.get_attribute('href')+'/all' for a in brands]

## saving the urls to a text file
with open('sephora_brand_pages.txt', 'w') as f:
	for url in brands:
		f.write(url+'\n')
f.close()
driver.close()
