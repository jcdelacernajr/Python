# Question 11
print("Question 11")
t1 = (6,1,2)
print(t1[0]/t1[2]*(t1[1]+t1[2]))

# Question 12
print("Question 12")
def get_result(t, z, res=0):
    for x in t:
        if x == z:
            res += 1
    return res

t = (50, 10, 60, 70, 50)
result = get_result(t, t[0])
print(result)

# Question 13
print("Question 13")
items = {"apple", "orange", 'apple', 'orange', 'durian'}
print(len(items))

# Question 14
print("Question 14")
content = {'name':"Guido",
           'job': ['BDFL',
                   'Python Founder',
                   {"Developer":('Dropbox',
                                 'Microsoft'
                                 )
                    }
                   ]
           }
print(content['job'][-1]['Developer'][1])

# Question 15
print("Question 15")
def test(a, z):
    return a * z

A = "question"
print(test(A[1], len(A)-1))









