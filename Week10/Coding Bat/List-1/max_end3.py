def max_end3(nums):
  a = nums[0]
  b = nums[-1]
  if a > b:
    return [a, a, a]
  else:
    return [b, b, b]