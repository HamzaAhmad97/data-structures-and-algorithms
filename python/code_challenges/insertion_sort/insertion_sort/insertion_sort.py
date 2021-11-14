def insertion_sort(li):
  for i in range(len(li)):
    j = i - 1 
    temp = li[i] 
    
    while j >= 0 and temp < li[j]:
      li[j + 1] = li[j] 
      j = j - 1 
      
    li[j + 1] = temp 
  return li

if __name__ == "__main__":
    li = [5,8,1,10]
    print(insertion_sort(li))