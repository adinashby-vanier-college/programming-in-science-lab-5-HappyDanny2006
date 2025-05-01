# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    result = ""
    if n == 1:
        result += "*"
    else:
        space = (n-2)
        result += "*" * n
        for i in range(n - 2):
            result += "\n" + "*" + (space * " ") + "*"
        result += "\n"+("*" * n)
    return result.rstrip()

# 1
# 12
# 123
# 1234
def number_pattern(n):
    count = 0
    result = ""
    while count < n:
        j = 1
        count += 1
        while j <= count:
            result += str(j)
            j += 1
        result += "\n"
    return result.rstrip()

# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    count = 0
    sum= 0
    while count <= n:
        sum += count
        count += 1
    result = (sum)
    return result

# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    space = n - 1
    count = 1
    result = ""
    for i in range(1,n+1):
        result += " " * space + "*" * count + "\n"
        count += 2
        space -= 1
    return result.rstrip()

print(hollow_square(5))
