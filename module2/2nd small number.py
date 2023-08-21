nums = []
print("Enter 10 Numbers (Elements) for List: ")
for i in range(10):
  nums.append(int(input()))

small = nums[0]
for i in range(10):
  if small>nums[i]:
    small = nums[i]

secondSmall = nums[0]
for i in range(10):
  if secondSmall>nums[i]:
    if nums[i]!=small:
      secondSmall=nums[i]

print("\nSecond Smallest Number is: ")
print(secondSmall)
