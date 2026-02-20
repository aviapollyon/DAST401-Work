def is_multiple(x, y):
    if y == 0:
        raise ValueError("y cannot be zero")
    if x % y == 0:
        print(True)
        return True
    else:
        print(False)
        return False
    
is_multiple()

x = "my name" #string

x = 1  # int
