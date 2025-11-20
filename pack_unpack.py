# Tuples

# Tuples a re hashable and immutable sequences, typically used to store collections of heterogeneous data.
coords = set() #lists not hashable (a requirement for sets), but tuples are
#a = [1, 2]
#b = [2, 2]

#Changed lists to tuples
a = (1, 2)
b = (2, 2)
coords.add(a)
coords.add(a)
coords.add(a)
coords.add(b)
print(coords)

#unpacking a tuple into variables
a, b, c = (1, 2, 3)
print(a, b, c)  # Output: 1 2 3

#packing variables into a tuple
x = 1
y = 2
z = 3
packed = (x, y, z)
print(packed)  # Output: (1, 2, 3)

# Memory with tuples vs lists
a = [1, 2]
b = [1, 2]
print(id(a))
print(id(b))  # Different memory addresses

# On the other hand, tuples with the same content may share memory
c = (1, 2)
d = (1, 2)
print(id(c))
print(id(d))  # May be the same memory address

