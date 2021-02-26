# Paranthesis balancing problem
def par_bal(par):
    x = 0
    for i in range(len(par),1,-1): #controls the length of the input string
    # print(par[i-1])
        # inner for loop provides sub-strings
        for j in range(0,x+1): # we want the inner loop to run only once for the 1st iteration
            #i=5,x=0 --> j=0 | i=4,x=1 --> j=0,1 | i=3,x=2 --> j=0,1,2 | i=2,x=3 --> j=0,1,2,3 | i=1,x=4 --> j=0,1,2,3,4
            sub = par[j:j+i]
            count = 0
            for s in sub:
                if s == '{':
                    count+=1
                else:
                    count-=1
                
                if count < 0: # will break out of the immediate loop when count = -1 '{}}'
                    break

            if count == 0:
                print(f'The longest balanced substring is')
                return sub
        x+=1
    else:
        print('No balanced substring found')

def user_input():
    s = ' '
    while s[0] not in ['{','}']:
        s = input('Enter the paranthesis string\n')
        if s[0] not in ['{','}']:
            print('Enter paranthesis only')
        else:
            return s

str_input = user_input()
par = par_bal(str_input)
print(par)