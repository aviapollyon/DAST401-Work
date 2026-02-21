def distinct(data):
    if isinstance(data, str):
        data = data.lower()
    else:
        data = [str(item).lower() for item in data]
    
    return len(data) == len(set(data))

print(distinct("Avinasha"))  # False - has duplicate 'a'
print(distinct(["a", "b", "c"]))       # True - all letters are different
print(distinct("hello"))     # False - has duplicate 'l'