"""
39. Combination Sum
Medium
Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers sum to target.
You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
frequency
 of at least one of the chosen numbers is different.
The test cases are generated such that the number of unique combinations that sum up to target
 is less than 150 combinations for the given input.
"""


def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    results = []

    def backtrack(start, current_combination, remaining_target):
        if remaining_target == 0:
            results.append(list(current_combination))
            return
        elif remaining_target < 0:
            return

        for i in range(start, len(candidates)):
            current_combination.append(candidates[i])
            backtrack(i, current_combination, remaining_target - candidates[i])
            current_combination.pop()

    backtrack(0, [], target)
    return results

candidates = [2,3,6,7]
target = 7
print(combinationSum(candidates, target))