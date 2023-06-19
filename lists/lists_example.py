# remove item by index
weekdays = ['sun','mon','tue','wed','thu','fri','sun','mon','mon']
weekdays.pop(2)
print(weekdays)
# ['sun', 'mon', 'wed', 'thu', 'fri', 'sun', 'mon', 'mon']

# remove item by index using del
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
del a[-1]
print(a)
# [0, 1, 2, 3, 4, 5, 6, 7, 8]

#Also supports slices:
del a[2:4]
print(a)
# [0, 1, 4, 5, 6, 7, 8, 9]

# count the occurrences of an individual element by using a <count()> function.
weekdays = ['sun','mon','tue','wed','thu','fri','sun','mon','mon']
print(weekdays.count('mon'))

# 3

weekdays = ['sun','mon','tue','wed','thu','fri','sun','mon','mon']
print([[x,weekdays.count(x)] for x in set(weekdays)])

# [['tue', 1], ['thu', 1], ['wed', 1], ['sun', 2], ['fri', 1], ['mon', 3]]


# convert a list into a string
weekdays = ['sun','mon','tue','wed','thu','fri','sat']
listAsString = ' '.join(weekdays)
print(listAsString)

# convert a list into a tuple
weekdays = ['sun','mon','tue','wed','thu','fri','sat']
listAsTuple = tuple(weekdays)
print(listAsTuple)

# convert a list into a set (also it removes duplicates)
weekdays = ['sun','mon','tue','wed','thu','fri','sat','sun','tue']
listAsSet = set(weekdays)
print(listAsSet)

names = ['Chris', 'Jack', 'John', 'Damal']
print(names[-1][-1])
# l

import copy

def test():
    a = [[1, 2, 3], [4, 5, 6]]
    b = copy.copy(a)
    #b = copy.deepcopy(a)
    print(a)
    # [[1, 2, 3], [4, 5, 6]]
    print(b)
    # [[1, 2, 3], [4, 5, 6]]
    a[0][1] = 10
    print(a)
    # [[1, 10, 3], [4, 5, 6]]
    print(b)  # b changes too -> Not a deepcopy.
    # [[1, 10, 3], [4, 5, 6]]

    x = 3
    y = x
    print(x, y)
    print(id(x), id(y))
    y = 4
    print(x, y)
    print(id(x), id(y))

test()

def longest(my_list):
    return max(my_list, key=len)

list1 = ["111", "234", "2000", "goru", "birthday", "09"]
print(longest(list1))

def extend_list_x(list_x, list_y):
    list3 = [list_y, list_x]
    flatten_list = sum(list3, [])
    print(str(list3))
    print(str(flatten_list))

x = [4, 5, 6]
y = [1, 2, 3]
extend_list_x(x, y)
#[1, 2, 3, 4, 5, 6]