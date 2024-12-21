def zero(n):
     count=0
     for i in range(1,n+1):
          if(str(i).count("0")>0):
               count+=1
     z=n
     n=n+count
     count1=0
     for j in range(z+1,n+1):
          if(str(j).count("0")>0):
               count1 += 1
     n=n+count1
     return n
print(zero(100))





