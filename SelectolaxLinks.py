from playwright.sync_api import sync_playwright
from selectolax.parser import HTMLParser
import pandas as pd
from datetime import datetime
import time

URLwc = "https://us.shein.com/Women-Clothing-c-2030.html?src_module=Women&src_identifier=on%3DIMAGE_COMPONENT%60cn%3Dshopbycate%60hz%3DhotZone_16%60ps%3D4_9%60jc%3Dreal_2030&src_tab_page_id=page_home1701123663929&ici=CCCSN%3DWomen_ON%3DIMAGE_COMPONENT_OI%3D12630207_CN%3DONE_IMAGE_COMPONENT_TI%3D50001_aod%3D0_PS%3D4-9_ABT%3D0"

URLdress = "https://us.shein.com/style/Dresses-sc-001148338.html?src_module=Women&src_identifier=on%3DIMAGE_COMPONENT%60cn%3Dshopbycate%60hz%3DhotZone_13%60ps%3D4_6%60jc%3DitemPicking_001148338&src_tab_page_id=page_home1701429098945&ici=CCCSN%3DWomen_ON%3DIMAGE_COMPONENT_OI%3D12688426_CN%3DONE_IMAGE_COMPONENT_TI%3D50001_aod%3D0_PS%3D4-6_ABT%3D0"

URLsweat =  "https://us.shein.com/recommend/Sweaters-Sweatshirts-sc-100190815.html?src_module=Women&src_identifier=on%3DIMAGE_COMPONENT%60cn%3Dshopbycate%60hz%3DhotZone_17%60ps%3D4_10%60jc%3DitemPicking_100190815&src_tab_page_id=page_home1701429181397&ici=CCCSN%3DWomen_ON%3DIMAGE_COMPONENT_OI%3D12688426_CN%3DONE_IMAGE_COMPONENT_TI%3D50001_aod%3D0_PS%3D4-10_ABT%3D0"

URLout = "https://us.shein.com/Women-Outerwear-c-2037.html?src_module=Women&src_identifier=on%3DIMAGE_COMPONENT%60cn%3Dshopbycate%60hz%3DhotZone_20%60ps%3D4_13%60jc%3Dreal_2037&src_tab_page_id=page_home1701429194989&ici=CCCSN%3DWomen_ON%3DIMAGE_COMPONENT_OI%3D12688426_CN%3DONE_IMAGE_COMPONENT_TI%3D50001_aod%3D0_PS%3D4-13_ABT%3D0"

URLunder = "https://us.shein.com/Underwear-&-Sleepwear-c-2038.html?src_module=Women&src_identifier=on%3DIMAGE_COMPONENT%60cn%3Dshopbycate%60hz%3DhotZone_19%60ps%3D4_12%60jc%3Dreal_2038&src_tab_page_id=page_home1701429211520&ici=CCCSN%3DWomen_ON%3DIMAGE_COMPONENT_OI%3D12688426_CN%3DONE_IMAGE_COMPONENT_TI%3D50001_aod%3D0_PS%3D4-12_ABT%3D0"

URLjewel = "https://us.shein.com/recommend/Jewelry-Accessories-sc-100115041.html?src_module=Women&src_identifier=on%3DIMAGE_COMPONENT%60cn%3Dshopbycate%60hz%3DhotZone_10%60ps%3D4_5%60jc%3DitemPicking_100115041&src_tab_page_id=page_home1701429240815&ici=CCCSN%3DWomen_ON%3DIMAGE_COMPONENT_OI%3D12688426_CN%3DONE_IMAGE_COMPONENT_TI%3D50001_aod%3D0_PS%3D4-5_ABT%3D0"

URLsports = "https://us.shein.com/Sports-&-Outdoor-c-3195.html?src_module=Women&src_identifier=on%3DIMAGE_COMPONENT%60cn%3Dshopbycate%60hz%3DhotZone_1%60ps%3D4_1%60jc%3Dreal_3195&src_tab_page_id=page_home1701429273738&ici=CCCSN%3DWomen_ON%3DIMAGE_COMPONENT_OI%3D12688426_CN%3DONE_IMAGE_COMPONENT_TI%3D50001_aod%3D0_PS%3D4-1_ABT%3D0"

