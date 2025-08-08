def narcissistic(value):
    a = str(value)
    sum = 0
    for i in a: 
        sum += int(i)**len(a)
    if sum == value:
        return True
    else:
        return False