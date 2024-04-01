my_list = ['samsung', 'apple', 'asus', 'intel', 'amd']
my_list1 = my_list.sort(key=len)
if my_list == my_list1:
    print("Text_identical", my_list1)
else:
    print("Text_not_identical", my_list)
