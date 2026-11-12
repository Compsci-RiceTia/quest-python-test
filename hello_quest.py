import sys
import platform

print("Hello from Northwestern Quest!")

print("Python version:", sys.version)
print("Operating system:", platform.system())

numbers = [10, 20, 30, 40, 50]

average = sum(numbers) / len(numbers)

print("Numbers:", numbers)
print("Average:", average)
