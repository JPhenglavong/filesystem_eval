#Got stuck on implementing cd
#cd - go into subfolder with given cd(folder_name) or cd() goes back home or cd(1) steps back 1
#/folders are like Nodes in a LinkedList. Will use set of strings for files
#Filesystem: /home {/user, /library} -> /user {/jp} -> /jp {/desktop, notes} -> /desktop {resume}
#                                    -> /library {libfile1, libfile2}

class FileSystem:
    def __init__(self):
        self.headval = None

class Folder:
    def __init__(self, name):
        self.name = name
        self.dataval = set()
        self.parentfolder = None

#ls() - list all files/folders inside set of current folder
    def ls(self):
        print(f"{self.name} contains {self.dataval}")

#touch(file_name) - create file with given name
    def touch(self, file_name):
        if file_name not in self.dataval:
            self.dataval.add(file_name)
            print(f"File {file_name} has been created.")
        else:
            print(f"File {file_name} already exists!")

#mkdir(folder_name) - create folder with given name
    def mkdir(self, folder_name):
        if folder_name not in self.dataval:
            self.dataval.add(folder_name)
            print(f"Folder {folder_name} has been created.")
        else:
            print(f"Folder {folder_name} already exists!")



#Filesystem: /home {/user, /library, homeFile} -> /user {/jp, passwords} -> /jp {/desktop} -> /desktop
#                                    -> /library {libfile1, libfile2}
filesystem = FileSystem()
home = Folder("/home")
user = Folder("/user")
library = Folder("/library")
jp = Folder("/jp")
filesystem.headval = home

home.ls()
home.mkdir(user.name)
home.mkdir(library.name)
home.mkdir(library.name)
home.touch("homeFile")
home.touch("homeFile")
home.ls()
user.mkdir(jp.name)
user.touch("passwords")

jp.mkdir("desktop")
jp.ls()

library.touch("libfile1")
library.touch("libfile2")
library.ls()

