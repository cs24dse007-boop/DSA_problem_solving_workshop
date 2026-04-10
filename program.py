# #factorial solution
# def factorial(num):
#     if num<=1:
#         return 1
#     return num * factorial(num-1)
# print(factorial(4))

#--------------------------------------------------------------------------------------------------
# def power(base,exponent):
#     if exponent==0:
#         return 1
#     return base *power(base,exponent-1)
# print(power(2,0))#1
# print(power(2,2))

#--------------------------------------------------------------------------------------------------
# def capitalizeFirst(arr):
#     result=[]
#     if len(arr)==0:
#         return result
#     result.append(arr[0][0].upper()+arr[0][1:])
#     return result + capitalizeFirst(arr[1:])
# print(capitalizeFirst(['car','taco','banana']))
#--------------------------------------------------------------------------------------------------
# def productofArray(arr):
#     if len(arr)==0:
#         return 1
#     return arr[0]*productofArray(arr[1:])
# print(productofArray([1,2,3]))
# print(productofArray([1,2,3,10]))
#--------------------------------------------------------------------------------------------------
# def fib(num):
#     if num<2:
#         return num
#     return fib(num-1)+fib(num-2)

# print(fib(4))