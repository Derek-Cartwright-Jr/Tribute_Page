package document;

/** 
 * A class that represents a text document
 * @author UC San Diego Intermediate Programming MOOC team
 */
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;


public abstract class Document {

	private String text;
	
	/** Create a new document from the given text.
	 * Because this class is abstract, this is used only from subclasses.
	 * @param text The text of the document.
	 */
	protected Document(String text)
	{
		this.text = text;
	}
	
	/** Returns the tokens that match the regex pattern from the document 
	 * text string.
	 * @param pattern A regular expression string specifying the 
	 *   token pattern desired
	 * @return A List of tokens from the document text that match the regex 
	 *   pattern
	 */
	protected List<String> getTokens(String pattern)
	{
		ArrayList<String> tokens = new ArrayList<String>();
		Pattern tokSplitter = Pattern.compile(pattern);
		Matcher m = tokSplitter.matcher(text);
		
		while (m.find()) {
			tokens.add(m.group());
		}
		
		return tokens;
	}
	
	// This is a helper function that returns the number of syllables
	// in a word.  You should write this and use it in your 
	// BasicDocument class.
	// You will probably NOT need to add a countWords or a countSentences method
	// here.  The reason we put countSyllables here because we'll use it again
	// next week when we implement the EfficientDocument class.
	protected int countSyllables(String word)
	{
		// TODO: Implement this method so that you can call it from the 
		// getNumSyllables method in BasicDocument (module 1) and 
	    // EfficientDocument (module 2).
		
		int count = 0;
		String l_word = word.toLowerCase();
		char[] cArray = l_word.toCharArray();		
		
		// For loop traces through the character array and checks to see if there are any situations where there is a consonant followed by a vowel
		// This situation is very  common and is the common makeup of a syllable
		// If the for loop ever gets to the situation where it meets a lone 'e' at the end of the word, it simply ignores that being a syllable because that's not in our definition
		// The method isn't perfect and there are some situations that don't get the syllable count perfectly correct but it works fine for all the test cases given and many other situations
		// If the word is either one or two characters long, then it automatically only has one syllable.
		if(cArray.length <= 2){
			count++;
			return count;
		}
		
		// For loop that iterates over all characters in the word being analyzed
		for(int i=0; i<cArray.length; i++){

				// If the current character being analyzed is a vowel, then automatically increment the count and go through the other checks ot make sure it's an acceptable syllable
				if(isVowel(cArray[i]) == true){
					count++;

					// If the for loop isn't at the last character and the adjacent character is a vowel then decrement the count
					if(i != cArray.length-1 && isVowel(cArray[i+1])){
						count--;
					}

					// If the last character is an e but there were earlier syllables then decrement the count
					if(i == cArray.length-1 && cArray[i] == 'e' && count > 0){
						count--;
						
					}

					// If the last character is an e and there are no syllables prior to it increment the count to 1
					if(i == cArray.length-1 && cArray[i] == 'e' && count == 0){
						count++;
						return count;
					}

					// If the last character is an e and the previous character is a vowel then we should still increment it since it's not a lone e.
					if(i == cArray.length-1 && cArray[i] == 'e' && isVowel(cArray[i-1])){
						count++;
						return count;
					}
				}
		}
		return count;
	}
		
	
	// isVowel helper function that confirms whether or not a character is a vowel.
	private boolean isVowel(char c){
			
		// Set up a character array of all acceptable vowels and check if the given character parameter is = to any of them.
		// Simply return true if it is and false if it isn't
		char[] vowels = {'a', 'e', 'i', 'o', 'u', 'y'};
		for(int ind = 0; ind<vowels.length; ind++){
			if(c == vowels[ind])
				return true;
		}
		return false;
	}
	
	/** A method for testing
	 * 
	 * @param doc The Document object to test
	 * @param syllables The expected number of syllables
	 * @param words The expected number of words
	 * @param sentences The expected number of sentences
	 * @return true if the test case passed.  False otherwise.
	 */
	public static boolean testCase(Document doc, int syllables, int words, int sentences)
	{
		System.out.println("Testing text: ");
		System.out.print(doc.getText() + "\n....");
		boolean passed = true;
		int syllFound = doc.getNumSyllables();
		int wordsFound = doc.getNumWords();
		int sentFound = doc.getNumSentences();
		if (syllFound != syllables) {
			System.out.println("\nIncorrect number of syllables.  Found " + syllFound 
					+ ", expected " + syllables);
			passed = false;
		}
		if (wordsFound != words) {
			System.out.println("\nIncorrect number of words.  Found " + wordsFound 
					+ ", expected " + words);
			passed = false;
		}
		if (sentFound != sentences) {
			System.out.println("\nIncorrect number of sentences.  Found " + sentFound 
					+ ", expected " + sentences);
			passed = false;
		}
		
		if (passed) {
			System.out.println("passed.\n");
		}
		else {
			System.out.println("FAILED.\n");
		}
		return passed;
	}
	
	
	/** Return the number of words in this document */
	public abstract int getNumWords();
	
	/** Return the number of sentences in this document */
	public abstract int getNumSentences();
	
	/** Return the number of syllables in this document */
	public abstract int getNumSyllables();
	
	/** Return the entire text of this document */
	public String getText()
	{
		return this.text;
	}
	
	/** return the Flesch readability score of this document */
	public double getFleschScore()
	{
	    // TODO: Implement this method
		// Retrieve the values for the number of words, number of sentences, and number of syllables
		// You can do this using the getNumWords() getNumSentences() and getNumSyllables methods from earlier
		// Finally just implement the equation and return that result
		
		double num_words = this.getNumWords();
		double num_sent = this.getNumSentences();
		double num_syl = this.getNumSyllables();
		double flesh = 206.835 - ((1.015)*(num_words/num_sent)) - ((84.6)*(num_syl/num_words));
	    
		return (double)Math.round(flesh*10d)/10d;
		
	}
	
	
	
}
