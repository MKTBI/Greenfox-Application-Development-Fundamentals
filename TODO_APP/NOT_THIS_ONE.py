print("TODO_DO_DO")
print("#########################")

from prettytable import PrettyTable

intro = "\n1.Enter L   Lists all the tasks.\n2.Enter A   Adds a new task.\n3.Enter R   Removes an task.\n4.Enter C   Completes an task.  "
print(intro)

my_todo_list = []
y = PrettyTable()

def list():
    y.field_names = ["","not completed yet: ",len(my_todo_list)]
    todonum = 0
    for i in my_todo_list:
        todonum += 1
        y.add_row(["[ ]",i,todonum])
    print(y.get_string(title="TO DO List"))
    y.clear_rows()
    
########################################################################  
run = True
while run: 
    user = input("\nWhat do you want to do? (A,L,R,C) : ").lower()
    if user == "a":
        new_todo = input("\nPlease enter your new TODO: ").lower()
        my_todo_list.append(new_todo)
        print("you added new TODO to do")
        
        
    elif user == "l":
        while True:
                list()
                break
        
    elif user == "r":
       while True:
        remove_item = int(input("\nplease enter a number of an item you want to delete: "))
        remove_item -= 1
        del my_todo_list[remove_item]
        break

    elif user == "c":
       while True:
            compeleted = []
            comnum = int(input("\nwhich task you wanna mark? "))
            comnum -= 1
            c = my_todo_list[comnum]
            compeleted.append(c)
            for i in compeleted:
                y.add_row(["[x]",i,"DONE"])
            del my_todo_list[comnum]
            list()
            break
        
    elif user == "" or user == "   ":
        print("please write something.")
    else:
        print("Enter valid value.")