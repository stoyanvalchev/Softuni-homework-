events = ["coding", "dog", "cat", "movie"]
coffee_count = 0
string = input()

while string != "END":

    if any(x in string.lower() for x in events):
        if string.isupper():
            coffee_count += 2
        else:
            coffee_count += 1

    string = input()

if coffee_count <= 5:
    print(coffee_count)
else:
    print("You need extra sleep")
