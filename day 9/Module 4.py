# Question 12
output = ""
try:
    a = 10/2
except ZeroDivisionError:
    print("Zero Division error")
except Exception as e:
    print("New error encountered :"+e)
else:
    print("No error")
  
