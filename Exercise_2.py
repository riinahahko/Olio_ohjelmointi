# File: Exercise_2.py
# Author: Riina Hahko
# Description: Exercise2, Task 3



def main(): 

    # 3.
    
    while True:
        user_input = input("Exercise points: ")

        try:
            point = int(user_input)

            if point >= 0 and point <= 120:
                
                if point >= 60 and point < 71:
                    print("Your grade is: 1")

                elif point >= 71 and point < 83:
                    print("Your grade is: 2")

                elif point >= 83 and point < 95:
                    print("Your grade is: 3")

                elif point >= 96 and point < 107:
                    print("Your grade is: 4")

                elif point >= 107 and point <= 120:
                    print("Your grade is: 5")
                    
                elif point < 60:
                    print("Your grade is: 0") 
                break

            else:
                print("Error: exercise points cannot be < 0 or > 120.")
        
        except ValueError:
            print("Error: exercise points cannot be < 0 or > 120.")
        

main()

def main(): 

    #5
    student_name = []
    current_student = ""
    student_amount = 0
    student_grade = []
    current_grade = 0
    grade_total = 0

    while True:
        current_student = input("Give students first name: ")
        student_name.append(current_student)
        student_amount += 1

        while True:
            try: 
                current_grade = int(input("Give students grade: "))
                if current_grade >= 0 and current_grade <= 5:
                    student_grade.append(current_grade)
                    grade_total += current_grade
                    break

                else:
                    print("Error; enter a grade between 0-5")
            except ValueError:
                print("Error; enter a grade between 0-5")
    
        user_choice = ""
        
        while user_choice != "Y" or user_choice != "y" or user_choice != "N" or user_choice != "n":
            user_choice = input("Do you want to add more students? Y/N: ")

            if user_choice == "Y" or user_choice =="y":
                break
            elif user_choice == "N" or user_choice == "n":
                break
        
        if user_choice == "Y" or user_choice == "y":
            continue
        elif user_choice == "N" or user_choice == "n":
            break

    print("The average grade from all students is: ", grade_total/student_amount)

main()
