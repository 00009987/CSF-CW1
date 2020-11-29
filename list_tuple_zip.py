# AN APPLICATION THAT HELPS TO CALCULATE TOTAL COST OF EACH PRODUCT


# declaring lists to store user inputs
names = []
numbers = []
prices = []
# initializing a variable to control while loop
started = True


# a function to ask user the name, number and price of the products
def about_product():
    print('Enter name of the product:')
    product_name = input('>')
    names.append(product_name)

    print('Enter number of the product:')
    product_number = int(input('>'))
    numbers.append(product_number)

    print('Enter price of the product (in US dollars):')
    product_price = float(input('>'))
    prices.append(product_price)


# a function to find out if user has more products to add or not
def finish_question():
    print('Is that all?')
    answer = input('Y (for Yes) / N (for No)').upper()
    # according to user's input, started variable's value changes
    if answer == 'Y':
        global started
        started = False
    # when input is N, user can again type out one more product details
    elif answer == 'N':
        about_product()
        finish_question()
    # when input is not Y or N then recursion will happen till input is equal to valid one
    else:
        finish_question()


# actual process where user is asked to enter inputs
while started:
    about_product()
    finish_question()

# looping through each item in lists to calculate total cost of the product
# zip(names, numbers, prices) => this will return list of tuples such as[(name, number, price), (name, number price)...]
# (name, number, price) in zip(names, numbers, prices) => unpacking each item according to its order
for (name, number, price) in zip(names, numbers, prices):
    total_price = str(number * price)
    # showing the user total cost of each item
    print(f'The total cost of {name} is ${total_price}')
