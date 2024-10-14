"""
40. Combination Sum II
Medium
Given a collection of candidate numbers (candidates) and a target number (target),
 find all unique combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.
"""


def combinationSum2(candidates: list[int], target: int) -> list[list[int]]:
    candidates.sort()
    results = []

    def backtrack(start, current_combination, remaining_target):
        if remaining_target == 0:
            results.append(list(current_combination))
            return
        elif remaining_target < 0:
            return

        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            current_combination.append(candidates[i])
            backtrack(i + 1, current_combination, remaining_target - candidates[i])
            current_combination.pop()

    backtrack(0, [], target)
    return results


candidates = [10,1,2,7,6,1,5]
target = 8
print(combinationSum2(candidates, target))