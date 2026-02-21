def distinct(data):
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] == data[j]:
                return False
    return True

print(distinct("Avinasha"))  # False - has duplicate 'a'
print(distinct("abc"))       # True - all letters are different
print(distinct("hello"))     # False - has duplicate 'l'