#Create a program that given a list, outputs number of homes above average price
prices = [125000, 78000, 110000, 65000, 300000, 250000, 210000, 150000, 165000, 140000, 125000, 85000, 90000, 128000, 230000, 225000, 100000, 300000]
av = (sum(prices)/len(prices))
count = 0
for house in prices:
    if house > av:
        count += 1

print(count)