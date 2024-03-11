# Problem: Write a program to take the input from the user as hours of the day 0-23 and another inpot value which denotes boolean value (True/False) if the dog is barking or not. If the dog is barking before 6 or after 22 hours of the day then the owner will wake up. If the dog is barking between 6 and 22 hours of the day then the owner will not wake up. If the dog is not barking then the owner will not wake up.
# Example: Input: 5, True Output: True
#          Input: 5, False Output: False
#          Input: 7, True Output: False
#          Input: 7, False Output: False


# Solution:
def should_wake_up(hour, is_barking):
    if is_barking and (hour < 6 or hour > 22):
        return True
    else:
        return False


time = int(input("Enter hour in 0-23: "))
bark = bool(input("Enter Dog barking in True/False: "))
wakeUp = should_wake_up(time, bark)
print()
if wakeUp:
    print("Owner should wake up")
else:
    print("Owner should not wake up")
