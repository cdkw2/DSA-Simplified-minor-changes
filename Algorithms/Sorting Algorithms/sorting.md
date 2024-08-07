## 🔀 What is Sorting? 

```
A sorting algorithm is used to rearrange a given collection of elements, 
according to a comparison operator on the elements. The comparison operator 
is used to decide the new order of elements within the collection.
```

Let's say we are given the following dataset:
```
2, 10, 3, 9, 22, 17, 40
```

Now, if we were to sort the given elements, such that the resulting arrangement would follow a non-decreasing order, we'd get the following rearrangement:

```
2, 3, 9, 10, 17, 22, 40
```

Similarly, if we wished to obtain such an arrangement where the collection of elements (numbers) would follow a non-increasing order, we'd get the following rearrangement:

```
40, 22, 17, 10, 9, 3, 2
```

<br>

Although when we are sorting a collection of numbers, there are generally only two ways to sort them (as shown above).

But when sorting a collection of a different dataset (say a different data structure like lists/arrays), then we have more ways to sort them.
In such cases we make use of a comparison operator/function (as talked above), which returns a boolean value, depending on the comparison computation it makes on each element of the dataset.

<hr>

### 📶 Sorting Algorithms 
There are a variety of ways through which we can sort a given collection of numbers.
Similarly there are a variety of algorithms, which make use of different instructions/computations, to sort a given dataset.

We'll begin with the ones which are the most intuitive and proceed our way up to the ones which are the most efficient.

1. [Selection Sort](Selection%20Sort/selection-sort.md)
2. [Bubble Sort](Bubble%20Sort/bubble-sort.md)
3. [Insertion Sort](insertion_sort/insertion_sort.md)
4. [Merge Sort](merge_sort/merge_sort.md)
5. [Quick Sort](quick_sort/quick_sort.md)
6. [Heap Sort](heap_sort/heap_sort.md)
7. [Counting Sort](counting_sort/counting_sort.md)
8. [Radix Sort](radix_sort/radix_sort.md)

Each of these sorting algorithms has its own strengths and weaknesses, making them suitable for different scenarios:

- **Selection Sort** and **Bubble Sort** are simple to understand and implement but are inefficient for large datasets.
- **Insertion Sort** performs well on small datasets or nearly sorted data.
- **Merge Sort** and **Quick Sort** are efficient divide-and-conquer algorithms with O(n log n) average time complexity.
- **Heap Sort** provides in-place sorting with O(n log n) time complexity.
- **Counting Sort** and **Radix Sort** can achieve linear time complexity for integer sorting under certain conditions.

Choose the appropriate sorting algorithm based on your specific requirements, such as the size of the dataset, the nature of the data, and the available memory.
