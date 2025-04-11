#!/usr/bin/env python3
import os
import sys

# Get two numbers from command line arguments
if len(sys.argv) != 3:
    print("Usage: python input.py <number1> <number2>")
    sys.exit(1)

try:
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
except ValueError:
    print("Please provide valid numbers")
    sys.exit(1)

# Create shared directory if it doesn't exist
os.makedirs('/data', exist_ok=True)

# Write numbers to a file in the shared volume
with open('/data/numbers.txt', 'w') as f:
    f.write(f"{num1}\n{num2}")

print(f"Numbers {num1} and {num2} saved to shared volume")