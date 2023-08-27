# 12.-Data-Structures-and-Algorithms-Learning-and-Practice-Python :large_blue_circle::heavy_minus_sign::large_blue_circle::heavy_minus_sign::large_blue_circle: 	:clipboard:
My learning journey of Data Structures and Algorithms in Python (work in progress)

## Thoughts on starting this learning journey
Back before I started programming,  I was introduced to a website for programmers to test their skills called LeetCode, which provides coding interview questions for coders
to try out. Curious, I went to look at the questions and found myself overwhelmed by how bizzare the questions look. I took a look around the internet to see how people solve LeetCode questions and realised they understood this important programming concept that I haven't touched before - Data Structures and Algorithms.

Hence the birth of this repository, for me to bridge this gap.

(Funnily enough, when I first looked at LeetCode I had no idea how to navigate their website. I saw they had an answer template where you can type in your code answers but 
it contained many different kinds of programming languages. Obviously I went for the one I knew, Python. But then there was 2 options, Python and Python3. Then I looked at
the starting code (at the time I didn't know about Object-Oriented Programming and Classes yet) and I couldn't tell which was the one I was supposed to use. Furthermore, I 
was literally unable to understand any of the questions and give any relevant answer. So as you can see, this is how disastrous my first LeetCode experience was. (Eventually I found out I was using Python3, which I'm pretty sure is the version everyone using Python is using, after copy-pasting some of the usual codes I've written and asking ChatGPT hahaha...))

Learning and Practices are both organised under each folder for their respective Data Structure/Algorithm.

<br>

**Source(s):**
+ https://www.youtube.com/playlist?list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12 (codebasics) 

<br>

## Table of Contents:
+ [Code Description](#codedescription)

  + [On Data Structures](#datastructures):
    + [Tutorial 1 - What are Data Structures](#tutorial1)  
    + [Tutorial 2 - Big O Notation](#tutorial2)  
    + [Tutorial 3 - Concept of Recursion](#tutorial3)  
    + [Tutorial 4 - Arrays (Data Structure)](#tutorial4)  
    + [Tutorial 5 - Linked Lists (Data Structure)](#tutorial5)  
    + [Tutorial 6 - Hash Tables (Data Structure)](#tutorial6)  
      + [Tutorial 6.1 - Hash Tables Collision Handling](#tutorial6.1)  
    + [Tutorial 7 - Stacks (Data Structure)](#tutorial7)  
    + [Tutorial 8 - Queues (Data Structure)](#tutorial8)  
    + [Tutorial 9 - Trees and General Trees (Data Structure)](#tutorial9)  
      + [Tutorial 9.1 - Binary Trees (Tree Data Structure variation) and Binary Search Trees (Binary Tree Data Structure variation)](#tutorial9.1)  
    + [Tutorial 10 - Graphs (Data Structure)](#tutorial10)  

  + [On Algorithms (Searching and Sorting Algorithms)](#algorithms):
    + [Tutorial 11 - What are Algorithms)](#tutorial11)  
    + [Tutorial 12 - Binary Search (Searching Algorithm) and Linear Search (Searching Algorithm)](#tutorial12)  
    + [Tutorial 13 - Bubble Sort (Sorting Algorithm)](#tutorial13)  
    + [Tutorial 14 - Quick Sort (Sorting Algorithm)](#tutorial14)  
    + [Tutorial 15 - Insertion Sort (Sorting Algorithm)](#tutorial15)   
      + [Tutorial 15.1 - Shell Sort (Sorting Algorithm) (improved Insertion Sort Algorithm variation)](#tutorial15.1)  
    + [Tutorial 16 - Merge Sort (Sorting ALgorithm)](#tutorial16)  
    + [Tutorial 17 - Selection Sort (Sorting Algorithm)](#tutorial17)  
    
+ [Thoughts after the learning journey](#thoughts)

<br>

<br>

## Code Description <a name = "codedescription"></a>  

<br>

## On Data Structures <a name = "datastructures"></a>
### Tutorial 1 - What are Data Structures <a name = "tutorial1"></a>
What are Data Structures?  
Data Structures are a specificied way to organise, manage, and store data in a specific memory layout. Similar to that of a physical container, which you can put and keep stuff in it. 

Source(s): https://www.youtube.com/watch?v=_t2GVaQasRY&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=1&t=5s (codebasics)

<br>

### Tutorial 2 - Big O Notation <a name = "tutorial2"></a>
What is the Big O Notation?  
The Big O Notation measures the running time (time complexity) or space requirements (space complexity)
for your computer program/algorithm (not very accurate to say it measures running time for your Data
Structure) grow as input grows for the worst case scenario.

Source(s): https://www.youtube.com/watch?v=IR_S8BC8KI0&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=2 (codebasics)

<br>

### Tutorial 3 - Concept of Recursion <a name = "tutorial3"></a>
What is the concept of Recursion?  
Recursion is a method of solving a computational problem where the solution depends on solutions to smaller instances of the same problem. Recursive function works and are functions that calls itself within the function.

Source(s): https://www.youtube.com/watch?v=9bsK03SlmNM&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=20 (codebasics)

<br>

### 4. Tutorial 4 - Arrays (Data Structure) <a name = "tutorial4"></a>
What is an Array?  
An Array is a linear data structure that is a collection of similar data elements stored at contiguous memory locations.

Source(s): https://www.youtube.com/watch?v=gDqQf4Ekr2A&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=3 (codebasics)

<br>

### Tutorial 5 - Linked Lists (Data Structure) <a name = "tutorial5"></a>
What is a Linked List?  
A Linked List is a linear data structure consisting of nodes where each node contains a data field and a reference(link)/pointer to the next node in the list. Each node consists of 2 components, data of an element in the Data Structure, and a pointer. 

What is a Node?  
Each node is stored at a random memory space (not continuous to other elements of the Linked List Data Structure, unlike Arrays) and is linked to other nodes via a pointer. (which stores the address of the memory storing the next element)

In this tutorial, we explored 2 types of Linked List Data Structures,  
  1. (Singly) Linked Lists
  2. Doubly Linked Lists

Source(s): https://www.youtube.com/watch?v=qp8u-frRAnU&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=4 (codebasics)

<br>

### Tutorial 6 - Hash Tables (Data Structure) <a name = "tutorial6"></a>
What is a Hash Table?  
A Hash Table is a linear data structure that maps keys to values. 

A Hash Table uses a hash function to compute an index, also called a hash code, into an array of buckets or slots in memory, from which the desired value can be found. During lookup, the key (object name/string) is hashed (is put through the hash function) and the resulting hash (result after the key is put through the hash function) indicates where the corresponding value is stored.

Note: You might sometimes come across the term 'Hash Map' which is essentially the same thing as a Hash Table (with some very minor differences)

Source(s): https://www.youtube.com/watch?v=ea8BRGxGmlA&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=5 (codebasics)

<br>

### Tutorial 6.1 - Hash Tables Collision Handling <a name = "tutorial6.1"></a>
What is a Collision in Hash Tables? And what is the Problem of Collisions when making Hash Tables?  
A Collision occurs when more than one value (of key-pair values) is hashed by a particular hash function hash to the same slot/produces the same hash (or index in the memory array) in the Hash Table being generated by that hash function.

What is Hash Table Collision Handling?  
Collision Handling is when we modify our existing Hash Table Data Structure such that it is able to handle these Collisions and still be able to store every key-value pair being given to it at a unique spot in the Hash Table's memory array such that they are still unique and won't override or affect other key-value pairs in the Hash Table.

In this tutorial, we explored 2 ways of Hash Table Collision Handling, 
  1. Seperate Chaining
  2. Linear Probing

Source(s): https://www.youtube.com/watch?v=54iv1si4YCM&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=6 (codebasics)

<br>

### 8. Tutorial 7 - Stacks (Data Structure) <a name = "tutorial7"></a>
What is a Stack?  
A Stack is a linear data structure that only opens at one end, stores items and perform operations using the Last In, First Out (LIFO) method. Whenever a new element is added to a stack, it is added to the top of the stack, and the top element is always removed first from a stack.

Source(s): https://www.youtube.com/watch?v=zwb3GmNAtFk&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=7 (codebasics)

<br>

### Tutorial 8 - Queues (Data Structure) <a name = "tutorial8"></a>
What is a Queue?  
A Queue is a linear data structure that opens at both ends, stores items and perform operations using the First In First Out (FIFO) method. Whenever a new element is added, it is added from one end of the queue, and all deletions froma Queue are made from the other end, always first removing the first element added into the queue. 

Source(s): https://www.youtube.com/watch?v=rUUrmGKYwHw&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=8 (codebasics)

<br>

***(Side lesson, for the Queue Data Structure excercise 1)***  
What is Multithreading?  
Lets define what a thread is first: A thread is a seperate flow of code execution. 

Each program has one thread by default, but we may need to create new threads to execute tasks concurrently within a single program.

Multithreading is a model of program execution that allows for multiple threads to be created and executed within a process, executing independently but concurrently sharing process resources. 

Source(s): https://www.youtube.com/watch?v=PJ4t2U15ACo&list=PLeo1K3hjS3uub3PRhdoCTY8BxMKSW7RjN&index=1 (codebasics)

<br>

### Tutorial 9 - Trees and General Trees (Data Structure) <a name = "tutorial9"></a>
What is a Tree?  
A Tree is a collection of non-linear data structures with a hierarchy-based structure with a set of connected nodes. (like those used in Linked Lists Data Structure)

What is a General Tree?  
You can sort of think of General Tree as the foundational Tree Data Structure blueprint for all other Tree Data Structure variations, such that other Tree Data Structure variations are modifications of the General Tree.

A General Tree is a Tree Data Structure where each node may have zero or more children nodes for every node (number of children nodes may vary depending on the Tree Data Structure variation).

Source(s): https://www.youtube.com/watch?v=4r_XR9fUPhQ&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=9 (codebasics)

<br>

### Tutorial 9.1 - Binary Trees (Tree Data Structure variation) and Binary Search Trees (Binary Tree Data Structure variation) <a name = "tutorial9.1"></a>
What is a Binary Tree?  
A Binary Tree is a variation of the (General) Tree Data Structure, a non-linear Data Structure with maximum of two children nodes for each node. The difference/modification between a General Tree and a Binary Tree is that each node in a General Tree can have zero to infinity number of children, while each node in a Binary Tree can only have a (zero to) maximum of 2 nodes left and right. 

Similar to a General Tree, a Binary Tree does not have its Nodes sorted. Usually, by itself, the Binary Tree is not very applicable/useful as its Nodes are unsorted, hence, it is usually implemented as one of its further variations, more commonly in the form of a Binary Search Tree (BST) (aka ordered/sorted Binary Tree).

What is a Binary Search Tree (BST)?  
A Binary Search Tree (BST) is a further variation of the Binary Tree Data Structure, sometimes known as an ordered/sorted Binary Tree. The 2 differences/modifications between a Binary Tree and Binary Search Tree is that a normal Binary Tree is unordered, and allows duplicates, while a Binary Search Tree is ordered (by some manner) that allows easy searching of a particular node, and dosen't allow duplicates (its not like BST don't allow, but we tell our BST to not allow it as duplicate data nodes sort of messes up the BST's ordering/sorting and subsequently the search function. We will be able to understand this once we learn how the BST's ordering/sorting works)

By the way, Binary Search Tree are called as such as due to their ordered/sorted characteristic, it increases the efficiency (Big O Notation) of searching (search operation) in a Binary Tree.

Source(s): 
https://www.youtube.com/watch?v=lFq5mYUWEBk&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=10 (Part 1) (codebasics)  
https://www.youtube.com/watch?v=JnrbMQyGLiU&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=11 (Part 2) (codebasics)

<br>

### Tutorial 10 - Graphs (Data Structure) <a name = "tutorial10"></a>
What is a Graph?  
A Graph is a non-linear data structure consisting of nodes and edges. The nodes are sometimes also referred to as vertices and the edges are lines or arcs that connect any two nodes in the Graph. 

A node refers to the individual entity storing data, while an edge refers to the line connecting 2 nodes.

There are 2 types of Graph Data Structures:  
  1. Undirected Graph
  2. Directed Graph

Also, the edges of Graph Data Structures may or may not be weighted.

In this tutorial, out of the 2 common ways to implement Graph Data Structures, as an Adjacency Matrix or Adjacency List, we only covered implementing Adjacency List Graph Data Structures.

In this tutorial, we explored 4 types of Graphs,  
  1. Adjacency List Directed Graph
  2. Adjacency List Undirected Graph
  3. Adjacency List Directed Weighted Graph
  4. Adjacency List Undirected Weighted Graph

Source(s): 
https://www.youtube.com/@AmulsAcademy/videos (Amulya's Academy)(referenced from various videos on Graph Data Structures from this Youtube channel)
https://www.youtube.com/watch?v=j0IYCyBdzfA&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=12 (codebasics)
https://www.simplilearn.com/tutorials/data-structure-tutorial/graphs-in-data-structure (simplilearn)

<br>

<br>

## On Algorithms (Searching Algorithms and Sorting Algorithms) <a name = "algorithms"></a>

### Tutorial 11 - What are Algorithms <a name = "tutorial11"></a>
What are Algorithms?  
Algorithms are a list set of instructions of how to solve a computational problem. These Algorithms are executed on Data Structures and together, Data Structures and Algorithms, creates a computer program.

Examples are infinite (possibilities are endless, much wider in variety than Data Structures), but common Algorithms that are first taught to new programmers will always be Searching and Sorting Algorithms.

Source(s): NIL

<br>

### Tutorial 12 - Binary Search (Searching Algorithm) and Linear Search (Searching Algorithm) <a name = "tutorial12"></a>
What is Binary Search?  
Binary Search is a searching algorithm used in a sorted array that searches for a value by repeatedly dividing the search interval in half and the correct interval to find is decided based on the searched value and the middle value of the interval.

Note that unlike some other Search Algorithms, Binary Search Algorithm works on the concept of the list to be searched, to be sorted beforehand. (So if the list is unsorted then Binary Search Algorithm dosen't work)

In this tutorial, we implemented the Binary Search Algorithm both iteratively and recursively.

What is Linear Search?  
Linear search is a searching algorithm where the list or data set is traversed from one end to the other end to find the desired value.

In this tutorial, we implemented the Linear Search Algorithm iteratively.

Source(s): https://www.youtube.com/watch?v=GnZ9ppr_zaI&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=13 (codebasics)

***(Side lesson, for comparing the time complexity of Binary Search Algorithm and Linear Search Algorithm in '[this](https://github.com/WindJammer6/12.-Data-Structures-and-Algorithms-Learning-and-Practice-Python/blob/main/zTutorial%2012%20-%20Binary%20Search%20(Searching%20Algorithm)%20and%20Linear%20Search%20(Searching%20Algorithm)/4.%20comparing_performance_of_Linear_Search_and_Binary_Search.py)' file)***   
What is a Decorator?  
Decorators are sort of the 'tags' that allow us to wrap other functions within a function (aka a 'wrapper function') in order to extend the behaviour of the wrapped function, without permanently modifying it. The Decorator 'tag' will be the name of the 'wrapper function', where the 'wrapper function' will be used to wrap other functions (pass other functions through it)

Source(s): https://www.youtube.com/watch?v=IVWZxr0kOyI&t=200s (codebasics)

<br>

### Tutorial 13 - Bubble Sort (Sorting Algorithm) <a name = "tutorial13"></a>
What is Bubble Sort?  
Bubble Sort is a sorting algorithm that sorts a list by examining each set of adjacent elements in the list, from left to right, switching their positions if they are out of order. The Bubble Sort Algorithm then repeats this process until it can run through the entire string and find no two elements that need to be swapped.

In this tutorial, we implemented the Bubble Sort Algorithm iteratively.

Source(s): https://www.youtube.com/watch?v=ppmIOUIz4uI&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=14 (codebasics)

<br>

<br>

### Tutorial 14 - Quick Sort (Sorting Algorithm) <a name = "tutorial14"></a>
What is Quick Sort?  
Quick Sort is a sorting algorithm that sorts a list by using the Divide and Conquer technique that picks an element as a pivot and partitions the given array around the picked pivot by placing the pivot in its correct position in the array. (In these Algorithm tutorials, the only 2 Algorithms (both Sorting Algorithms) that uses the Divide and Conquer paradigm is Quick Sort Algorithm and Merge Sort Algorithm)

In this tutorial, we implemented the Quick Sort Algorithm recursively.

In this tutorial, we explored 2 schemes of Partitioning,
  1. Hoare Partition scheme
  2. Lomuto Partition scheme

Source(s): https://www.youtube.com/watch?v=5iSZ7mh_RAk&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=15 (codebasics)

<br>

### Tutorial 15 - Insertion Sort (Sorting Algorithm) <a name = "tutorial15"></a>
What is Insertion Sort?  
Insertion Sort is a sorting algorithm that sorts a list by iteratively building a sorted subarray within the given unsorted array. The algorithm splits the unsorted array into 2 subarrays, the sorted subarray and unsorted subarray. It starts with the first element as the sorted subarray (since a single element is always considered sorted), and then it repeatedly takes the next element from the unsorted part of the array and inserts it into its correct position in the sorted subarray until the whole array becomes sorted (all the elements in the unsorted subarray is brought to the sorted subarray, and there is no more unsorted subarray, and the initial List now only contains the sorted subarray and is now sorted)

In this tutorial, we implemented the Insertion Sort Algorithm iteratively.

Source(s): https://www.youtube.com/watch?v=K0zTIF3rm9s&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=16 (codebasics)

<br>

### Tutorial 15.1 - Shell Sort (Sorting Algorithm) (improved Insertion Sort Algorithm variation) <a name = "tutorial15.1"></a>
What is Shell Sort?  
Shell Sort is mainly an optimised variation of Insertion Sort. 

Shell Sort is a sorting algorithm that sorts a list by dividing the array into smaller subarrays and sort each of these subarrays using Insertion Sort Algorithm. The key difference is that the elements within each subarray are not adjacent, but are separated by a certain gap (Shell Sort Algorithm leverages on the idea of gaps). This gap is initially larger, and after each gap's iteration of sorting via Insertion Sort of these smaller subarrays, the gap is gradually reduced during the sorting process until it reaches 1, at which when the gap is 1, this gap's (1) iteration of sorting transitions into a standard Insertion Sort Algorithm.

In this tutorial, we implemented the Shell Sort Algorithm iteratively.

Source(s): 
~~https://www.youtube.com/watch?v=VxNr9Vudp4Y&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=18 (codebasics)~~ (I didn't like codebasics' video on how he explained the Shell Sort Algorithm, so I sourced from other websites for a better explanation of the Shell Sort Algorithm)  
https://www.youtube.com/watch?v=IViqgakt-Eg (Geekific)  
https://www.youtube.com/watch?v=SHcPqUe2GZM&t=1s (GeeksforGeeks)

<br>

### Tutorial 16 - Merge Sort (Sorting ALgorithm) <a name = "tutorial16"></a>
What is Merge Sort?  
Merge Sort is a sorting algorithm that sorts a list by using the Divide and Conquer technique that divides an array into smaller subarrays, sorting each subarray recursively (via the same Merge Sort Algorithm), and then merging the sorted subarrays back together to form the final sorted array. (In these Algorithm tutorials, the only 2 Algorithms (both Sorting Algorithms) that uses the Divide and Conquer paradigm is Quick Sort Algorithm and Merge Sort Algorithm)

The way Merge Sort Algorithm does this is by continuously splitting the array in half until it cannot be further divided i.e., the array has only one element left (an array with one element is always sorted). Then the sorted subarrays are merged into one sorted array.

In this tutorial, we implemented the Merge Sort Algorithm recursively.

Source(s): https://www.youtube.com/watch?v=nCNfu_zNhyI&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=17 (codebasics)

<br>

### Tutorial 17 - Selection Sort (Sorting ALgorithm) <a name = "tutorial17"></a>
What is Selection Sort?  
Selection Sort is a sorting algorithm that sorts a list by repeatedly selecting the smallest (or largest) element from the unsorted subarray of the initial unsorted List and moving it to the sorted subarray of the initial unsorted List. 

In this tutorial, we implemented the Selection Sort Algorithm iteratively.

Source(s): https://www.youtube.com/watch?v=hhkLdjIimlw&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=19 (codebasics)

<br>

<br>

## Thoughts after the learning journey <a name = "thoughts"></a>

<br>

Have a gif:

![Semantic description of image](https://media4.giphy.com/media/8vQSQ3cNXuDGo/200w.webp?cid=ecf05e47lb7yvtozvuuqp8dv9l1v22lipc5w2ppg752l8kpg&ep=v1_gifs_search&rid=200w.webp&ct=g)
