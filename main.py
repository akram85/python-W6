#list ,dictionary ,tuples
'''l=list(range(10))
print(l)
print(6 in l)

x=[1,2,3,4,2,1]
x.append(10)
print(x)
print(type(x))

y={1,2,3,4,2,1}
y.add(44)

print(y)
print(type(y))

s=set(range(100))
print(s)
print(44 in s)

d={}
d['akram']=12345
d['hassan']=333244
print(d)
print(d['hassan'])'''
'''for i in range(len(l)):
  print(l[i])'''
'''for i in l:
  print(i)'''

l = [
  'It', 'was', 'the', 'monday', 'morning', 'I', 'woke', 'up', 'in', 'the',
  'the', 'morning'
]

for x in l:
  print(x)

s = set(l)
#print(s)

d = {}
max = 0
for x in l:
  d[x] = 0
  
for x in l:
  d[x] = d[x] + 1
  if (d[x] > max):
    max = d[x]

print(d)
print(max)
#tuples
t =(1,2,3,4,5)
print(t)

for key in d:
  print(key ,d[key])