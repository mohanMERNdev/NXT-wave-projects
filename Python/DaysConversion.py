n = int(input())
years = n // 365
weeks = (n - (years * 365)) // 7
days = (n - ((years * 365) + (weeks* 7)))
print(str(years) + " " + "years " + str(weeks) + " " + "weeks " + str(days) + " " + "days")
