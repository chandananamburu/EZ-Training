def check_subset(nums,target):
    def backtrack(start,sum):
        if sum==target:
            return True
        if sum>target or start==len(nums):
            return False
        if backtrack(start+1,sum + nums[start]):
           subset.append(nums[start])
           return True
        return backtrack(start+1,sum)