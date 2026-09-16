# #1.	Write a program that stores your name, age, and GPA in variables and prints their types using type().
# name = "Shabab"
# age = 20
# gpa = 3.4
# print("Type of name: ", type(name))
# print("Type og age: ",type(age))
# print("Type of GPA: ", type(gpa))

# # 2.	Take two numbers as input and print their sum, difference, product, quotient, floor division, and modulus.
# num1 = int(input("Enter number 1: "))
# num2 = int(input("Enter number 2: "))
# sum = num1 + num2
# diff = num1 - num2
# product = num1 * num2
# quotient = num1 / num2
# div = num1 // num2
# mod = num1 % num2 

# print("Calculations")
# print("Sum = ", sum)
# print("Difference = ", diff)
# print("Product = ", product)
# print("Quotient = ", quotient)
# print("Floor division = ", div)
# print("Modulus = ", mod)

# #3.	Convert a temperature given in Fahrenheit (as a string input) to Celsius using type casting.
# print("\n")
# temp_in_fahrenheit = input("Enter temperature in Fahrenheit: ")
# temp_in_fahrenheit = int(temp_in_fahrenheit)
# in_celsius = (5/9) * (temp_in_fahrenheit - 32)
# print("Temperature in celsius: ", in_celsius)
# print("\n")

# #4.	Using f-strings, print a formatted receipt showing item name, quantity, price, and total (quantity × price).
# print("\n")
# name = "Toy car"
# quantity = 6
# price = 8000
# total = quantity * price
# print("Receipt")
# print(f"Item name: {name}\nQuantity: {quantity}\nPrice: {price}\nTotal: {total}")

# print("\n")

# #5.	Given radius r, compute and print the area and circumference of a circle (use round() to 2 decimals).
# import math
# r = 4
# area = math.pi * (r * r)
# circumference = 2 * math.pi * r
# print("Given r = ", r)
# print(f"Area of circle: {round(area,2)}")
# print(f"Cicumference of circle: {round(circumference,2)}")

#6.	Write a program using bitwise operators to check whether a given integer is even or odd (hint: n & 1).
# print("\n")
# num = int(input("Enter any number: "))
# print("0 = Even, 1 = Odd")
# print("Answer is ", num & 1)

#7.	Write a program to check whether a number is positive, negative, or zero using if-elif-else.
# print("\n")
# num = int(input("Enter number: "))
# if(num > 0):
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")
#8.	Print all prime numbers between 1 and 100 using nested loops and break.
# print("\n")
# print("Prime numbers between 1 and 100")
# for x in range(2,100):
#     count = 0
#     for y in range(2,x):
#         ans = x % y
#         if(ans == 0):
#             count = count + 1
#     if (count == 0):
#         print(x)
#     else:
#         continue
#9.	Write a function factorial(n) that returns n! using a while loop.
# print("\n")
# def factorial(n):
#     res = 1
#     while(n > 1):
#         res = res * n
#         n = n - 1
#     return res
# num = int(input("Enter any number: "))
# ans = factorial(num)
# print(ans)

#1.	Write a Python program that swaps the values of two variables without using a third variable.
# print("\n")
# variable_1 = 10
# variable_2= 20
# print("Before swapping\nVariable 1 = ", variable_1," Variable 2 = ", variable_2)
# variable_1, variable_2 = variable_2, variable_1
# print("Before swapping\nVariable 1 = ", variable_1," Variable 2 = ", variable_2)
#2.	Write a function is_prime(n) that returns True if n is a prime number, otherwise False.
# def is_prime(n):
#     if n < 2 :
#         return False
#     for i in range(2,n):
#         if n % i == 0:
#             return False
#     return True
# n = int(input("Enter any number: "))
# print(is_prime(n))
#3.	Write a program to print the Fibonacci sequence up to n terms using a loop.
# n = int(input("Enter number of terms: "))

# prev = 0
# curr = 1

# for i in range(n):
#     print(prev, end=" ")
    
#     new = prev + curr
#     prev = curr
#     curr = new
#4.	Write a function that takes a list of numbers and returns a new list with duplicates removed, preserving original order.
# def remove_duplicates(num_list):
#     new_list=[]
#     for i in num_list:
#         if i not in new_list:
#             new_list.append(i)
#     return new_list
# print("List after removing duplicates\n")
# print(remove_duplicates([4,5,6,8,2,3,4,5,7,23,98]))
#5.	Write a program that counts the number of vowels, consonants, digits, and spaces in a given string.
# str = "hello my name is $#@b@b! 07"
# is_letter = 0
# is_number = 0
# is_sign = 0
# is_space = 0
# special_signs = '!@#$%^&*()_+'
# for i in str:
#     if 'A' <= i <= 'Z' or 'a' <= i <= 'z':
#         is_letter = is_letter + 1
#     elif '0' <= i <= '9':
#         is_number = is_number + 1
#     elif i in special_signs:
#         is_sign = is_sign + 1
#     elif i == ' ':
#         is_space = is_space + 1
# print("String = ", str)
# print("Spaces = ",is_space)
# print("Letters = ", is_letter)
# print("Numbers = ", is_number)
# print("Signs = ", is_sign)

