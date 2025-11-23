# Playing with filters

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared = filter(lambda x: x < 3, numbers)
print(list(squared))