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

"""
This repository contains my This repository contains my Python solutions to the "Blind 75" coding questions, a curated list of top interview questions often asked by tech companies. Whether you're preparing for technical interviews or looking to improve your algorithm and data structure skills, this collection of solutions provides a comprehensive resource to help you succeed. Each solution is accompanied by detailed explanations and comments, making it a valuable learning tool for developers of all levels.

Features:

Python solutions to the Blind 75 coding questions.
Comprehensive explanations and comments for each solution.
Organized and categorized solutions for easy navigation.
A valuable resource for interview preparation and algorithm practice.
Feel free to customize this description as needed, and best of luck with your repository!



"""
