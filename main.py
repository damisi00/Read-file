# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}



def read_file_content(filename):
    # [assignment] Add your code here 
    file = open(filename, "r")          # To open file
    content = file.read()                 # To read text from file
    return content

print(read_file_content("story.txt"))   
read_file_content("story.txt")
    
    

def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    # To remove whitespaces, ",", "?", "\n", tab space and convert all the words to lowercase
    words = text.strip().replace(",", "").replace("?", "").replace("\n", "").replace("  ", " ").casefold().split(" ") 
    
    dicOfWords = {}
    for word in words:
        if word in dicOfWords: 
            dicOfWords[word] += 1 
        else:
            dicOfWords[word] = 1
    
    print(dicOfWords)
    return dicOfWords

count_words()
     
    # return {"as": 10, "would": 20}
