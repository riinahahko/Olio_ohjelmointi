# File: cellphone.py
# Author: Riina Hahko
# Description: Task 4, programming demo


import random

class Cellphone:
    def __init__(self):
        self.id = 0
        self.manufacturer = ""
        self.model = ""
        self.retail = 0 

    def setID(self, value):
        self.id = value

    def setManufact(self):
        self.manufacturer = input("")
    
    def setModel(self):
        self.model = input("")
    
    def setRetail(self):
        self.retail = int(input(""))

    def getManufact(self):
        return self.model 

    def getRetail(self):
        return self.retail

    def getModel(self):
        return self.model

    def __str__(self):
        return (
            f"Phone ID: {self.id} \n"
            f"Manufacturer: {self.manufacturer} \n"
            f"Model: {self.model} \n"
            f"Retail price: {self.retail} \n"
        )
    # \n tekee uuden rivin outputille.

