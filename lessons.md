# Lessons
Here are all lessons on [codility](https://www.codility.com/) that I have done.

TODO:
- [x] Lesson 1 - Iterations
- [x] Lesson 2 - Arrays
- [x] Lesson 3 - Time Complexity
- [x] Lesson 4 - Counting Elements
- [x] Lesson 5 - Prefix Sums
- [ ] Lesson 6 - Sorting
- [ ] Lesson 7 - Stacks and Queues
- [ ] Lesson 8 - Leader
- [ ] Lesson 9 - Maximum slice problem
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

```py
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

```py
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
```py
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

```py
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
```py
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
```py
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

```py
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

```py
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

```py
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

```py
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

```py
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

```py
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

```py
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
[Solution reference](https://www.martinkysel.com/codility-minavgtwoslice-solution/)
```py
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

```py
44% 22m
def solution(A):
    # sorted in nlon desc
    A = sorted(A, reverse=True)
    # return the largest 3 elem
    return A[0] * A[1] * A[2]
```

```py
77% 18m
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

```py
100% 8m
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

```py
100% 2m
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

```py
75% 15m
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

```py
100% 26m
ref: https://codesays.com/2014/solution-to-triangle-by-codility/
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

```

```py

```