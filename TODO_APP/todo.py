print("\n"+"TODO_DO_DO")
print("#########################")

from prettytable import PrettyTable
import sys


sys.stdout.write("\n1.Enter -l   Lists all the tasks.\n2.Enter -a   Adds a new task.\n3.Enter -r   Removes an task.\n4.Enter -c   Completes an task.\n \n ")
   
my_todo_list = []
y = PrettyTable()
completed = []

def my_list():                                                                                      
   y.field_names = ["","not completed yet: ",len(my_todo_list)]
   todonum = 0
   for i in my_todo_list:
      todonum += 1
      y.add_row(["[ ]",i,todonum])
   for c in completed:
      y.add_row(["[x]",c,"DONE"])
   print(y.get_string(title="TO DO List"))
   y.clear_rows() 

with open("save.txt","r") as f:
   read = f.readlines()
   for line in read:
      if line.rstrip("\n"):
         my_todo_list.append(line)
   f.close()      
         
with open("save2.txt", "r") as f:
   comtask = f.readlines()
   for coms in comtask:
      if coms.rstrip("\n"):
         completed.append(coms)    
   f.close()      


#########################################################################################  
if __name__ == "__main__":
   try:

      if len(sys.argv) > 2 and sys.argv[1] == "-a":
         new_task = sys.argv[2]
         my_todo_list.append(new_task)
         
      
      elif sys.argv[1] == "-a":
         new = input("write down...please"+"\n")
         my_todo_list.append(new)
         my_list()


      elif sys.argv[1] == "-l":
            while True:
               my_list()
               break

      elif sys.argv[1] == "-r":
         while True:
            my_list()
            remove_item = int(input("\nplease enter a number of an item you want to delete: "))
            remove_item -= 1
            del my_todo_list[remove_item]
            break
            
      elif sys.argv[1] == "-c":
         while True:
            my_list()
            comnum   = int(input("\nwhich task you wanna mark? "))
            comnum -= 1
            c = my_todo_list[comnum]
            completed.append(c)
            del my_todo_list[comnum]
            break
            

      else: 
         sys.stdout.write("Enter valid value.")
            
            
      with open("save.txt", "w") as f:
         for rows in my_todo_list:
            f.write(rows + "\n")
      f.close()
      with open("save2.txt", "w") as f:
         for cows in completed:
            f.write(cows +"\n")  
      f.close()
   except IndexError:
      pass