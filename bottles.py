beverage = "beer"

for count in range(100):
    print(count, "bottles of", beverage, "on the wall")
    print(count, "bottles of", "water")
    print("Take one down, pass it around")
    count = count - 1
    print(count, "bottles of", beverage, "on the wall")

    print("")

print("No more bottles of beer on the wall, no more bottles of beer.")