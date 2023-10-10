# Sorting-Algorithms
The following file provides the algorithms for Selection sort, Insertion sort, Merge sort & Quick sort

Selection sort algorithm:
	it has one single function "select_sort" which takes 3 arguments a, i, n and sorts the list in ascending order from index i to the end of the list.
	'a' is the list that needs to be sorted.
  'i' is the index of the list from where the list needs to be sorted.
  		if 'i' is provide with a value 0, then the entire list will be sorted in ascending order.
  'n' is the length of the the list 'a'
  time complexity is of O(n^2)

Insertion sort algorithm
  it has one single function "insert_sort" which takes 3 arguments a, i, n and sorts the list in ascending order from index i to the end of the list
  'a' is the list that needs to be sorted.
  'i' is the index of the list from where the list needs to be sorted.
    if 'i' is provide with a value 0, then the entire list will be sorted in ascending order.
  'n' is the length of the the list 'a'
  worst case time complexity is of O(n^2) but it is relatively better than Selection sort in many cases.
  
  
Merge sort algorithm
	it has two functions "merge" and "merge_sort".
	"merge" takes two already sorted lists 'a' and 'b' as arguments, to combine them and returns a sorted list which has length  = sum of lengths of list 'a' and list 'b'
	"merge_sort" is the main function which takes one single list as an argument for sorting. It splits a list into two halves and uses the above mentioned "merge" fucntion to combine again. It also recursively calls itself inside merge function to split the actual list provided into its base case(size one list) where lists to be combined have only a single element which are sorted by defaualt...
	worst case time complexity is of O(n*logn) which is better than Insertion and selection sort algorithms.
	But everytime when it merges two sorted lists it creates a new list thereby increasing the space complexity.

Quick sort sort algorithm
 This algorithm is kinda a sibling to the Merge sort but sorts the list inplace and don't take up any extra space.
 it takes three arguments: a list 'a' and two index positions 'l' for left, 'r' for right between which the list is sorted.
 if l = 0, r = len of the list, then the entire list will be sorted.
 the algorithm divides the total list(or sub list with sepcified 'l' and 'r' indices)into two parts, such that, the elements less than or equal to the first element of the list(or sublist) into first part and values greater will be in second part. the first element(with which the comparison is made) is then later placed between the two divided parts so all the elements less are left side and greater are right side. 
 It keeps on doing the same operation recursively and gets to base case where the lists are already sorted and thus yielding an entire sorted list.
 Time complexity is O(n^2) worst case. O(nlogn) for average and best cases. But it is an inplace sorting algo, so space complexity far better when compared to Merge sort
