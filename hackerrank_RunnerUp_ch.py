#n = int(input('entries'))
##arr = list(map(int, input().rstrip().split(',')))
##
##print(arr)


##n = input('entries')

##arr = list(map(int,n.split(' ')))
##print(arr)
##print([n for n in range(2,6)])
##
##while True:
##    try:
##        n = int(input('mention entries'))
##        if n in range(2,11):
##            break
##        else:
##        
##            raise ValueError('mention appropriate entries')
##
##    except ValueError as e:
##        print(e)
    
##n = int(input('mention range'))
##if n in range(2,11):
##
##    arr = list(map(int, input('mention scores').split(' ')))
##    A = list((filter(lambda x:x>=-100 and x <= 100),arr))
##        
##    win = max(A)
##    runA = A.remove(win)
##    runup = max(runA)

##    print(runup)
##
##else:
##    print('Invalid Range')


n=input()
a=map(int,input().split())
a=list(set(a))
a.remove(max(a))
print (max(a))
