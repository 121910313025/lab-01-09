#Implement parentesis matching algorithm using stack

open_list=["[","{","("]
close_list=["]","}",")"]
def check(Str):
    stack=[]
    for i in Str:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            k=close_list.index(i)
            if((len(stack)>0) and (open_list[k]==stack[len(stack)-1])):
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack)==0:
        return "Balanced"
    else:
        return "Unbalanced"
#display output
string="{[]{()}}"
print(string,"-",check(string))
string="({}"
print(string,"-",check(string))


        
        
    
    
