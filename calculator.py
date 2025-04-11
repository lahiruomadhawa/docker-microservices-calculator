#!/usr/bin/env python3
import os
import time

# Wait for input file to be created (in a real system, you might use a message queue)
input_file = "/data/numbers.txt"
max_retries = 10
retries = 0

while not os.path.exists(input_file) and retries < max_retries:
    print(f"Waiting for input file... (attempt {retries+1}/{max_retries})")
    time.sleep(2)
    retries += 1

if not os.path.exists(input_file):
    print("Input file not found. Exiting.")
    exit(1)

# Read the numbers
with open(input_file, "r") as f:
    lines = f.readlines()

if len(lines) != 2:
    print("Invalid input format. Expected 2 numbers.")
    exit(1)

try:
    num1 = float(lines[0].strip())
    num2 = float(lines[1].strip())
except ValueError:
    print("Invalid numbers in input file")
    exit(1)

# Calculate the sum
result = num1 + num2

# Write the result to the shared volume
with open("/data/result.txt", "w") as f:
    f.write(str(result))

print(f"Calculation complete: {num1} + {num2} = {result}")
