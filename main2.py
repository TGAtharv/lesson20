def OnTime(n):
    literation=0
    for i in range(1,n+1):
        literation+=1
    print("When n is ",n," Literations = ",literation)

OnTime(10)
OnTime(20)
OnTime(42)

print("\nWith every 'n' the time taken and literations will increase linearly")