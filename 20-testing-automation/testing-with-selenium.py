from selenium import webdriver

# firefox_brower = webdriver.Firefox()
# firefox_brower.maximize_window()

chrome_browser = webdriver.Chrome('./chromedriver')
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
# chrome_browser.maximize_window()

# check for text in title
print('Selenium Easy Demo' in chrome_browser.title)

# grab button with classname
show_message_button = chrome_browser.find_element_by_class_name('btn-default')
# print innerHTML of button class
print(show_message_button.get_attribute('innerHTML'))

assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element_by_id('user-message')
user_message.clear()

# inputs message in input field
user_message.send_keys("I'm the king of the world")
# click button
show_message_button.click()

output_message = chrome_browser.find_element_by_id('display')

print("I'm the king of the world" in output_message.text)

# Can use css selectors like .class > #id
sum1 = chrome_browser.find_element_by_css_selector('#sum1')

# close browser
# chrome_browser.close()
# quit all browser windows
# chrome_browser.quit()

# use wait and sleep methods to better emulate humans
chrome_browser.implicitly_wait(10)