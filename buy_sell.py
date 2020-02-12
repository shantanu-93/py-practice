class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy=sys.maxsize
        for i in range(0,len(prices)):
            if min_buy>prices[i]:
                min_buy = prices[i]
            elif (prices[i] - min_buy) > max_profit:
                max_profit = prices[i]-min_buy
        return max_profit

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
            prices = stringToIntegerList(line);
            
            ret = Solution().maxProfit(prices)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()