# -------- VOID FUNCTION -------- #
# Void functions are created to perform a particular task without returning any values 

# receiving user inputs and converting x and y to integer
x = int(input('First number: '))
y = int(input('Second number: '))
operator = input('Operator (type +, -, *, /):')

# x, y, and operator below are arguments  
def simpleCalculator(x, y, operator): 
    # according to user's provided operator, calculations will be performed
    if operator == '+':
        # showing result to the user
        print(x + y)
    elif operator == '-':
        print(x - y)
    elif operator == '*':
        print(x * y)
    elif operator == '/':
        # validating division
        if y == 0:
            print(f'{x} can not be divided by 0')
        else:
            print(x // y)
    else:
        # validating operator
        print('Please enter only +, -, *, or /')

# invoking the function
simpleCalculator(x, y, operator)




# -------- VALUE RETURNING FUNCTION -------- #
# a return is a value that a function returns to the calling script or function when it completes its task. 

# receiving user inputs and converting x and y to integer
z = int(input('First number: '))
t = int(input('Second number: '))
operator2 = input('Operator (type +, -, *, /):')

def calculator(z, t, operator2):
    # according to user's provided operator, calculations will be performed
    if operator2 == '+':
        # receiving sum of numbers
        result = sumNums(z, t);
    elif operator2 == '-':
        # receiving difference of numbers
        result = subtractNums(z, t)
    elif operator2 == '*':
        # receiving multiplication of numbers
        result = multiplyNums(z, t)
    elif operator2 == '/':
        # receiving division of numbers
        result = divideNums(z, t)
    else:
        # validating operator
        print('Please enter only +, -, *, or /')
    # showing user's the calculation result
    print(result)
    

# Helper Functions that return values
def sumNums(z, t):
    return (z + t)


def subtractNums(z, t):
    return (z-t)


def multiplyNums(z, t):
    return (z * t)


def divideNums(z, t):
    # validating division
    if t == 0:
        return (f'{z} can not be divided by 0')
    else:
        return (z // t)

# invoking the function
calculator(z, t, operator2)