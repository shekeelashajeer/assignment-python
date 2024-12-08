
# sum

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum_result=num1+num2

print(f"The sum of {num1} and {num2} is: {sum_result}")

# sum

num1 = int(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
sum_result = float(num1+num2)

print(f"The sum of {num1} and {num2} is : {sum_result}")

# interest

p = int(input("Enter principal amount : "))
t = float(input("Enter the time period : "))
r = float(input("Enter the interest rate : "))

si = float(p*r*t)/100
print("Simple Interest is : " ,si)

# pass or fail

mark = float(input("Enter your mark: "))
if mark >= 50:
    print("Passed")
else:
    print("Failed")

# grad

total_mark = float(input("Enter the total mark percentage: "))
if total_mark >90:
    grade = "A"
elif 80 <= total_mark <=89:
    grade ="B"
elif 70 <= total_mark <=79:
    grade ="C"
elif 60 <= total_mark <=69:
    grade ="D"
elif 50 <= total_mark <=59:
    grade ="E"
else: 
    grade = "Failed"

print(f"The grade is: {grade}")

# day

day_number = int(input("Enter the number (1 -7): "))
days = {
    1: "Sunday",
    2: "Monday",
    3: "Tuesday",
    4: "Wednesday",
    5: "Thursday",
    6: "Friday",
    7: "Saturday"
}
day = days.get(day_number, "Invalid Entry")
print(day)

# multiplication table

number = int(input("Enter the number: "))
print(f"Multiplication table for {number}: ")
for i in range(1, 11):
    print(f"{i}*{number} = {i*number}")

# sum of odd number

limit = int(input("Enter a limit: "))
sum_of_odds = sum(num for num in range(1, limit +1) if num % 2 != 0)
print(f"Sum of odd number = {sum_of_odds}")

# pattern

rows = 5
for i in range(1, rows + 1 ):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# swapping array

size = int(input("Enter the size of arrays: "))
array1 = list(map(int, input("Enter the values of Array 1: ").split(',')))
array2 = list(map(int, input("Enter the values of Array 2: ").split(',')))

array1, array2 = array2, array1

print("Arrays after swapping: ")
print("Array1:",','.join(map(str, array1)))
print("Array2:",','.join(map(str, array2)))

# even number

size = int(input("Enter the size of an array: "))
array = list(map(int, input("Enter the values of the array separated by commas: ").replace("","").split(',')))

even_count = sum(1 for num in array if num % 2 == 0)

print(f"Number of even number is given in the array is {even_count}.")

# Sorted array

size = int(input("Enter the size of an array: "))
array = list(map(int, input("Enter the value of an array separated by commas: ").split(',')))
 
array.sort(reverse=True)
print("Sorted array:")
print(", ".join(map(str, array)))

#  palindrome

string = input("Enter the string: ")
string_lower = string.lower()
if string_lower == string_lower[::-1]:
    print("Entered string is a palindrome")
else:
    print("Entered string is not a palindrome")

# sum of two array

size = int(input("Enter the size of arrays: "))
print("Enter the value of array 1:")
array1 = []
for i in range(size):
    row = list(map(int, input().split()) )
    array1.append(row)

print("Enter the value of array 2:")
array2 = []
for i in range(size):
    row = list(map(int, input().split()) )
    array2.append(row)

sum_array = []
for i in range(size):
    row_sum = []
    for j in range(size):
        row_sum.append(array1[i][j] + array2[i][j])
    sum_array.append(row_sum)

print("Sum of 2 arrays is:")
for row in sum_array:
    print(" ".join(map(str, row)))

# sum of two array

size = int(input("Enter the size of arrays: "))
print("Enter the value of array 1:")
array1 = []
for i in range(size):
    row = list(map(int, input().split()) )
    array1.append(row)

print("Enter the value of array 2:")
array2 = []
for i in range(size):
    row = list(map(int, input().split()) )
    array2.append(row)

sum_array = []
for i in range(size):
    row_sum = []
    for j in range(size):
        row_sum.append(array1[i][j] + array2[i][j])
    sum_array.append(row_sum)

print("Sum of 2 arrays is:")
for row in sum_array:
    print(" ".join(map(str, row)))

# function

def getArray(arr, size):
    print("Enter the value of array:")
    for i in range (size):
        arr[i] = int(input(f"Element {i+1}: "))
def displayArray(arr, size):
    print("The array values are:")
    for i in range (size):
        print(arr[i], end=" ")
    print()

def main():
    size = int(input("Enter the size of array: "))
    arr = [0] * size

    getArray(arr, size)
    displayArray(arr, size)

if __name__ ==" __main__":
    main()

# calculate grade


def calculate_grade(written_test, lab_exams, assignments):
   
    weight_written_test = 70
    weight_lab_exams = 20
    weight_assignments = 10

    grade = (written_test * weight_written_test / 100) + \
            (lab_exams * weight_lab_exams / 100) + \
            (assignments * weight_assignments / 100)
    return grade


print("Enter the marks scored by the student:")
written_test = float(input("Written test: "))
lab_exams = float(input("Lab exams: "))
assignments = float(input("Assignments: "))


grade = calculate_grade(written_test, lab_exams, assignments)


print(f"Grade of the student is {grade:.1f}")

# income tax


def calculate_income_tax(annual_income):
    tax = 0.0

    if annual_income > 10000000:
        tax += (annual_income - 10000000) * 0.30
        annual_income = 10000000
    if annual_income > 5000000:
        tax += (annual_income - 5000000) * 0.20
        annual_income = 5000000
    if annual_income > 250000:
        tax += (annual_income - 250000) * 0.05

    return tax

annual_income = float(input("Enter the annual income: "))

tax_amount = calculate_income_tax(annual_income)

print(f"Income tax amount = {tax_amount:.2f}")

# array next


def multiply_adjacent_values(input_array):
    result_array = []
    for i in range(len(input_array) - 1):
        result_array.append(input_array[i] * input_array[i + 1])
    return result_array

n = int(input("Enter the array limit: "))
print("Enter the values of array:")
input_array = [int(input()) for _ in range(n)]
output_array = multiply_adjacent_values(input_array)
print("Output:")
print(" ".join(map(str, output_array)))

# array function

def getArray(size):
    
    print(f"Enter the values for the array ({size}x{size}):")
    array = []
    for i in range(size):
        row = list(map(int, input().split()))
        array.append(row)
    return array

def addArray(array1, array2, size):
   
    result = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            result[i][j] = array1[i][j] + array2[i][j]
    return result

def displayArray(array):
   
    print("Resultant Array:")
    for row in array:
        print("\t".join(map(str, row)))

def main():
   
    size = int(input("Enter the size of the array: "))
    
    print("Array 1:")
    array1 = getArray(size)
    
    print("Array 2:")
    array2 = getArray(size)
    
    result = addArray(array1, array2, size)
    
    displayArray(result)


if __name__ == "__main__":
    main()




