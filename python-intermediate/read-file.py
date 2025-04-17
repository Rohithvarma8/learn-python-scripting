"""
reading and writing a file in python

syntax :- (Opening a file)
    - file = open("filename.txt", "mode")
    
    common modes:-
        Mode	Description
        'r'	    Read (default)
        'w'	    Write (overwrite)
        'a'	    Append (add at end)
        'x'	    Create new file
        'b'	    Binary mode (rb, wb)
        't'	    Text mode (default)
"""

"""
    def create_file(filename):
        try:
            with open(filename, "x") as name_file:  # throws you an error not preferred to use if file already exsits always use it with try-except block
                pass

        except FileExistsError:
            print("Sorry File already exsists")

    def write_file(filename, text):
        with open(filename, "w") as name_file: # overwrites the exsisting data in the text better use append
            name_file.write(text)

    def read_file(filename):
        with open(filename,"r") as name_file:
            contents = name_file.read()
            print(contents)

    if __name__ == "__main__":
        filename_1 = "create-file.txt"
        create_file(filename_1)
        name = "rohith"
        write_file(filename_1, name)
        read_file(filename_1)

"""

# more better approach

def create_file(txt_file_name):
    try:
        with open(txt_file_name, "x") as txt_file:
            print("Text file is Created successfully")
    
    except FileExistsError:
        print("Sorry bro file exsists")

def write_file(txt_file_name, *args, **kwargs):
    with open(txt_file_name,"w") as txt_file: # since i don't want to have any duplicates i wrote "w" prefer "a"
        for line in args:
            txt_file.write(line + "\n")

        for key, value in kwargs.items():
            txt_file.write(f"{key} = {value} \n")

def append_file(txt_file_name, *args, **kwargs):
    with open(txt_file_name,"a") as txt_file: # since i don't want to have any duplicates i wrote "w" prefer "a"
        for line in args:
            txt_file.write(line + "\n")

        for key, value in kwargs.items():
            txt_file.write(f"{key} = {value} \n")


def read_file(txt_file_name):
    with open(txt_file_name, "r") as txt_file:
        contents = txt_file.read()
        print(contents)


if __name__ == "__main__":
    file_1 = "person.txt"
    create_file(file_1)
    write_file(file_1, "This is a file for person details", "", "details: ", name="Rohith", age=23) #prefer calling only once since it rewrites
    append_file(file_1, nationality="India", gender="Male")
    read_file(file_1)
