beverage = "beer"

for count in range(100):
    
    if count == 94:
        print("If one of those bottles should happen to fall, 98 bottles of beer on the wall...")
    else:
        print(count, "bottles of", beverage, "on the wall")
        print(count, "bottles of", "water")
        if count%2 == 0:
            print("Take one down, pass it around")
        else:
            print("if one of those bottles should happen to fall")
        count = count - 1
        print(count, "bottles of", beverage, "on the wall")

    print("")

print("No more bottles of beer on the wall, no more bottles of beer.")
print("We've taken them down and passed them around; now we're drunk and passed out!")