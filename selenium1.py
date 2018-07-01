# Python Selenium script to open some Web Dev Resources in Chrome or Firefox
# LOTS of Tabs :)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Chrome
chrome_options = Options()
browser = webdriver.Chrome(executable_path="C:\chromedriver.exe")

# Disable Chrome is being controlled by automated testing software message
chrome_options.add_argument("--disable-infobars")

## Firefox
## browser = webdriver.Firefox(executable_path="C:\geckodriver.exe")

# Tab 1
browser.get("https://devdocs.io")
# Tab 2
browser.execute_script("window.open('about:blank', 'tab2');")
browser.switch_to.window("tab2")
browser.get("https://developer.mozilla.org")
# Tab 3
browser.execute_script("window.open('about:blank', 'tab3');")
browser.switch_to.window("tab3")
browser.get("https://devhints.io")
# Tab 4
browser.execute_script("window.open('about:blank', 'tab4');")
browser.switch_to.window("tab4")
browser.get("https://docs.emmet.io/cheat-sheet")
# Tab 5
browser.execute_script("window.open('about:blank', 'tab5');")
browser.switch_to.window("tab5")
browser.get("https://github.com")
# Tab 6
browser.execute_script("window.open('about:blank', 'tab6');")
browser.switch_to.window("tab6")
browser.get("https://stackoverflow.com")
# Tab 7
browser.execute_script("window.open('about:blank', 'tab7');")
browser.switch_to.window("tab7")
browser.get("https://www.w3schools.com")
# Tab 8
browser.execute_script("window.open('about:blank', 'tab8');")
browser.switch_to.window("tab8")
browser.get("https://css-tricks.com")
# Tab 9
browser.execute_script("window.open('about:blank', 'tab9');")
browser.switch_to.window("tab9")
browser.get("https://codepen.io")
# Tab 10
browser.execute_script("window.open('about:blank', 'tab10');")
browser.switch_to.window("tab10")
browser.get("https://jslint.com/")
# Tab 11
browser.execute_script("window.open('about:blank', 'tab11');")
browser.switch_to.window("tab11")
browser.get("https://www.npmjs.com/")
# Tab 12
browser.execute_script("window.open('about:blank', 'tab12');")
browser.switch_to.window("tab12")
browser.get("https://pypi.org/")
# Tab 13
browser.execute_script("window.open('about:blank', 'tab13');")
browser.switch_to.window("tab13")
browser.get("https://packagist.org/")
# Tab 14
browser.execute_script("window.open('about:blank', 'tab14');")
browser.switch_to.window("tab14")
browser.get("https://www.smashingmagazine.com/")
# Tab 15
browser.execute_script("window.open('about:blank', 'tab15');")
browser.switch_to.window("tab15")
browser.get("https://medium.com/tag/web-development")
# Tab 16
browser.execute_script("window.open('about:blank', 'tab16');")
browser.switch_to.window("tab16")
browser.get("http://forums.devshed.com/")
# Tab 17
browser.execute_script("window.open('about:blank', 'tab17');")
browser.switch_to.window("tab17")
browser.get("https://www.reddit.com/r/webdev/")
# Tab 18
browser.execute_script("window.open('about:blank', 'tab18');")
browser.switch_to.window("tab18")
browser.get("https://www.hongkiat.com/blog/")