# menuy.py - function style menu
# Imports typically listed at top
# each import enables us to use logic that has been abstracted to other files and folders
from Week0 import animation, matrix, menu, Tree
from Week1 import fibonacci, list
from Week2 import gcd, factorial, factor

# Main list of [Prompts, Actions]
# Two styles are supported to execute abstracted logic
# 1. file names will be run by exec(open("filename.py").read())
# 2. function references will be executed directly file.function()
main_menu = [
    
]

# Submenu list of [Prompt, Action]
# Works similarly to main_menu
sub_menu = [
    ["animation", animation.cupcake],
    ["Tree", Tree.grow_tree],
   # ["Palindrome", palindrome.tester]
]

patterns_sub_menu = [
    ["swap", menu.swap],
    ["matrix", matrix.tester ],
    ["fibonacci", fibonacci.tester],
    ["factorial", factorial.tester],
    ["GCD", gcd.gcd],
    ["Factors", factor.tester],

]
data_sub_menu = [
    ["for loop", list.tester1],
    ["while loop", list.tester2 ],
    ["recursive loop", list.tester3 ]
    

]
# Menu banner is typically defined by menu owner
border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"

# def menu
# using main_menu list:
# 1. main menu and submenu reference are created [Prompts, Actions]
# 2. menu_list is sent as parameter to menuy.menu function that has logic for menu control
def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Miscellaneous", submenu])
    menu_list.append(["Math", patterns_submenu])
    menu_list.append(["Data", datasubmenu])
    buildMenu(title, menu_list)

# def submenu
# using sub menu list above:
# sub_menu works similarly to menu()
def submenu():
    title = "Function Submenu" + banner
    buildMenu(title, sub_menu)
def datasubmenu():
    title = "Function Submenu" + banner
    buildMenu(title, data_sub_menu)

def patterns_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, patterns_sub_menu,)

def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
        
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    # end validation try

    buildMenu(banner, options)  # recursion, start menu over again


if __name__ == "__main__":
    menu()
