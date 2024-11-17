'''
You are given an array of integers arr[]. Your task is to reverse the given array.

Input: arr = [1, 4, 3, 2, 6, 5]
Output: [5, 6, 2, 3, 4, 1]
Explanation: The elements of the array are 1 4 3 2 6 5. After reversing the array, the first element goes to the last position, the second element goes to the second last position and so on. Hence, the answer is 5 6 2 3 4 1.

Input: arr = [4, 5, 2]
Output: [2, 5, 4]
Explanation: The elements of the array are 4 5 2. The reversed array will be 2 5 4.

'''

def reverseArray(arr):
    reversed_array=[] 
    for i in range(len(arr)):
        reversed_array.append(arr[-(i + 1)])
    return reversed_array
    
print(reverseArray([1,2,3,4]))
