print(2 ** 5) # Exponentiation


# Floor division OR Integer Division is a normal division operation except that it returns the largest possible integer. 
# This integer is either less than or equal to the normal division result
print(10//3)  # 3 
print(-10//3) # -4



# The result of standard division (/) is always a float, even if the dividend is evenly divisible by the divisor
print(type(10 / 5)) # <class 'float'>

# When the result of floor division (//) is positive, it is as though the fractional portion is truncated off, leaving only the integer portion. When the result is negative, the result is rounded down to the next smallest (greater negative) integer

'''
&=
Bitwise AND assignment.

^=
Bitwise XOR assignment.

|=
Bitwise OR assignment.
'''
x=5

y = bin(x)
print(y)
y = bin(3)
print(y)

x^=3
print(x) # 5 XOR 3 = 6

x=5
x&=3
print(x) # 5 AND 3 = 1

x=5
x|=3
print(x) # 5 OR 3 = 7

x=5
x<<=1
print(x) # 5 left shift by 1 = 10 
x=5
x<<=2
print(x) # 5 left shift by 1 = 20
x=5
x>>=1
print(x) # 5 right shift by 1 = 2
