from  datetime import timedelta,date

class Borrowing_order:
    def __init__(self , book_id , cliend_id , status):
        self.__start_data = date.today()
        self.__end_data = date.today() + timedelta(days=int(input('your days : ')))
        self.__book_id = book_id
        self.__cliend_id = cliend_id
        self.__status = status

    def get_start_data(self):
        return self.__start_data
    def get_end_data(self):
        return self.__end_data
    def get_book_id(self):
        return self.__book_id
    def get_cliend_id(self ):
        return self.__cliend_id
    def get_status(self ):
        return self.__status
    def display(self):
        return {
            'Book ID : ' : self.__book_id,
            "Client ID" : self.__cliend_id,
            "Status now " : self.__status,
            'Start day ': self.__start_data,
            "End day" :self.__end_data
        }
