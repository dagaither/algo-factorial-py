def factorial(num):
    product = 1
    while num > 1:
        product *= num
        num -= 1
    return(product)
