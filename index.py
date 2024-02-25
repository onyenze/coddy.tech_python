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


# challebge 18
    



# challenge 19
def calculate_sum():
    total_sum = sum(range(1, 10001))
    print( total_sum)

def main():
    try:
        num_iterations = int(input("Enter the number of times to execute the function: "))
        for _ in range(num_iterations):
            calculate_sum()
    except ValueError:
        print("Please enter a valid number.")


main()

# challenge 20


def calculate_product(num1, num2):
    product = num1 * num2
    print( product)

def main():
    try:
        num1 = float(input())
        num2 = float(input())
        calculate_product(num1, num2)
    except ValueError:
        print("Please enter valid numbers.")


main()


# challenge 21
def get_bigger(num1, num2):
    if num1 >= num2:
        return num1
    else:
        return num2

def iterate_operations(iterations, num1, num2):
    bigger_num = get_bigger(num1, num2)
    for _ in range(iterations):
        if num1 < 2 or num2 < 2:
            break
        bigger_num = get_bigger(num1, num2)
        bigger_num /= 2
        if num1 >= num2:
            num1 = bigger_num
        else:
            num2 = bigger_num
        print(bigger_num)

def main():
    try:
        iterations = int(input())
        num1 = float(input())
        num2 = float(input())
        iterate_operations(iterations, num1, num2)
    except ValueError:
        print("Please enter valid numbers.")

main()


# challenge 22
usernameInput = input()
passwordInput = input()

def is_valid(username, password):
    valid_usernames = ["admin", "user"]
    if username == "admin":
        return True
    elif username == "user" and password == "qweasd":
        return True
    else:
        return False


print(is_valid(usernameInput, passwordInput))


# challenge 23
def values(lst):
    for i in range(len(lst)):
        print(lst[i], end=' ')

# challenge 24 
def change_element(lst, index, new_element):
    if 0 <= index < len(lst):
        lst[index] = new_element
        return lst
    else:
        print("Index out of range")
        return lst
    
# challenge 25
def merge(list1, list2):
    merged_list = sorted(list1 + list2)
    return merged_list

# challenge 26
def prod(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

# challenge 27
def reverse(numbers):
    reversed_list = []
    for i in range(len(numbers) - 1, -1, -1):
        reversed_list.append(numbers[i])
    return reversed_list

# Example usage:
# result = reverse([1, 2, 3])
# print(result)  # Output: [3, 2, 1]


# challenge 28
def values(lst):
    for i in range(len(lst)):
        print(lst[i])

# Example usage:
my_list = [10, 20, 30, 40, 50]
values(my_list)

# challenge 29
def print_pyramid(n):
    # Print the upper part of the pyramid
    for i in range(1, n + 1, 2):
        spaces = " " * ((n - i) // 2)
        stars = "*" * i
        print(spaces + stars + spaces)

# Input
n = int(input())

# Check if the input is within the specified range
if n % 2 != 0 and 1 <= n < 1000:
    print_pyramid(n)
else:
    print("Input must be an odd integer within the range [1, 1000).")

# challenge 30
def transpose(lst):
    # Get the number of rows and columns in the original list
    num_rows = len(lst)
    num_cols = len(lst[0]) if lst else 0
    
    # Transpose the list
    transposed = []
    for j in range(num_cols):
        transposed_row = []
        for i in range(num_rows):
            transposed_row.append(lst[i][j])
        transposed.append(transposed_row)
    
    return transposed