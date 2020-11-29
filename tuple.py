# A VERY SIMPLE USAGE EXAMPLE OF DICTIONARY, LIST, TUPLE AND ITEMS METHOD,

# declaring a dictionary that holds data
capitals = {
    'Uzbekistan': 'Tashkent',
    'Germany': 'Berlin',
    'United Kingdom': 'London',
    'Russia': 'Moscow',
    'United States': 'Washington'
}

# returning a list of tuples that holds data from the dictionary
tuple_value = list(capitals.items())

print(tuple_value)
