min = int(input())
year = int(min/60/24/30/12)
y = min/60/24/30/12
month = int((y-year)*12)
print(year,"\t",month)
