from filecmp import dircmp
from shutil import copy
import sys, os
from threading import Thread


# copy the different files. 

def copy_diff_files_in_subdirs(dircmp_obj: dircmp, src: str, dest: str): 
    for cd in dircmp_obj.common_dirs: 
        print("Common dirs " + cd)
        for df in dircmp_obj.subdirs[cd].diff_files: 
            src_file_path = src + "/" + cd + "/"+ df
            dest_file_path = dest + "/" + cd + "/"+ df
            # copy the files. 
            copy(src_file_path, dest_file_path)
        # recursive call to the function so that it can check the subdirs. 
        copy_diff_files_in_subdirs(dircmp_obj.subdirs[cd], src + "/" + cd, dest+ "/" + cd)

# delete the files only in the right hand side. 
def remove_files_in_dest(dircmp_obj: dircmp, dest: str):
    # print the files in the right. 
    # print(dircmp_obj.right_only)
    for fs in dircmp_obj.right_only:
        file_path = dest + "/" + fs
        os.remove(file_path) if os.path.isfile(file_path) else os.removedirs(file_path)

    for key, value in dircmp_obj.subdirs.items():
        remove_files_in_dest(value, dest + "/" + key)

def copy_files_added_to_source(dircmp_obj: dircmp, src: str, dest: str):
    for fs in dircmp_obj.left_only:
        src_file_path = src + "/" + fs
        copy(src_file_path, dest)

    for dir_key in dircmp_obj.subdirs.keys:
        dir_val = dir_obj.subdirs[dir_key]
        copy_files_added_to_source(dircmp_obj[dir_key], src + "/" + dir_key, dest + "/" + dir_key)



def files_info(dircmp_obj: dircmp) -> dircmp:
    dircmp_obj.phase0()
    dircmp_obj.phase1()
    dircmp_obj.phase2()
    dircmp_obj.phase3()
    dircmp_obj.phase4()
    dircmp_obj.phase4_closure()
    return dircmp_obj


cmp: list[str] = sys.argv[1:len(sys.argv)]
dircmp_obj = dircmp(cmp[0], cmp[1])

dircmp_obj = files_info(dircmp_obj)


copy_diff_thread = Thread(target=copy_diff_files_in_subdirs, args = (dircmp_obj, cmp[0], cmp[1]))
copy_diff_thread.run()
remove_diff_thread = Thread(target=remove_files_in_dest, args = (dircmp_obj, cmp[1]))
remove_diff_thread.run()
copy_files_thread = Thread(target=copy_files_added_to_source, args = (dircmp_obj, cmp[0], cmp[1]))
copy_files_thread.run()

