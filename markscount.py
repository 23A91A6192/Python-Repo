def count(python):
    try:
        with open(python,'r')as file:
            content=file.read()
            character=len(content)
            words=len(content.split())
            nw_lines=content.count('\n')+1 if content else 0
            print(character)
            print(words)
            print(nw_lines)
    except Exception as e:
        print("not found")
count("marks.csv")
