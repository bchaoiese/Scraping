from SelectolaxLinks import parsing
import pandas as pd
import time
from datetime import datetime

links_dictionary = {

'URLwc' : "https://us.shein.com/Women-Clothing-c-2030.html?src_module=Women&src_identifier=on%3DIMAGE_COMPONENT%60cn%3Dshopbycate%60hz%3DhotZone_16%60ps%3D4_9%60jc%3Dreal_2030&src_tab_page_id=page_home1701123663929&ici=CCCSN%3DWomen_ON%3DIMAGE_COMPONENT_OI%3D12630207_CN%3DONE_IMAGE_COMPONENT_TI%3D50001_aod%3D0_PS%3D4-9_ABT%3D0",

'URLdress' : "https://us.shein.com/style/Dresses-sc-001148338.html?src_module=Women&src_identifier=on%3DIMAGE_COMPONENT%60cn%3Dshopbycate%60hz%3DhotZone_13%60ps%3D4_6%60jc%3DitemPicking_001148338&src_tab_page_id=page_home1701429098945&ici=CCCSN%3DWomen_ON%3DIMAGE_COMPONENT_OI%3D12688426_CN%3DONE_IMAGE_COMPONENT_TI%3D50001_aod%3D0_PS%3D4-6_ABT%3D0",

'URLsweat' : "https://us.shein.com/recommend/Sweaters-Sweatshirts-sc-100190815.html?src_module=Women&src_identifier=on%3DIMAGE_COMPONENT%60cn%3Dshopbycate%60hz%3DhotZone_17%60ps%3D4_10%60jc%3DitemPicking_100190815&src_tab_page_id=page_home1701429181397&ici=CCCSN%3DWomen_ON%3DIMAGE_COMPONENT_OI%3D12688426_CN%3DONE_IMAGE_COMPONENT_TI%3D50001_aod%3D0_PS%3D4-10_ABT%3D0",

'URLout' : "https://us.shein.com/Women-Outerwear-c-2037.html?src_module=Women&src_identifier=on%3DIMAGE_COMPONENT%60cn%3Dshopbycate%60hz%3DhotZone_20%60ps%3D4_13%60jc%3Dreal_2037&src_tab_page_id=page_home1701429194989&ici=CCCSN%3DWomen_ON%3DIMAGE_COMPONENT_OI%3D12688426_CN%3DONE_IMAGE_COMPONENT_TI%3D50001_aod%3D0_PS%3D4-13_ABT%3D0",

'URLunder' : "https://us.shein.com/Underwear-&-Sleepwear-c-2038.html?src_module=Women&src_identifier=on%3DIMAGE_COMPONENT%60cn%3Dshopbycate%60hz%3DhotZone_19%60ps%3D4_12%60jc%3Dreal_2038&src_tab_page_id=page_home1701429211520&ici=CCCSN%3DWomen_ON%3DIMAGE_COMPONENT_OI%3D12688426_CN%3DONE_IMAGE_COMPONENT_TI%3D50001_aod%3D0_PS%3D4-12_ABT%3D0",

'URLjewel' : "https://us.shein.com/recommend/Jewelry-Accessories-sc-100115041.html?src_module=Women&src_identifier=on%3DIMAGE_COMPONENT%60cn%3Dshopbycate%60hz%3DhotZone_10%60ps%3D4_5%60jc%3DitemPicking_100115041&src_tab_page_id=page_home1701429240815&ici=CCCSN%3DWomen_ON%3DIMAGE_COMPONENT_OI%3D12688426_CN%3DONE_IMAGE_COMPONENT_TI%3D50001_aod%3D0_PS%3D4-5_ABT%3D0",

'URLsports' : "https://us.shein.com/Sports-&-Outdoor-c-3195.html?src_module=Women&src_identifier=on%3DIMAGE_COMPONENT%60cn%3Dshopbycate%60hz%3DhotZone_1%60ps%3D4_1%60jc%3Dreal_3195&src_tab_page_id=page_home1701429273738&ici=CCCSN%3DWomen_ON%3DIMAGE_COMPONENT_OI%3D12688426_CN%3DONE_IMAGE_COMPONENT_TI%3D50001_aod%3D0_PS%3D4-1_ABT%3D0",

'URLbags' : "https://us.shein.com/recommend/Shoes-and-Bags-sc-100123139.html?src_module=Women&src_identifier=on%3DIMAGE_COMPONENT%60cn%3Dshopbycate%60hz%3DhotZone_14%60ps%3D4_7%60jc%3DitemPicking_100123139&src_tab_page_id=page_home1701429424597&ici=CCCSN%3DWomen_ON%3DIMAGE_COMPONENT_OI%3D12688426_CN%3DONE_IMAGE_COMPONENT_TI%3D50001_aod%3D0_PS%3D4-7_ABT%3D0"




}

