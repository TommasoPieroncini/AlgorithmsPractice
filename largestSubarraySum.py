arr = [2,4,-2,-5,5,-6,3,1,5,3,-5]

def largestSubarraySum(array):
    largestSumToDate = arr[0]
    currentSum = arr[0]
    for i, item in enumerate(arr[1:]):
        if item + currentSum > 0:
            currentSum = currentSum + item
        else:
            if i != len(arr) - 1:
                currentSum = arr[i+1]
        if currentSum > largestSumToDate:
            largestSumToDate = currentSum


print largestSubarraySum(arr)