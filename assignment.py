items = []
inventory = []
user = []
cart = []

#Utility function to check whether user exists or not
def isUser(username):
    for i in user:
        flag = 0
        if i[0] == username:
            flag = 1
    return flag

#Utility function to check whether item exists or not    
def isItem(category,brand):
    flag = 0
    for i in items:
        if i[0]==category and i[1]==brand:
            flag = 1
    return flag


#Adding a new item.
def addItem():
    print("Creating a new item")
    category = input("Enter the name of category:")
    brand = input("Enter the name of brand:")
    price  = input("Enter the price of item:")
    x = [category,brand,price]
    try:
        items.append(x)
    except Exception:
        print("There was a problem adding the item.")
    print("Item added successfully.")
    print(items)


#Add an item to inventory.
def addItemToInventory():
    print("Adding an item to inventory")
    category = input("Enter Category:")
    brand = input("Enter brand name:")
    isItemExist = isItem(category, brand)

    if isItemExist==0:
        print("Item does not exist.")
        return

    quantity = input("Quantity:")
    x = [category,brand,quantity]
    try:
        inventory.append(x)
    except Exception:
        print("There was an error adding item to the inventory.")
    print("Item successfully added to the inventory.")
    print(inventory)

#Add a new user.
def addUser():
    username = input("Enter username:")
    walletAmount = input("Enter wallet Amount:")
    x = [username,walletAmount]
    try:
        user.append(x)
    except Exception:
        print("There was a problem adding the user.")
    print(user)

#Add an item to the cart.
def addToCart():
    username = input("Enter username:")
    isUserExist = isUser(username)
    if isUserExist == 0:
        print("User does not exist please create a user.")
        return
    
    category = input("Enter the name of category.")
    brand = input("Enter the name of brand.")
    isItemExist = isItem(category, brand)
    if isItemExist == 0:
        print("Item of the given category and brand does not exist.")
        return

    quantity = input("Quantity:")
    x = [username,category,brand,quantity]
    try:
        cart.append(x)
        print(cart)
    except Exception:
        print("There was an error adding the item to the cart.")

#updates an existing item in the cart.
def updateCart():
    username = input("Enter username:")
    category = input("Enter the name of category.")
    brand = input("Enter the name of brand.")
    flag = 0
    for i in cart:
        if i[0]==username and i[1]==category and i[2]==brand:
            quantity = input("Enter the updated quantity:")
            try:
                i[3] = quantity
                print(cart)
            except Exception:
                print("There was an error updating the quantity.")
            print("Item updated successfully.")     
            return
        else:
            print("Either username does not exist or item does not exist in cart.")

#removes an element from the cart
def removeFromCart():
    username = input("Enter username:")
    category = input("Enter the name of category.")
    brand = input("Enter the name of brand.")
    flag = 0
    for i in cart:
        if i[0]==username and i[1]==category and i[2]==brand:
            cart.remove(i)
            print(cart)
            return
    
#get all the items in a cart of a user.
def getCart():
    username = input("Enter username:")
    isUserExist = isUser(username)
    if isUserExist==0:
        print("User does not exist.")
    else:
        for i in cart:
            if i[0]==username:
                print(i)

#checks out a user, calculates the bill and updates the wallet.
def cartCheckout():
    bill = 0
    price = 0
    quantity = 0
    wallet = 0
    username = input("Enter username:")
    isUserExist = isUser(username)
    if isUserExist==0:
        print("User does not exist.")
    else:
        for i in cart:
            if username == i[0]:
                category = i[1]
                brand = i[2]
                quantity = int(i[3])
                for j in items:
                    if j[0]==category and j[1]==brand:
                        price = int(j[2])
                        bill = bill + (price * quantity)
        
        for x in user:
            if x[0] == username:
                wallet = int(x[1])
            if wallet < bill:
                print("You don' have enough amount in your wallet.")
            else:
                x[1] = str(wallet - bill)
            print("checkout successfull.")
            return

#get the wallet amount of a user.
def getWallet():
    username = input("Username:")
    for i in user:
        if i[0] == username:
            print("Current wallet balance: ", i[1])
            return
        
#update the wallet amount.
def updateWallet():
    username = input("Username:")
    amount = input("Enter the amount to be added.")
    for i in user:
        if i[0] == username:
            i[1] = str(int(i[1]) + int(amount))
            return
        print("User does not exist.")

#get all the items in the inventory.
def getItemsInventory():
    for i in inventory:
        print(i)

        
        
#Driver Code........
dict1 = {
    "1": addItem,
    "2": addItemToInventory,
    "3": addUser,
    "4": addToCart,
    "5": updateCart,
    "6": removeFromCart,
    "7": getCart,
    "8": cartCheckout,
    "9": getWallet,
    "10": updateWallet,
    "11": getItemsInventory
}

def myMain(val):
    dict1[val]()

print("Enter 1 to add a new item.")
print("Enter 2 to add an item to inventory.")
print("Enter 3 to add a new user.")
print("Enter 4 to add an item to cart.")
print("Enter 5 to update the quantity of an existing item in the cart.")
print("Enter 6 to delete an item from the cart.")
print("Enter 7 to get the cart of a user.")
print("Enter 8 to check out.")
print("Enter 9 to get user wallet amount.")
print("Enter 10 to update user wallet amount.")
print("Enter 11 to get all the items in inventory.")
print("Enter q to exit the terminal.")
val = input("Enter a value.")

while val.lower()!='q':
    myMain(val)
    print("Enter 1 to add a new item.")
    print("Enter 2 to add an item to inventory.")
    print("Enter 3 to add a new user.")
    print("Enter 4 to add an item to cart.")
    print("Enter 5 to update the quantity of an existing item in the cart.")
    print("Enter 6 to delete an item from the cart.")
    print("Enter 7 to get the cart of a user.")
    print("Enter 8 to check out.")
    print("Enter 9 to get user wallet amount.")
    print("Enter 10 to update user wallet amount.")
    print("Enter 11 to get all the items in inventory.")
    print("Enter q to exit the terminal.")
    val = input("Enter a value.")
