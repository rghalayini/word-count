def word_count(filename):
    from collections import Counter
    text = filename.lower()
    skips = [".", ",", ";", ":", "'", '"', "\n", "!", "?", "(", ")"]
    for ch in skips:
        text = text.replace(ch,"")
    word_counts=Counter(text.split(" "))
    x=0
    for value in word_counts.values():
        x=x+value
    print("The number of words in this file is:", x)

    for k, v in word_counts.items():
        if v==max(word_counts.values()):
            print("The most frequent word is", k, "and was repeated", v, "times") 
        else:
            None        
    return word_counts

