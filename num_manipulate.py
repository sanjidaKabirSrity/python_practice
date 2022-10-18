import os

li = []

while True:
    print("Menu:")
    print("1. Add")
    print("2. Insert")
    print("3. Edit")
    print("4. Delete")
    print("5. Display")
    print("0. Exit")
    print("Enter a Menu:", end="")
    
    #os.system("clear")

    num1 = int(input())
    
    if num1 == 1 :
        add_num = int(input("Please Enter a Integer value: ")) 
        li.append(add_num)
    elif num1 == 2 :
        index = int(input("Inserted an index: "))
        insert_num = int(input("Insert the value: "))
        li.insert(index, insert_num)
    elif num1 == 3 :
        length = len(li)
        print("Please enter an index between 0 to ", length-1, ": ", end = "")
        index_num = int(input())
        li[index_num] = int(input("Enter the value: "))
    elif num1 == 4 :
        length = len(li)
        print("Please enter an index between 0 to ", length-1, ": ", end = "")
        index_num = int(input())
        temp = li[index_num]
        del(li[index_num])
        print("The deleted number ", temp)
    elif num1 == 5 :
        print(li)
    elif num1 == 0 :
        break

    

