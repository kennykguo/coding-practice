class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        num_coins = [float("infinity") for i in range(amount + 1)]
        cur_state = [False for i in range(amount + 1)]
        # [0, -1, -1, ... -1]
        num_coins[0] = 0
        cur_state[0] = True

        for i in range(amount + 1):  # over all amounts, in order
            for coin in coins:  # over all coins
                if i - coin >= 0 and cur_state[i - coin]:
                    # first check is bounds check, second is that we have a set that adds up to that
                    cur_state[i] = True
                    num_coins[i] = min(num_coins[i], num_coins[i - coin] + 1)

        if amount == 0:
            return 0

        return num_coins[-1] if cur_state[-1] else -1
