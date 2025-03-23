from solutions.remove_duplicates import Solution

def test_remove_duplicates():
    assert Solution().removeDuplicates([1, 1, 2]) == 2
    assert Solution().removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5
    assert Solution().removeDuplicates([]) == 0
    assert Solution().removeDuplicates([1]) == 1