### Scraping today's data ######

timestamp = int(time.time())
time_stamp = (datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d'))

links, product_names = parsing(links_dictionary['URLwc'], 32)
df_wc = pd.DataFrame(data={'links':links, 'product_names':product_names})
df_wc["sub_category"] = 'Womens Clothing'
df_wc.to_csv('WomensClothingLinks' + time_stamp + '.csv', index=False)


links, product_names = parsing(links_dictionary['URLdress'], 31)
df_dress = pd.DataFrame(data={'links':links, 'product_names':product_names})
df_dress["sub_category"] = 'Dresses'
df_dress.to_csv('DressLinks' + time_stamp + '.csv', index=False)

links, product_names = parsing(links_dictionary['URLsweat'], 31)
df_sweat = pd.DataFrame(data={'links':links, 'product_names':product_names})
df_sweat["sub_category"] = 'Sweaters'
df_sweat.to_csv('SweaterLinks' + time_stamp + '.csv', index=False)


links, product_names = parsing(links_dictionary['URLjewel'], 32)
df_jewel = pd.DataFrame(data={'links':links, 'product_names':product_names})
df_jewel["sub_category"] = 'Jewelry'
df_jewel.to_csv('JewelryLinks' + time_stamp + '.csv', index=False)

links, product_names = parsing(links_dictionary['URLout'], 29)
df_outer = pd.DataFrame(data={'links':links, 'product_names':product_names})
df_outer["sub_category"] = 'Outer Wear'
df_outer.to_csv('OuterLinks' + time_stamp + '.csv', index=False)

links, product_names = parsing(links_dictionary['URLunder'], 31)
df_under = pd.DataFrame(data={'links':links, 'product_names':product_names})
df_under["sub_category"] = 'Underwear'
df_under.to_csv('UnderwearLinks' + time_stamp + '.csv', index=False)
    
links, product_names = parsing(links_dictionary['URLsports'], 30)
df_sports = pd.DataFrame(data={'links':links, 'product_names':product_names})
df_sports["sub_category"] = 'Sports'
df_sports.to_csv('SportsClothingLinks' + time_stamp + '.csv', index=False)

links, product_names = parsing(links_dictionary['URLbags'], 32)
df_bags = pd.DataFrame(data={'links':links, 'product_names':product_names})
df_bags["sub_category"] = 'Bags'
df_bags.to_csv('BagsLinks' + time_stamp + '.csv', index=False)
###########################################################
#Comparing the data sets. 
#There will be 8 data sets created from each day's scraping.
#Then one combined, one new, one old.
df = pd.concat([df_sweat, df_bags, df_dress, df_jewel, df_outer, df_sports, df_under, df_wc], ignore_index = True, axis = 0)
df.to_csv('currentLinks.csv', index=False)
df = df.rename(columns = {'product_names' : 'productNames'})
currentSet = pd.read_csv("currentLinks.csv")

df['links'] = df['links'].astype(str)
currentSet['links'] = currentSet['links'].astype(str)

old = pd.merge(currentSet, df, how = 'left', on = 'links')
new = pd.merge(currentSet, df, how = 'right', on = 'links')
old = old[old['productNames'].isna()]
new = new[new['product_names'].isna()]
timestamp = int(time.time())
time_stamp = (datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d'))

#df.rename(columns = {'productNames': 'product_names'}).to_csv('currentLinks.csv', index=False)
old.to_csv('oldLinks'+ time_stamp + '.csv', index=False)
new.to_csv('newLinks' + time_stamp + '.csv', index=False)