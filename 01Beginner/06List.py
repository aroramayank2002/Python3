l = [1,"h",3.4 ,4 ,2 ,3 ]

print(l)
print(len(l))

print(l[1])
print(type(l))
print(l[:]) # All
print(l[:2]) # value at index 2 is not included
print(l[1:3]) # value at index 1 is included
print(l[-2]) # Access from right, starts from 1 ( not 0 )
print(l[-2:-3]) # []
print(l[-2:-1]) # [2]
print(l[-5:-1]) # ['h', 3.4, 4, 2]
print(l[-2:-0]) # []
print(l[-2:0]) # []

for x in l:
    print(x)

# Combine list
x = [1,2]
print(l+x)
print(x*2) # No other operations cab be done
print(max(x)) # would not work if list has str
print(min(x)) # would work if list has float

x.append(3)
print(x)

x.insert(0,5)
print(x)

x.remove(5) # value is removed, # Value error if element not found
print(x) 

x.pop(2) # Remove from index
print(x)


print(l.index("h")) # Index of value

x = [2,4,1,6,2,3]
x.sort()
print(x)

x = [2,4,1,6,2,3]
print(sorted(x)) # x is not modified

# Touples (), immutable.
y = (5,2,4)
# Won't work update, pop, sort
# y[2]=3 TypeError: 'tuple' object does not support item assignment
print(sorted(y)) # ok
# y.sort() error
#y.pop(2)

#To change a Tuples cast them
y = list(y)
y[2] = 1
y = tuple(y)
print(y)