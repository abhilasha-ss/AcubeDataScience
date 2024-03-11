# This file walks through the while loop in python

# While loop is used to repeat a block of code multiple times
# The while loop will keep executing the code block under it as long as the condition is true
# The condition is checked every time at the beginning of the loop
# If the condition is true, the code block will be executed, otherwise the loop will stop
# The while loop is used when you don't know the number of iterations in advance

# The syntax of while loop is:
# while condition:
#     statement(s)

for i in range(1, 6):
    print(i)

# Example:
i = 1
while i < 6:
    print(i)
    i += 1

# The while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 1
# We also need to define the end point of the loop, which is 6 in this example
# At the beginning of the loop, we set the variable i to 1, then we execute the print statement
# Then we increase the i by 1
# Now the i is 2, so the condition is true, and we execute the print statement again
# This process repeats until the condition becomes false, which happens when i becomes 6
# The while loop is often used to loop indefinitely

# The while loop is useful when you don't know how many times you need to execute a block of code
# The while loop can be used to iterate through a block of code as long as the condition is true

# Difference between while loop and for loop
# The for loop is used to iterate over a sequence of items
# The while loop is used to iterate over a block of code as long as the condition is true


# explain while else loop
# The else statement is used to run a block of code if the condition is false
# The else block just after for/while is executed only when the loop is NOT terminated by a break statement

# Example:
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

# Example:
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
else:
    print("i is no longer less than 6")

# Example:
# i = 1
# while i < 6:
#     print(i)
#     if i == 3:
#         continue
#     i += 1
# else:
#     print("i is no longer less than 6")



