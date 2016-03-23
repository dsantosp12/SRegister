# Use this helper to install library
# This will install the library and update
# the requirements file and push it to GitHub

import os


def get_library_name():
    """Return the command to run"""
    return input("Enter the library name >> ")


def run_command(library_name):
    """Return the exit code of the command ran"""
    command = "pip3 install %s" % library_name
    return os.system(command)


def update_requirements():
    """Use pip3 freeze to update the file."""
    os.system("pip3 freeze > requirements.txt")


def push_to_github(library_name):
    """This push the updated file to the repo"""
    os.system(
        "git add requirements.txt "
        "&& git commit -m '{} installed' "
        "&& git push".format(library_name))


def menu():
    print("[1] Install Only")
    print("[2] Install and Push")
    print("[0] Quit")
    while True:
        choice = input(">> ")
        if choice is "1" or choice is "2" or choice is "0":
            break
        else:
            print("The selection is not valid")
            continue
    return choice


def install_and_push():
    push_to_github(
        install_only()
    )


def install_only():
    """Get the name of the library, install it and return
    the name of the library for farther useage."""
    lib_name = get_library_name()
    if run_command(lib_name) is 0:
        update_requirements()
    else:
        raise FileNotFoundError("This library was not installed")
    return lib_name


def run():
    selection = menu()

    if selection is "1":
        install_only()

    elif selection is "2":
        install_and_push()

    elif selection is "0":
        quit()


if __name__ == '__main__':
    run()
