import re
import time
import random
import requests
import urllib3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "https://www.food4rhino.com/app/robot-components"

PATH = "D:\Portable_Programs\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get(link)
search_results = WebDriverWait(driver, 20).until(
EC.presence_of_element_located((By.CLASS_NAME, "image-style-thumbnail"))
) 
# search = driver.find_element_by_name("q")
image_objects = driver.find_elements_by_css_selector("image-style-thumbnail")
image_elements = driver.find_elements_by_xpath("//div[@class='field field-name-field-project-image field-type-image field-label-hidden view-mode-_custom_display']/figure/img")
image_elements = driver.find_elements_by_xpath("//*[@id='block-system-main']/div/div/div/div[5]/div/div/div/div/figure/img")
# print(image_objects)
print(image_elements)
if len(image_elements)>1:
    print("WARNING: more than one image found")
image_source = ""
for image in image_elements:
    source_link = image.get_attribute('src')
    # print(source_link)
plugin_title = driver.find_elements_by_xpath("//*[@id='block-system-main']/div/div/div/div[1]/div/div/div/div/div")
plugin_author = driver.find_elements_by_xpath("//*[@id='block-system-main']/div/div/div/div[1]/div/div/div/div/div/div")
plugin_descr = driver.find_elements_by_xpath("//*[@id='body-content']")
print(plugin_title[0].text, plugin_author[0].text)

# items = ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]

desc_max_char = 200
plugin_title_only = re.sub(r" ?\([^)]+\)", "", plugin_title[0].text)
# plugin_author_clean = re.search(r"\(([A-Za-z0-9_]+)\)", plugin_title[0].text)
plugin_author_clean = plugin_author[0].text
plugin_desc_cutoff = plugin_descr[0].text[:desc_max_char]
print(plugin_title[0].text)
print(plugin_author_clean)
print(plugin_desc_cutoff)
print(plugin_title_only)

time.sleep(random.randint(0,5))
# bufferedImage = ImageIO.read(new URL(src));
# File outputfile = new File("saved.png");
# ImageIO.write(bufferedImage, "png", outputfile);
driver.quit()


# #######
import drawSvg as draw
import textwrap

# d = draw.Drawing(200, 100, origin='center', displayInline=False)
d = draw.Drawing(200, 100, displayInline=False)

# Draw text
d.append(draw.Text(plugin_title_only, 8, 10, 90, fill='blue', font_family="Arial, Helvetica, sans-serif"))  # Text with font size 8
d.append(draw.Text(plugin_author_clean, 8, 10, 80))
d.append(draw.Text(textwrap.fill(plugin_desc_cutoff, 40)+"....", 8, 10, 55))
# d.append(draw.Text(['Multi-line', 'text'], 8, path=p, text_anchor='end'))

d.setPixelScale(2)  # Set number of pixels per geometry unit
#d.setRenderSize(400,200)  # Alternative to setPixelScale
d.saveSvg('example.svg')