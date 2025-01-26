def Bubble(ele):
    for i in len(ele):
        for i in range(ele):
            if ele[i]>ele[i]+1:
                temp=ele[i]
                ele[i]=ele[i]+1
                ele[i+1]=temp
    for i in ele:
        print(i,end=' ')

arr=[3,7,2,5,8,9]
Bubble(arr)