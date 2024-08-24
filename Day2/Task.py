# class Books:
#     def bookMethod(self,book) :
#         print("this Book Name is "+book)

# class Authors:
#     def authorMethod(self,author) :
#         print("authors is "+author)        

# class Prices(Authors,Books):
#     def __init__(self,book,author,price):
#         super().bookMethod(book)
#         super().authorMethod(author)
#         print("Price is :"+str(price))

# obj=Prices("python","A1",1000)


 #Another method
class Books:
    def __init__(self, book):
        print("This Book Name is " ,book)
        
    def __init__(self, author,hi):
        print("Author is " ,author)

class Authors:
    def __init__(self, author):
        print("Author is " ,author)

class Prices(Books, Authors):
    def __init__(self, book, author, price):
        Books.__init__(self, book)  
        Authors.__init__(self, author)   
        print("Price is: ",price)

obj = Prices("Python", "A1",1000)
