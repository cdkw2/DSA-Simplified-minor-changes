
# Quick Sort

Quick sort is an efficient, in-place sorting algorithm that uses a divide-and-conquer strategy. It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot.

## How It Works

1. Choose a pivot element from the array.
2. Partition the array around the pivot, such that:
   - Elements smaller than the pivot are on the left.
   - Elements greater than the pivot are on the right.
3. Recursively apply the above steps to the sub-array of elements with smaller values and the sub-array of elements with greater values.

## Example

Let's sort the array `[64, 34, 25, 12, 22, 11, 90]` using quick sort.

1. Choose the last element as pivot (90).
   Partition: `[64, 34, 25, 12, 22, 11] [90]`

2. Recursively sort the left partition:
   Choose 11 as pivot: `[11] [64, 34, 25, 12, 22]`
   Choose 22 as pivot: `[12] [22] [64, 34, 25]`
   Choose 25 as pivot: `[25] [64, 34]`
   Choose 34 as pivot: `[34] [64]`

3. Combining all partitions:
   `[11, 12, 22, 25, 34, 64, 90]`

The array is now sorted.

## Time Complexity

- Worst-case time complexity: O(n^2)
- Average-case time complexity: O(n log n)
- Best-case time complexity: O(n log n)

## Space Complexity

The space complexity of quick sort is O(log n) due to the recursive call stack.

## Advantages and Disadvantages

Advantages:
- Generally faster in practice compared to other O(n log n) algorithms
- In-place sorting (requires only a small auxiliary stack)
- Works well for a variety of real-world data

Disadvantages:
- Worst-case time complexity of O(n^2)
- Not stable (relative order of equal elements may change)
- Performance depends heavily on the choice of pivot
