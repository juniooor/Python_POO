def bisexto(year):
    leap = False
    if (year % 4 == 0 and year % 100 !=0) or (year % 400 == 0):
        leap=True
        return leap
    else:
        leap = False
        return leap
    
year = int(input())

print(bisexto(year))



