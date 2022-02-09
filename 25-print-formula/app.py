import math

def calculateFormula():
    c = 50
    h = 30
    
    d = input("Insert a comma separated values: ")
    d = d.split(",")
        
    res = []
    for value in d:
        res.append(round(math.sqrt(2 * c * int(value.strip()) / h)))

    return res
        
print(calculateFormula())