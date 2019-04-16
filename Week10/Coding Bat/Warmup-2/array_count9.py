def array_count9(nums):
  cnt = 0
  for i in nums:
    if i == 9:
      cnt = cnt + 1
  return cnt