URLbags = "https://us.shein.com/recommend/Shoes-and-Bags-sc-100123139.html?src_module=Women&src_identifier=on%3DIMAGE_COMPONENT%60cn%3Dshopbycate%60hz%3DhotZone_14%60ps%3D4_7%60jc%3DitemPicking_100123139&src_tab_page_id=page_home1701429424597&ici=CCCSN%3DWomen_ON%3DIMAGE_COMPONENT_OI%3D12688426_CN%3DONE_IMAGE_COMPONENT_TI%3D50001_aod%3D0_PS%3D4-7_ABT%3D0"

def parsing(URL, numPages):
    links = []
    product_names = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = True)
        page = browser.new_page()
        for i in range(1, numPages + 1):
        
            page.goto(URL + '&page=' + str(i))

            page.wait_for_load_state("networkidle")
            page.wait_for_load_state("domcontentloaded")
            page.wait_for_selector('section[aria-label]')

            if i == 1:
                #page.click('body > div.c-outermost-ctn.j-outermost-ctn > div.j-vue-coupon-package-container.c-vue-coupon > div > div.sui-dialog.coupon-dialog.has-custom-theme > div > div > div.sui-dialog__body > div.c-coupon-box > i')
                page.click('body > div.j-quick-register-container > div.c-quick-register.j-quick-register > div.quickg-outside > i')
        
            html = page.inner_html("body")
            tree = HTMLParser(html)

            #page.screenshot(path="shein.png", full_page = True)

            bigDiv = tree.css('section[role="main"]')
            # div.product-card__top-wrapper > a href
            
            print(len(bigDiv))
            print(type(bigDiv[0]))
            divs = bigDiv[0].css_first('div').css('section[aria-label]')
            print(len(divs))

            try:
                for d in divs:
                    links.append(d.css_first('div > a').attrs['href'])
                    product_names.append(d.css_first('div > a').attrs['aria-label'])
            except (ModuleNotFoundError, AttributeError):
                break

    return links, product_names


if __name__ == "__main__":
    timestamp = int(time.time())
    time_stamp = (datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d'))

    links, product_names = parsing(URLwc, 32)
    df = pd.DataFrame(data={'links':links, 'product_names':product_names})
    df["sub_category"] = 'Womens Clothing'
    df.to_csv('WomensClothingLinks' + time_stamp + '.csv', index=False)


    links, product_names = parsing(URLdress, 31)
    df = pd.DataFrame(data={'links':links, 'product_names':product_names})
    df["sub_category"] = 'Dresses'
    df.to_csv('DressLinks' + time_stamp + '.csv', index=False)

    links, product_names = parsing(URLsweat, 31)
    df = pd.DataFrame(data={'links':links, 'product_names':product_names})
    df["sub_category"] = 'Sweaters'
    df.to_csv('SweaterLinks' + time_stamp + '.csv', index=False)


    links, product_names = parsing(URLjewel, 32)
    df = pd.DataFrame(data={'links':links, 'product_names':product_names})
    df["sub_category"] = 'Jewelry'
    df.to_csv('JewelryLinks' + time_stamp + '.csv', index=False)

    links, product_names = parsing(URLout, 29)
    df = pd.DataFrame(data={'links':links, 'product_names':product_names})
    df["sub_category"] = 'Outer Wear'
    df.to_csv('OuterLinks' + time_stamp + '.csv', index=False)

    links, product_names = parsing(URLunder, 31)
    df = pd.DataFrame(data={'links':links, 'product_names':product_names})
    df["sub_category"] = 'Underwear'
    df.to_csv('UnderwearLinks' + time_stamp + '.csv', index=False)
    
    links, product_names = parsing(URLsports, 30)
    df = pd.DataFrame(data={'links':links, 'product_names':product_names})
    df["sub_category"] = 'Sports'
    df.to_csv('SportsClothingLinks' + time_stamp + '.csv', index=False)

    links, product_names = parsing(URLbags, 32)
    df = pd.DataFrame(data={'links':links, 'product_names':product_names})
    df["sub_category"] = 'Bags'
    df.to_csv('BagsLinks' + time_stamp + '.csv', index=False)