def isequal(matn1,matn2):
 min_str,max_str=matn1,matn2 if matn2>matn1 else matn2,matn1
 difference=0
 i=0
 while difference<2:
  if max_str[i]==min_str[i]:
    i+=1
  elif  min_str[i]==max_str[i+1]
  else:
   difference+=1