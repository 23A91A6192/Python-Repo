def sort_words_in_file(python,out):
    try:
        with open(python,'r')as file:
            words=file.read().split()
            sorted_words=sorted(word.lower() for word in words)
            with open(out,'w')as file:
                for word in sorted_words:
                    file.write(word+'\n')
    except Exception as e:
        print("not found")
sort_words_in_file("marks.csv","out.csv")