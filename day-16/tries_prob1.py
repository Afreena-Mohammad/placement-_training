'''ip: 5 no.of queries
 1 school
 1 world
 1 word
 1 scholar
 2 word
 3 sch
 if you have 1 insert the word
 2 is to search for a word 
 3 search for a word with prefix
 op:TRUE
    FALSE
    TRUE
TESTcase: ip:7
1 car
1 cap
2 ca
3 ca
1 can
3 ca
2 cap
op:False
True
True'''
'''n = int(input())
a = []
for i in range(n):
    item = input()
    a.append(item)

for item in a:
    print(item)
    for i in range(len(item)):
        if item[0]==1:'''
'''
x = no of queries-->int(input())
q = 7
1--->school
1--->world
1--->word
1--->scholar
2--->word
2--->wood
3--->sch

1-->insert the word
2-->search for the word
3-->print T/F if there exists words starting with 'sch'

op:
True
False
True


----------------------------->
Test case:2
q=7
1-->car
1-->cap
2-->ca
1-->ca
1-->can
3-->ca
2-->cap

op:
False
True
True
'''
'''testcase-3: ip:5
1 word
1 word
3 wo
4 word
2 word
op:1
False'''

x = int(input())  
q = []
for _ in range(x):
    query = input().strip().split(' ')
    q.append((int(query[0]), query[1]))
d = {} 
for query in q:
    qv = query[0]
    word = query[1]
    if qv == 1:
        d[word] = True
    elif qv == 2:
        if word in d:
            print("True")
        else:
            print("False")
    elif qv == 3:
        found = False
        for key in d:
            if key.startswith(word):
                found = True
                break
        print(found)
    elif qv == 4:
        del d[word]
        print(l)
        print(d)
             
            
            