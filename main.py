# import functools
# import math
# import string

# numbers = [1, 2, 3]
# print(list(filter(lambda x: (x + 1) * 3 / 3 % 3 == 0, numbers)))

# l = [-2, 4]
# m = list(map(lambda x: x*2, l))
# print(m)

# def oddlist(lst):

# if lst==[]:

#  return []

#  elif (lst[0]%2==0):

# return [lst[0]]+oddlist(lst[1:])
# else:

#  return oddlist(lst[1:]) 

# x = [12, 34]
# print(len(''.join(list(map(int, x)))))

# lst = [2,6,10,4,12]
# lst = lst.sort(1, 18, 4, 5)
# print(lst)

# m=functools.reduce(lambda x,y: x+y-3 in range(4, 10))
# print(list(m))

# a = [x for x in [10,25,30,45] if x % 5 == 0 ]
# a = str(a)
# print(type(a))

# lst = [1,2,3,5,7,9]

# def oddlist(lst):

#      if lst==[]:

#          return []

#      elif (lst[0]%2==0):

#          return oddlist(lst[1:]) 

#      else:

#          return [lst[0]]+oddlist(lst[1:])


# elements = [0, 1, 2]

# def incr(x):
# 	return x+1 
# print(list(map(elements, incr)))

# print (type(type(())))

# print(list(map(lambda x: 2*x, filter(lambda x: x>10, [3, 17, 11, 9, 7, 2, 19, 17]))))

# import functools
# m=functools.reduce(lambda x: x-3 in range(4, 10))
# print(list(m))

# numbers = [1, 2, 3]

# print(list(map(lambda x: x % 2 == 0, numbers)))

# func = lambda x: return x
# print(func(2))

# def to_upper(k):
#     return k.upper()
# x = ['ab', 'cd']
# print(list(map(to_upper, x)))

# def filter_func(isPrime, [2,3,4,5,6,7,8]): 
#     return [x for x in func_list if p(x)]

# x = [34, 56]

# print(len(map(str, x)))

# i = 0
# while i < 3:
# 	print(i)
# 	i += 1
# 	if i == 3:
# 		print(0)

# lst = [12, 2, 3, 4, 5, 6]

# foldr(max, [], lst)

# x = 2
# y= 10
# x*=y*x+1
# print(x)

# x = "abcd"
# print(list(map([], x)))

# x = ["ab", "cd"]

# print(len(map(list, x)))

# alist=[4,3,2,1]
# alist = alist.reverse()
# print(alist)

# l = [1, -2, -3, 4, 5]
# def f1(x):
#     return x<-1
# m1 = map(f1, l)
# print(list(m1))

# x = ["12", "34"]
# print(len(list(map(len, x))))

# i = 0 
# while i < 5: 
#     print(i) 
#     i += 1 
#     if i == 3: 
#         break 
#     else:
#         print(0)

# a = True 
# b = False 
# c = False
# if not a or b: 
#     print (1)
# elif not a or not b and c: 
#     print (2) 
# elif not a or b or not b and a: 
#     print (3) 
# else: 
#     print (4)

# list_1 = []
# for i in "123":
#     if i in "123":
#         list_1.append(1)

# print(list_1)

# x = ['ab', 'cd']
# print(len(list(map(list, x))))))

# def to_upper(k):
#     k.upper()
# x = ['ab', 'cd']
# print(list(map(to_upper, x)))

# l = [1, -2, -3, 4, 5]
# def f1(x):
#     return x<-1
# m1 = map(f1, l)
# print(list(m1))

# a = sum(int(['123', '123']))

# l = [-2, 4]
# m = list(map(lambda x: x*2, l))
# print(m)

# def square(x):
# 	return(x*x)

# def thisfunction(x):
# 	lst = ['1', 3, 4, '6', 8, 11, '54']
# 	return lst[x]

# for x in range(2, 1360, -1):
# 	print("wasd")

# def stoptime(time):
# 	endoftime = 999

# 	if(time == endoftime-1):
# 		return -1

# 	time = 0
# 	running = 0

# 	while time == running:
# 		if(time > endoftime):
# 			time += 1
# 		running += 1
# 	return 1

# for x in range(20, 9, -1):
# 	print("asrfsdf")

# def stopTime(Time):
#     endOftime = 999
    
#     if(Time == endOftime-1):
#         return -1
#     else:
#         return 0
    
#     time = 0
#     running = 0

#     while time == running:
#         time +=1
#         time = stopTime(time)
#         running += 1

# adj = ['red', 'big']
# fruits = ['banana', 'apple']

# def nested():
# 	for x in fruits:
# 		for y in adj:
# 			print(y, x)

# mylst = ["asdsadsad", [0,1,2,3,4,5,6,7], ['85'], [[1,2,3]]]

# def whatisthis(x):
# 	return foo1()+2
# def foo1():
# 	def foo2(x):
# 		return 1+x
# 	return foo2(2)

# n = 10
# s = 7
# b = 5

# while n > s and s >= b:
# 	a = b+1
# 	print("sdf")

