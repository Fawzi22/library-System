from Client import Client
class Librarian(Client):
    def __init__(self, full_name ,age , id_no , phone_number , salary = 0.0):
        super().__init__( full_name ,age , id_no , phone_number)
        self.__salary = salary

    def get_salary(self):
        return self.salary

    def info(self):
        return {
            'id' : self.__id,
            "full_name" : self.__full_name,
            "age" : self.__age,
            'id_no': self.__id_no,
            "phone_number" :self.__phone_number,
            'Salary': self.__salary
        }
