class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        nums.sort(reverse=True)
        result = []
        curr_sum = 0
        
        for n in nums:
            result.append(n)
            curr_sum += n
            if curr_sum > total - curr_sum:
                break
        
        return result