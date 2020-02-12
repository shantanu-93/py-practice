import math as math
#code
def max_mid(left,mid, right, arr):
    sum = 0
    left_sum=0
    for i in range(mid, left-1,-1):
        sum += arr[i]
        if sum > left_sum:
            left_sum = sum
    sum = 0
    right_sum=0
    for i in range(mid+1, right+1):
        sum += arr[i]
        if sum > right_sum:
            right_sum = sum
    return left_sum+right_sum
        
        
def max_sum(left, right, arr):
    print("left and right: ",left,right)
    if left == right:
        return arr[left]
    mid = int((left+right)//2)
    leftist = max_sum(left,mid,arr)
    rightist = max_sum(mid+1,right,arr)
    centrist = max_mid(left,mid,right,arr)
    return max(leftist,rightist,centrist)
if __name__ == "__main__":
    t = int(input())
    for i in range(0,t):
        print("Test ",i)
        n = int(input())
        print("Array size ",n)
        arr=list(map(int,input().split()))
        print(max_sum(0,len(arr)-1,arr))
    