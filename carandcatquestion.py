#car ca T
#cr car T
#ar car T
#caaar car F
#cara car T
#carss car F
matn1,matn2="cara","car"
min_m,max_m=(matn1,matn2) if len(matn2)>len(matn1) else (matn2,matn1)

difference=0
i=0
j=0
def isequal(matn1,matn2):
    if matn1==matn2:
     return True

    while difference<2 and len(max_m)>i and len(min_m)>j:
        if len(max_m)==len(min_m)+1:
            if(max_m[i]!=min_m[j]):
             difference+=1
             i+=1
            else:
                j+=1
                i+=1
        
        elif len(max_m)==len(min_m):
            if max_m[i]!=min_m[j]:
                difference+=1
                i+=1
                j+=1
        else:
             return False
    return difference<2
   




