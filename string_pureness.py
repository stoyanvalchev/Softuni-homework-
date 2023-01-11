n = int(input())
not_pure_items =[",", ".", "_"]
for i in range (n):
    str_name = input()
    # if not str_name.__contains__(not_pure_items):
    if not any(x in str_name for x in not_pure_items):
        print(f"{str_name} is pure.")
    else:
        print(f"{str_name} is not pure!")