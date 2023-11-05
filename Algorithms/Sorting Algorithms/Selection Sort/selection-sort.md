# Selection Sort

We'll begin with an example array, which we'll sort in **non-decreasing order**.

```python
arr = [70, 40, 21, 2, 11, 8]
```

Firstly, we should be aware that the *Selection Sort* Algorithm consists of multiple **Rounds / Passes**.

With each Round, say `r` (1-based), we place the *`r`<sup>th</sup> minimum element* at its correct place.

Let's begin..


<hr>
<br>

We'll iterate through `arr` with index `i = 0`.

Let length of `arr` be `n = 6`.
### Round 1

Find the index of the smallest element in the array from index `i = 0` till the end of the array.

```python
  0   1   2  3   4  5
[70, 40, 21, 2, 11, 8]
 ^           ^
 i  |  minimum element's index -> 3
```

Swap the elements at `arr[i]` and `arr[min_element_index]`.

### Round 2

Find the index of the smallest element in the array from index i = 1 till the end of the array.

```python
  0   1   2   3   4  5
[ 2, 40, 21, 70, 11, 8]
      ^              ^
      i  |  minimum element's index -> 5
```

Swap the elements at the given indices `i` and `min_element_index`.

### Round 3

We increment `i` each round, and the rest of the procedure remains the same.

```python
  0   1   2   3   4  5
[ 2,  8, 21, 70, 11, 40]
          ^       ^
          i  |  minimum element's index -> 4

swap(arr[i], arr[min_element_index])
```

### Round 4

```python
  0   1   2   3   4  5
[ 2,  8, 11, 70, 21, 40]
              ^   ^
              i  |  minimum element's index -> 4

swap(arr[i], arr[min_element_index])
```

### Round 5

```python
  0   1   2   3   4  5
[ 2,  8, 11, 21, 70, 40]
                  ^   ^
                  i  |  minimum element's index -> 5

swap(arr[i], arr[min_element_index])
```

<hr>

After 5 Rounds, our array looks like this:

```python
arr = [2, 8, 11, 21, 40, 70]
```

Notice that when `n = 6`, the # of Rounds to sort the array was `r = n - 1 = 5`. This is simply because after 5 Rounds, we'll be left with only 1 element to be put at its right place. But since all the other elements have already been placed correctly, the last element is itself at the correct position.

Try to sort another array, say 
```python
arr = [45, 35, 90, 21, 33, 11]
```
on your own, following the same steps as shown above.

Now when we are done with an example,
Let's have a look at the pseudocode, that will generalise the steps we have talked about so far. 

<hr>

## Pseudocode 

1. Traverse `arr` from `i = 0`.
2. For each `i`, find the index of the minimum element of `arr` between indices `i` and `arr.length - 1` (inclusive).
3. Swap `arr[i]` with `arr[min_element_index]`
4. Increment `i` and repeat steps 2. and 3. till `i < arr.length - 1`.
