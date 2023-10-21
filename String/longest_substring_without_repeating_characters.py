def longest_substring_without_repeating_characters(s: str) -> int:
    max_len, start = 0, 0
    N = len(s)
    window = set()

    for end in range(N):
        cur_char = s[end]
        while cur_char in window:
            window.remove(s[start])
            start += 1
        window.add(cur_char)
        max_len = max(max_len, (end - start) + 1)
    return max_len


def test_longest_substring_without_repeating_character():
    assert longest_substring_without_repeating_characters("abcabcbb") == 3
    assert longest_substring_without_repeating_characters("bbbbb") == 1
    assert longest_substring_without_repeating_characters("pwwkew") == 3


if __name__ == "__main__":
    test_longest_substring_without_repeating_character()
    print("All test cases passed.")