#8.	Write a function multiply(*args) that returns the product of any number of arguments using *args.
# def multiply(*args):
#     product = 1
#     for i in args:
#         product = product * i
#     return product
# print("Product = ", multiply(3,4,1))
#9.	Write a dictionary comprehension to create a dictionary mapping each character in a string to its frequency.
# str = input("Enter string: ")
# frequency = {char : str.count(char) for char in str}
# print("Frequency of letters\n", frequency)
print("\n")
#10.	Given a list of dictionaries representing employees (name, department, salary), 
# #write code to find the employee with the highest salary.
# employees = [
#     {'name' : 'Shabab', 'department' : 'CS','salary' : 8000},
#     {'name' : 'Zuriyat', 'department' : 'BBA','salary' : 9000},
#     {'name' : 'Noor', 'department' : 'AI','salary' : 6000},
#     {'name' : 'Ansa', 'department' : 'CS','salary' : 10000},
#     {'name' : 'Suhana', 'department' : 'CS','salary' : 7000},
# ]
# highest = employees[0]
# for i in employees :
#     if i["salary"] > highest["salary"]:
#         highest = i

# print(highest)

#11.	Write a program that checks whether a given string is a palindrome, ignoring case and spaces.
# str = "Race Car"
# str = str.lower().replace(" ", "")
# if str == str[::-1]:
#     print("Palindrome")
# else:
#     print("Not a plaindrome")

#12.	Write a lambda function combined with filter() to extract all odd numbers from a list.
# num_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
# odd_numbers = list(filter(lambda x : x % 2 != 0, num_list))
# print(odd_numbers)

#13.	Create a 1D NumPy array of integers from 1 to 30 and reshape it into a 5x6 matrix.
# import numpy as np
# one_d = np.array(range(1,31))
# reshaped = one_d.reshape(5,6)
# print("Array of integers\n",one_d)
# print("Reshaped\n", reshaped)
#14.	Using NumPy, create a 6x6 identity matrix and replace its diagonal with the values [1,2,3,4,5,6].
import numpy as np
# identity_matrix = np.eye(6,6)
# print(identity_matrix)
# np.fill_diagonal(identity_matrix, [1,2,3,4,5,6])
# print("Diagonal Filled\n", identity_matrix)


#15.	Given a NumPy array of 25 random integers between 1 and 100, find the sum, mean, and standard deviation.
# arr = np.random.randint(1, 100, 25)
# print("Sum = ",np.sum(arr))
# print("Mean = ", np.mean(arr))
# print("Standard Deviation = ", np.std(arr))

#16.	Given a 2D NumPy array of shape (4,4), extract the diagonal elements using np.diag() and compute their sum.
# arr = np.array([[1,2,3,4], [5,6,7,8], [7,8,7,5], [3,0,5,3]])
# diagonal = np.diag(arr)
# summ = np.sum(diagonal)
# print("Sum of diagonal is : ",summ)

#17.	Create two NumPy arrays of shape (3,3) and demonstrate the difference between 
# #element-wise multiplication (*) and matrix multiplication (@).
# arr1 = np.array([[1,2,3], [4,5,6], [7,8,9]])
# arr2 = np.array([[5,3,8], [2,4,9], [1,6,7]])
# print("element-wise multiplication\n", arr1 * arr2)
# print("matrix multiplication\n", arr1 @ arr2)

#18.	Given a NumPy array representing daily temperatures for a month, 
# #use boolean masking to find all days with temperature above 35°C and count them.
# temps = np.array([46,56,34,40,44,42,50,48,37,47,30, 29, 31, 28])
# hot_days = temps[temps > 35]
# print("Temperature above 35 C : ", hot_days)
# print("Total number of days with temperature > 35 : ", np.sum([temps > 35]))

#19.	Write NumPy code to normalize an array (scale all values to the range 0-1) using the formula (x - min) / (max - min).
# arr = np.array([10,20,30,40,50,60])
# min_val = np.min(arr)
# max_val = np.max(arr)
# normalized = (arr - min_val) / (max_val - min_val)
# print("Normalized Array:\n", normalized)


