def sort_words_in_file(python,tout):
    try:
        with open(python,'r')as file:
            words=file.read().split()
            sorted_words=sorted(word.lower() for word in words)
            with open(tout,'w')as file:
                for word in sorted_words:
                    file.write(word+'\n')
                print("next")
    except Exception as e:
        print("not found")
sort_words_in_file("test.csv","tout.csv")


public class Permutation
{   
    public static void find_permutations(String str,String result)
    {
        if(str.isEmpty())
        {
            System.out.println(result);
        }
        else
        {
            int n=str.length();
            for(int i=0;i<n;i++)
            {
                char ch=str.charAt(i);
                String remaining=str.substring(0,i)+str.substring(i+1);
                find_permutations(remaining,result+ch);
            }
        }
    }
    public static void main(String args[])
    {
       String input="AB";
       find_permutations(input," ");
    }
}