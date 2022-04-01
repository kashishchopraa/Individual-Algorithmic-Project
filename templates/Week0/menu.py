"""
Introduction to Console Programming
Writing a function to print a menu
"""


# Menu options in print statement
def print_menu1():
    print('1 -- Stringy' )
    print('2 -- Numby' )
    print('3 -- Listy' )
    print('4 -- Exit' )
    runOptions()


# Menu options as a dictionary
menu_options = {
    1: 'Stringy',
    2: 'Numby',
    3: 'Listy',
    4: 'Exit',
}

# Print menu options from dictionary key/value pair

numbers = [ [1,2,3],[4,5,6],[7,8,9] ]

def matrix():
   for i in numbers:
      print(i)

def swap():
  num1 = input('Enter First Number: ')
  num2 = input('Enter Second Number: ')

  print("Value of num1 before swapping:", num1)
  print("Value of num2 before swapping:", num2)

  temp = num1
  num1 = num2
  num2 = temp

  print("Value of num1 after swapping: ", num1)
  print("Value of num2 after swapping: ", num2)
  
def print_menu2():
    for key in menu_options.keys():
        print(key, '--', menu_options[key] )
    runOptions()

# menu option 1
def stringy():
    print('You chose \' 1 -  Stringy\'')

# menu option 2
def numby():
    print('You chose \' 2 - Numby\'')

# menu option 3
def listy():
    print('You chose \'3 - Listy\'')


# call functions based on input choice
def runOptions():
    # infinite loop to accept/process user menu choice
    while True:
        try:
            option = int(input('Enter your choice 1-4: '))
            if option == 1:
                stringy()
            elif option == 2:
                numby()
            elif option == 3:
                listy()
            # Exit menu
            elif option == 4:
                print('Exiting! Thank you! Good Bye...')
                exit() # exit out of the (infinite) while loop
            else:
                print('Invalid option. Please enter a number between 1 and 4.')
        except ValueError:
            print('Invalid input. Please enter an integer input.')

if __name__=='__main__':
    # print_menu1()
    print_menu2()