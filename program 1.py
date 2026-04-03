val1=int(input("Enter the value of val1"))#100
val2=int(input("Enter the value of val2"))#200
print("before swapping")
print("val1:",val1,"val2",val2)

val1=val1+val2 #val1=100+200
val2=val1-val2 #val2=300-200
val1=val1-val2 #val1=300-200
print("after swapping")
print("val1:",val1,"val2",val2)
