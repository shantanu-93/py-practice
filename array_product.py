#sudo pip3 install simplejson
import json as json
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 0
        count = 0
        for i in range(0,len(nums)):
            if nums[i] != 0:
                if product == 0:
                    product = 1
                product *= nums[i]
            else:
                count +=1
        arr = []
        for i in range(0,len(nums)):
            num = 0
            if count==1 and nums[i]!=0:
                num = 0
            elif count>1:
                num = 0
            elif nums[i] == 0:
                num = product
            else:
                num = product//nums[i]
            arr.append(num)
        return arr

def stringToIntegerList(input):
    return json.loads(input)

def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums = stringToIntegerList(line);
            
            ret = Solution().productExceptSelf(nums)

            out = integerListToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()