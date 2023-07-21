##  1a.) Pull and store the values from the "Item Specifics" section on each listing.
##  1b.) Send it all to a database.
    ## 1bs.) Create a nested ifs filter so that the search data returns only on matching item specifics.  

##ebay $285: https://www.ebay.com/itm/204395783252?hash=item2f96f02454:g:hfYAAOSwS6ZksB-J&amdata=enc%3AAQAIAAAA4LTxr7UoR3gAmfuVSnKHPUJ7NJzGcWEhsRP4zm3BQ4P5aT%2FeugRR71%2B1j5z54jmKx%2FNoMZj5KdGKOAkvXPoKCuvg5%2F6WeyULEl9TnxDRZ1s0WMNK2IXyzLWmazc%2B6gBi3rzJQxymwz8n54hOJx09h%2F9r1VyD8%2BKwC235TrfZhnDk3NwIn5pv1GwSpcumcz1HHWePVPgl%2BN6wVLIpy%2BCXmmiFpy6bsPgMfjBN7ygTh%2BXxfvvFU8icmI9btbZ3AWUz180Y7jRrT6xzuReFIqk4hSlzdwTv1%2FiafA%2FeixYAj0kv%7Ctkp%3ABk9SR7rFz9iuYg 
##ebay $270: https://www.ebay.com/itm/155651571536?hash=item243d8e7f50:g:as8AAOSw~QJkkgfn&amdata=enc%3AAQAIAAABAN27frC7waopkh1ljmQxGy74dmo2DPV%2B0I62UqYpeBGE89VGw7b4KKNvn7V%2Fn7vCJfIuo8LyUFAGQU9ETlChV%2FPJBfo75axvDuiZp6FcIv1g7DgIsDsxx3UvakNB8WsDiLa4QNpQ%2B4lC7484PVBsHSwvmUQWA1ARKNcvqQlFJ8Unz8yII%2F84vouq%2F82ccqPI0NfMMhU6SypGDL5fubzZzZPZFFD5fhaArv4qIfPkKfNUWwxex8AmYR3ZBuQLiJ6nurOJzqBI4yFnzf%2B4pYjueDVrDs2asaUGGuMjW3lNnDEHLE5HaxL8BmoGRqTFXWDnmroDrrdqI8KQET%2Bu3tXTUnU%3D%7Ctkp%3ABk9SR7rFz9iuYg
##ebay $250: https://www.ebay.com/itm/394719369143?hash=item5be71b97b7:g:b4AAAOSw3~Bkow-a&amdata=enc%3AAQAIAAABAKjz1qS3jNN2fgrRsbSspSOXdLKgF9c9K%2BBcr%2FdbrnUyALo2HHYhe2awZSDK%2BH0RrzDoUR3lhnN3BgNcoHoOhknFcMjOF6ZjvhVrrGg2LKuMTwLiUV%2FVJnBEvGl9%2B3OGqfo9KvjqE0cudHpr4jKvqzdhn9XZHU%2F8oXqnt52BlL3LXA%2Fx%2BtKSWmaPqykDeEl4v4uwxH6ApFh%2BgXPsZfqF2jPigi79DMZ3sAWZe1aWS7bCdFmL8DMJEna5Lr4MuOrNfCkChtC4KZPO17RkruAXTaXWpJtaxgL20SMTefVf%2Fx4qsLbYTbNDEtbbpnK5jzJkNf9ZzZvjV%2FKmE6CIfcBUZZw%3D%7Ctkp%3ABk9SR7rFz9iuYg 

from bs4 import BeautifulSoup
import requests
import json 

url_285 = "https://www.ebay.com/itm/204395783252?hash=item2f96f02454:g:hfYAAOSwS6ZksB-J&amdata=enc%3AAQAIAAAA4LTxr7UoR3gAmfuVSnKHPUJ7NJzGcWEhsRP4zm3BQ4P5aT%2FeugRR71%2B1j5z54jmKx%2FNoMZj5KdGKOAkvXPoKCuvg5%2F6WeyULEl9TnxDRZ1s0WMNK2IXyzLWmazc%2B6gBi3rzJQxymwz8n54hOJx09h%2F9r1VyD8%2BKwC235TrfZhnDk3NwIn5pv1GwSpcumcz1HHWePVPgl%2BN6wVLIpy%2BCXmmiFpy6bsPgMfjBN7ygTh%2BXxfvvFU8icmI9btbZ3AWUz180Y7jRrT6xzuReFIqk4hSlzdwTv1%2FiafA%2FeixYAj0kv%7Ctkp%3ABk9SR7rFz9iuYg"
result_285 = requests.get(url_285)
doc_285 = BeautifulSoup(result_285.text, "html.parser")

#push this into github