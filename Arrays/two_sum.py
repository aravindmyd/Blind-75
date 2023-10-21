from typing import Dict, List


def two_sum(nums: List[int], target: int) -> List[int]:
    hash: Dict = {}

    for ind, num in enumerate(nums):
        cur_target = target - num
        if cur_target in hash:
            return [hash[cur_target], ind]
        else:
            hash[num] = ind
    return None


def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]


if __name__ == "__main__":
    test_two_sum()
    print("All test cases passed.")
