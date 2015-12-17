package textgen;

import java.util.AbstractList;


/** A class that implements a doubly linked list
 * 
 * @author UC San Diego Intermediate Programming MOOC team
 *
 * @param <E> The type of the elements stored in the list
 */
public class MyLinkedList<E> extends AbstractList<E> {
	LLNode<E> head;
	LLNode<E> tail;
	int size;

	/** Create a new empty LinkedList */
	public MyLinkedList() {
		// TODO: Implement this method
		this.head = new LLNode<E>(null);
		this.tail = new LLNode<E>(null);
		head.next = tail;
		tail.prev = head;
		this.size = 0;
	}

	/**
	 * Appends an element to the end of the list
	 * @param element The element to add
	 */
	
	public boolean add(E element ) 
	{
		// TODO: Implement this method
		// Linked List already contains elements
		if(element == null){
			throw new NullPointerException("Can't add that!");
		}
		LLNode<E> node = new LLNode<E>(element);
		node.next = tail;
		node.prev = tail.prev;
		tail.prev.next = node;
		tail.prev = node;
		this.size++;
		return true;
	}

	/** Get the element at position index 
	 * @throws IndexOutOfBoundsException if the index is out of bounds. */
	public E get(int index) 
	{
		// TODO: Implement this method.
		LLNode<E> node = this.Traversal(index);
		return node.data;
	}

	/**
	 * Add an element to the list at the specified index
	 * @param The index where the element should be added
	 * @param element The element to add
	 */
	public void add(int index, E element ) 
	{
		// TODO: Implement this method
		if(element == null){
			throw new NullPointerException("Can't add that!");
		}
		LLNode<E> current = new LLNode<E>(element);
		if(this.size == 0){
			current.next = tail;
			current.prev = head;
			head.next = current;
			tail.prev = current;
			this.size++;
		}
		else{
			LLNode<E> node = this.Traversal(index);
			this.add_node(element, node.prev, node);
			this.size++;
		}
	}
	
	// Helper method that will add a node anywhere in the linked list
	private void add_node(E element, LLNode<E> p, LLNode<E> n){
		LLNode<E> node = new LLNode<E>(element);
		node.prev = p;
		node.next = n;
		p.next = node;
		n.prev = node;
	}

	/** Return the size of the list */
	public int size() 
	{
		// TODO: Implement this method
		return this.size;
	}

	/** Remove a node at the specified index and return its data element.
	 * @param index The index of the element to remove
	 * @return The data element removed
	 * @throws IndexOutOfBoundsException If index is outside the bounds of the list
	 * 
	 */
	public E remove(int index) 
	{
		// TODO: Implement this method
		LLNode<E> node = this.Traversal(index);
		this.delete_node(node, node.prev, node.next);
		this.size--;
		return node.data;
	}
	
	private void delete_node(LLNode<E> node, LLNode<E> p, LLNode<E> n){
		p.next = n;
		n.prev = p;
		node.next = null;
		node.prev = null;
	}

	/**
	 * Set an index position in the list to a new element
	 * @param index The index of the element to change
	 * @param element The new element
	 * @return The element that was replaced
	 * @throws IndexOutOfBoundsException if the index is out of bounds.
	 */
	public E set(int index, E element) 
	{
		// TODO: Implement this method
		if(element == null){
			throw new NullPointerException("Can't add that!");
		}
		
		LLNode<E> node = this.Traversal(index);
		E val = node.data;
		node.data = element;
		return val;
	}   
	
	// Linked List traversal method to grab and return a node in the list
	private LLNode<E> Traversal(int i){
		if(i >= this.size || i < 0){
			throw new IndexOutOfBoundsException("That index is out of bounds.");
		}
		else{
			int count = 0;
			LLNode<E> current = head.next;
			while(count < i){
				current = current.next;
				count++;
			}
			return current;
		}
	}
}

class LLNode<E>{

	LLNode<E> prev;
	LLNode<E> next;
	E data;

	// TODO: Add any other methods you think are useful here
	// E.g. you might want to add another constructor
	public LLNode(E e) 
	{
		this.data = e;
		this.prev = null;
		this.next = null;
	}
}
