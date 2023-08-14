"""def fun(greatting, name='You'):
    return '{}, {}.'.format(greatting, name)
#Using default argument in the function.
print(fun("Hi"))"""

"""def fun(name, place):
    return (f'{name}, {place}.')

print(fun('Ravi', 'Germany'))"""

def country_info(*args, **kwargs):
    print(args)
    print(kwargs)

state=['delhi','southIndia','NorthEast']
food={'Delhi': 'State of food','SouthIndia':'Briyani', 'NorthEast':'Momo'}

print(country_info(*state,**food))
