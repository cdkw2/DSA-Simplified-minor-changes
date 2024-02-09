# Bubble Sort

Let us take this time the following array named `arr`, and we'll sort it in **non-decreasing order**.

```python
arr = [10, 11, 7, 6, 40, 19]
```

Like Selection Sort, Bubble Sort comprises of different rounds, and with each $round$  (1-based), we put the $round^{th}$ maximum element at its correct position.

<hr>

Let $round = 0$ and $n = arr.length$

We'll traverse the array and increment $round$ till $round < n$, and since with each round we put the $round^{th}$ maximum element at its correct place, each time our traversal would be a step shorter.
### Round 1

Let $i = 1$ , and till $i < n - round$ 
- if $arr[i-1] > arr[i]$ , then $swap(arr[i-1],\ arr[i])$
- $i = i + 1$

```python
[10, 11, 7, 6, 40, 19]  # no swap
      ^
    i = 1

[10, 11, 7, 6, 40, 19] -> [10, 7, 11, 6, 40, 19] # 11 > 7
         ^
       i = 2

[10, 7, 11, 6, 40, 19] -> [10, 7, 6, 11, 40, 19] # 11 > 6
            ^
          i = 3

[10, 7, 6, 11, 40, 19] # no swap
                ^
              i = 4

[10, 7, 6, 11, 40, 19] -> [10, 7, 6, 11, 19, 40] # 40 > 19
                    ^
                  i = 5
```

### Round 2
Increment $round$, and repeat the same traversal, i.e. $i = 1$ and increment $i$ till $i < n - round$

```python 
[10, 7, 6, 11, 19, 40] ->  [7, 10, 6, 11, 19, 40] # 10 > 7
     ^   

[7, 10, 6, 11, 19, 40] -> [7, 6, 10, 11, 19, 40] # 10 > 6
        ^

[7, 6, 10, 11, 19, 40] # no swap
            ^

[7, 6, 10, 11, 19, 40] # no swap
                ^
```

### Round 3

Increment $round$ till $round < n$ and keep repeating the same traversal process discussed above.

```python
[7, 6, 10, 11, 19, 40] -> [6, 7, 10, 11, 19, 40] # 7 > 6
    ^

[6, 7, 10, 11, 19, 40] # no swap
        ^

[6, 7, 10, 11, 19, 40] # no swap
            ^
```

<br>

## Optimizing Bubble Sort

The traversals from **Round 4** ($round = 3$), till **Round 6** ($round = 5$) don't swap any values. Since, as you must have already seen, the array was fully sorted in **Round 3**. 

Well then can't we just stop right when the array is fully sorted, saving ourselves (or the computer) to do a few extra redundant steps?

<br>

After pondering a little, we can deduce a condition to stop traversing the array any further (when sorted), i.e. we'll stop progressing into the further rounds, if there were no swaps made in the current round.

To do this we can simply make use of a boolean variable $swapped$ which will be initialized to $false$ before the beginning of each round. If a swap is made, $swapped$ is made $true$. At the end of a round, we check if $swapped == false$. If yes, then we *break* out of the loop, else we continue with the traversal steps as usual.

This not only breaks out of the algorithm once the array is sorted, but moreover it reduces the time complexity of the best case scenario of the algorithm, i.e. when the array is already sorted, we only traverse the full array once! Even better than Selection Sort, isn't it?

<br>

## Pseudocode
1. Traverse `arr` with variable $round = 0$, incrementing it till $round < arr.length$
2. In each round, traverse `arr` with a variable $i = 1$, incrementing it till $i < arr.length - round$; while testing the following condition:
    - if $arr[i-1] > arr[i]$, then $swap(arr[i-1],\ arr[i])$
3. Keep the track of a swap happening in a round with a bool variable $swapped$, which is initialized to $false$ at the beginning of each round, and is assigned $true$ when a swap occurs.
4. After a round:
    - if $swapped == false$, then break out of the loop (array is sorted now)
    - otherwise repeat steps 2, 3 and 4
5. Break out of loop when $round < arr.length$ is no longer $true$.

<br>

## Time and Space Complexity

The worst case time complexity of Bubble Sort is the same as Selection Sort's, i.e.

$$ Time \ Complexity \ (Worst \ Case) \rightarrow  O(n^2) $$

However, its best case time complexity is $O(n)$.

$$ Space \ Complexity \rightarrow O(1)$$