for x in range(5):
    print(x)
print("-------")
for x in range(2,5):
    print(x)

print("-------")

x=0
while x < 5:
    if x == 3:
        break
    x += 1
    print(x)

print("-------")

x=0
while x < 5:
    x += 1
    if x == 3:
        continue
    print(x)

print("-------")

x=10
if x < 40:
    pass # for later implementation

for x in range(5):
    pass

print("passed")