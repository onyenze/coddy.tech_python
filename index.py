# challenge 1
print("Hello World!")

# challenge 2
var = 5

# challenge 3
coddy = "I am learning to code with Coddy!"

# challenge 4
boolean = True

# challenge 5
k = 88
PI = 3.14
name = "bob"

# challenge 6
count = 0
count += 4
count *= 2
count -= 1

# challenge 7
n1 = 8
n2 = 9
n3 = n1>n2

# challenge 8
b1 = 5>2
b2 = 4>2
b3 = b1 or b2

# challenge 9
a=6
b=4
c = b * a

# challenge 10
b1 = True
b2 = True
b3 = False

# Don't change the line below
b4 = b1 and b2 and (not b3)

# challenge 11
a = 20
b = 15

# Don't change below this line
c = 0
if a >= b and not b < 10:
    c = 2

c += 1

# challenge 12
wind = int(input()) # Don't change this line
status = "unset"

if wind < 8:
    status="Calm"
elif wind >=8 and wind <= 31:
    status ="Breeze"
elif wind >=32 and wind <=63:
    status = "Gale"
else:
    status = "Storm"


# challenge 13
    n1 = int(input()) # Don't change this line
n2 = int(input()) # Don't change this line
op = input() # Don't change this line
result = 0

if op == "+":
    result = n1+n2
elif op == "-":
    result = n1-n2
elif op == '/':
    result = n1/n2
elif op == "*":
    reslut = n1*n2

# challenge 14
rnd = input() # Don't change this line
print(f"The input is: {rnd}")

# challenge 15
for i in range (3,28):
    print(f"Hello Coddy:{i}")

# challenge 16
var = float(input())

while var >= 3.5:
    var /= 2
print(var)

# challenge 17
for i in range(1, 11):
    if i == 6:
        break
    print(i)