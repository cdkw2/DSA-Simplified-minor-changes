# Radix Sort

Radix sort is a non-comparative integer sorting algorithm that sorts data with integer keys by grouping the keys by individual digits that share the same significant position and value. It can be applied to strings as well.

## How It Works

1. Find the maximum element to know the number of digits.
2. Do counting sort for every digit. Note that instead of passing digit number, exp is passed. exp is 10^i where i is current digit number.
3. Start from the least significant digit to the most significant digit.

## Example

Let's sort the array `[170, 45, 75, 90, 802, 24, 2, 66]` using radix sort.

1. First pass: Sort by the ones place
   ```
   [170, 90, 802, 2, 24, 45, 75, 66]
   ```

2. Second pass: Sort by the tens place
   ```
   [802, 2, 24, 45, 66, 170, 75, 90]
   ```

3. Third pass: Sort by the hundreds place
   ```
   [2, 24, 45, 66, 75, 90, 170, 802]
   ```

The array is now sorted.

## Time Complexity

- Worst-case time complexity: O(d(n+k)), where d is the number of digits, n is the number of elements, and k is the range of input (usually 10 for decimal system)
- Average-case time complexity: O(d(n+k))
- Best-case time complexity: O(d(n+k))

## Space Complexity

The space complexity of radix sort is O(n+k), where n is the number of elements and k is the range of input.

## Advantages and Disadvantages

Advantages:
- Can be faster than O(n log n) algorithms for integers with a limited number of digits
- Stable sorting algorithm
- Efficient for sorting strings or integers with fixed-length

Disadvantages:
- Not efficient for large digit numbers or large alphabets
- Requires extra space
