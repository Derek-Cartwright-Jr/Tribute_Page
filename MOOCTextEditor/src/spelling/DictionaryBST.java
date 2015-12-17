package spelling;

import java.util.TreeSet;

/**
 * @author UC San Diego Intermediate MOOC team
 *
 */
public class DictionaryBST implements Dictionary 
{
   private TreeSet<String> dict;
	
    // TODO: Implement the dictionary interface using a TreeSet.  
 	// You'll need a constructor here
	public DictionaryBST(){
		this.dict = new TreeSet<String>();
	}
    
    /** Add this word to the dictionary.  Convert it to lowercase first
     * for the assignment requirements.
     * @param word The word to add
     * @return true if the word was added to the dictionary 
     * (it wasn't already there). */
    public boolean addWord(String word) {
    	// TODO: Implement this method
    	// Again, take in a word for this method and check if it's in the dictionary tree already
    	// If it's not, then add the word into the dictionary tree
    	// Else, it's already in the tree and don't add it
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
    public boolean isWord(String s) {
    	//TODO: Implement this method
    	s = s.toLowerCase();
    	if(this.dict.contains(s)){
    		return true;
    	}
        return false;
    }

}
