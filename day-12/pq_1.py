'''ip:given two lists the two lists mixture of even numbers and odd number [6,3,2,9,4,7]
[8,7,5,3,6,9]
generate another list all the even numbers should matched with all odd numbers from another list
ex:op:[6+7,6+5,6+3,6+9,2+7,2+5,2+3,2+9,4+7,4+5,4+3,4+9]
op:[13,11,9,15,9,7,5,11,11,9,7,13]'''
def fun(l):
    e=[i for i in l if i%2==0]
    o=[j for j in l if j%2!=0]
    return e,o
def com(e,o,even_index=0,odd_index=0,res=None):
    if result is None:
        result=[]
    if even_index>=len(e):
        return result
    if odd_index>=len(o):
        return com(e,o,even_index+1,0,result)
    result.append(e[even_index]+o[odd_index])
    return com(e,o,even_index,odd_index+1,result)
l
    
    
        
        
    
    
    
    
        
        