#task 2 to make a to do list
tasks=[]
def addtask():
    task=input("please enter a task: ")
    #now append it to the tasks array 
    tasks.append(task)
    print(f"task '{task}' added to the list")
#define a function listtask
def listtask():
    if not tasks:
        print("there are no tasks currently")
    else:
        print("current tasks: ")
        for index, task in enumerate(tasks):#we use enumerate function to get both the index and value of the element in the list
            print(f"task #{index}. {task}")
#now define another function deletetask
def deletetask():
    #call the function that we still have to write 
    listtask()
    try:
        tasktodelete=int(input("choose the number of the task you want to delete: "))
        if tasktodelete>=0 and tasktodelete < len(tasks):
            tasks.pop(tasktodelete)
            print(f"task '{tasktodelete}' has been deleted from the list")
        else:
            print(f"task '{tasktodelete}' was not found")#in the curly braces we write the variables name 
    except:
        print("invalid")
#create a main method 
if __name__=="__main__":
    #write a welcome statement
    print("welcome to the to do list app")
    #create a loop to run the app we'll use while loop tht will run infinetly until we tell it to stop 
    while True:
        print("\nplease select one of the following options")
        #list all the menu options you want in your app 
        print("----------------------------------------------")
        print("1. Add a task")
        print("2. Delete a task")
        print("3. List task")
        print("4. Exit")
        #now we need to give choices to user to choose from 
        choice=int(input("enter your choice between 1-4: "))
        #now use conditional statements
        if choice==1:
            addtask()
        elif choice==2:
            deletetask()
        elif choice==3:
            listtask()
        elif choice==4:
            break
    #if the user chooses option 4 then print thankyou statement 
    print("thankyou for using this app")