# Lesson 141 - Web Scraping Control Browser With Selenium
# Video: https://www.youtube.com/watch?v=rovYCAv8_tU

# ---------------------------------------------------
# -- Web Scraping => Control Browser With Selenium --
# ---------------------------------------------------
# - Control Browser With Selenium For Automated Testing
# - Download File From The Internet
# - Subtitle Download And Add On Your Movies [ Many Modules ]
# - Get Quotes From Websites
# - Get Gold and Currencies Rate
# - Get News From Websites
# - --------------------------------------------

# pip install selenium webdriver-manager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

browser.get("https://elzero.org")

# ملاحظة: الأمر find_element_by_css_selector حذف من الإصدار 4.3 من المكتبة
# الطريقة الحالية هي find_element(By.CSS_SELECTOR, "...") كما في الأسطر التالية
# وأسماء العناصر في الموقع قد تتغير مع الوقت، فإذا لم يجدها افحص الصفحة من جديد

# browser.find_element(By.CSS_SELECTOR, ".search-field").send_keys("Front-End Developer")

# browser.implicitly_wait(5)

# browser.find_element(By.CSS_SELECTOR, ".search-submit").click()

# browser.find_element(By.CSS_SELECTOR, ".all-search-posts .search-post:first-of-type h3 a").click()

# browser.implicitly_wait(5)

# views_count = browser.find_element(By.CSS_SELECTOR, ".z-article-info .z-info:last-of-type span:last-child")

# browser.implicitly_wait(5)

# print(views_count.get_attribute('innerHTML'))

# browser.quit() # إغلاق المتصفح بعد الانتهاء

