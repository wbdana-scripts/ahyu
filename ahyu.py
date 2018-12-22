import os
import subprocess
import git


aur_path = '/home/wbdana/aur-packages'
aur_packages = [dir_name for dir_name in os.listdir(aur_path) if os.path.isdir(os.path.join(aur_path, dir_name))]
aur_packages = filter(lambda x: x[0:1] != '.', aur_packages)
aur_packages = [x for x in aur_packages if x is not None]
aur_packages.sort()


class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)


def loop_update_packages():
    for aur_package in aur_packages:
        path = aur_path + '/' + aur_package
        with cd(path):
            print(os.getcwd())
            print(aur_package)
            repo = git.Repo(path)
            print("repo " + str(repo))
            origin = repo.remotes.origin
            origin.pull()
            subprocess.call(['cat', 'PKGBUILD'])
            response = input("Would you like to update ${}? [Y / n]".format(aur_package))
            if response == "y" or response == "Y":
                subprocess.call(['makepkg', '-sirc'])


loop_update_packages()
