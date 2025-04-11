#!/usr/bin/env python3
import os
import time

# Wait for result file to be created
result_file = "/data/result.txt"
max_retries = 10
retries = 0

while not os.path.exists(result_file) and retries < max_retries:
    print(f"Waiting for result file... (attempt {retries+1}/{max_retries})")
    time.sleep(2)
    retries += 1

if not os.path.exists(result_file):
    print("Result file not found. Exiting.")
    exit(1)

# Read the result
with open(result_file, "r") as f:
    result = f.read().strip()

# Store the result (here we're just printing and saving to a permanent file)
print(f"Data saved: The sum is {result}")

# Save to a persistent file
with open("/data/stored_result.txt", "w") as f:
    f.write(f"The sum is {result}")

print("Result has been stored successfully")
