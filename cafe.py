

menu = ["croissant", "steak", "sandwich", "coffee"] # Menu list; the invisible indexes are 0-croissant, 1-steak, 2-sandwich, and 3-coffee.
stock = {0 : 200 , 1 : 130 , 2 : 100 , 3 : 300} # The stock dictionary values represent the items in stock (eg. 300 units of coffee). The dictionary keys match the 'menu' list's indexes.
price = {0 : 2 , 1 : 3 , 2 : 2 , 3 : 3} # The price dictionary keys match the 'menu' list's indexes (0,1,2,3). The dictionary values represent unit cost eg. $3 per steak.

total = 0 # This RUNNING TOTAL for-loop multiplies the 2 dictionary values, then it sums the 4 results to give the total stock value.
for i in range (0,4): # We have 4 menu items.
    itemValue = stock[i] * price[i] # Multiplying values in each dictionary.
    total = total + itemValue # Sum of the 4 multipied values.


print(f'The total stock value of the Café Sur Le Pont is ${total}.')