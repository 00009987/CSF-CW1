# declaring and initializing variables to keep track of user inputs
student_names = []
ordered_names = {}
# switcher of while loop
started = True


# a function that helps user to enter names
def name_inserting():
    name = input('>')
    # when user finishes entering names, this will trigger
    if name.lower() == 'stop':
        global started
        started = False
    else:
        # inserting names to the above-mentioned list
        global student_names
        student_names.append(name)

    # reminder about how to finish the application
    if len(student_names) == 2:
        print("When you finish, type 'Stop'.")


# a function which turns list into a dictionary so that it can be enumerated and ordered
def enumerate_names():
    global ordered_names
    ordered_names = dict(enumerate(student_names))


# an actual process starts here
print("Please enter your students' names one by one.")
while started:
    name_inserting()
    enumerate_names()

# showing user ordered list of names
for item in ordered_names:
    print(f'{item + 1}. {ordered_names[item]}')

