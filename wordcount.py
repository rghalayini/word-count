def word_count(filename):
    with open (filename, 'r') as f:
        first_list=[]
        for line in f:
            first_list.append(line.split())
        word_list=[] 
        def reemovNestings(random_list):
            for i in random_list: 
                if type(i) == list: 
                    reemovNestings(i) 
                else: 
                    word_list.append(i)
        reemovNestings(first_list)
       
        print('The number of words in the file is: ', len(word_list))

        #return word_list
        frequency=dict()
        for word in word_list:
            if word in frequency:
                frequency[word]+=1
            else:
                frequency[word]=1

        frequency_tuples = []
        for key in frequency:
            t = (key, frequency[key])
            frequency_tuples.append(t)
        
        #from operator import itemgetter, attrgetter
        #sorted_tuples=sorted(frequency_tuples, key=itemgetter(1))  

        sorted_tuples=sorted(frequency_tuples, key=lambda frequency_tuples: frequency_tuples[1])
        reversed_sorted=sorted_tuples[::-1]
        print ("The top words in the file are:")

        for s, val in reversed_sorted[:19]:
                print ("s: "+s+": "+str(val))

word_count('poem.txt')