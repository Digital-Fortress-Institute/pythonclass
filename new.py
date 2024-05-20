def myadd(x , y):
    try:
        return(kx + y)
    except TypeError:
        return ('Strings can not be evaluated')
    except NameError:
        return ("Invalid Parameter")
print(myadd(20, 30))
print(myadd('a', 30))
print(myadd(20, 30))
print('Success')
print('Application Running End Here')