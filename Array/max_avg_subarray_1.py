class Solution:
    def findMaxAverage(self, nums, k):
        current_window_sum = sum(nums[:k])
        max_sum = current_window_sum
        for i in range(k, len(nums)):
            current_window_sum += nums[i] - nums[i - k]
            if current_window_sum > max_sum:
                max_sum = current_window_sum
        return float(max_sum) / k
