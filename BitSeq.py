# Function to find the longest bitonic subsequence in a list
def calculateLBS(nums):
 
    n = len(nums)
 
    # base case
    if n == 0:
        return 0
 
    # `I[i]` store the length of the longest increasing subsequence,
    # ending at `nums[i]`
    I = [0] * n
 
    # `D[i]` stores the length of the longest decreasing subsequence,
    # starting with `nums[i]`
    D = [0] * n
 
    I[0] = 1
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i] and I[j] > I[i]:
                I[i] = I[j]
        I[i] = I[i] + 1
 
    D[n - 1] = 1
    for i in reversed(range(n - 1)):
        for j in reversed(range(i + 1, n)):
            if nums[j] < nums[i] and D[j] > D[i]:
                D[i] = D[j]
        D[i] = D[i] + 1
 
    # consider each element as a peak and calculate LBS
    lbs = 1
    for i in range(n):
        lbs = max(lbs, I[i] + D[i] - 1)
 
    return lbs
 
 
if __name__ == '__main__':
 
    nums = [4, 2, 5, 9, 7, 6, 10, 3, 1]
    print('The length of the longest bitonic subsequence is', calculateLBS(nums))
 

