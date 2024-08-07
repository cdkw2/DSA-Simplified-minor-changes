# Heap Sort

Heap sort is a comparison-based sorting algorithm that uses a binary heap data structure. It divides its input into a sorted and an unsorted region, and it iteratively shrinks the unsorted region by extracting the largest element and moving that to the sorted region.

## How It Works

1. Build a max heap from the input data.
2. Swap the first element (maximum) with the last element of the heap.
3. Reduce the size of the heap by 1 and heapify the root.
4. Repeat steps 2-3 until the size of the heap is 1.

## Example

Let's sort the array `[4, 10, 3, 5, 1]` using heap sort.

1. Build max heap:
   ```
        10
       /  \
      5    3
     / \
    4   1
   ```

2. Swap 10 and 1, heapify:
   ```
   [1, 5, 3, 4] | [10]
        5
       / \
      4   3
     /
    1
   ```

3. Swap 5 and 1, heapify:
   ```
   [1, 4, 3] | [5, 10]
        4
       / \
      1   3
   ```

4. Swap 4 and 3, heapify:
   ```
   [3, 1] | [4, 5, 10]
     3
    /
   1
   ```

5. Swap 3 and 1:
   ```
   [1] | [3, 4, 5, 10]
   ```

The array is now sorted: `[1, 3, 4, 5, 10]`

## Time Complexity

- Worst-case time complexity: O(n log n)
- Average-case time complexity: O(n log n)
- Best-case time complexity: O(n log n)

## Space Complexity

The space complexity of heap sort is O(1) as it sorts in-place.

## Advantages and Disadvantages

Advantages:
- Efficient time complexity of O(n log n)
- In-place sorting (requires no extra space)
- Works well for large datasets

Disadvantages:
- Not stable (relative order of equal elements may change)
- Poor cache performance due to its non-localized comparisons

