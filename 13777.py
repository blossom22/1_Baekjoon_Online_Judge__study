# Baekjoon_BRONZE1_13777: Hunt The Rabbit 

import sys
nums=[i for i in range(1,51)]
while True:
    n = int(sys.stdin.readline())
    if n!=0:
        left = 0
        right = 49
        while left<=right:
            mid = (left+right)//2
            if n==nums[mid]:
                print(n)
                break
            elif n>nums[mid]:
                left = mid + 1
                print(nums[mid], end=' ')
            else:
                right = mid - 1
                print(nums[mid], end=' ')
    else:
        break