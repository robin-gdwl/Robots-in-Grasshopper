import re
import time
import random
import requests
import urllib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "https://www.food4rhino.com/app/robot-components"

PATH = "D:\Portable_Programs\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get(link)
# wait until page has loaded
search_results = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "image-style-thumbnail")))

# get thumbnail image
image_objects = driver.find_elements_by_css_selector("image-style-thumbnail")
image_elements = driver.find_elements_by_xpath("//div[@class='field field-name-field-project-image field-type-image field-label-hidden view-mode-_custom_display']/figure/img")
image_elements = driver.find_elements_by_xpath("//*[@id='block-system-main']/div/div/div/div[5]/div/div/div/div/figure/img")

print(image_elements)
if len(image_elements)>1:
    print("WARNING: more than one image found")
image_source = ""
for image in image_elements:
    source_link = image.get_attribute('src')
    print(source_link)
    # download the image
    urllib.request.urlretrieve(source_link, "thumbnail.png")

# Get Title, Author and Description 
plugin_title = driver.find_elements_by_xpath( "//*[@id='block-system-main']/div/div/div/div[1]/div/div/div/div/div")
plugin_title = plugin_title[0].text
plugin_author = driver.find_elements_by_xpath("//*[@id='block-system-main']/div/div/div/div[1]/div/div/div/div/div/div")
plugin_author_clean = plugin_author[0].text

# remove the author from the title (due to nested <div>-elements)
if plugin_author_clean in plugin_title:
    print("subtracting", plugin_title)
    plugin_title = plugin_title.replace(plugin_author_clean, "")
plugin_title_only = plugin_title
# plugin_title_only = re.sub(r" ?\([^)]+\)", "", plugin_title[0].text)

plugin_descr = driver.find_elements_by_xpath("//*[@id='body-content']")
desc_max_char = 86
desc_truncated = plugin_descr[0].text[:desc_max_char]
desc_truncated = desc_truncated.split()
desc_truncated.pop(-1)
plugin_desc_cutoff = " ".join(desc_truncated)

print(plugin_title)
print(plugin_author_clean)
print(plugin_desc_cutoff)
print(plugin_title_only)

time.sleep(random.randint(0,3))
driver.quit()

# #######
import drawSvg as draw
import textwrap

# Subclass DrawingBasicElement if it cannot have child nodes
# Subclass DrawingParentElement otherwise
# Subclass DrawingDef if it must go between <def></def> tags in an SVG
class Hyperlink(draw.DrawingParentElement):
    TAG_NAME = 'a'
    def __init__(self, href, target=None, **kwargs):
        # Other init logic...
        # Keyword arguments to super().__init__() correspond to SVG node
        # arguments: stroke_width=5 -> stroke-width="5"
        super().__init__(href=href, target=target, **kwargs)

img_width = 400
img_height = 120

# d = draw.Drawing(200, 100, origin='center', displayInline=False)
d = draw.Drawing(img_width, img_height, displayInline=False)
# d.draw(draw.Rectangle(0, 0,  img_width, img_height, fill='white'))
d.draw(draw.Rectangle(1, 1,  img_width*0.99, img_height*0.99, fill='white', stroke='#E4E2E2', rx=4.5)) 
# border_rect = draw.Path(stroke= )

f4r_w = int(67/2.6)
f4r_h = int(45/2.6)
d.append(draw.Image(20, img_height-f4r_h -22, f4r_w, f4r_h, path="./Resources/F4R_logo_small.png", embed=True, mimeType=None))
# Draw text
# Create hyperlink
hlink = Hyperlink(link+"#columns", target='_blank')
# Add child elements
# hlink.append(draw.Circle(0,0,0.5, fill='green'))
# hlink.append(draw.Text('Hyperlink',0.2, 0,0, center=0.6, fill='white'))
titlelength = len(plugin_title_only)
print(titlelength)
if titlelength > 20:

    cardtitle = textwrap.wrap(plugin_title_only, width=24)
    lines = len(cardtitle)
    cardtitle = "\n".join(cardtitle)
else: 
    cardtitle = plugin_title_only
    lines = 1
print(cardtitle)
print("::::::")
title_size = 18
hlink.append(draw.Text(cardtitle, 
                        title_size,
                        50, 
                        img_height-35, 
                        fill='#68b84c', font_weight=600, font_family="Arial, Helvetica, sans-serif"))
d.append(hlink)

# draw author
d.append(draw.Text(plugin_author_clean[1:-1], 
                    14, 60,
                    img_height-35-(title_size*lines), 
                    fill='#363636', 
                    font_weight=600, 
                    font_family="Arial, Helvetica, sans-serif"))
# draw description
d.append(draw.Text(textwrap.fill(plugin_desc_cutoff, 42)+"[....]",
                    10, 60, 
                    img_height-35-(title_size*lines)-14-8, 
                    fill='#a3a3a3', font_weight=300,font_family="Arial, Helvetica, sans-serif"))
# d.append(draw.Text(['Multi-line', 'text'], 8, path=p, text_anchor='end'))
thumb_size = 60
d.append(draw.Image(img_width-thumb_size-20, img_height-thumb_size-20, thumb_size, thumb_size, path="thumbnail.png", embed=True, mimeType=None))
d.append(draw.Rectangle(img_width-thumb_size-20, img_height-thumb_size-20, thumb_size, thumb_size, fill='#ffffff00', stroke='gray', stroke_width=1, rx=3 ))

d.setPixelScale(1)  # Set number of pixels per geometry unit
#d.setRenderSize(400,200)  # Alternative to setPixelScale
saved = d.saveSvg('example.svg')
print(saved)