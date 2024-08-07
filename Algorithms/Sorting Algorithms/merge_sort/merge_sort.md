# Merge Sort

Merge sort is an efficient, stable, divide-and-conquer sorting algorithm. It works by dividing the unsorted list into n sublists, each containing one element (a list of one element is considered sorted). Then, it repeatedly merges sublists to produce new sorted sublists until there is only one sublist remaining.

## How It Works

1. Divide the unsorted list into n sublists, each containing one element.
2. Repeatedly merge sublists to produce new sorted sublists until there is only one sublist remaining.

## Example

Let's sort the array `[38, 27, 43, 3, 9, 82, 10]` using merge sort.

1. Divide the array into two halves:
   `[38, 27, 43, 3]` and `[9, 82, 10]`

2. Recursively divide these subarrays:
   `[38, 27]` `[43, 3]` `[9, 82]` `[10]`

3. Further divide:
   `[38]` `[27]` `[43]` `[3]` `[9]` `[82]` `[10]`

4. Now start merging:
   `[27, 38]` `[3, 43]` `[9, 82]` `[10]`

5. Merge again:
   `[3, 27, 38, 43]` `[9, 10, 82]`

6. Final merge:
   `[3, 9, 10, 27, 38, 43, 82]`

The array is now sorted.

## Time Complexity

- Worst-case time complexity: O(n log n)
- Average-case time complexity: O(n log n)
- Best-case time complexity: O(n log n)

## Space Complexity

The space complexity of merge sort is O(n) because it requires additional space to store the merged subarrays during the sorting process.

## Advantages and Disadvantages

Advantages:
- Stable sort (doesn't change the relative order of elements with equal keys)
- Guaranteed O(n log n) performance
- Well-suited for external sorting (when data doesn't fit in memory)

Disadvantages:
- Requires additional O(n) space
- Slower for smaller tasks compared to other sorting algorithms
