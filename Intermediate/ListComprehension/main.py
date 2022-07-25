numbers = [1,2,3]
new_numbers = [nums + 1 for nums in numbers]
print(new_numbers)

# range is end exclusive
range_list = [n * 2 for n in range(1,5)]
print(range_list)

veget = ["apples", "bananas", "jeff", "hugo"]
# return the string with only 4 letters (with if-statement)
new_veget = [n for n in veget if len(n) == 4]
print(new_veget)

new_veget2 = [n.upper() for n in veget if len(n) > 4]
print(new_veget2)
