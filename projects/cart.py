class Item:
  def __init__(self, name, price):
    self.name = name
    self.price = price

class Store:
  def __init__(self):
    self.__cart = []


  def addToCart(self, item):
    self.__cart.append(item)

  def removeFromCart(self,index):
    self.__cart.pop(index)


  def calculateTotal(self):
    total = 0
    for item in self.__cart:
      total += item.price

    return total
  def displayCart(self):
    for i in range(0, len(self.__cart)):
      print (i, self.__cart[i].name, self.__cart[i].price)

  def cartLength(self):
    return len(self.__cart)
store = Store()
store.displayCart()


print("Hello welcome to our store")
while True:
  store.displayCart()
  store.calculateTotal()

  print("Press A to add item")
  print("Press R to remove item")
  print("Press X to Exit")
  userInput = input("Please enter a command ")
  if userInput == "x":
    break
  elif userInput == "a":
    itemName = input("Please give the item a name ")
    
    hasValidPrice = True
    while hasValidPrice:
      price = input("Please give the item a price ")
      if price.isnumeric():
        store.addToCart(Item(itemName, int(price)))
        hasValidPrice = False
        
  elif userInput == "r":
    index = int(input("Please give the index of item to remove "))

    cartLength = store.cartLength()
    
    while index < 0 or index >= cartLength:
      index = int(input("Please give a valid index of item to remove "))
      
      
    store.removeFromCart(index)

  else:
    print("Please enter a valid input")
  