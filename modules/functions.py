dynamic_path = "todos.txt"
""" 
Functions.py will open the file read the content (get_todos) and
write the data accordingly (write_todos)
"""
print ("Dynamic path defined in functions.py")

""" base_dir = os.path.join("D:","Udemy", "D6")  
sub_dir = "Bonus"
dynamic_path = os.path.join(base_dir, sub_dir,"todos.txt") """

def cursor_position():
    #checks if each line has new line character
    #if it does go to next line if not add a carriage return
    with open(dynamic_path, "a+") as file:
        while True:
            line = file.readline()
            line_length = len(line)

            if line_length > 0 and line[line_length-1] == "\n":
                #print("new line")
                pass
            else:
                #with open(dynamic_path, "a") as append:
                #You have to use a+ to append to end of the file
                file.write("\n")
            #if text does not exist exit the loop
            if not line:
                break


def get_todos():
    with open(dynamic_path, 'r') as file:
        todos_local = file.readlines() #should be a different name that is local
    return todos_local

def write_todos(new_todos):
    with open(dynamic_path, 'w') as file:
        file.writelines(new_todos)  #This will automatically close the file

#testing functions.py
if __name__ == "__main__":
    print("Hello")
    print(get_todos())

    #This will only happen in the functions module
    #__name__ is the name of the function you are currently running (directly). 
    #inside functions is main outside it is the name of the program