// C versions of the program included in the main code

// 1.Addition
int main()

{
    int a,b;
    scanf("%d %d",&a,&b);
    int c;
    c=a+b;
    printf("%d",c)
}

// 2.Subtraction
int main()

{
    int a,b;
    printf("Enter the two numbers to be subtracted as num2 - num1");
    int c;
    c=a-b;
    printf("%d",c)
}

// 3.Multiplication
int main()

{
    int a,b;
    scanf("%d %d",&a,&b);
    int c;
    c=a*b;
    printf("%d",c)
}

// 4.Sum of user entered 8 numbers
int main()
{
    int n;
    scanf("%d",&n);
    sum=0;
    for(int i=0;i<=8;i++)
    {
        sum = sum + i;
    }
    printf("%d",sum);
} 
