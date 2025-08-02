# Assignment 6: Medians and Order Statistics & Elementary Data Structures

## Overview  
This repository contains two Python modules and a report of empirical and theoretical findings for:  
1. **Selection Algorithms** (deterministic Median-of-Medians and randomized Quickselect)  
2. **Elementary Data Structures** (DynamicArray, Matrix, Stack, Queue, LinkedList, TreeNode)

## Prerequisites  
- Python 3.6 or later  
- No external libraries required  

## Running the Selection Algorithms  
1. Open a terminal and navigate to this directory.  
2. Execute:
   ```bash
   python3 selection_algorithms.py
You will see a table of timings (in milliseconds) comparing the deterministic and randomized selection algorithms on random, sorted, and reverse-sorted inputs of sizes 1 000, 5 000, and 10 000.

Running the Data Structures Module
In the same directory, run:

python3 data_structures.py
You will see the preorder traversal of a sample rooted tree printed to the console:

Summary of Findings
The deterministic Median-of-Medians algorithm guarantees a worst-case linear runtime by choosing a “good” pivot, but its extra grouping and median computations incur higher constant factors. Randomized Quickselect achieves expected linear time with lower overhead and consistently outperforms the deterministic method in wall-clock tests across varied input distributions. Both algorithms scale linearly, but Quickselect’s simplicity and speed make it suitable for general-purpose use; the deterministic method is best when strict worst-case guarantees are required.

The data structures module demonstrates common trade-offs:

DynamicArray delivers amortized O(1) append and O(1) access

Matrix supports flexible row/column operations in O(r×c)

Stack and Queue wrappers provide amortized O(1) push/pop and enqueue/dequeue

LinkedList offers true O(1) head operations and O(n) traversal or tail operations

TreeNode preorder traversal runs in O(n) and models hierarchical data

These implementations can be adapted to real-world applications ranging from statistical selection and streaming medians to graph algorithms, grid-based simulations, and hierarchical data processing.