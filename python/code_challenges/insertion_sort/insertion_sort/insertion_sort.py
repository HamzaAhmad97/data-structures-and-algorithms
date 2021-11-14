def insertion_sort(li):
  for i in range(len(li)):
    j = i - 1 
    temp = li[i] 
    
    while j >= 0 and temp < li[j]:
      li[j + 1] = li[j] 
      j = j - 1 
      
    li[j + 1] = temp 
  return li