# Complete sentences automatically  
 
In order to make the user experience of the Google search engine better, the development team decided to enable the completion of sentences from articles, documentation and information files on various technological topics.  

Startup Function - The purpose of the function is to obtain a list of text sources on which
the search engine will run, each source contains a collection of sentences. 
The completion function - the function must accept a string - which is the text that the
user typed - the function must return the five best completions(good completion will be
defined below.

The complete operation
The purpose of the completion operation is to make it easier for the user to find the most appropriate sentence.  
We'll match a sentence verse with text that the user typed if:  
●	The text is a substring of the verse (including the beginning, middle,or end of the verse)..  
●	Text in which if we make one correction then the text will be a substring of the verse.   
Correction is defined as: 
 ● Character replacement. Example: The string "to be not to by" is considered a sub-string of the text "to be or not to be so is the question", with the substitution of the character "y" in the word "by" for "e". 
● Delete a character. Example: The string "to be or nt" is considered a sub-string of the text "to be or not to be that is the question", with the deletion of the character "o" in the word "not". 
● Add a character. Example: The string "to bee or not" is considered a sub-string of the text "to be or not to be is the question", with the addition of the character "e" in the word "be". 

Specify the match
In the case of multiple matches to the typed text, we will set a score(per match:
●	The base score is double the number of characters typed for which a match was found.  
●	Replacement a character reduces the score according to the following: first character 5 points, second character 4, third character 3, fourth character 2, fifth character and so on- 1.
●	Delete or adding a character  receives a reduction of 2 points except for the first 4 characters( first character 10 points, second character 8, third character 6, fourth character 4).
