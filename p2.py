# Step 1: Create a byte array
byte_arr = bytearray([72, 101, 108, 108, 111])
print(byte_arr)
# Step 2: Display original array
print("Original byte array:")
for i in byte_arr:
    print(i)

# Step 3: Modify elements
# Let's change the second element (index 1) to 99
byte_arr[1] = 65
print(byte_arr)
# Step 4: Display modified array
print("\nModified byte array:")
for i in byte_arr:
    print(i)

