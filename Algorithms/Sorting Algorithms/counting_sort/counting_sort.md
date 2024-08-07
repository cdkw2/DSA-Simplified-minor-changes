# Counting Sort

Counting sort is an integer sorting algorithm that operates by counting the number of objects that possess distinct key values, and applying prefix sum on those counts to determine the positions of each key value in the output sequence.

## How It Works

1. Find the maximum value in the array.
2. Initialize a count array of size [max+1] with all elements 0.
3. Store the count of each element in the count array.
4. Modify the count array by adding the previous counts.
5. Output each object from the input sequence followed by decreasing its count by 1.

## Example

Let's sort the array `[4, 2, 2, 8, 3, 3, 1]` using counting sort.

1. Find max value (8) and create count array:
   ```
   Index:  0  1  2  3  4  5  6  7  8
   Count: [0, 0, 0, 0, 0, 0, 0, 0, 0]
   ```

2. Count occurrences:
   ```
   Index:  0  1  2  3  4  5  6  7  8
   Count: [0, 1, 2, 2, 1, 0, 0, 0, 1]
   ```

3. Calculate cumulative sum:
   ```
   Index:  0  1  2  3  4  5  6  7  8
   Count: [0, 1, 3, 5, 6, 6, 6, 6, 7]
   ```

4. Build the output array:
   ```
   [1, 2, 2, 3, 3, 4, 8]
   ```

The array is now sorted.

## Time Complexity

- Worst-case time complexity: O(n + k), where n is the number of elements and k is the range of input
- Average-case time complexity: O(n + k)
- Best-case time complexity: O(n + k)

## Space Complexity

The space complexity of counting sort is O(k), where k is the range of input.

## Advantages and Disadvantages

Advantages:
- O(n) complexity when k = O(n)
- Stable sorting algorithm
- Efficient for small ranges of integers

Disadvantages:
- Inefficient if the range of input values is very large
- Not suitable for non-integer inputs without modification
