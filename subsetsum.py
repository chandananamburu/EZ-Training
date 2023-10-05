def check(nums,target):
  subset = []
  def backtrack(start,sum):
    if sum==target:
      return True
    if sum>target or start==len(nums):
      return False
    if backtrack(start+1,sum+nums[start]):
      subset.append(nums[start])
      return True
    return backtrack(start+1,sum)
  if backtrack(0,0):
    return True, subset
  else:
    return False, [ ]
nums=list(map(int,input().split(" ")))
target_sum=int(input())

bool, subset = check(nums, target_sum)

if bool:
  print("subset with sum", target_sum, "exists:", subset)
else:
  print("No subset with sum", target_sum, "exists:", subset)

