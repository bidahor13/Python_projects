import os
def rename_files():
    #(1)get file name from the  folder
    file_list = os.listdir(r"C:\Users\Babatunde\Desktop\WOU\AAAA\Fall 2015\CS133\Python_GitHub_Files\P8_wk3_Bacity\prank")
    #print(file_list)
    saved_path = os.getcwd()
    print("Current working directory" + saved_path)
    os.chdir(r"C:\Users\Babatunde\Desktop\WOU\AAAA\Fall 2015\CS133\Python_GitHub_Files\P8_wk3_Bacity\prank")

    # for each file, rename filename
    for file_name in file_list:
        #os.rename(src, dst)
        os.rename(file_name, file_name.lstrip("0123456789") )
    os.chdir(saved_path)    
    
rename_files()
