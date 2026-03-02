#import os
# folder="My_files"
# if not os.path.exists(folder):
#     os.makedirs(folder)
# for i in range(1,11):
#         file_name=f"file_{i}.py"
#         full_path = os.path.join(folder, file_name)
#         with open(full_path, "w") as f:
#          f.write(f"This is file number {i}")
# print("10 file has been created!")


#file name changed which is inside on the folder
# import os
#old_file=os.path.join("folder name","file name")
# old_file=os.path.join("My_files","file_1.txt")

#new_file=os.path.join(folder name,new file name which you want to changed!)
# new_file=os.path.join("My_files","file.txt")

# os.rename(old_file,new_file)
# print("file name has been changed")



#folder name changed
# import os
#os.rename("old folder name","New folder name")
# os.rename("my_files","os_module in py")

import os
folder="os_module"
if not os.path.exists(folder):
    os.makedirs(folder)
for i in range(1,11): # if i delete 10 out of 11 we use (2,11)
#file create inside the folder
    file_name=f"module {i}.py"
    file_path=os.path.join(folder,file_name)
#     with open(file_path,"w") as f:
#      f.write(f"this is file{i}")
# print("10 file successfully created!")


# Note:file delete in os module
    # file_to_delete = os.path.join(folder, f"lesson_{i}.py")
    # if os.path.exists(file_to_delete):
    #     os.remove(file_to_delete)
    
#file rename changed
#     old_name = os.path.join(folder, f"module {i}.py")
#     new_name = os.path.join(folder, f"lesson_{i}.py")
#     if os.path.exists(old_name):
#      os.rename(old_name, new_name)