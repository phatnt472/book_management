class Book:
    __book_number = 0

    def __init__(self,book_id=0,name="",year=0):
        self.__book_id = book_id
        self.__name = name
        self.__year = year
        Book.__book_number +=1
    
    def get_book_number(self):
        return self.__book_number

    def get_book_id(self):
        return self.__book_id
    
    def get_name(self):
        return self.__name
    
    def get_year(self):
        return self.__year
    
    def set_name(self,name):
        self.__name = name
    
    def set_year(self,year):
        self.__year = year

    def set_book_id(self,book_id):
        self.__book_id = book_id

    name = property(get_name, set_name)
    book_id = property(get_book_id, set_book_id)
    year = property(get_year, set_year)

   


