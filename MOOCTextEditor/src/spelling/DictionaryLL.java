package spelling;

import java.util.LinkedList;

/**
 * A class that implements the Dictionary interface using a LinkedList
 *
 */
public class DictionaryLL implements Dictionary 
{

	private LinkedList<String> dict;
	
    // TODO: Add a constructor
	// Constructor should simply create an empty linked list of strings
	public DictionaryLL(){
		this.dict = new LinkedList<String>();
	}


    /** Add this word to the dictionary.  Convert it to lowercase first
     * for the assignment requirements.
     * @param word The word to add
     * @return true if the word was added to the dictionary 
     * (it wasn't already there). */
    public boolean addWord(String word) {
    	// TODO: Implement this method
    	// change the word variable to be in all lowercase
    	// if the word is not in the linked list dictionary then add the word to the list and return true
    	// else return false if the word is already in the list 
    	word = word.toLowerCase();
    	if(!this.dict.contains(word)){
    		this.dict.add(word);
    		return true;
    	}
        return false;
    }


    /** Return the number of words in the dictionary */
    public int size()
    {
        // TODO: Implement this method
        return this.dict.size();
    }

    /** Is this a word according to this dictionary? */
    // isWord method should put a string in lowercase and then check to see if it's in the linked list dictionary
    // if it is in the linked list return true
    // else return false
    public boolean isWord(String s) {
        //TODO: Implement this method
    	s = s.toLowerCase();
    	if(this.dict.contains(s)){
    		return true;
    	}
        return false;
    }

    
}
