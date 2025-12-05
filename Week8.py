'''def meghana(source,output):
    try:
        with open(source,"r") as file:
            words=file.read().split()
        sorted_words=sorted(word.lower() for word in words)
        with open(output,"w") as file:
            for word in sorted_words:
                file.write(word+'\n')
        print("Sorted words can be seen in output")
    except Exception as e:
        print("File not exist")

output="output.txt"source="Source.txt"
meghana(source,output)
def line_reverse(reverse):
    try:
        with open(reverse,'r') as file:
            for line in file:
                print(line.rstrip()[::-1])
    except Exception as e:
        print(e)

line_reverse("Source.txt")'''
def content_line(source):
    try:
        with open(source,'r')as file:
            content=file.read()
            num_char=len(content)
            num_words=len(content.split())
            num_line=content.count('\n')+1 if content else 0
            print(f"Number character:{num_char}")
            print(f"Number of words:{num_words}")
            print(f"number of line:{num_line}")
    except Exception as e:
        print(e)
content_line("Source.txt")
        