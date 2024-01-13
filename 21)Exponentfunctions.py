print(2**3) #2power3






def raise_to_power(base_no, power_no):
    result = 1
    for i in range(power_no):
        result=result*base_no
    return result
rel=raise_to_power(2,5)
print(int(rel))