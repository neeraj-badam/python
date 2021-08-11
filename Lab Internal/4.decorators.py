#function decorators
def italic(function):
    def inner():
        return '<i>'+function()+'</i>'
    return inner

def bold(function):
    def inner():
        return '<b>'+function()+'</b>'
    return inner

def underline(function):
    def inner():
        return '<u>'+function()+'</u>'
    return inner

@bold
@underline
@italic
def hello():
    return ("hey")

print(hello())