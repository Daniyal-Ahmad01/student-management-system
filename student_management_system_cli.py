students=["Ali","Ahmad"]


def add_student(students):
    name=input("Enter the name of the student whom you want to add: ")
    students.append(name)
    print(f"Added student {name}\nList after adding name is {students}","\n")


def remove_student(students):
    rm=input(f"{students}\nWrite the name you want to remove: ")
    if rm in students:
        students.remove(rm)
        print(f"Removed name {rm}\nList after removing the name is:")
    else:
        print("It is already not in the list")
    print(students,"\n")
    

def search_student(students):
    search=input("Enter the name you want to search for: ")
    if search in students:
        print(f"The name you provided was found in the list at index {students.index(search)}\n{students}\n")
    else:
        print(f"Not found\n{students}\n")


def save_students(students):
    file=input(f"Enter the name of the file in which you want to save the list {students} : ")
    with open(file,"w+") as f:
        f.write(str(students))
        f.seek(0)
        print(f"Saved in file {file} as {f.read()}\n")


def show_menu():
    print("Press 1 to add student\nPress 2 to remove student\nPress 3 to search for the student\nPress 4 to save the list of students to file\nPress 5 to quit")


while True:    
    try:
        show_menu()
        choice=int(input("Enter your choice: "))
        if choice==1:
            add_student(students)
        elif choice==2:
            remove_student(students) 
        elif choice==3:
            search_student(students)
        elif choice==4:
            save_students(students)
        elif choice==5:
            break
        else:
            print("Invalid choice!\n")
    except ValueError:
        print("Value should be appropriate!\n")

print("Program ended")