#Arithmetic Operators
a = 10
b = 3

print("Addition:", a + b)        # 13
print("Subtraction:", a - b)     # 7
print("Multiplication:", a * b)  # 30
print("Division:", a / b)        # 3.333...
print("Floor Division:", a // b) # 3
print("Modulus:", a % b)         # 1
print("Exponentiation:", a ** b) # 1000

#Assignment Operators
x = 5
x += 3  # x = x + 3 → 8
print("After += :", x)

x -= 2  # x = x - 2 → 6
print("After -= :", x)

x *= 4  # x = x * 4 → 24
print("After *= :", x)

x /= 6  # x = x / 6 → 4.0
print("After /= :", x)

x %= 3  # x = x % 3 → 1.0
print("After %= :", x)

#Comparison Operators
a = 7
b = 10

print("a == b:", a == b)  # False
print("a != b:", a != b)  # True
print("a > b:", a > b)    # False
print("a < b:", a < b)    # True
print("a >= b:", a >= b)  # False
print("a <= b:", a <= b)  # True

#Logical Operators
x = 5
print("x > 3 and x < 10:", x > 3 and x < 10)  # True
print("x > 10 or x < 3:", x > 10 or x < 3)    # False
print("not(x > 3):", not(x > 3))              # False

# Identity Operators
a = [1, 2]
b = a
c = [1, 2]

print("a is b:", a is b)      # True (same object)
print("a is c:", a is c)      # False (same value, different objects)
print("a is not c:", a is not c)  # True

#Membership Operators
colors = ["red", "blue", "green"]

print("'blue' in colors:", "blue" in colors)      # True
print("'yellow' not in colors:", "yellow" not in colors)  # True

#Bitwise Operator
a = 5        # 0b0101
b = 3        # 0b0011

print("a & b:", a & b)     # 1  (0101 & 0011 = 0001)
print("a | b:", a | b)     # 7  (0101 | 0011 = 0111)
print("a ^ b:", a ^ b)     # 6  (0101 ^ 0011 = 0110)
print("~a:", ~a)           # -6 (bitwise NOT → flips all bits of 5)
print("a << 1:", a << 1)   # 10 (shift bits left by 1 → 1010)
print("a >> 1:", a >> 1)   # 2  (shift bits right by 1 → 0010)
