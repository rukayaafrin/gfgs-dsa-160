'''
Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

Note: The second largest element should not be equal to the largest element.
'''

def getSecondLargest(arr):
        unique_sorted_arr = sorted(set(arr), reverse=True)
        if len(unique_sorted_arr) < 2:
            return -1
        
        return unique_sorted_arr[1]
