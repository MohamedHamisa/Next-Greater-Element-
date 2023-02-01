class Solution(object):
    def nextGreaterElements(self, nums):
        n = len(nums)
        ret = [-1] * n
        stack = nums[::-1]
        for i in range(n - 1, -1, -1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            if stack:
                ret[i] = stack[-1]
            stack.append(nums[i])
        return ret

'''
Use the stack to record the reversed array nums. Loop the array from last integer to the first one. If the last integer in stack is bigger than the current interger in array, 
we have found the answer. Otherwise,
we need to keep pop up the integer in stack. Besides, we need to push the current integer to the stack in each step.

Because in the description, there is a condition: If it (the next greater number) doesn't exist, return -1 for this number.
So ret = [-1] * n means I give a default value -1 for each element.
If later I find the next greater number for the element, I would replace this default value ret[i] = stack[-1].
Hope this helps.
'''