#20.	Given a 2D array of shape (5,3) representing 5 students' marks in 3 subjects, 
# #compute the total and average marks per student using axis-based aggregation.
# arr = np.array([[89,78,67],[76,65,98],[65,87,56],[56,78,68],[90,80,67]])
# total = np.sum(arr, axis=1)
# print("Total Marks: ",total)
# average = np.mean(arr, axis=1)
# print("Average Marks per student: ", np.round(average,2))

#21.	Use np.where() to replace all even numbers in a NumPy array with -1 and keep odd numbers unchanged.
# arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
# new_arr = np.where(arr % 2 == 0, -1, arr)
# print("New Array: ", new_arr)

#1.	Create a 4x4 matrix using np.arange().reshape() and compute its transpose, determinant, and inverse (if invertible).
# arr = np.arange(1,17).reshape(4,4)
# print(arr)
# transpose = arr.T
# print("Transpose:\n", transpose)
# determinant = np.linalg.det(arr)
# print("Determinant:\n", determinant)
# if(determinant != 0):
#     inverse = np.linalg.inv(arr)
#     print("Inverse:\n", inverse)
# else:
#     print("MAtrix is not invertible")
#23.	Given two NumPy 1D arrays representing vectors, compute their dot product manually with a loop and verify it against np.dot().
# arr1 = np.array([1,2,3,4,5])
# arr2 = np.array([6,5,4,3,1])
# dot_product = 0
# i=0
# while(i < len(arr1)):
#     dot_product = dot_product + (arr1[i] * arr2[i])
#     i += 1
# print("Dot product using Loop: ", dot_product)
# print("Dot product using np.dot(): ", np.dot(arr1, arr2))

#24.	Write a program combining Python and NumPy: read 10 numbers from user input into a list, 
# #convert to a NumPy array, and print the sorted array along with its median.
# user_list = []
# for i in range(1,11):
#     num = int(input(f"Enter number {i}: "))
#     user_list.append(num)
# print("List = ",user_list)
# arr = np.array(user_list)
# print("Array = ", arr)
# sorted_arr = np.sort(arr)
# print("SOrted Array = ", sorted_arr)
# median_arr = np.median(sorted_arr)
# print("Median = ", median_arr)

#25.	Given a NumPy array of shape (3,4), use fancy indexing to select rows [0, 2] and columns [1, 3] simultaneously.
# arr = np.array([
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ])
# result = arr[[0, 2], [1, 3]]
# print(result)

#26.	Write a function that accepts a 2D NumPy array and returns True if the array is symmetric (equal to its transpose), otherwise False.

# def is_symmetric(arr):
#     return np.array_equal(arr, arr.T)

# arr = np.array([[1, 2, 3],[2, 4, 5],[3, 5, 6]])

# print(is_symmetric(arr))

#27.	Stack three NumPy arrays of shape (2,2) using np.vstack() and np.hstack(); print the resulting shapes and explain the difference.
# import numpy as np

# arr1 = np.array([[1, 2], [3, 4]])
# arr2 = np.array([[5, 6], [7, 8]])
# arr3 = np.array([[9, 10], [11, 12]])

# v = np.vstack((arr1, arr2, arr3))
# h = np.hstack((arr1, arr2, arr3))

# print("Vertical Stack:\n", v)
# print("Shape:", v.shape)

# print("\nHorizontal Stack:\n", h)
# print("Shape:", h.shape)


#28.	Given a NumPy array of 30 days of temperature readings, 
# #plot a line chart with the day number on the x-axis and temperature on the y-axis, including a title and axis labels.
# import numpy as np
# import matplotlib.pyplot as plt

# temps = np.array([32, 34, 30, 33, 36, 38, 37, 35, 30, 36,
#                   39, 40, 38, 37, 35, 42, 36, 39, 41, 40,
#                   38, 36, 35, 42, 39, 42, 41, 38, 36, 35])

# days = np.arange(1, 31)
# plt.plot(days, temps)

# plt.title("Daily Temperature for 30 Days")
# plt.xlabel("Day")
# plt.ylabel("Temperature")

# plt.show()

#29.	Plot y = sin(x) and y = cos(x) on the same figure for x from 0 to 2π using np.linspace(); 
# include a legend distinguishing the two curves.
# import numpy as np
# import matplotlib.pyplot as plt

# x = np.linspace(0, 2*np.pi, 100)
# y1 = np.sin(x)
# y2 = np.cos(x)

# plt.plot(x, y1, label="sin(x)")
# plt.plot(x, y2, label="cos(x)")

