import java.util.Scanner;
public class Number
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int c1=0,c2=0;
        int x=sc.nextInt();
        while(x!=0)
        {    
            int r=x%10;
            if(r%2==0) c1++;
            else c2++;
            x=x/10;
        }
        if(c1>0&&c2==0)
        {
            System.out.println("Even");
        }
        else if(c1==0&&c2>0)
        {
            System.out.println("Odd");
        }
        else
        {
            System.out.println("Mixed");
        }
    }
}