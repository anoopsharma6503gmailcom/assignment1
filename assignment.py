#Q1 find average of three nubers

n1=int(input("enter first number"))
n2=int(input("enter second number"))
n3=int(input("enter third number"))
print((n1+n2+n3)/3)

#Q2 person income tax

gross_income=int(input("enter gross income"))
dependent=int(input("number of dependent"))
taxincome=gross_income-10000-(dependent*3000)
tax=0.2*taxincome #tax eate is 20%
print("The person has to pay",tax)

#Q3 store different data types in a string

n1=int(input("Number of students"))
lts=["Sid","Name","Gender","CourseName","CGPA"]
for i in range(n1):
    nlst=[]
    Sid=int(input("Enter sid:"))
    Name=input("Enter name:")
    Gender=input("Enter the gender:")
    cname=input("Enter the course name:")
    cg=float(input("Enter CGPA:"))
    nlst.append(Sid)
    nlst.append(Name)
    nlst.append(Gender)
    nlst.append(cg)
    print(lts)
    print(nlst)


#Q4 marks of 5 students

s1=float(input("Enter marks of first student:"))
s2=float(input("Enter marks of second student:"))
s3=float(input("Enter marks of third student:"))
s4=float(input("Enter marks of forth student:"))
s5=float(input("Enter marks of fifth student"))
slst=[s1,s2,s3,s4,s5]
slst.sort()
print(slst)

#Q5 a
color=["Red","Green","White","Black","Pink","Yellow"]
color.pop(3)
print(color)
#b
color[3]="Purple"
