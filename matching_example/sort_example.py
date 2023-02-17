def myFunc(str: str):
    return str.lower()

sentence = 'The quick brown fox jumps over the lazy dog'

my_list = sentence.split(" ")
my_list.sort(key=(lambda x: x.lower()))
print(my_list)
