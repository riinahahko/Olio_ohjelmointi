# File: cellphone_main.py
# Author: Riina Hahko
# Description: 

import cellphone

def main():
        
        cellphone_list = []
        
        for i in range(0,6):

            Cell_1 = cellphone.Cellphone()
            print("Enter the details of your device")
            Cell_1.setID(i+1)
        #Aina kun kutsutaan jonkin sisäistä asiaa lisää piste. 

            print("Enter the manufacturer: ")
            Cell_1.setManufact()

            print("Enter the model: ")
            Cell_1.setModel()

            print("Enter the retail price: ")
            Cell_1.setRetail()

            cellphone_list.append(Cell_1)
            print(f"Details you have given:\n{Cell_1}")

        print(cellphone_list)
        
        
    
main()