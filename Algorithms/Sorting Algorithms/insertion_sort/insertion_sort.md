# Insertion Sort

Insertion sort is a simple sorting algorithm that builds the final sorted array one item at a time. It's much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.

## How It Works

1. We start from the second element (index 1) of the array.
2. We compare this element with the one before it.
3. If this element is smaller, we swap them.
4. We continue comparing and swapping until the element is in its correct position.
5. We then move to the next element and repeat steps 2-4.

## Example

Let's sort the array `[5, 2, 4, 6, 1, 3]` using insertion sort.

Initial array: `[5, 2, 4, 6, 1, 3]`

1. Start with `2`:
   - `[5, 2, 4, 6, 1, 3]` → `[2, 5, 4, 6, 1, 3]`

2. Move to `4`:
   - `[2, 5, 4, 6, 1, 3]` → `[2, 4, 5, 6, 1, 3]`

3. `6` is already in the correct position.

4. Move to `1`:
   - `[2, 4, 5, 6, 1, 3]` → `[1, 2, 4, 5, 6, 3]`

5. Finally, place `3`:
   - `[1, 2, 4, 5, 6, 3]` → `[1, 2, 3, 4, 5, 6]`

The array is now sorted.

## Time Complexity

- Worst-case time complexity: O(n^2)
- Average-case time complexity: O(n^2)
- Best-case time complexity: O(n) (when the array is already sorted)

## Space Complexity

The space complexity of insertion sort is O(1) because it only uses a constant amount of additional memory space regardless of the input size.

## Advantages and Disadvantages

Advantages:
- Simple implementation
- Efficient for small data sets
- Adaptive (efficient for data sets that are already substantially sorted)

Disadvantages:
- Inefficient for large data sets
- Generally performs worse than other quadratic sorting algorithms like selection sort
