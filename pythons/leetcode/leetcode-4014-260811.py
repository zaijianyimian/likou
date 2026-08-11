class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices.sort(reverse=True)
        discounts.sort(reverse=True)
        ans = 0
        for i,p in enumerate(prices):
            d = discounts[i] if i < len(discounts) else 0
            ans += p * (100 - d)
        return ans / 100