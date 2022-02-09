def total_cost(dollar, cent, ncupcakes):
    cents = (ncupcakes * dollar * 100) + (ncupcakes * cent)
    
    return int(cents / 100), cents % 100

print(total_cost(10, 15, 2))
