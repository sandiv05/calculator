def add(a,b):
    c=a+b;
    return c ;

def sub(a,b):
    c=a-b;
    return c ;

def multiply(a,b):
    c=a*b;
    return c ;

def percentage (a,b):
    c=(a/b)*100;
    return c;

def divide(a,b):
    c=(a/b);
    return c;

def square(a):
    c=a*a;
    return c;

def cube (a):
    c=a*a*a;
    return c;

def average2  (a,b):
    c=(a+b)/2;
    return c;


def average3 (a,b,c):
    d=(a+b+c)/3;
    return d

print('i am going to add two numbers')
sum = add (2,3)
print('the result is = ',sum)

print('i am going to subract two numbers')
difference = sub (12,3)
print('the result is = ',difference)

print ('i am going to multiply two numbers')
product=multiply (15,10)
print("the result is = ",product)


print ('i am going to find percentage of my english exam mark')
englishPercentage=percentage(17,20)
print("the result is = ",englishPercentage)

print ('i am going to find percentage of my math exam mark')
mathPercentage=percentage(14,20)
print("the result is = ",mathPercentage)

print ('i am going to find percentage of my science exam mark')
sciencePercentage=percentage(19,20)
print("the result is = ",sciencePercentage)

print ('i am going to find percentage of my tamil exam mark')
tamilPercentage=percentage(19,20)
print("the result is = ",tamilPercentage)

print ('i am goig to divide two numbers')
qoution=divide(2,2)
print('the result is =',qoution)

print ('i am going to square one number')
product=square(5)
print('the result is=',product)

print ('i am going to cube one number')
product=cube(3)
print ('the result is = ',product)

print('i am going to averagetwo numbers')
averageResult=average2(4,2)
print('the result is=',averageResult)


print ('i am going to average three numbers')
averageResult=average3(4,5,3)
print('the result is=',averageResult)