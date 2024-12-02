"""
837. New 21 Game
Medium
Alice plays the following game, loosely based on the card game "21".
Alice starts with 0 points and draws numbers while she has less than k points.
During each draw, she gains an integer number of points randomly from the range [1, maxPts],
where maxPts is an integer. Each draw is independent and the outcomes have equal probabilities.
Alice stops drawing numbers when she gets k or more points.
Return the probability that Alice has n or fewer points.
Answers within 10-5 of the actual answer are considered accepted.
"""


def new21Game(n: int, k: int, maxPts: int) -> float:
    if k == 0 or n >= k + maxPts:
        return 1.0

    dp = [0.0] * (n + 1)
    dp[0] = 1.0
    windowSum = 1.0
    result = 0.0

    for i in range(1, n + 1):
        dp[i] = windowSum / maxPts
        if i < k:
            windowSum += dp[i]
        else:
            result += dp[i]

        if i >= maxPts:
            windowSum -= dp[i - maxPts]

    return result


print(new21Game(10, 1, 10))
print(new21Game(6, 1, 10))
print(new21Game(21, 17, 10))
