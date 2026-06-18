l=["Ali","Ahmad"]
while True:    
    try:
        print("Press 1 to add student\nPress 2 to remove student\nPress 3 to search for the student\nPress 4 to save the list of students to file\nPress 5 to quit")
        choice=int(input("Enter your choice: "))
        if choice==1:
            l.append(input("Enter the name of the student whom you want to add: "))
            print(l,"\n")
        elif choice==2:
            rm=input(f"{l}\nWrite the name you want to remove: ")
            if rm in l:
                l.remove(rm)
            else:
                print("It is already not in the list")
            print(l,"\n")
        elif choice==3:
            search=input("Enter the name you want to search for: ")
            if search in l:
                print(f"The name you provided was found in the list at index {l.index(search)}\n{l}\n")
            else:
                print(f"Not found\n{l}\n")
        elif choice==4:
            file=input(f"Enter the name of the file in which you want to save the list {l} : ")
            with open(file,"w+") as f:
                f.write(str(l))
                f.seek(0)
                print(f"Saved in file {file} as {f.read()}\n")
        elif choice==5:
            break
        else:
            print("Invalid choice!\n")
    except ValueError:
        print("Value should be appropriate!\n")
print("Program ended")