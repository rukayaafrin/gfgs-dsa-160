'''
Given an array arr[]. Push all the zeros of the given array to the right end of the array while maintaining the order of non-zero elements. Do the mentioned change in the array in place.
Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
Output: [1, 2, 4, 3, 5, 0, 0, 0]
Explanation: There are three 0s that are moved to the end.

'''

def pushZerosToEnd(arr):
        non_zero_index = 0

        for i in range(len(arr)):
            if arr[i] != 0:
                arr[non_zero_index], arr[i] = arr[i], arr[non_zero_index]
                non_zero_index += 1
        return arr
