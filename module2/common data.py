def common(nums, lsts):
    for x in lsts:
        if x in nums:
            return True
    return False    
print(common([10, 20, 30, 40, 50, 60], [22, 42]))
print(common([10, 20, 30, 40, 50, 60], [20, 80]))
