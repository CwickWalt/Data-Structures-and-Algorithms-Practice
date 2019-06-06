# If given a sum, find the two numbers in the list whose sum
# is equal to the given sum
# assuming the list is sorted
# big = index of the value that starts on the right side of the list
# small = index of the value that starts on the left side of the list


def findSum(list, small, big, sum):
    # Base Case:
    # if big is greater than small, start recursive case
    if big > small:
        target = list[small] + list[big]
        # Recursive Case:
        # if the sum of list[big] and list[small] (target) is equal to sum
        # return the values
        if target == sum:
            return(list[small], list[big])
        # if target is greater than sum
        # move right-sided value to the left
        # call function again with new value
        elif target > sum:
            big = big - 1
            return findSum(list, small, big, sum)
        # if not, then target must be less than sum
        # move left-sided value to the right
        # call function again with new value
        else:
            small = small + 1
            return findSum(list, small, big, sum)
    # if the base case is not fulfilled, return -1
    # ex. empty list or no pair with a sum equal to the given sum
    else:
        return -1

# test

nums = [0, 1, 1, 2, 4, 6, 8, 12, 13, 14, 15]
nums2 = [1, 2, 3]
nums3 = []

findSum(nums, 0, len(nums)-1, 10)
findSum(nums2, 0, len(nums2)-1, 10)
findSum(nums3, 0, len(nums3)-1, 10)
