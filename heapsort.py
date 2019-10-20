t=int(input())

for i in range(t):
         l=list(map(int,input().split()))
         """ to sort the the given elements using heap sort u should perform creation and deletion of thr hea"""
         """ creating heap """
         maxheap=[]
         maxheap.append(l[0])
         for i in range(1,len(l)):
            maxheap.append(l[i])
            cp=len(maxheap)
            parent=(cp//2)-1
            
            while maxheap[parent]<l[i]:
                    temp=maxheap[parent]
                    maxheap[parent]=l[i]
                    maxheap[cp-1]=temp
                    cp=parent+1
                    parent=(cp//2)-1
                    if parent<0:
                        break
         print(maxheap)
         """deletion and storing in another array"""
         l=[0]
         for i in range(len(maxheap)):
            l.insert(0,maxheap[0])
            maxheap[0]=maxheap[-1]
            maxheap = maxheap[0:len(maxheap)-1]
            cp=1
            child1=cp*2
            child2=(cp*2)+1
            while maxheap[child1-1]>maxheap[0] or maxheap[child2-1]>maxheap[0]:
                if maxheap[child1-1]>maxheap[child2-1]:
                    temp=maxheap[child1-1]
                    maxheap[child1-1]=maxheap[0]
                    maxheap[0]=temp
                    cp=child1
                    child1=cp*2
                    child2=(cp*2)+1
                elif maxheap[child1-1]<maxheap[child2-1]:
                    temp=maxheap[child2-1]
                    maxheap[child2-1]=maxheap[0]
                    maxheap[0]=temp
                    cp=child2
                    child1=cp*2
                    child2=(cp*2)+1
                if child1>len(maxheap)-1 and child2>len(maxheap)-1:
                    break
                print(l,maxheap)
    
