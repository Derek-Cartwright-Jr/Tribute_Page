# Data-Structures-And-Algorithms
Data Structures and Algorithms implemented in Python

<ul>
<li>Linear Data Structures</li>
  <ul>
    <li>ArrayList</li>
    <li>Linked List</li>
    <li>Queue</li>
    <li>Stack</li>
  </ul>
<li>Trees and Tries</li>
  <ul>
    <li>Binary Search Tree</li>
    <li>Binary Heap</li>
    <li>Trie</li>
  </ul>
<li>Hash Table</li>
<li>Graphs</li>
</ul>


Linear Data Structures
- ArrayList
    
  - Benefits:
    - Random access is done in constant time
    - No implementation necessary in virtually all languages.
    
  - Disadvantages:
    - Insertion and Removal of elements requires O(n) time. I.e., you must shift all existing elements to either create room for the         new element or fill the empty space in the array.
    - The size of the arrays is fixed. Therefore, you must know the size of the array before hand. Also, in general, the upper limit         of the allocated memory is rarely reached.
    
  - Time Complexities:
    - Average Case:
    - Access: O(1); Insertion: O(n); Removal: O(n); Search: O(n)
      
    - Worst Case:
    - Access: O(1); Insertion: O(n); Removal: O(n); Search: O(n)
    
  - Space Complexity:
    - O(n)
      
- Linked Lists

  - Benefits: 
    - Insertion and Removal of an element is done in constant O(1) time. 
    - Linked lists have dynamic size where you do not need to worry about the upper limit of the list size before hand.
    - Elements of linked lists sit in memory non-contiguously. Therefore, you don't have to worry about the size of the list growing.
  
  - Disadvantages:
    - Random access is not allowed. You must sequentially iterate over the elements of the list to until you reach the desired              element.
    - There is extra memory space allocated for the "next node" pointer in each list node.
    - Arrays have better cache locality that can make a pretty big difference in performance.
  
  - Uses:
    - Representing other data structures such as stacks and queues.
  
  - Time Complexities:
    - Average Case:
    - Access: O(n); Insertion: O(n); Removal: O(n); Search: O(n)
    
    - Worst Case:
    - Access: O(n); Insertion: O(n); Removal: O(n); Search: O(n)
  
  - Space Complexity:
    - O(n)
- Queue
 
  - Uses: Used to keep track of order of operations such as a typing input buffer. The structure follows a First In First Out             principle.
  
  - Time Complexities:
    - Average/Worst Case:
    - Access: O(n); Enqueue: O(1) (depending on structure used to implement queue); Dequeue: O(1) (depending on structure used to           implement queue); Search: O(n)
  
  - Space Complexity:
    - O(n)
    
- Stack
  
  - Uses: Used to linearly reverse the order of sequential data. 
  
  - Time Complexities:
    - Average/Worst Case:
    - Access: O(n); Insert: O(1); Removal: O(1); Search: O(n)
  
  - Space Complexity:
    - O(n)
Trees
- Binary Search Trees
  
  - Benefits:
    - We can get all keys in sorted order via an Inorder BST Traversal. This isn't a natural operation in Hash Tables.
    - Binary Search is a natural operation of a balanced BST. It is done in O(log n) time! 
    - Binary Search Trees are much easier to implement than a hash table. 
    - Given a balanced BST such as an AVL tree, operations search, insert, removal, and access are guaranteed to be done in O(log n) 
      which is much faster than O(n) time.
  
  - Disadvantages:
    - Depending on the order of insertion, a BST will have the same operation performances of a linked list without the constant             insertion and removal performance time advantages, therefore defeating the purpose of having one in the first place. 
  
  - Traversals:
    - InOrder Traversal
      1.  Visit all your left subtree
      2.  Visit yourself
      3.  Visit all your right subtree
      
    - PreOrder Traversal
      1.  Visit yourself
      2.  Visit all your left subtree
      3.  Visit all your right subtree
    
    - PostOrder Traversal
      1.  Visit all your left subtree
      2.  Visit all your right subtree
      3.  Visit yourself
    
    - Level Order Traversal (Breadth First Traversal)
      1.  Keep a visited list of nodes you visited
      2.  Keep a explore list of nodes you need to explore still (children)
      3.  Then add the children of that node to the explore list
  
  - Uses:
    - Used in many search applications where data is constantly inserted/removed from the structure since all three operations can be       averagely looked up in O(log n) time.

  - Time Complexities:
    - Average Case:
    - Access: O(log n); Insertion: O(log n); Removal: O(log n); Search: O(log n)
    
    - Worst Case:
    - Access: O(n); Insertion: O(n); Removal: O(n); Search: O(n)
  
  - Space Complexity:
    - O(n)

- Binary Heap
  
  - Benefits:
    - Priority Queues can be efficiently implemented using binary heaps because it supports insert, removal, extractmax/extractmin          operations in O(log n) time.
    - Can be used in graph algorithms like Dijkstra's Shortest Path.
    - All levels of the heap will be guaranteed to be filled except for the last level (leaves).
    - Heap Sort can be done in O(n log n) time which is on average a better performance than a good amount of other sorting algos.
  
  - Uses:
    - Can implement a priority queue which is used in algos like Dijkstra's Shortest Path.
    - Order Statistics: Heap data structure can be used to efficiently find the kth smallest or largest element in an array.

  - Time Complexities:
    - Average/Worst Case:
    - Heapify: O(n); FindMax/FindMin (Depends if heap is min heap or max heap): O(1); ExtractMax/ExtractMin: O(log n); Insert: O(log        n); Removal O(log n); IncreaseKey/DecreaseKey: O(log n)

  - Space Complexity:
    - O(n)

- Hashing
  
  - Benefits:
    - Inserting, Removal, and Searching operations are done in O(1) on average. This advantage becomes more apparent when the number        of entries is large. However, in most cases it is difficult to reach these optimal performances.
  
  - Disadvantages:
    - Hash Tables are ineffective whe nthe number of entries is very small.
    - Hash Tables tend to have many collisions given a poor hash function.
  
  - Uses:
    - Caches: auxiliary data tables that are used to speed up the access to data that is primarily stored in the slower media. Hash 
      collisions can be handled by discarding older items and hanging on to the most recent item.
    - Sets: Hash table can be used to tell wheter or not such an entry exists or not. The set simply records whether or not a given         key belongs to a specified set of keys.
  
  - Time Complexities:
    - Average Case:
    - Access: O(1); Insert: O(1); Removal: O(1); Search: O(1)
    
    - Worst Case:
    - Access: O(n); Insert: O(n); Removal: O(n): Search: O(n)
  
  - Space Complexity:
    - O(n)

- Graphs
  
  - Benefits:
    - Can be used to represent large networks such as maps and social networks.
  
  - Disadvantages:
    -
  
  - Uses:
    - Social Networks (Each person is a graph node and each connection between that person and another person is a graph edge).
    - Google Maps (Each place is represented as graph node and the roads or pathways connecting them is a graph edge).
  
  - Time Complexities:
    - Worst Case:
      - Adjacency List: Storage: O(|V| + |E|); Add Vertex: O(1); Add Edge: O(1); Remove Vertex: O(|V| + |E|); Remove Edge: O(|E|);
      - Adjacency Matrix: Storage: O(|V|^2); Add Vertex: O(|V|^2); Add Edge: O(1); Remove Vertex: O(|V|^2); Remove Edge: O(1)
