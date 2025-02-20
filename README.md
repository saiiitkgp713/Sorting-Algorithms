# Sorting Algorithms

This repository contains implementations of **Selection Sort, Insertion Sort, Merge Sort, and Quick Sort** algorithms.

## Selection Sort  
The `select_sort` function sorts a list in ascending order from a given index `i` to the end of the list. It takes three arguments:  
- **`a`** – The list to be sorted.  
- **`i`** – The starting index for sorting. If `i = 0`, the entire list is sorted.  
- **`n`** – The length of the list.  

**Time Complexity:** O(n²)  

## Insertion Sort  
The `insert_sort` function sorts a list in ascending order from a specified index `i` to the end. It takes three arguments:  
- **`a`** – The list to be sorted.  
- **`i`** – The starting index for sorting. If `i = 0`, the entire list is sorted.  
- **`n`** – The length of the list.  

**Time Complexity:**  
- **Worst case:** O(n²)  
- Generally performs better than selection sort in many cases.  

## Merge Sort  
Merge sort consists of two functions: `merge` and `merge_sort`.  
- **`merge`** – Combines two already sorted lists (`a` and `b`) into a single sorted list.  
- **`merge_sort`** – Recursively splits a list into two halves, sorts them, and merges them back using the `merge` function.  

**Time Complexity:** O(n log n)  
- More efficient than selection and insertion sort.  
- Requires additional memory due to new list creation during merging.  

## Quick Sort  
Quick sort is similar to merge sort but sorts the list **in place**, avoiding extra space usage. It takes three arguments:  
- **`a`** – The list to be sorted.  
- **`l`** – Left index (starting position).  
- **`r`** – Right index (ending position).  

If `l = 0` and `r = length of list`, the entire list is sorted. The algorithm partitions the list into two parts based on a pivot element, ensuring all smaller values are on the left and larger values on the right. It then recursively applies the same process until the list is sorted.  

**Time Complexity:**  
- **Worst case:** O(n²)  
- **Best & Average case:** O(n log n)  

Since it sorts **in place**, its **space complexity is significantly better** compared to merge sort.

---

Feel free to contribute and enhance these implementations!
