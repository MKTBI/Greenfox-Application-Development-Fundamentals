
# TODO application




### Documentation


this app by using sys module in python will get inforamtion
such as task from the user and store them 
first for strating this program we need to import two module 
```import sys``` and ``` from prettytable import PrettyTable```
__________________________________________________________________
##### [prettytable](https://pypi.org/project/prettytable/)
is a A simple Python library for easily displaying tabular data in a 
visually appealing ASCII table format which is give beautiful look
to our project and is safe to use

__________________________________________________________________


there is two list in this project first by name : ```my_todo_list```
and second one ```completed``` 
when program start to run and look for the function which is define for it 
if program can't find the functions will only show the options menu 
to the user 
and if program can find the function will run the function that called for.

### functions
#### [-a]
there is two way to add new task into this program:
first by writing this function [-a] and press enter, program will ask
user to write the new task 
and second way is write [-a] as argv[1] and user write something as 
argv[2]
after user adding the new task, task will get add to my_todo_list
and prettytable will show it to the user 
#### [-r]
this function will show the list to the user and remove any task that user 
call for 
#### [-c]
after compeleting one task user can call for this function and mark
the task they want as compelet 
after calling this function program will go and remove the task from 
my_todo_list and add the same task to compeleted list which have 
diffrent look from normal task 
#### [-l]
this function by looking up the list in program will show compeleted
task and uncompeleted task in one place for user

### final look
```
 +----------------------------------+
|            TO DO List            |
+-----+---------------------+------+
|     | not completed yet:  |  2   |
+-----+---------------------+------+
| [ ] |        test 1       |  1   |
|     |                     |      |
| [ ] |        test 2       |  2   |
|     |                     |      |
| [x] |        test 3       | DONE |
|     |                     |      |
+-----+---------------------+------+
```