# def f1(x):
# 	if x == 0:
# 		return True
# 	else:
# 		return f2(x-1)
# def f2(x):
# 	if x == 0:
# 		return False
# 	else:
# 		return f1(x-1)

# for i in range(90, 100):
# 	if i%2 != 0:
# 		print(i)

# def powerx(x, y):
# 	result = 1
# 	while x >=1:
# 		result = result - x
# 		y = y-1
# 	return result


# lst = [1,2,3,4,5]
# def forfunc(lst):
# 	for el in lst:
# 		lst = lst + [el]
# 	return len(lst)

# def tester2(p):
# 	while p < 10:
# 		p +=1
# 		t = p**2
# 		return t*2

# def function(lst):
# 	a = 0
# 	if lst == []:
# 		return 1
# 	else:
# 		a+=1
# 		return a*function(lst[1:]) * math.sqrt(16)
# def f(n):
# 	if n == 0:
# 		return 0
# 	else:
# 		return n+f(n-1)

# def f1(x):
#     if x == 0:
#         return True
#     else:
#         return f2(x-1)

# def f2(x):
#     if x == 0:
#         return False
#     else:
#         return f1(x-1)

# lst = [["COMRKFFK", [12,12,23,45]], ["LFLJDJJFDG", [56,67,78,78,89]]]

# def get_courses(std):
# 	ccode_lst = []
# 	for courses in std:
# 		ccode_lst.append(courses[0])
# 	return ccode_lst

# def get_grade(std, ccode):
# 	for courses in std:
# 		if ccode == courses[0]:
# 			return sum(courses[1])

# a = get_grade(lst, "COMRKFFK")

# print(a)

# a = {"abc": 123, "dfg": 567}

# print(a[0])

# print(a.values())

# for x in range(len(a)):
# 	if x == 0:
# 		print()


# def country_population(countriep):
# 	c_list = []

# 	for x,y in countries.items():
# 		if y <= max_pop and y >= min_pop
# 		c_list.append(x)
		
# 	print(c_list)

# Python3 code to demonstrate working of 
# Key index in Dictionary 
# Using list() + keys() + index() 
  
# initializing dictionary 
# test_dict = {'all' : 1, 'food' : 2, 'good' : 3, 'have' : 4} 
  
# initializing search key string 
# search_key = 'good'
  
# printing original dictionary 
# print("The original dictionary is : " + str(test_dict)) 
  
# Using list() + keys() + index() 
# Key index in Dictionary 
# res = list(test_dict.keys()).index(search_key) 
  
# printing result  
# print("Index of search key is : " + str(res)) 

# def isDivisor(num, num2):
# 	return num % num2 == 0

# def divisorList(num):
# 	return [x for x in range(1, num) if isDivisor(num, x)]

# def sumList(lst):
# 	return sum(lst)

# def perfectOrNot(num):
# 	if sumList(divisorList(num)) > num:
# 		return "Abundant"
# 	elif sumList(divisorList(num)) == num:
# 		return "Perfect"
# 	else:
# 		return "Deficient"

# def make_empty_tree():
# 	return ("BT", [])

# def makeTree(root, left, right):
# 	return ("BT", [root, left, right])

# def root(tree):
# 	return tree[1][0]

# def right_subtree(tree):
# 	return tree[1][2]

# def left_subtree(tree):
# 	return tree[1][1]

# def is_empty_tree(tree):
# 	return tree == (make_empty_tree())

# def is_btree(tree):
# 	return type(tree) == tuple and type(tree[0]) == list and tree[0] == "BT"

# def is_leaf_tree(tree):
# 	return is_btree(tree) and is_empty_tree(left_subtree(tree)) and is_empty_tree(right_subtree(tree))

# a = string.ascii_letters
# a = string.ascii_lowercase+string.ascii_uppercase

# print(a, "\n")

IncidentPriority = {"PersonalInjury" : 100,"DownedPowerLine" : 90, "OpenDrain" : 80}

def make_incidentReportDB():
	return ("report", [])

def make_incidentReport(address, town, incidentType):
	return [address, town, incidentType]

def getTown(r):
	return r[1]

def getStreetAddress(r):
	return r[0]

def getIncidenttype(r):
	return r[2]

def add_incidentPriority(db, r):
	db[1].append(r)

def delete_incidentReport(db, r):
	db.remove(r)

def get_incidentPriority(r):
		if r == []:
			return 0
		if getIncidenttype(r) == "PersonalInjury":
			return 100
		elif getIncidenttype(r) == "DownedPowerLine":
			return 90
		elif getIncidenttype(r) == "OpenDrain":
			return 80
		else:
			return 60

def get_highPriorityList(db):
	return list(filter(is_HighPriority, db))

def is_HighPriority(r):
	return get_incidentPriority(r) >= 90

def get_nextReportToDispatch(db):
	if db == []:
		return None
	def get_higherPriorityIncident(r1, r2):
		if(get_incidentPriority(r1) >= get_incidentPriority(r2)):
			return r1
		else:
			return r2
	return foldr(get_higherPriorityIncident, [], db)