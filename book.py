import random
class Book:
    def __init__(self , title , description , author ):
        self.__id = random.randint(1,1000)
        self.__title = title
        self.__description = description
        self.__author = author
        self.__status = 'Not ordered'

    def get_id(self):
        return self.__id
    def get_title(self):
        return self.__title
    def get_description(self):
        return self.__description
    def get_author(self):
        return self.__author
    def get_status(self ):
        return self.__status

    def display(self):
        return {
            'Book Id : ' : self.__id,
            'Title : '  : self.__title,
            'Description : ' : self.__description,
            'Author : ' : self.__author,
            'State : ' : self.__status
        }
