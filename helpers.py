# Thomas Safago
# 03/03/2025


from Variable import Variable
from Function import Function


# Helpers
def Variables(*args):
    return [Variable(arg) if type(arg) is str else arg for arg in args]

def Functions(*args):
    return [Function(arg) if type(arg) is str else arg for arg in args]
