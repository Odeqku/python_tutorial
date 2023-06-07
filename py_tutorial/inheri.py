#!/usr/bin/python3

class Manager:
    def __init__(self, Name, Department, Years_of_service, respon):
        self.__Name = Name
        self.__Department = Department
        self.__Years_of_service = Years_of_service
        self.__responsibility(respon)
    def responsibility(self, respon):
        self.respon = respon
        print('I am {}, and my department is {}, my years of experience is {} and my responsibility include \'{}\''.format(self.__Name, self.__Department, self.__Years_of_service, self.respon))
    __responsibility = responsibility

job = Manager('Yewande', 'Networking', 10, "Coordinating members of staff and field contractors")

'''
job.responsibility("\'Coordinating members of staff and field contractors\'")
'''
