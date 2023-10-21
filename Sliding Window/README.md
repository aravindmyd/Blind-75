# Sliding Window Example

## Problem Statement

Given an array of integers and a fixed positive integer `k`, find the maximum sum of any contiguous subarray of size `k`.

**Example:**

Suppose we have the following array of integers: [2, 1, 5, 1, 3, 2]


And `k` is set to 3, meaning we want to find the maximum sum of a contiguous subarray of size 3.

## Solution using Sliding Window

1. Initialize two pointers, `left` and `right`, both pointing to the start of the array.

2. Calculate the sum of the first `k` elements within the initial window:

   - Initial Window: `[2, 1, 5]`
   - Sum: `2 + 1 + 5 = 8`

3. This sum, 8, is the maximum sum we've seen so far. Let's store it as the `maxSum`.

4. Start sliding the window to the right:

   - Move the `left` pointer one position to the right, and the ` right` pointer one position to the right. The window is now: `[1, 5, 1]`.

5. Calculate the sum of this new window:

   - Sum: `1 + 5 + 1 = 7`

6. Compare the sum of this new window with the `maxSum`. If it's greater, update `maxSum`:

   - The current sum is not greater than `maxSum`, so `maxSum` remains 8.

7. Continue sliding the window to the right until the `right` pointer reaches the end of the array:

   - Next Window: `[5, 1, 3]`, Sum: `5 + 1 + 3 = 9`
   - Update `maxSum` to 9.

   - Next Window: `[1, 3, 2]`, Sum: `1 + 3 + 2 = 6`

8. When the `right` pointer reaches the end of the array, the process ends.

9. The `maxSum` is 9, which is the maximum sum of any contiguous subarray of size 3 within the given array.

In this example, the sliding window technique allowed us to efficiently find the maximum sum of a subarray of size 3 by avoiding unnecessary re-computation and achieving a time complexity of O(n), where `n` is the length of the array. This is a classic example of how the sliding window technique can be used to solve array-related problems.
