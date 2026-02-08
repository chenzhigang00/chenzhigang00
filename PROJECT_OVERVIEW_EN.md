# Project Overview

## Introduction

This is **chenzhigang00**'s personal GitHub profile repository, containing personal introduction and algorithm implementation code.

## Author Information

- **Name**: Chen Zhigang
- **Email**: 1312383034@qq.com
- **University**: Sun Yat-sen University (SYSU)
- **Major**: Software Engineering
- **Interest**: Artificial Intelligence
- **Current Research**: Federated Learning

## Project Structure

```
chenzhigang00/
├── README.md              # GitHub profile page
├── nyanparrot.gif         # Decorative GIF
└── algorithm/             # Algorithm implementations
    └── n-queen/          # Multiple solutions for N-Queens Problem
        ├── FIFO_Queue.py                    # FIFO Queue Branch and Bound
        ├── Priority_Queue.py                # Priority Queue Branch and Bound
        ├── backtrack_PermutationTree.py     # Backtracking with Permutation Tree
        ├── backtrack_SubsetTree.py          # Backtracking with Subset Tree
        └── 绘图1.vsdx                       # Algorithm diagram document
```

## Core Content: N-Queens Problem

### Problem Description

The N-Queens problem is a classic backtracking algorithm problem: Place N chess queens on an N×N chessboard so that no two queens can attack each other. This means no two queens can be in the same row, column, or diagonal.

### Implementation Methods

This project implements **4 different solutions**, demonstrating different algorithm design paradigms:

#### 1. **Backtracking - Subset Tree** (`backtrack_SubsetTree.py`)
- **Algorithm Idea**: Place queens row by row, trying N positions per row
- **Search Space**: Subset tree structure
- **Pruning Strategies**: 
  - Feasibility pruning: Check column and diagonal conflicts
  - Symmetry pruning: Utilize board symmetry, search only half the solution space
- **Features**: Simple implementation, easy to understand

#### 2. **Backtracking - Permutation Tree** (`backtrack_PermutationTree.py`)
- **Algorithm Idea**: Transform the problem into a permutation problem
- **Search Space**: Permutation tree structure
- **Optimizations**: 
  - Construct permutations by swapping elements
  - Naturally satisfies "one queen per row and column" constraint
  - Only needs to check diagonal conflicts
  - Uses symmetry pruning to reduce search space
- **Features**: Smaller search space, more efficient

#### 3. **Branch and Bound - FIFO Queue** (`FIFO_Queue.py`)
- **Algorithm Idea**: Use First-In-First-Out queue for breadth-first search
- **Data Structure**: Python `queue.Queue`
- **Features**: 
  - Level-order traversal of search tree
  - Uses feasibility and symmetry pruning
  - Suitable for finding all solutions

#### 4. **Branch and Bound - Priority Queue** (`Priority_Queue.py`)
- **Algorithm Idea**: Use priority queue (heap) to optimize search order
- **Data Structure**: Python `heapq` (max heap)
- **Priority Strategy**: Greater depth means higher priority
- **Features**: 
  - Intelligently selects nodes to expand
  - May find solutions faster
  - Suitable for finding optimal solutions

### Common Optimization Techniques

All implementations employ the following optimizations:

1. **Symmetry Pruning**: Leverage board symmetry by searching only the first half of positions in the first row, then obtaining symmetric solutions through mirroring
2. **Feasibility Pruning**: Check constraints before placing queens to avoid invalid searches
3. **Result Display**: Show all solutions in intuitive board format (using "Q" for queens, "." for empty spaces)

### Algorithm Comparison

| Algorithm Type | Time Complexity | Space Complexity | Use Case |
|---------------|-----------------|------------------|----------|
| Backtracking-Subset | O(N^N) | O(N) | Small-scale problems, easy to understand |
| Backtracking-Permutation | O(N!) | O(N) | Medium-scale, more efficient |
| Branch & Bound-FIFO | O(N^N) | O(N^N) | Need all solutions |
| Branch & Bound-Priority | O(N^N) | O(N^N) | Finding optimal solutions |

## Usage

Run any Python script:

```bash
cd algorithm/n-queen
python3 FIFO_Queue.py
# or
python3 Priority_Queue.py
# or
python3 backtrack_PermutationTree.py
# or
python3 backtrack_SubsetTree.py
```

Then enter the value of N (e.g., 4, 8), and the program will output the number of all feasible solutions and their specific arrangements.

### Example

When inputting `4`, it outputs all solutions for the 4-Queens problem:

```
2
[[2, 4, 1, 3], [3, 1, 4, 2]]

.Q..
...Q
Q...
..Q.

..Q.
Q...
...Q
.Q..
```

## Tech Stack

- **Programming Language**: Python 3
- **Main Libraries**: 
  - `queue` - FIFO queue implementation
  - `heapq` - Priority queue implementation

## Learning Value

This project is excellent for learning:

1. **Algorithm Design Paradigms**: Backtracking, Branch and Bound
2. **Data Structure Applications**: Queue, Priority Queue, Tree Structures
3. **Optimization Techniques**: Pruning strategies, symmetry exploitation
4. **Python Programming**: List operations, recursion, class definitions

## Summary

This is an excellent project showcasing algorithmic thinking and programming skills. Through comparing multiple solutions to the same problem, it provides deep understanding of different algorithms' characteristics and applicable scenarios. The code is clear with detailed comments, making it a great resource for learning classic algorithm problems.
