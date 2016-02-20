# Data-Structures-And-Algorithms
Data Structures and Algorithms implemented in Python

<ul>
<li>Linear Data Structures</li>
  <ul>
    <li>ArrayList</li>
    <li>Linked Lists</li>
    <li>Queue</li>
    <li>Stack</li>
  </ul>
<li>Trees and Tries</li>
  <ul>
    <li>Binary Search Tree</li>
    <li>Binary Heap</li>
    <li>Trie</li>
  </ul>
<li>Graphs</li>
</ul>


Linear Data Structures
- ArrayList
    
  - Benefits:
    - Random access is done in constant time
      - No implementation necessary.
    
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
    - Random access is not allowed. You must sequentially iterate over the elements of the list to until you reach the desired element.
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
      1.  
      2.  
      3.  
    
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
