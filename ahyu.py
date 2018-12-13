import os

aur_path = '/home/wbdana/aur-packages'
aur_packages = [dir_name for dir_name in os.listdir(aur_path) if os.path.isdir(os.path.join(aur_path, dir_name))]
aur_packages = filter(lambda x: x[0:1] != '.', aur_packages)

def loop_update_packages():
    for dir in aur_packages:
        print(dir)

loop_update_packages()