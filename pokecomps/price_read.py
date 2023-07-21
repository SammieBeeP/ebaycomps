from bs4 import BeautifulSoup
import requests
import json 

## HTML From Website

url = "https://www.ebay.com/itm/155651571536?hash=item243d8e7f50:g:as8AAOSw~QJkkgfn&amdata=enc%3AAQAIAAABAN27frC7waopkh1ljmQxGy74dmo2DPV%2B0I62UqYpeBGE89VGw7b4KKNvn7V%2Fn7vCJfIuo8LyUFAGQU9ETlChV%2FPJBfo75axvDuiZp6FcIv1g7DgIsDsxx3UvakNB8WsDiLa4QNpQ%2B4lC7484PVBsHSwvmUQWA1ARKNcvqQlFJ8Unz8yII%2F84vouq%2F82ccqPI0NfMMhU6SypGDL5fubzZzZPZFFD5fhaArv4qIfPkKfNUWwxex8AmYR3ZBuQLiJ6nurOJzqBI4yFnzf%2B4pYjueDVrDs2asaUGGuMjW3lNnDEHLE5HaxL8BmoGRqTFXWDnmroDrrdqI8KQET%2Bu3tXTUnU%3D%7Ctkp%3ABk9SR7rFz9iuYg"
##Changing the URL *might* make the code not work. Check the HTML parents of the price if error occurs.
result = requests.get(url)
soupdoc = BeautifulSoup(result.text, "html.parser")
#print(doc.prettify())

##The HTML on the default site that holds the price data is [<span id="" class="notranslate vi-VR-cvipPrice">US $285.00</span>]
price = soupdoc.find("span", class_="notranslate vi-VR-cvipPrice")

##This is to prep the data for JSON:
price_data = {}
##data is prepped. les continue...
##The print is commented out so I can test recall code further down.
if price:
    price_data["price"] = price.text
    #print(price.text)
else:
    price_data["price"] = "Price not found. Check HTML code."
    #print("Price not found. Check HTML code.")

##I can change the ebay url to another charizard and it gave the correct price. I want to test it with a few more links, then find out how to save it in a way I can recall the information to categorize later. Asked ChatGPT in "eBay Price Scraping"
##I also want to learn how to give and save multiple results from multiple websites.

##Writing to a JSON file:
with open("price_data.json", "w") as file:
    json.dump(price_data, file)
##When the URL changes, the json file is overwritten. I need to figure out how to add to it and organize it instead of just dumping it. 

##Reading the json:
with open("price_data.json", "r") as file:
    json_data = json.load(file)
#print(json_data)

##Next Steps:: 
##  item_specifics.py (or currently below until I figure out how to pull from other programs)
##  1a.) Pull and store the values from the "Item Specifics" section on each listing.
##  1b.) Send it all to a database.
    ## 1bs.) Create a nested ifs filter so that the search data returns only on matching item specifics.  

##  2a.) Find relevant sales page links on ebay search page - ask mason about the key words for search relevancy
##  2b.) Run the links through this code ^ 