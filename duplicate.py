class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numset = set(nums)
        if len(nums) > len(numset):
            return True
        else:
            return False

def stringToIntegerList(input):
    return json.loads(input)

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
            
            ret = Solution().containsDuplicate(nums)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()