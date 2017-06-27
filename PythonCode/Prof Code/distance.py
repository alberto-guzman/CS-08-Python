# Ask user for speed
speed = float(input("Speed (mph): "))
# Ask user for time
time = float(input("Time (hr): "))
# Compute distance
distance = speed * time
# print distance
print(format(distance, ".1f"), "miles traveled")
