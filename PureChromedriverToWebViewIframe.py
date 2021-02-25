from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option('androidPackage', 'org.chromium.webview_shell')
options.add_experimental_option('androidActivity', '.WebViewBrowserActivity')
driver = webdriver.Chrome(r'C:\Tools\chromedriver-88.0.4324.96.exe',
                          options=options)
driver.get('https://www.quirksmode.org/iframetest.html')
driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
h1 = driver.find_element_by_tag_name('h1')
assert h1.text == "Test page in iframe"
