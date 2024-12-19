# ! IKKE JOBB MED GRAFIKK, sier SERDAR

# Task 1
# while True:
#     number = int(input("Enter a postive number: "))
#     if number <= 0:
#          print(number, "is not a positive number.")
#          continue
#     for i in range(number, -1, -1):
#          print(i)

# import pandas as pd
# data = pd.read_csv("medier.csv", index_col = 0, skiprows=[0], sep=";", na_values=[".", ".."], encoding="latin-1")
# print(data)
# print(data.head())


# Task 2
# numberz = int(input("Enter a number for the multiplication table: "))
# for multiplier in range(1, 11):
#     print(f"{numberz} x {multiplier} = {numberz * multiplier}")

# # Task 3
# numberz = 42
# print("Guess a number between 1 and 100.")
# while True:
#     guesser = int(input("Enter your guess: "))
#     if guesser == numberz:
#         print("Congratulations! You guessed correctly!")
#         break
#     elif guesser < numberz:
#         print("Too low. Try again.")
#     else:
#         print("Too high. Try again.")

# Task 4
# def k(num):
#     if num < 2:
#         return False
#     for divisor in range(2, int(num ** 0.5) + 1):
#         if num % divisor == 0:
#             return False
#     return True

# print("The prime numbers in between 1 and 100 are:")
# for value in range(1, 101):
#     if k(value):
#         print(value)

# # Task 5
# def e(radius):
#     import math
#     return math.pi * radius ** 2

# print("Calculate the area of circles. Type ''stop' to exit.")
# while True:
#     uesb = input("Enter the radius: ")
#     if uesb.lower() == "stop":
#         break
#     this = float(uesb)
#     print(f"The area of a circle is: {e(this):.2f}")

# # Task 6
# print("Enter text. Type 'stop' to finish and see the total word count.")
# counter = 0
# while True:
#     zaText = input("Text: ")
#     if zaText.lower() == "stop":
#         break
#     counter += len(zaText.split())
# print(f"Total word count: {counter}")

