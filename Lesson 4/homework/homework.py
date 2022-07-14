str = "43 більше ніж 34 але менше ніж 56"
match = [sum(int(number) for number in str.split() if number.isdigit())]
print(*match)

my_list = ["animal", "Andy", "Bob", "apple", "134"]
my_list2 = [ i for i in my_list if  i.lower().startswith('a')]
print(my_list2)

list_1 = ["apple", "banana", "Bob", 5, 10, 15]
list_2 = [10, 15, 35, "animal", "apple", "Bob"]
difference_1 = set(list_1).difference(set(list_2))
difference_2 = set(list_2).difference(set(list_1))
list_3 = list(difference_1.union(difference_2))
print(list_3)

my_list3 = []
print("Введите символы")
my_str = input()
if len(my_str) % 2 !=0:
    my_str += '_'
while len(my_str) > 0:
    my_list3.append(my_str[:2])
    my_str = my_str[2:]
print(my_list3)


