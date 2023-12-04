from playwright.sync_api import sync_playwright
from selectolax.parser import HTMLParser
import pandas as pd
from selectolax.parser import Node
from datetime import datetime
import time
import numpy as np

def parse_products(linkSet):
    isPageLoaded = True

    df = pd.DataFrame()
    df['product_name'] = None
    df['sku'] = None
    df['original price'] = None
    df['discount price'] = None 
    df['reviews'] = None 
    df['sizes'] = None 
    df['descriptions'] = None 
    df['model wearing'] = None 
    df['model height'] = None 
    df['model waist'] = None 
    df['model bust'] = None 
    df['model hips'] = None 
    df['brand'] = None 
    df['time stamp'] = None 

    with sync_playwright() as p:
        c = 1
        browser = p.chromium.launch(headless = True)
        page = browser.new_page()
        primera = True
        for index, row in linkSet.iterrows():
            if c > 50:
                break

            URL = 'http://us.shein.com'  + row[0] 
            #linkSet['links']

            while isPageLoaded:
                page.goto(URL)

                try:
                    page.wait_for_load_state("networkidle")
                    page.wait_for_load_state("domcontentloaded")
                    try:
                        page.wait_for_selector('div.product-intro')
                    except (TimeoutError):
                        pass
                    break
                except (TimeoutError):
                    pass

            if primera:
                #page.click('body > div.c-outermost-ctn.j-outermost-ctn > div.j-vue-coupon-package-container.c-vue-coupon > div > div.sui-dialog.coupon-dialog.has-custom-theme > div > div > div.sui-dialog__body > div.c-coupon-box > i')
                page.click('body > div.j-quick-register-container > div.c-quick-register.j-quick-register > div.quickg-outside > i')
                primera = False

            html = page.inner_html("body")
            tree = HTMLParser(html)

            mainDiv = tree.css_first('div').css_first('div[class="product-intro__info-sticky"]')

            #page.wait_for_selector('span.price-estimated-percent__price')

            try:
                product_name = (mainDiv.css_first('h1[class="product-intro__head-name"]').text())
                sku = (mainDiv.css_first('div.product-intro__head-sku').text().split(sep= ' ')[-1])

            except (IndexError, AttributeError):
                pass


            try:
                original_price = (mainDiv.css_first('span.price-estimated-percent__price').text())
            except (IndexError, AttributeError):
                pass

            try:
                discount_price = (mainDiv.css_first('span.price-num').text())
                reviews = (mainDiv.css_first('div.product-intro__head-reviews > span').attrs['aria-label'].split(sep=' ')[2])
            except (IndexError, AttributeError):
                pass


            try:
                sizes_list = (''.join(mainDiv.css_first('div.product-intro__size > div.product-intro__size-choose.fsp-element').text()))
                descriptions = (mainDiv.css_first('div.product-intro__description-table').text())
            except (IndexError, AttributeError):
                pass

            try:
                model_wearing = (mainDiv.css_first('div.product-intro__sizeguide-summary-list > div').text())
                model_height = (mainDiv.css('div.product-intro__sizeguide-summary-list > div.model-item > div')[0].text())
                model_bust = (mainDiv.css('div.product-intro__sizeguide-summary-list > div.model-item > div')[1].text())
                model_waist = (mainDiv.css('div.product-intro__sizeguide-summary-list > div.model-item > div')[2].text())
                model_hips = (mainDiv.css('div.product-intro__sizeguide-summary-list > div.model-item > div')[3].text())
            except (IndexError, AttributeError):
                pass

            try:
                brand = (mainDiv.css_first('div.shop-entry__entryBox > div.shop-entry__contentBox > div.shop-entry__storeEntry > div.top-level > div.info-box > div.name-line > div.title').text())
            except (IndexError, AttributeError):
                pass

            timestamp = int(time.time())
            time_stamp = (datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S'))

            df.at[index, 'product_name'] = product_name
            df.at[index, 'sku'] = sku
            df.at[index, 'original price'] = original_price
            df.at[index, 'discount price'] = discount_price
            df.at[index, 'reviews'] = reviews
            df.at[index, 'sizes'] = sizes_list
            df.at[index, 'descriptions'] = descriptions
            df.at[index, 'model wearing'] = model_wearing
            df.at[index, 'model height'] = model_height
            df.at[index, 'model waist'] = model_waist
            df.at[index, 'model bust'] = model_bust
            df.at[index, 'model hips'] = model_hips
            df.at[index, 'brand'] = brand
            df.at[index, 'time stamp'] = time_stamp

            print(c)
            c += 1

    return df

def product_intro_head(node: Node, selectors: list):
    parsed = {}

    for s in selectors:
        match = s.get('match')
        type_ = s.get('type')
        selector = s.get('selector')
        name = s.get('name')
        
        if match == "all":
            matched = node.css(selector)

            if type_ == "text":
                parsed[name] = [node.text() for node in matched]
            elif type_ == "node":
                parsed[name] = matched
            else:
                parsed[name] = matched.attrs[type_]
        

        elif match == "first":
            matched = node.css_first(selector)

            if type_ == "first":
                parsed[name] = matched.text()
            elif type_ == "node":
                parsed[name] = matched
            else:
                parsed[name] = matched.attrs[type_]

    return parsed




if __name__ == "__main__":
    linkSet = pd.read_csv("newLinks.csv")
    parse_products(linkSet).to_csv('productDetails.csv', index=False)