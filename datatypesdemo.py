str1 = "demo"
str2 = "operations"
print(str1+str2)
print(str1 + " " +str2)
x1 = '3'
x2 = '7'
print (x1 + x2)
x1 = int(x1)
x2 = int(x2)
print("addition")
print (f"{x1 + x2}")
res_sub = x2-x1
print("subtraction")
print("result of {} - {} is {}".format(x2,x1,res_sub))
res_mul = x1*x2
print("multiply")
print("{} * {} = {}".format(x1,x2,res_mul))
x1 = float(x1)
x2 = float(x2)
print("division")
print(f"{x1}/{x2} is {x1/x2}")
print("integer division")
x1 = int(x1)
x2 = int(x2)
res_div = x1/x2
print(f"{x1}/{x2} is {res_div}")
print("reminder")
print(f"{x1} % {x2} = {x1%x2}")
print(f"{x2} % {x1} = {x2%x1}")
print("operation //")
res_1 = x1//x2
print("{}//{} is {}".format(x1,x2,res_1))
print(f"the result of {x2} // {x1} = {x2//x1}")
print("operation **")
print(f"{x1} ** {x2} = {x1**x2}")
print(f"{x2} ** {x1} = {x2**x1}")
num = x1
num **= x1
print("result of",x1,"** is",num)



