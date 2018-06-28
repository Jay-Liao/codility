# Lessons
Here are all lessons on [codility](https://www.codility.com/) that I have done.

TODO:
- [x] Lesson 1 - Iterations
- [x] Lesson 2 - Arrays
- [x] Lesson 3 - Time Complexity
- [x] Lesson 4 - Counting Elements
- [x] Lesson 5 - Prefix Sums
- [x] Lesson 6 - Sorting
- [x] Lesson 7 - Stacks and Queues
- [x] Lesson 8 - Leader
- [x] Lesson 9 - Maximum slice problem
- [ ] Lesson 10 - Prime and composite numbers
- [ ] Lesson 11 - Sieve of Eratosthenes
- [ ] Lesson 12 - Euclidean algorithm
- [ ] Lesson 13 - Fibonacci numbers
- [ ] Lesson 14 - Binary search algorithm
- [ ] Lesson 15 - Caterpillar method
- [ ] Lesson 16 - Greedy algorithms
- [ ] Lesson 17 - Dynamic programming
- [ ] Lesson 90 - Tasks from Indeed Prime 2015 challenge
- [ ] Lesson 91 - Tasks from Indeed Prime 2016 challenge
- [ ] Lesson 92 - Tasks from Indeed Prime 2016 College Coders challenge
- [ ] Lesson 99 - Future training


## Lesson 1 - Iteration
### 1-1 BinaryGap 100%
---
```
Task description
A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.

Write a function:

def solution(N)

that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.

Assume that:

N is an integer within the range [1..2,147,483,647].
Complexity:

expected worst-case time complexity is O(log(N));
expected worst-case space complexity is O(1).
Copyright 2009–2018 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
```

```python
def solution(N):
    # shift N
    while N % 2 != 1:
        N = N >> 1
    bs = bin(N)[2:]
    counter = 0
    max_zero_count = 0
    bs_size = len(bs)
    index = bs_size - 1

    while index >= 0:
        if bs[index] == "0":
            counter += 1
        else:
            max_zero_count = counter if counter > max_zero_count else max_zero_count
            counter = 0
        index -= 1
    return max_zero_count
```

## Lesson 2 - Array
### 2-1 CyclicRotation 100%
---
```
An array A consisting of N integers is given. Rotation of the array means that each element is shifted right by one index, and the last element of the array is moved to the first place. For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] (elements are shifted right by one index and 6 is moved to the first place).

The goal is to rotate array A K times; that is, each element of A will be shifted to the right K times.

Write a function:

def solution(A, K)

that, given an array A consisting of N integers and an integer K, returns the array A rotated K times.

For example, given

    A = [3, 8, 9, 7, 6]
    K = 3
the function should return [9, 7, 6, 3, 8]. Three rotations were made:

    [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
    [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
    [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]
For another example, given

    A = [0, 0, 0]
    K = 1
the function should return [0, 0, 0]

Given

    A = [1, 2, 3, 4]
    K = 4
the function should return [1, 2, 3, 4]

Assume that:

N and K are integers within the range [0..100];
each element of array A is an integer within the range [−1,000..1,000].
In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.

Copyright 2009–2018 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
```

```python
def solution(A, K):
    if len(A) <= 1 or len(A) == K:
        return A
    while K > 0:
        A.insert(0, A.pop())
        K -= 1
    return A
```

### 2-2 OddOccurrencesInArray 100%
---
```
Task description
A non-empty array A consisting of N integers is given. The array contains an odd number of elements, and each element of the array can be paired with another element that has the same value, except for one element that is left unpaired.

For example, in array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the elements at indexes 0 and 2 have value 9,
the elements at indexes 1 and 3 have value 3,
the elements at indexes 4 and 6 have value 9,
the element at index 5 has value 7 and is unpaired.
Write a function:

def solution(A)

that, given an array A consisting of N integers fulfilling the above conditions, returns the value of the unpaired element.

For example, given array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the function should return 7, as explained in the example above.

Assume that:

N is an odd integer within the range [1..1,000,000];
each element of array A is an integer within the range [1..1,000,000,000];
all but one of the values in A occur an even number of times.
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(1) (not counting the storage required for input arguments).
Copyright 2009–2018 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
```
```python
def solution(A):
    num_map = dict()
    for num in A:
        if num not in num_map:
            num_map[num] = 1
        else:
            num_map[num] += 1
    for k, v in num_map.items():
        if v % 2 == 1:
            return k
```
## Lesson 3 - Time Complexity 
### 3-1 FrogJmp 100%
---
```
Task description
A small frog wants to get to the other side of the road. The frog is currently located at position X and wants to get to a position greater than or equal to Y. The small frog always jumps a fixed distance, D.

Count the minimal number of jumps that the small frog must perform to reach its target.

Write a function:

def solution(X, Y, D)

that, given three integers X, Y and D, returns the minimal number of jumps from position X to a position equal to or greater than Y.

For example, given:

  X = 10
  Y = 85
  D = 30
the function should return 3, because the frog will be positioned as follows:

after the first jump, at position 10 + 30 = 40
after the second jump, at position 10 + 30 + 30 = 70
after the third jump, at position 10 + 30 + 30 + 30 = 100
Assume that:

X, Y and D are integers within the range [1..1,000,000,000];
X ≤ Y.
Complexity:

expected worst-case time complexity is O(1);
expected worst-case space complexity is O(1).
Copyright 2009–2018 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
```

```python
def solution(X, Y, D):
    distance = Y - X
    jumps = distance // D
    jumps = jumps + 1 if distance % D else jumps
    return jumps
```

### 3-2 PermMissingElem 100%

```
Task description
An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

def solution(A)

that, given an array A, returns the value of the missing element.

For example, given array A such that:

  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
the function should return 4, as it is the missing element.

Assume that:

N is an integer within the range [0..100,000];
the elements of A are all distinct;
each element of array A is an integer within the range [1..(N + 1)].
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(1) (not counting the storage required for input arguments).
Copyright 2009–2018 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
```
```python
def solution(A):
    expected_sum = 0
    for i in range(1, len(A) + 2):
        expected_sum += i
        
    for num in A:
        expected_sum -= num
    return expected_sum
```
### 3-3 TapeEquilibrium 100%


```
Task description
A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.

Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].

The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

In other words, it is the absolute difference between the sum of the first part and the sum of the second part.

For example, consider array A such that:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
We can split this tape in four places:

P = 1, difference = |3 − 10| = 7 
P = 2, difference = |4 − 9| = 5 
P = 3, difference = |6 − 7| = 1 
P = 4, difference = |10 − 3| = 7 
Write a function:

def solution(A)

that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.

For example, given:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
the function should return 1, as explained above.

Assume that:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−1,000..1,000].
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N) (not counting the storage required for input arguments).
Copyright 2009–2018 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
```
```python
def solution(A):
    # accumulate sum
    sum = 0
    for num in A:
        sum += num
    min = None
    accu = 0
    for i in range(len(A) - 1):
        num = A[i]
        accu += num
        diff = accu - (sum - accu)
        abs_diff = -diff if diff < 0 else diff
        if min is None:
            min = abs_diff
        elif abs_diff < min:
            min = abs_diff
    return min
```

## Lesson 4 - Counting Elements
### 4-1 FrogRiverOne 100%
---
```
Task description
A small frog wants to get to the other side of a river. The frog is initially located on one bank of the river (position 0) and wants to get to the opposite bank (position X+1). Leaves fall from a tree onto the surface of the river.

You are given an array A consisting of N integers representing the falling leaves. A[K] represents the position where one leaf falls at time K, measured in seconds.

The goal is to find the earliest time when the frog can jump to the other side of the river. The frog can cross only when leaves appear at every position across the river from 1 to X (that is, we want to find the earliest moment when all the positions from 1 to X are covered by leaves). You may assume that the speed of the current in the river is negligibly small, i.e. the leaves do not change their positions once they fall in the river.

For example, you are given integer X = 5 and array A such that:

  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
In second 6, a leaf falls into position 5. This is the earliest time when leaves appear in every position across the river.

Write a function:

def solution(X, A)

that, given a non-empty array A consisting of N integers and integer X, returns the earliest time when the frog can jump to the other side of the river.

If the frog is never able to jump to the other side of the river, the function should return −1.

For example, given X = 5 and array A such that:

  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
the function should return 6, as explained above.

Assume that:

N and X are integers within the range [1..100,000];
each element of array A is an integer within the range [1..X].
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(X) (not counting the storage required for input arguments).
Copyright 2009–2018 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
```

```python
def solution(X, A):
    record_map = dict()
    for i in range(1, X+1):
        record_map[i] = True
    # print(f"record_map: {record_map}")
    for index in range(len(A)):
        num = A[index]
        record_map.pop(num, None)
        if len(record_map.keys()) == 0:
            return index
    return -1
```

### 4-2 MissingInteger 100%
---
```
Task description
This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Assume that:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N) (not counting the storage required for input arguments).
Copyright 2009–2018 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
```

```python
def solution(A):
    max_num = max(A)
    if max_num < 0:
        return 1
    num_map = dict()
    for num in A:
        num_map[num] = True
    for num in range(max_num):
        if num > 0 and not num_map.get(num, False):
            return num
    return max_num + 1

```

### 4-3 PermCheck 100%
---
```
Task description
A non-empty array A consisting of N integers is given.

A permutation is a sequence containing each element from 1 to N once, and only once.

For example, array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
is a permutation, but array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
is not a permutation, because value 2 is missing.

The goal is to check whether array A is a permutation.

Write a function:

def solution(A)

that, given an array A, returns 1 if array A is a permutation and 0 if it is not.

For example, given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
the function should return 1.

Given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
the function should return 0.

Assume that:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [1..1,000,000,000].
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N) (not counting the storage required for input arguments).
Copyright 2009–2018 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
```

```python
def solution(A):
    num_map = dict()
    sum = 0
    for num in A:
        sum += num
        is_existing = num_map.get(num, False)
        if is_existing:
            return 0
        else:
            num_map[num] = True
    
    expected_sum = (1 + len(A)) * len(A) // 2
    if sum != expected_sum:
        return 0
    else:
        return 1
```

### 4-4 MaxCounters 100%
---
```
Task description
You are given N counters, initially set to 0, and you have two possible operations on them:

increase(X) − counter X is increased by 1,
max counter − all counters are set to the maximum value of any counter.
A non-empty array A of M integers is given. This array represents consecutive operations:

if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
if A[K] = N + 1 then operation K is max counter.
For example, given integer N = 5 and array A such that:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the values of the counters after each consecutive operation will be:

    (0, 0, 1, 0, 0)
    (0, 0, 1, 1, 0)
    (0, 0, 1, 2, 0)
    (2, 2, 2, 2, 2)
    (3, 2, 2, 2, 2)
    (3, 2, 2, 3, 2)
    (3, 2, 2, 4, 2)
The goal is to calculate the value of every counter after all operations.

Write a function:

def solution(N, A)

that, given an integer N and a non-empty array A consisting of M integers, returns a sequence of integers representing the values of the counters.

The sequence should be returned as:

a structure Results (in C), or
a vector of integers (in C++), or
a record Results (in Pascal), or
an array of integers (in any other programming language).
For example, given:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the function should return [3, 2, 2, 4, 2], as explained above.

Assume that:

N and M are integers within the range [1..100,000];
each element of array A is an integer within the range [1..N + 1].
Complexity:

expected worst-case time complexity is O(N+M);
expected worst-case space complexity is O(N) (not counting the storage required for input arguments).
Copyright 2009–2018 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
```

```python
def solution(N, A):
    max_counter = N + 1
    counter_map = dict()
    # keep max_value
    max_value = 0
    # keep base_value
    base_value = 0
    for num in A:
        index = num - 1
        # 1 <= X <= N, increase(X)
        if num <= N:
            counter_value = counter_map.get(index, base_value)
            counter_value += 1
            counter_map[index] = counter_value
            if counter_value > max_value:
                max_value = counter_value
        # X = N + 1, set max_counter
        elif num == max_counter:
            counter_map = dict()
            base_value = max_value
            
    counter_list = [0] * N
    for index in range(len(counter_list)):
        counter_list[index] = counter_map.get(index, base_value)
    return counter_list
```

## Lesson 5 - Prefix Sums
### 5-1 CountDiv 100%
---
```
Task description
Write a function:

def solution(A, B, K)

that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

{ i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

Assume that:

A and B are integers within the range [0..2,000,000,000];
K is an integer within the range [1..2,000,000,000];
A ≤ B.
Complexity:

expected worst-case time complexity is O(1);
expected worst-case space complexity is O(1).
Copyright 2009–2018 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
```

```python
def solution(A, B, K):
    answer = B // K - A // K
    if A % K == 0:
        answer += 1
    return answer
```
### 5-2 PassingCars 100%
---
```
Task description
A non-empty array A consisting of N integers is given. The consecutive elements of array A represent consecutive cars on a road.

Array A contains only 0s and/or 1s:

0 represents a car traveling east,
1 represents a car traveling west.
The goal is to count passing cars. We say that a pair of cars (P, Q), where 0 ≤ P < Q < N, is passing when P is traveling to the east and Q is traveling to the west.

For example, consider array A such that:

  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).

Write a function:

def solution(A)

that, given a non-empty array A of N integers, returns the number of pairs of passing cars.

The function should return −1 if the number of pairs of passing cars exceeds 1,000,000,000.

For example, given:

  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
the function should return 5, as explained above.

Assume that:

N is an integer within the range [1..100,000];
each element of array A is an integer that can have one of the following values: 0, 1.
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(1) (not counting the storage required for input arguments).
Copyright 2009–2018 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
```

```python
def solution(A):
    all_west = 0
    for num in A:
        if num == 1:
            all_west += 1
            
    counter = 0
    current_west = all_west
    for num in A:
        if num == 0:
            counter += current_west
        elif num == 1:
            current_west -= 1
    
    return counter if counter <= 1000000000 else -1
```

### 5-3 GenomicRangeQuery 100%
---
```
Task description
A DNA sequence can be represented as a string consisting of the letters A, C, G and T, which correspond to the types of successive nucleotides in the sequence. Each nucleotide has an impact factor, which is an integer. Nucleotides of types A, C, G and T have impact factors of 1, 2, 3 and 4, respectively. You are going to answer several queries of the form: What is the minimal impact factor of nucleotides contained in a particular part of the given DNA sequence?

The DNA sequence is given as a non-empty string S = S[0]S[1]...S[N-1] consisting of N characters. There are M queries, which are given in non-empty arrays P and Q, each consisting of M integers. The K-th query (0 ≤ K < M) requires you to find the minimal impact factor of nucleotides contained in the DNA sequence between positions P[K] and Q[K] (inclusive).

For example, consider string S = CAGCCTA and arrays P, Q such that:

    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6
The answers to these M = 3 queries are as follows:

The part of the DNA between positions 2 and 4 contains nucleotides G and C (twice), whose impact factors are 3 and 2 respectively, so the answer is 2.
The part between positions 5 and 5 contains a single nucleotide T, whose impact factor is 4, so the answer is 4.
The part between positions 0 and 6 (the whole string) contains all nucleotides, in particular nucleotide A whose impact factor is 1, so the answer is 1.
Write a function:

def solution(S, P, Q)

that, given a non-empty string S consisting of N characters and two non-empty arrays P and Q consisting of M integers, returns an array consisting of M integers specifying the consecutive answers to all queries.

The sequence should be returned as:

a Results structure (in C), or
a vector of integers (in C++), or
a Results record (in Pascal), or
an array of integers (in any other programming language).
For example, given the string S = CAGCCTA and arrays P, Q such that:

    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6
the function should return the values [2, 4, 1], as explained above.

Assume that:

N is an integer within the range [1..100,000];
M is an integer within the range [1..50,000];
each element of arrays P, Q is an integer within the range [0..N − 1];
P[K] ≤ Q[K], where 0 ≤ K < M;
string S consists only of upper-case English letters A, C, G, T.
Complexity:

expected worst-case time complexity is O(N+M);
expected worst-case space complexity is O(N) (not counting the storage required for input arguments).
Copyright 2009–2018 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
```

```python
def solution(S, P, Q):
    answers = list()
    for index in range(len(P)):
        dna_seq = S[P[index]:Q[index]+1]
        if "A" in dna_seq:
            answer = 1
        elif "C" in dna_seq:
            answer = 2
        elif "G" in dna_seq:
            answer = 3
        elif "T" in dna_seq:
            answer = 4
        answers.append(answer)
    return answers
```

### 5-4 MinAvgTwoSlice 100%
---
```
Task description
A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P < Q < N, is called a slice of array A (notice that the slice contains at least two elements). The average of a slice (P, Q) is the sum of A[P] + A[P + 1] + ... + A[Q] divided by the length of the slice. To be precise, the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).

For example, array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
contains the following example slices:

slice (1, 2), whose average is (2 + 2) / 2 = 2;
slice (3, 4), whose average is (5 + 1) / 2 = 3;
slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.
The goal is to find the starting position of a slice whose average is minimal.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the starting position of the slice with the minimal average. If there is more than one slice with a minimal average, you should return the smallest starting position of such a slice.

For example, given array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
the function should return 1, as explained above.

Assume that:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−10,000..10,000].
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N) (not counting the storage required for input arguments).
Copyright 2009–2018 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
```

```python
"""
ref: https://www.martinkysel.com/codility-minavgtwoslice-solution/
"""

def solution(A):
    min_v = None
    idx = -1
    for index in range(len(A) - 1):
        v = (A[index] + A[index + 1]) / 2
        if min_v is None:
            min_v = v
            idx = index
        elif v < min_v:
            min_v = v
            idx = index
            
    for index in range(len(A) - 2):
        v = (A[index] + A[index + 1] + A[index + 2]) / 3
        if min_v is None:
            min_v = v
            idx = index
        elif v < min_v:
            min_v = v
            idx = index
    return idx
```
## Lesson 6 - Sorting
### 6-1 MaxProductOfThree 100%
---
```
Task description
A non-empty array A consisting of N integers is given. The product of triplet (P, Q, R) equates to A[P] * A[Q] * A[R] (0 ≤ P < Q < R < N).

For example, array A such that:

  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6
contains the following example triplets:

(0, 1, 2), product is −3 * 1 * 2 = −6
(1, 2, 4), product is 1 * 2 * 5 = 10
(2, 4, 5), product is 2 * 5 * 6 = 60
Your goal is to find the maximal product of any triplet.

Write a function:

def solution(A)

that, given a non-empty array A, returns the value of the maximal product of any triplet.

For example, given array A such that:

  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6
the function should return 60, as the product of triplet (2, 4, 5) is maximal.

Assume that:

N is an integer within the range [3..100,000];
each element of array A is an integer within the range [−1,000..1,000].
Complexity:

expected worst-case time complexity is O(N*log(N));
expected worst-case space complexity is O(1) (not counting the storage required for input arguments).
Copyright 2009–2018 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
```

```python
"""
44% 22m
"""

def solution(A):
    # sorted in nlon desc
    A = sorted(A, reverse=True)
    # return the largest 3 elem
    return A[0] * A[1] * A[2]
```

```python
"""
77% 18m
"""

def solution(A):
    # build positive/negative num list
    PA = list()
    NA = list()
    is_zero = False
    for num in A:
        if num > 0:
            PA.append(num)
        else:
            NA.append(num)
        if num == 0:
            is_zero = True
            
    PA = sorted(PA, reverse=True)
    NA = sorted(NA, reverse=True)
    """
    there are some cases would be largest three product
    1. 3 largest positive numbers
    2. 1 largest positive number * 2 largest negative numbers
    3. 3 smallest negative numbers
    4. zero
    """
    case1 = None
    case2 = None
    case3 = None
    case4 = None if not is_zero else 0
    if len(PA) >= 3:
        case1 = PA[0] * PA[1] * PA[2]
    if len(PA) > 0 and len(NA) >= 2:
        case2 = PA[0] * NA[0] * NA[1]
    if len(PA) == 0:
        case3 = NA[0] * NA[1] * NA[2]
    candidates = [case1, case2, case3, case4]
    candidates = [candidate for candidate in candidates if candidate is not None]
    candidates = sorted(candidates, reverse=True)
    return candidates[0]
```

```python
"""
100% 8m
"""

def solution(A):
    # build positive/negative num list
    PA = list()
    NA = list()
    is_zero = False
    for num in A:
        if num > 0:
            PA.append(num)
        elif num < 0:
            NA.append(num)
        else:
            is_zero = True
            
    PA = sorted(PA, reverse=True)
    NA = sorted(NA)
    """
    there are some cases would be largest three product
    1. 3 largest positive numbers
    2. 1 largest positive number * 2 largest negative numbers
    3. 3 smallest negative numbers
    4. zero
    """
    case1 = PA[0] * PA[1] * PA[2] if len(PA) >= 3 else None
    case2 = PA[0] * NA[0] * NA[1] if len(PA) > 0 and len(NA) >= 2 else None
    case3 = NA[-1] * NA[-2] * NA[-3] if len(PA) == 0 else None
    case4 = 0 if is_zero else None
    candidates = [case1, case2, case3, case4]
    candidates = [candidate for candidate in candidates if candidate is not None]
    candidates = sorted(candidates, reverse=True)
    return candidates[0]
```

### 6-2 Distinct 100%
---
```
Task description
Write a function

class Solution { public int solution(int[] A); }

that, given an array A consisting of N integers, returns the number of distinct values in array A.

Assume that:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
For example, given array A consisting of six elements such that:

 A[0] = 2    A[1] = 1    A[2] = 1
 A[3] = 2    A[4] = 3    A[5] = 1
the function should return 3, because there are 3 distinct values appearing in array A, namely 1, 2 and 3.

Complexity:

expected worst-case time complexity is O(N*log(N));
expected worst-case space complexity is O(N) (not counting the storage required for input arguments).
Copyright 2009–2018 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
```

```python
"""
100% 2m
"""

def solution(A):
    return len(set(A))
```

### 6-3 Triangle 100%
---
```
Task description
An array A consisting of N integers is given. A triplet (P, Q, R) is triangular if 0 ≤ P < Q < R < N and:

A[P] + A[Q] > A[R],
A[Q] + A[R] > A[P],
A[R] + A[P] > A[Q].
For example, consider array A such that:

  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20
Triplet (0, 2, 4) is triangular.

Write a function:

int solution(int A[], int N);

that, given an array A consisting of N integers, returns 1 if there exists a triangular triplet for this array and returns 0 otherwise.

For example, given array A such that:

  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20
the function should return 1, as explained above. Given array A such that:

  A[0] = 10    A[1] = 50    A[2] = 5
  A[3] = 1
the function should return 0.

Assume that:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
Complexity:

expected worst-case time complexity is O(N*log(N));
expected worst-case space complexity is O(N) (not counting the storage required for input arguments).
Copyright 2009–2018 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
```

```python
"""
75% 15m
"""

def solution(A):
    # early return if N is invalid
    if len(A) < 3:
        return 0
    
    # check all combinations    
    for i in range(len(A) - 2):
        for j in range(i + 1, len(A) - 1):
            for k in range(j + 1, len(A)):
                if is_triangular(A[i], A[j], A[k]):
                    return 1
    return 0


def is_triangular(a, b, c):
    return (a + b > c) and (a + c) > b and (b + c) > a
```

```python
"""
100% 26m
ref: https://codesays.com/2014/solution-to-triangle-by-codility/
"""

def solution(A):
    # early return in N is invalid
    if len(A) < 3:
        return 0
    
    # sort A asc, ex. -11, -10, -9, -8, 0, 1, 2, 3, 99, 100
    A = sorted(A)
    for index in range(len(A) - 2):
        """
        if A[index+2] >= 0
        A[index+1] + A[index+2] > A[index]
        A[index+2] + A[index] > A[index+1]
        only check:
            A[index] + A[index+1] > A[index+2]
            
        if A[index+2] < 0 just pass
        because A < B < C < 0, B + C < A
        """
        if A[index+2] >= 0 and A[index] + A[index+1] > A[index+2]:
            return 1
    
    return 0
```

### 6-4 NumberOfDiscIntersections
---
```
Task description
We draw N discs on a plane. The discs are numbered from 0 to N − 1. An array A of N non-negative integers, specifying the radiuses of the discs, is given. The J-th disc is drawn with its center at (J, 0) and radius A[J].

We say that the J-th disc and K-th disc intersect if J ≠ K and the J-th and K-th discs have at least one common point (assuming that the discs contain their borders).

The figure below shows discs drawn for N = 6 and A as follows:

  A[0] = 1
  A[1] = 5
  A[2] = 2
  A[3] = 1
  A[4] = 4
  A[5] = 0


There are eleven (unordered) pairs of discs that intersect, namely:

discs 1 and 4 intersect, and both intersect with all the other discs;
disc 2 also intersects with discs 0 and 3.
Write a function:

def solution(A)

that, given an array A describing N discs as explained above, returns the number of (unordered) pairs of intersecting discs. The function should return −1 if the number of intersecting pairs exceeds 10,000,000.

Given array A shown above, the function should return 11, as explained above.

Assume that:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [0..2,147,483,647].
Complexity:

expected worst-case time complexity is O(N*log(N));
expected worst-case space complexity is O(N) (not counting the storage required for input arguments).
Copyright 2009–2018 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
```

```python
"""
56% 12m
"""

def solution(A):
    intersects = 0
    # intersect mean any point in other disc
    for i in range(len(A) - 1):
        for j in range(i + 1, len(A)):
            distance = j - i
            if distance <= A[i] + A[j]:
                intersects += 1
    if intersects > 10000000:
        return -1
    else:
        return intersects
```

```python
"""
100% 57m
ref: http://www.lucainvernizzi.net/blog/2014/11/21/codility-beta-challenge-number-of-disc-intersections/
"""

def solution(A):
    events = []
    for i, a in enumerate(A):
        events += [(i-a, +1), (i+a, -1)]
    events.sort(key=lambda x: (x[0], -x[1]))
    intersections, active_circles = 0, 0
    for _, circle_count_delta in events:
        intersections += active_circles * (circle_count_delta > 0)
        active_circles += circle_count_delta
        if intersections > 10E6:
            return -1
    return intersections
```

## Lesson 7 - Sorting
### 7-1 StoneWall 100%
---
```
Task description
You are going to build a stone wall. The wall should be straight and N meters long, and its thickness should be constant; however, it should have different heights in different places. The height of the wall is specified by an array H of N positive integers. H[I] is the height of the wall from I to I+1 meters to the right of its left end. In particular, H[0] is the height of the wall's left end and H[N−1] is the height of the wall's right end.

The wall should be built of cuboid stone blocks (that is, all sides of such blocks are rectangular). Your task is to compute the minimum number of blocks needed to build the wall.

Write a function:

int solution(int H[], int N);

that, given an array H of N positive integers specifying the height of the wall, returns the minimum number of blocks needed to build it.

For example, given array H containing N = 9 integers:

  H[0] = 8    H[1] = 8    H[2] = 5
  H[3] = 7    H[4] = 9    H[5] = 8
  H[6] = 7    H[7] = 4    H[8] = 8
the function should return 7. The figure shows one possible arrangement of seven blocks.



Assume that:

N is an integer within the range [1..100,000];
each element of array H is an integer within the range [1..1,000,000,000].
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N) (not counting the storage required for input arguments).
Copyright 2009–2018 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
```

```python
"""
100% 60m
ref: https://www.martinkysel.com/codility-stonewall-solution/
"""

def solution(H):
    if len(H) <= 1:
        return len(H)
    
    stack = list()
    blocks = 0
    
    for height in H:
        while len(stack) > 0 and stack[-1] > height:
            stack.pop()
        
        if len(stack) > 0 and stack[-1] == height:
            pass
        else:
            stack.append(height)
            blocks += 1
    return blocks
```

### 7-2 Brackets 100%
---
```
Task description
A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

S is empty;
S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, the string "{[()()]}" is properly nested but "([)()]" is not.

Write a function:

def solution(S)

that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.

Assume that:

N is an integer within the range [0..200,000];
string S consists only of the following characters: "(", "{", "[", "]", "}" and/or ")".
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N) (not counting the storage required for input arguments).
Copyright 2009–2018 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
```

```python
"""
50% 20m
"""

def solution(S):
    if len(S) == 0:
        return 1
        
    if len(S) % 2 > 0:
        return 0
        
    if S[0] in [")", "]", "}"]:
        return 0
        
    cmap = {
         "(": ")", 
         ")": "(",
         "[": "]",
         "]": "[",
         "{": "}",
         "}": "{"
    }
    
    for index in range(len(S)//2):
        c = S[index]
        if cmap[S[index]] != S[len(S) - index - 1]:
            return 0
    return 1
```

```python
"""
100% 10m
ref: https://codesays.com/2014/solution-to-brackets-by-codility/
"""

def solution(S):
    if len(S) % 2 > 0:
        return 0
        
    targets = ["{", "[", "("]
    cmap = {
        "}": "{",
        "]": "[",
        ")": "("
    }
    stack = list()
    
    for c in S:
        if c in targets:
            stack.append(c)
        else:
            if len(stack) == 0:
                return 0
            if cmap[c] != stack.pop():
                return 0
                
    if len(stack) == 0:
        return 1
    else:
        return 0
```

### 7-3 Fish
---
```
Task description
You are given two non-empty arrays A and B consisting of N integers. Arrays A and B represent N voracious fish in a river, ordered downstream along the flow of the river.

The fish are numbered from 0 to N − 1. If P and Q are two fish and P < Q, then fish P is initially upstream of fish Q. Initially, each fish has a unique position.

Fish number P is represented by A[P] and B[P]. Array A contains the sizes of the fish. All its elements are unique. Array B contains the directions of the fish. It contains only 0s and/or 1s, where:

0 represents a fish flowing upstream,
1 represents a fish flowing downstream.
If two fish move in opposite directions and there are no other (living) fish between them, they will eventually meet each other. Then only one fish can stay alive − the larger fish eats the smaller one. More precisely, we say that two fish P and Q meet each other when P < Q, B[P] = 1 and B[Q] = 0, and there are no living fish between them. After they meet:

If A[P] > A[Q] then P eats Q, and P will still be flowing downstream,
If A[Q] > A[P] then Q eats P, and Q will still be flowing upstream.
We assume that all the fish are flowing at the same speed. That is, fish moving in the same direction never meet. The goal is to calculate the number of fish that will stay alive.

For example, consider arrays A and B such that:

  A[0] = 4    B[0] = 0
  A[1] = 3    B[1] = 1
  A[2] = 2    B[2] = 0
  A[3] = 1    B[3] = 0
  A[4] = 5    B[4] = 0
Initially all the fish are alive and all except fish number 1 are moving upstream. Fish number 1 meets fish number 2 and eats it, then it meets fish number 3 and eats it too. Finally, it meets fish number 4 and is eaten by it. The remaining two fish, number 0 and 4, never meet and therefore stay alive.

Write a function:

def solution(A, B)

that, given two non-empty arrays A and B consisting of N integers, returns the number of fish that will stay alive.

For example, given the arrays shown above, the function should return 2, as explained above.

Assume that:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [0..1,000,000,000];
each element of array B is an integer that can have one of the following values: 0, 1;
the elements of A are all distinct.
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N) (not counting the storage required for input arguments).
Copyright 2009–2018 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
```

```python
"""
37% 16m
"""

def solution(A, B):
    # keep fish in stack
    # pop fish one by one if encounter oppsite direction
    fish_stack = list()
    index = len(A) - 1
    while index >= 0:
        current_fish = (A[index], B[index])
        if len(fish_stack) == 0 or current_fish[-1] == fish_stack[-1][-1]:
            fish_stack.append(current_fish)
        else:
            while len(fish_stack) > 0 and current_fish[0] > fish_stack[-1][0]:
                fish_stack.pop()
            if len(fish_stack) == 0:
                fish_stack.append(current_fish)
        index -= 1
    return len(fish_stack)
```

```python
"""
100% 25m
"""

def solution(A, B):
    pass_fish = 0
    downstream_fish = list()
    for index in range(len(A)):
        # encounter upstream fish
        if B[index] == 0:
            if len(downstream_fish) == 0:
                pass_fish += 1
            else:
                while len(downstream_fish) > 0 and downstream_fish[-1] < A[index]:
                    downstream_fish.pop()
                if len(downstream_fish) == 0:
                    pass_fish += 1
        # encounter downstream fish
        else:
            downstream_fish.append(A[index])
    return pass_fish + len(downstream_fish)
```

### 7-4 Nesting
---
```
Task description
A string S consisting of N characters is called properly nested if:

S is empty;
S has the form "(U)" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, string "(()(())())" is properly nested but string "())" isn't.

Write a function:

def solution(S)

that, given a string S consisting of N characters, returns 1 if string S is properly nested and 0 otherwise.

For example, given S = "(()(())())", the function should return 1 and given S = "())", the function should return 0, as explained above.

Assume that:

N is an integer within the range [0..1,000,000];
string S consists only of the characters "(" and/or ")".
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(1) (not counting the storage required for input arguments).
Copyright 2009–2018 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
```

```python
"""
12% 7m
"""

def solution(S):
    if len(S) == 0:
        return 1
    if len(S) % 2 > 0:
        return 0
    
    cmap = {
        "(": ")",
        ")": "("
    }
    
    for index in range(len(S)):
        if cmap[S[index]] != S[len(S) - 1 - index]:
            return 0
    return 1
```

```python
"""
50% 7m
"""

def solution(S):
    if len(S) == 0:
        return 1
    if len(S) % 2 > 0:
        return 0
    if S[0] != "(":
        return 0
    
    cmap = {
        "(": ")",
        ")": "("
    }
    
    for index in range(len(S)):
        if cmap[S[index]] != S[len(S) - 1 - index]:
            return 0
    return 1
```

```python
"""
100% 9m
"""

def solution(S):
    if len(S) == 0:
        return 1
    if len(S) % 2 > 0:
        return 0
    
    stack = list()
    for c in S:
        if c == "(":
            stack.append(c)
        else:
            try:
                stack.pop()
            except:
                return 0
    return 1 if len(stack) == 0 else 0
```

## Lesson 8 - Leader
### 8-1 Dominator
---
```
Task description
An array A consisting of N integers is given. The dominator of array A is the value that occurs in more than half of the elements of A.

For example, consider array A such that

 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3
The dominator of A is 3 because it occurs in 5 out of 8 elements of A (namely in those with indices 0, 2, 4, 6 and 7) and 5 is more than a half of 8.

Write a function

def solution(A)

that, given an array A consisting of N integers, returns index of any element of array A in which the dominator of A occurs. The function should return −1 if array A does not have a dominator.

Assume that:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
For example, given array A such that

 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3
the function may return 0, 2, 4, 6 or 7, as explained above.

Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(1) (not counting the storage required for input arguments).
Copyright 2009–2018 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
```

```python
"""
100% 26m
"""

def solution(A):
    half = len(A) // 2
    
    counter = dict()
    for index in range(len(A)):
        num = A[index]
        if num not in counter:
            counter[num] = list()
        counter[num].append(index)
        
    for k, v in counter.items():
        if len(v) > half:
            return v[0]
    return -1
```

### 8-2 EquiLeader
---
```
Task description
A non-empty array A consisting of N integers is given.

The leader of this array is the value that occurs in more than half of the elements of A.

An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N − 1] have leaders of the same value.

For example, given array A such that:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
we can find two equi leaders:

0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.
The goal is to count the number of equi leaders.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the number of equi leaders.

For example, given:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
the function should return 2, as explained above.

Assume that:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N) (not counting the storage required for input arguments).
Copyright 2009–2018 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
```

```python
"""
33% 18m
[1, 2] -> error
"""

def solution(A):
    half = len(A) // 2
    
    counter = dict()
    for index in range(len(A)):
        num = A[index]
        if num not in counter:
            counter[num] = list()
        counter[num].append(index)
        
    target = None
    for k, v in counter.items():
        if len(v) > half:
            target = v
            
    count = 0
    stack = list()
    for index in target:
        stack.append(index)
        pre_len = index + 1
        post_len = len(A) - pre_len
        
        if len(stack) > pre_len // 2 and len(target) - len(stack) > post_len // 2:
            count += 1
    
    return count
```

```python
"""
44% 2m
optimize: early return 0 if there is no leader
[4, 4, 2, 5, 3, 4, 4, 4] -> expected 3, but 2
"""

def solution(A):
    half = len(A) // 2
    
    counter = dict()
    for index in range(len(A)):
        num = A[index]
        if num not in counter:
            counter[num] = list()
        counter[num].append(index)
        
    target = None
    for k, v in counter.items():
        if len(v) > half:
            target = v
            
    if target is None:
        return 0
            
    count = 0
    stack = list()
    for index in target:
        stack.append(index)
        pre_len = index + 1
        post_len = len(A) - pre_len
        
        if len(stack) > pre_len // 2 and len(target) - len(stack) > post_len // 2:
            count += 1
    
    return count
```

```python
"""
66% 21m
optimize: go through all index
"""

def solution(A):
    half = len(A) // 2
    
    counter = dict()
    for index in range(len(A)):
        num = A[index]
        if num not in counter:
            counter[num] = list()
        counter[num].append(index)
        
    target = None
    for k, v in counter.items():
        if len(v) > half:
            target = v
            
    if target is None:
        return 0
            
    count = 0
    stack = list()
    for index in range(len(A)):
        if index in target:
            stack.append(index)
        pre_len = index + 1
        post_len = len(A) - pre_len
        if len(stack) > pre_len // 2 and len(target) - len(stack) > post_len // 2:
            count += 1
        
    return count
```

```python
"""
77% 4m
optimize: avoid check element in list
"""

def solution(A):
    half = len(A) // 2
    
    counter = dict()
    for index in range(len(A)):
        num = A[index]
        if num not in counter:
            counter[num] = list()
        counter[num].append(index)
        
    target = None
    for k, v in counter.items():
        if len(v) > half:
            target = v
            
    if target is None:
        return 0
            
    total_target = len(target)
    count = 0
    stack = list()
    for index in range(len(A)):
        if len(target) > 0 and target[0] == index:
            stack.append(target.pop(0))
        pre_len = index + 1
        post_len = len(A) - pre_len
        if len(stack) > pre_len // 2 and len(target) > post_len // 2:
            count += 1
        
    return count
```

```python
"""
100% 3m
optimize: avoid pop first element from list, it takes O(N)
"""

def solution(A):
    half = len(A) // 2
    
    counter = dict()
    for index in range(len(A)):
        num = A[index]
        if num not in counter:
            counter[num] = list()
        counter[num].append(index)
        
    target = None
    key = None
    for k, v in counter.items():
        if len(v) > half:
            target = v
            key = k
            
    if target is None:
        return 0
            
    total_target = len(target)
    count = 0
    key_count = 0
    for index in range(len(A)):
        if A[index] == key:
            key_count += 1
        pre_len = index + 1
        post_len = len(A) - pre_len
        if key_count > pre_len // 2 and total_target - key_count > post_len // 2:
            count += 1
        
    return count
```

## Lesson 9 - Maximum slice problem
### 9-1 MaxProfit
---
```
Task description
An array A consisting of N integers is given. It contains daily prices of a stock share for a period of N consecutive days. If a single share was bought on day P and sold on day Q, where 0 ≤ P ≤ Q < N, then the profit of such transaction is equal to A[Q] − A[P], provided that A[Q] ≥ A[P]. Otherwise, the transaction brings loss of A[P] − A[Q].

For example, consider the following array A consisting of six elements such that:

  A[0] = 23171
  A[1] = 21011
  A[2] = 21123
  A[3] = 21366
  A[4] = 21013
  A[5] = 21367
If a share was bought on day 0 and sold on day 2, a loss of 2048 would occur because A[2] − A[0] = 21123 − 23171 = −2048. If a share was bought on day 4 and sold on day 5, a profit of 354 would occur because A[5] − A[4] = 21367 − 21013 = 354. Maximum possible profit was 356. It would occur if a share was bought on day 1 and sold on day 5.

Write a function,

def solution(A)

that, given an array A consisting of N integers containing daily prices of a stock share for a period of N consecutive days, returns the maximum possible profit from one transaction during this period. The function should return 0 if it was impossible to gain any profit.

For example, given array A consisting of six elements such that:

  A[0] = 23171
  A[1] = 21011
  A[2] = 21123
  A[3] = 21366
  A[4] = 21013
  A[5] = 21367
the function should return 356, as explained above.

Assume that:

N is an integer within the range [0..400,000];
each element of array A is an integer within the range [0..200,000].
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(1) (not counting the storage required for input arguments).
Copyright 2009–2018 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
```

```python
"""
44% 30m
For example, for the input [8, 9, 3, 6, 1, 2] the solution returned a wrong answer (got 1 expected 3).
"""

def solution(A):
    if len(A) == 0:
        return 0
    
    min_num = A[0]
    min_lst = [min_num] * len(A)
    for index in range(len(A)):
        min_num = min(min_num, A[index])
        min_lst[index] = min_num
        
    max_num = A[len(A) - 1]
    max_lst = [max_num] * len(A)
    for index in range(len(A) - 1, -1, -1):
        max_num = max(max_num, A[index])
        max_lst[index] = max_num
    
    for index in range(len(A)):
        max_profit = max(0, max_lst[index] - min_lst[index])
    
    if max_profit == 0:
        return 0
    else:
        return max_profit
```

```
"""
100% 4m
"""

def solution(A):
    if len(A) == 0:
        return 0
    
    min_num = A[0]
    min_lst = [min_num] * len(A)
    for index in range(len(A)):
        min_num = min(min_num, A[index])
        min_lst[index] = min_num
        
    max_num = A[len(A) - 1]
    max_lst = [max_num] * len(A)
    for index in range(len(A) - 1, -1, -1):
        max_num = max(max_num, A[index])
        max_lst[index] = max_num
    
    max_profit = 0
    for index in range(len(A)):
        max_profit = max(max_profit, max_lst[index] - min_lst[index])
        
    if max_profit == 0:
        return 0
    else:
        return max_profit
```

### 9-2 MaxDoubleSliceSum
---
```
Task description
A non-empty array A consisting of N integers is given.

A triplet (X, Y, Z), such that 0 ≤ X < Y < Z < N, is called a double slice.

The sum of double slice (X, Y, Z) is the total of A[X + 1] + A[X + 2] + ... + A[Y − 1] + A[Y + 1] + A[Y + 2] + ... + A[Z − 1].

For example, array A such that:

    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2
contains the following example double slices:

double slice (0, 3, 6), sum is 2 + 6 + 4 + 5 = 17,
double slice (0, 3, 7), sum is 2 + 6 + 4 + 5 − 1 = 16,
double slice (3, 4, 5), sum is 0.
The goal is to find the maximal sum of any double slice.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the maximal sum of any double slice.

For example, given:

    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2
the function should return 17, because no double slice of array A has a sum of greater than 17.

Assume that:

N is an integer within the range [3..100,000];
each element of array A is an integer within the range [−10,000..10,000].
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N) (not counting the storage required for input arguments).
Copyright 2009–2018 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
```

```python
"""
53% 18m
Timeout: O(N**3)
"""

def solution(A):
    if len(A) < 3:
        return 0
    
    max_sum = 0
    for i in range(len(A) - 2):
        for j in range(i + 1, len(A) - 1):
            for k in range(j + 1, len(A)):
                slice1_sum = sum(A[i + 1:j])
                slice2_sum = sum(A[j + 1:k])
                max_sum = max(max_sum, slice1_sum + slice2_sum)
    return max_sum
```

```python
"""
100% 57m
ref: https://rafal.io/posts/codility-max-double-slice-sum.html
"""

def solution(A):
    n = len(A)
    if n < 3:
        return 0
    
    s1 = [0] * n
    # ignore first and last element
    for index in range(1, n - 1):
        s1[index] = max(0, s1[index - 1] + A[index])
        
    s2 = [0] * n
    for index in range(n - 2, 0, -1):
        s2[index] = max(s2[index+1]+A[index], 0)
        
    max_double = 0
    for index in range(1, n - 1):
        max_double = max(max_double, s1[index - 1] + s2[index + 1])
        
    return max_double
```

### 9-3 MaxSliceSum
---
```
Task description
A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P ≤ Q < N, is called a slice of array A. The sum of a slice (P, Q) is the total of A[P] + A[P+1] + ... + A[Q].

Write a function:

def solution(A)

that, given an array A consisting of N integers, returns the maximum sum of any slice of A.

For example, given array A such that:

A[0] = 3  A[1] = 2  A[2] = -6
A[3] = 4  A[4] = 0
the function should return 5 because:

(3, 4) is a slice of A that has sum 4,
(2, 2) is a slice of A that has sum −6,
(0, 1) is a slice of A that has sum 5,
no other slice of A has sum greater than (0, 1).
Assume that:

N is an integer within the range [1..1,000,000];
each element of array A is an integer within the range [−1,000,000..1,000,000];
the result will be an integer within the range [−2,147,483,648..2,147,483,647].
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N) (not counting the storage required for input arguments).
Copyright 2009–2018 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
```

```python
"""
53% 5m
For example, for the input [-2, 1] the solution returned a wrong answer (got -1 expected 1).
"""

def solution(A):
    if len(A) == 0:
        return 0
    if len(A) == 1:
        return A[0]
        
    pref = [0] * len(A)
    pref[0] = A[0]
    for index in range(1, len(A)):
        pref[index] = pref[index - 1] + A[index]
    return max(pref)
```


```python
"""
30% 16m
For example, for the input [-2, -2] the solution returned a wrong answer (got 0 expected -2).
"""

def solution(A):
    if len(A) == 0:
        return 0
    if len(A) == 1:
        return A[0]
    
    max_lst = [0] * len(A)
    max_lst[0] = A[0]
    for index in range(1, len(max_lst)):
        max_lst[index] = max(0, A[index], A[index - 1] + A[index])
    return max(max_lst)
```

```python
"""
53% 2m
Fix: max_lst[index] = max(A[index], A[index - 1] + A[index])
For example, for the input [1, 1, 1] the solution returned a wrong answer (got 2 expected 3).
"""

def solution(A):
    if len(A) == 0:
        return 0
    if len(A) == 1:
        return A[0]
    
    max_lst = [0] * len(A)
    max_lst[0] = A[0]
    for index in range(1, len(max_lst)):
        max_lst[index] = max(A[index], A[index - 1] + A[index])
    return max(max_lst)
```

```python
"""
100% 5m
Fix: max_lst[index] = max(A[index], max_lst[index - 1] + A[index])
"""

def solution(A):
    if len(A) == 0:
        return 0
    if len(A) == 1:
        return A[0]
    
    max_lst = [0] * len(A)
    max_lst[0] = A[0]
    for index in range(1, len(max_lst)):
        max_lst[index] = max(A[index], max_lst[index - 1] + A[index])
    return max(max_lst)
```

## Lesson 10 - Prime and composite numbers
### 10-1 CountFactors
---
```
Task description
A positive integer D is a factor of a positive integer N if there exists an integer M such that N = D * M.

For example, 6 is a factor of 24, because M = 4 satisfies the above condition (24 = 6 * 4).

Write a function:

def solution(N)

that, given a positive integer N, returns the number of its factors.

For example, given N = 24, the function should return 8, because 24 has 8 factors, namely 1, 2, 3, 4, 6, 8, 12, 24. There are no other factors of 24.

Assume that:

N is an integer within the range [1..2,147,483,647].
Complexity:

expected worst-case time complexity is O(sqrt(N));
expected worst-case space complexity is O(1).
Copyright 2009–2018 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
```

```python
"""
35% 22m
RUNTIME ERROR: N=16, N=36
TIMEOUT ERROR: N=3,628,800=10!, N=5,621,892, N=4,999,696
"""

def solution(N):
    max_factor = 0
    factors = 0
    for i in range(1, N + 1):
        if i == max_factor:
            return factors
        if N % i == 0:
            max_factor = max(i, N // i)
            factors += 2
```

```python
"""
50% 17m
TIMEOUT ERROR: N=1,000,000,000, N=MAX_INT, N=2147,395,600
"""

def solution(N):
    prime_map = dict()
    for i in range(2, N + 1):
        while is_prime(i) and N % i == 0:
            N = N // i
            if i not in prime_map:
                prime_map[i] = 0
            prime_map[i] = prime_map[i] + 1
    factors = 1
    for _, v in prime_map.items():
        factors *= (v + 1)

    return factors
        
def is_prime(num):
    if num == 1:
        return False
    counter = 0
    for i in range(1, num + 1):
        if num % i == 0:
            counter += 1
        if counter > 2:
            return False
    
    return counter == 2
```

```python
"""
100% 6m
ref: lesson pdf
"""

def solution(N):
    i = 1
    factors = 0
    while i * i < N:
        if N % i == 0:
            factors += 2
        i += 1
    if i * i == N:
        factors += 1
    return factors
```

### 10-2 MinPerimeterRectangle
---
```
Task description
```

```python
"""
100% 10m
"""

def solution(N):
    min_sum_of_sides = None
    i = 1
    while i * i < N:
        if N % i == 0:
            sum_of_sides = i + N // i
            min_sum_of_sides = sum_of_sides if min_sum_of_sides is None else min(min_sum_of_sides, sum_of_sides)
        i += 1
    if i * i == N:
        sum_of_sides = i * 2
        min_sum_of_sides = sum_of_sides if min_sum_of_sides is None else min(min_sum_of_sides, sum_of_sides)
    return min_sum_of_sides * 2
```

### 10-3 Flags
---
```
Task description
A non-empty array A consisting of N integers is given.

A peak is an array element which is larger than its neighbors. More precisely, it is an index P such that 0 < P < N − 1,  A[P − 1] < A[P] and A[P] > A[P + 1].

For example, the following array A:

    A[0] = 1
    A[1] = 2
    A[2] = 3
    A[3] = 4
    A[4] = 3
    A[5] = 4
    A[6] = 1
    A[7] = 2
    A[8] = 3
    A[9] = 4
    A[10] = 6
    A[11] = 2
has exactly three peaks: 3, 5, 10.

We want to divide this array into blocks containing the same number of elements. More precisely, we want to choose a number K that will yield the following blocks:

A[0], A[1], ..., A[K − 1],
A[K], A[K + 1], ..., A[2K − 1],
...
A[N − K], A[N − K + 1], ..., A[N − 1].
What's more, every block should contain at least one peak. Notice that extreme elements of the blocks (for example A[K − 1] or A[K]) can also be peaks, but only if they have both neighbors (including one in an adjacent blocks).

The goal is to find the maximum number of blocks into which the array A can be divided.

Array A can be divided into blocks as follows:

one block (1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2). This block contains three peaks.
two blocks (1, 2, 3, 4, 3, 4) and (1, 2, 3, 4, 6, 2). Every block has a peak.
three blocks (1, 2, 3, 4), (3, 4, 1, 2), (3, 4, 6, 2). Every block has a peak. Notice in particular that the first block (1, 2, 3, 4) has a peak at A[3], because A[2] < A[3] > A[4], even though A[4] is in the adjacent block.
However, array A cannot be divided into four blocks, (1, 2, 3), (4, 3, 4), (1, 2, 3) and (4, 6, 2), because the (1, 2, 3) blocks do not contain a peak. Notice in particular that the (4, 3, 4) block contains two peaks: A[3] and A[5].

The maximum number of blocks that array A can be divided into is three.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the maximum number of blocks into which A can be divided.

If A cannot be divided into some number of blocks, the function should return 0.

For example, given:

    A[0] = 1
    A[1] = 2
    A[2] = 3
    A[3] = 4
    A[4] = 3
    A[5] = 4
    A[6] = 1
    A[7] = 2
    A[8] = 3
    A[9] = 4
    A[10] = 6
    A[11] = 2
the function should return 3, as explained above.

Assume that:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [0..1,000,000,000].
Complexity:

expected worst-case time complexity is O(N*log(log(N)));
expected worst-case space complexity is O(N) (not counting the storage required for input arguments).
Copyright 2009–2018 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
```

```python
"""
45% 16m
"""

def solution(A):
    counter = 0
    for idx, n in enumerate(A):
        prev = A[idx - 1] if idx > 0 else None
        nxt = A[idx + 1] if idx < len(A) - 1 else None
        if prev is None or nxt is None:
            continue
        if n > prev and n > nxt:
            counter += 1
    return counter
```

### 10-4 Peaks
---
```
Task description
```

```python
```
