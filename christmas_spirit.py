quantity_of_decorations = int(input())
days_left_until_christmas = int(input())

day_counter = 0
total_spirit = 0
total_price = 0

for day_counter in range(1,days_left_until_christmas+1):

    if day_counter % 11 == 0:
        quantity_of_decorations += 2
    if day_counter % 2 == 0: # buy ornament set every 2nd day
        total_price += 2*quantity_of_decorations
        total_spirit += 5
    if day_counter % 3 == 0: # buy tree skirts and tree garlands every 3rd day
        total_price += 8*quantity_of_decorations  # 5 + 3
        total_spirit += 13# 3 + 10
    if day_counter % 5 == 0: # buy tree lights every 5th day
        total_price += 15*quantity_of_decorations
        total_spirit += 17
    if day_counter % 15 == 0: # additional spirit
        total_spirit += 30
    if day_counter % 10 == 0:
        total_spirit -= 20 # cat ruins the tree
        total_price +=23   #15 + 3 + 5
        if days_left_until_christmas == day_counter:
            total_spirit -= 30


# if days_left_until_christmas % 10 == 0:
#     total_spirit -= 30
print(f"Total cost: {total_price}")
print(f"Total spirit: {total_spirit}")
