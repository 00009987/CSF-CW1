# ------ FUNCTIONAL APPROACH ------ #
# functional programming is a programming paradigm with software primarily composed of functions processing 
# data throughout its execution. python allows us to code in a functional, declarative style.

# this app creates 3 web template files (such as index.html, style.css, app.js) automatically every time it runs

def file_names():
    names = []
    # receiving names of the files
    html_name = input('HTML name: ')
    css_name = input('CSS name: ')
    js_name = input('JS name: ')

    # pushing names to the list
    names.append(html_name)
    names.append(css_name)
    names.append(js_name)
    # returning name list
    return names


def create_files():
    # receiving name list
    names = file_names()
    # declering extensions of the files
    extensions = ['.html', '.css', '.js']

    for i in range(0, len(names)):
        # creating the files according to their order
        file = open(f'{names[i]}{extensions[i]}', 'w')
        file.close()


# invoking the function
create_files()




# ------ OBJECT-ORIENTED APPROACH ------ #
class TemplateFiles:
    # the constructor is called when an object is created from a class and
    # it allows the class to initialize the attributes of the class
    def __init__(self, html_name, css_name, js_name):
        self.html_name = html_name
        self.css_name = css_name
        self.js_name = js_name
    
    def create_files(self):
        # declering names list
        names = []
        names.append(self.html_name)
        names.append(self.css_name)
        names.append(self.js_name)
        # declering extensions of the files
        extensions = ['.html', '.css', '.js']

        for i in range(0, len(names)):
            # creating the files according to their order
            file = open(f'{names[i]}{extensions[i]}', 'w')
            file.close()

# creating TemplateFiles instance
template1 = TemplateFiles('index', 'style', 'app')
template1.create_files()