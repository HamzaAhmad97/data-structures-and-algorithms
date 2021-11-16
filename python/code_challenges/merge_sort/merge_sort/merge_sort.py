def merge_sort(li):
    n = len(li)
    if n > 1:
        mid = n//2
        left = li[:mid]
        right = li[mid:]

        merge_sort(left)
        merge_sort(right)
        merge(left, right, li)
        print(li)
def merge(left, right, li):
    i = j = k = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            li[k] = left[i]
            i += 1
        else:
            li[k] = right[j]
            j += 1

        k += 1
        print("before while")
        print(li, " ", left, " ", right)
        while i < len(left):
            li[k] = left[i]
            i += 1
            k += 1
  
        while j < len(right):
            li[k] = right[j]
            j += 1
            k += 1 
        print("after while")
        print(li, " ", left, " ", right)
    
if __name__ == "__main__":
    li = [8,4,23,42,16,15]
    merge_sort(li)
    print("xxx" ,li)