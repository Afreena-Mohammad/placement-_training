#ip:longest common sub sequence from two strings
#abcd
#axbdc
#op:abc
def sub_sequence(s):
    seq=[]
    sub_sequence_r(s,'',0,seq)
    return seq
def sub_sequence_r(s,c,i,seq):
    if i ==len(s):
        seq.append(c)
        return
    sub_sequence_r(s,c,i+1,seq)
    sub_sequence_r(s,c+s[i],i+1,seq)
    

s=input()

print(sub_sequence(s))
    