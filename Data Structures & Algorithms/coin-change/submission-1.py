class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def dfs(remaining):
            if not remaining: return 0
            if remaining in cache: return cache[remaining]

            res = amount+1
            for coin in coins:
                if remaining - coin>=0:
                    res = min(res, 1+dfs(remaining - coin))
            cache[remaining] = res
            return res
        min_coins = dfs(amount)
        return -1 if min_coins>=amount+1 else min_coins