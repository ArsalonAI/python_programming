class Page:
    def __init__(self, words, page_number):
        self.words = words
        self.page_number = page_number
    
    # overloaded additional method to add two pages    
    def __add__(self, other):
        new_words = self.words + other.words
        new_page_number = max(self.page_number, other.page_number) + 1
        return Page(new_words, new_page_number)
    
page1 = Page("Arsalon is a good teacher! ", 1)
page2 = Page("He's also handsome.", 2)
page3 = page1 + page2
print(page3.words, page3.page_number)
 
class StoreItem:
    TAX = 0.12
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.after_tax_price = 0
        self.set_after_tax_price()
    
    def set_after_tax_price(self):
        self.after_tax_price = round(self.price * (1 + self.TAX))
        
    def __sub__(self, discount):
        return StoreItem(self.name, self.price - discount)   
    
    def __mul__(self, value):
        return StoreItem(self.name, round(self.price * value)) 
        
bread = StoreItem("Bread", 7)
discounted_bread = bread - 2
print(discounted_bread.price)
discounted_bread_2 = bread * 0.8
print(discounted_bread_2.price)