# plt.title("Sine and Cosine Curves")
# plt.xlabel("x")
# plt.ylabel("y")

# plt.legend()

# plt.show()
#30.	Create a bar chart comparing the average marks of 4 subjects, with a distinct color for the highest-scoring subject.
# import matplotlib.pyplot as plt
# import numpy as np

# subjects = ["CS", "ML", "DSA", "CN"]
# marks = [78, 85, 72, 92]

# highest = np.argmax(marks)

# colors = ["purple"] * 4
# colors[highest] = "green"

# plt.bar(subjects, marks, color=colors)

# plt.title("Average Marks of 4 Subjects")
# plt.xlabel("Subjects")
# plt.ylabel("Average Marks")

# plt.show()

# 31.	Generate a histogram of 500 normally distributed random numbers and overlay a vertical line at the mean using plt.axvline().
# import numpy as np
# import matplotlib.pyplot as plt

# data = np.random.normal(50, 10, 500)

# mean = np.mean(data)

# plt.hist(data, bins=20)
# plt.axvline(mean, label="Mean")

# plt.title("Histogram of Random Numbers")
# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.legend()

# plt.show()



# 32.	Create a 2x2 grid of subplots showing four different chart types (line, bar, scatter, histogram) from the same dataset.
# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y = [10, 20, 15, 25, 30]

# fig, axes = plt.subplots(2, 2)

# axes[0,0].plot(x, y)
# axes[0,0].set_title("Line Chart")

# axes[0,1].bar(x, y)
# axes[0,1].set_title("Bar Chart")

# axes[1,0].scatter(x, y)
# axes[1,0].set_title("Scatter Plot")

# axes[1,1].hist(y)
# axes[1,1].set_title("Histogram")

# plt.tight_layout()
# plt.show()





# 33.	Load a small DataFrame of 6 products (name, price, quantity) and compute a new column 'total' as price × quantity.
# import pandas as pd

# data = {
#     "name": ["Pen", "Book", "Bag", "Pencil", "Bottle", "Notebook"],
#     "price": [50, 300, 1500, 30, 500, 250],
#     "quantity": [5, 2, 1, 10, 3, 4]
# }

# df = pd.DataFrame(data)

# df["total"] = df["price"] * df["quantity"]

# print(df)
# print("\n")


# 34.	Given a DataFrame of exam scores across 3 subjects for 10 students, use groupby-style aggregation to find each student's average and identify the top performer.
# import pandas as pd
# data = {
#     "student": ["Ali", "Sara", "Ahmed", "Hina", "Usman"],
#     "Math": [80, 90, 75, 95, 85],
#     "English": [70, 85, 80, 90, 88],
#     "Computer": [90, 95, 85, 92, 90]}
# df = pd.DataFrame(data)
# df["Average"] = df[["Math", "English", "Computer"]].mean(axis=1)
# print(df)
# top_student = df.loc[df["Average"].idxmax()]
# print("Top Performer:", top_student)








print("\n")
# 35.	Given a DataFrame with a 'date' column and a 'sales' column, sort by date and plot sales over time using Pandas' built-in .plot() method.
# import pandas as pd
# import matplotlib.pyplot as plt

# data = {
#     "date": ["2026-03-03", "2026-03-01", "2026-03-04", "2026-03-02"],
#     "sales": [500, 300, 700, 450]
# }

# df = pd.DataFrame(data)

# df["date"] = pd.to_datetime(df["date"])

# df = df.sort_values("date")

# df.plot(x="date", y="sales", kind="line")

# plt.title("Sales Over Time")
# plt.xlabel("Date")
# plt.ylabel("Sales")

# plt.show()





# # 36.	Given a DataFrame with missing values in a 'score' column, fill the missing values with the column mean and confirm no NaNs remain.
# import pandas as pd

# data = {
#     "name": ["Ali", "Sara", "Ahmed", "Hina", "Usman"],
#     "score": [80, 90, None, 70, None]
# }

# df = pd.DataFrame(data)

# mean_score = df["score"].mean()

# df["score"] = df["score"].fillna(mean_score)

# print(df)

# print("NaNs remaining:", df["score"].isna().sum())
# 37.	Combine Pandas and Matplotlib: read a small CSV of monthly expenses into a DataFrame, group by category, and plot the totals as a pie chart.
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("expenses.csv")

category_total = df.groupby("category")["amount"].sum()

print(category_total)

category_total.plot(kind="pie", autopct="%1.1f%%")

plt.title("Monthly Expenses by Category")
plt.ylabel("")

plt.show()












print("\n")
