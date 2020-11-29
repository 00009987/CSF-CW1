student_names = []
ordered_names = {}
started = True


def name_inserting():
    name = input('>')
    if name.lower() == 'stop':
        global started
        started = False
    else:
        global student_names
        student_names.append(name)

    if len(student_names) == 2:
        print("When you finish, type 'Stop'.")


def enumerate_names():
    global ordered_names
    ordered_names = dict(enumerate(student_names))


print("Please enter your students' names one by one.")
while started:
    name_inserting()
    enumerate_names()

for item in ordered_names:
    print(f'{item + 1}. {ordered_names[item]}')

