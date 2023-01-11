all_budget = float(input())
kg_flour = float(input())
pack_of_eggs = 0.75 * kg_flour
liter_milk = 1.25 * kg_flour
count_of_loafs = 0
coloured_eggs = 0
budget_for_one_loaf = kg_flour + pack_of_eggs + liter_milk/4

while all_budget >= 0:
    all_budget -= budget_for_one_loaf
    if all_budget < 0:
        all_budget +=budget_for_one_loaf
        break
    count_of_loafs+=1
    coloured_eggs+=3

    if count_of_loafs % 3 == 0:
        coloured_eggs = coloured_eggs - (count_of_loafs - 2)

print(f"You made {count_of_loafs} loaves of Easter bread! Now you have {coloured_eggs} eggs and {all_budget:.2f}BGN left.")
