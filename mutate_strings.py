first_str = input()
second_str = input()
new_str = ""

for i in range(0, len(first_str), 1):
    new_str = second_str[:i+1] + first_str[i+1:]
    if first_str[i] != second_str[i]:
        print(new_str)
