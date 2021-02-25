from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option('androidPackage', 'org.chromium.webview_shell')
options.add_experimental_option('androidActivity', '.WebViewBrowserActivity')
driver = webdriver.Chrome(r'C:\Tools\chromedriver-83.0.4103.39.exe',
                          options=options)
driver.get('https://en.m.wikipedia.org/wiki/Donner_Pass')
section_0 = driver.find_element_by_id('section_0')
assert section_0.text == "Donner Pass"
