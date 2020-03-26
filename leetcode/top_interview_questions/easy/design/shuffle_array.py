"""Shuffle a set of numbers without duplicates.

Example:

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of
[1,2,3] must equally likely to be returned.  solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();

"""

from random import randint


class Solution:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums[:]
        self.now = nums[:]

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.now = self.nums[:] # list(self.nums) also create new array
        return self.now

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        for i in range(len(self.now) - 1):
            idx = randint(i, len(self.now) - 1)
            self.now[i], self.now[idx] = self.now[idx], self.now[i]
        return self.now


def test():
    """
    Your Solution object will be instantiated and called as such:
    obj = Solution(nums)
    param_1 = obj.reset()
    param_2 = obj.shuffle()
    """

    nums = [i for i in range(4)]
    obj = Solution(nums)
    param_1 = obj.reset()
    expected = set(nums)

    for i in range(1):
        result = obj.shuffle()
        assert expected >= set(result)
