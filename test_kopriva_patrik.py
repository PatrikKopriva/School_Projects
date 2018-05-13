#1. ukol
def table(n):
    for i in range (n):
        for j in range (n):
            if i>j:
                print(i-j, end=" ")
            else:
                print(j-i, end=" ")
        print()

#2. ukol
def print_above_avg(number_list):
    for i in number_list:
        if i>average_value(number_list):
            print(i, end=" ")
            
def average_value(number_list):
    summary=0
    for i in number_list:
        summary+=i
    x=summary/len(number_list)
    return(x)

#3. ukol
def gcd(a,b):
    n=0
    if a<b:
        i=a
    else:
        i=b
    while n!=i:
        n+=1
        if (a%n)+(b%n)==0:
            divider=n
    return(divider)

#4. ukol
def ceasar_sequence(string_list):
    x=0
    for i in string_list:
        result=""
        for j in range (len(i)):
            if x+ord(i[j])>122:
                y=chr(x+ord(i[j])-26)
            else:
                y=chr(x+ord(i[j]))
            result+=y
        string_list[x]=result
        x+=1
    return(string_list)
