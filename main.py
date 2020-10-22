from selenium import webdriver
import time

searchQuery = None
website = "https://amazon.com"

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1300,800")
client = webdriver.Chrome("chromedriver.exe", options=options)


def takeQueryInput():
    while True:
        searchQuery = input("Search: ")
        if searchQuery:
            break


# takeQueryInput()
searchQuery = "iphone x"


client.get(website)
# ? Search Field
searchField = client.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
searchField.click()
searchField.send_keys(searchQuery)

# ? Search button
client.find_element_by_xpath('//*[@id="nav-search"]/form/div[2]/div/input').click()

# time.sleep(10)
links = []

for position in range(3, 23):
    try:
        links.append(
            client.find_element_by_xpath(
                f'//*[@id="search"]/div[1]/div[1]/div/span[4]/div[1]/div[3]/div/span/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a/span')
        )

    except:
        try:
            links.append(
                client.find_element_by_xpath(
                    f'//*[@id="search"]/div[1]/div[2]/div/span[4]/div[1]/div[3]/div/span/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a/span'
                )
            )
        except:
            pass

print(links)
