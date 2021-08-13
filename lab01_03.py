print(" *** Summation of each digit ***")
n=int(input("Enter a positive number : "))
sum=0
while(n>0):
    dig=n%10
    sum=sum+dig
    n=n//10
print("Summation of each digit = ",sum)