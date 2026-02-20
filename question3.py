def create_list(x,y):
    # =  y
    result = list(range(y+1))
    print(result)
    for i in range(y):
        result[i] = x * (x)
    return result

print(create_list(2,8))