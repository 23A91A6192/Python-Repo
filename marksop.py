def reverse(python):
    try:
        with open(python,'r')as file:
            for line in file:
                print(line.rstrip()[::-1])
    except Exception as e:
        print("not found")
reverse("marks.csv")