def count(list_var):
    value = []
    for i in list_var:
        count = 0
        for j in i:
            count += 1
        value.append(count)
    return value

ab = ['abc','defgh','pqrstuvw']
print(count(ab))