#binary search algorithm
#O(log(n)) base = 2
iterations = 0
def binary_search(arr, target):
    l = 0
    r = len(arr)-1
    
    while l < r:
        m = (l+r)//2
        
        if arr[0] == target:
            return 0
         
        elif arr[len(arr)-1] == target:
            return len(arr)-1
           
        if arr[m] == target:
            return m
            
        elif arr[m] < target:
            l = m+1
        
        elif arr[m] >  target:
            r = m-1
   
    return -1
 
def bs_index_occurance(arr, target):
    index = binary_search(arr, target)
    print(f"index: {index}")
    index_list = []
    
    #check left side
    i = index - 1
    while i > 0:
        if arr[i] == target:
            print(f"left i {i}")
            index_list.append(i)
        
        if target not in arr[0:i]:
            break
            
        i -= 1
    
    #check right side
    i = index + 1
    while i < len(arr) - 1:
        if arr[i] == target:
            print(f"right i {i}")
            index_list.append(i)
        if target not in arr[i: len(arr)-1]:
            break
           
        i += 1
    
    index_list.sort()
    return index_list
    
    
    
    

def binary_search_iteration(array, target):
    l = 0
    r = len(array)-1
    i = 0
    #occurance = {target: 0}
    m = 0
    
    while l < r:
        m = (l + r)//2
        i +=1
        if array[0] == target:
            return 0, i
            
        elif array[len(array)-1] == target:
            return len(array)-1
     
        elif array[m] == target:
            return m, i
            
        elif array[m] < target:
            l = m+1
        
        elif array[m] > target:
            r = m-1
        
    return -1, i
    
def binary_search_recursive(arr, l, r, target, occurance):
    if target not in arr:
        return -1
    
    if r < l:
        return -1

    
    m = (l+r)//2

    if arr[m] == target: # and m not in occurance[target]
        #return m
        #occurance[target].append(m)
        #print(occurance)
        #l = m+1
        #l = 0
        #r = len(arr)-1    
        return m
        
    elif arr[m] < target:
        l = m+1
    else:
        r = m-1
        
    
    return binary_search_recursive(arr, l, r, target, occurance)
     
if __name__ == "__main__":
    arr = [4,15,9,11,17,15,21,25,29,32,15,38,40]
    l = 0
    r = len(arr)-1
    target = 15
    print(bs_index_occurance(arr, target))
    print(arr)
    print(arr[:5:-1])
    #occurance = {target: []}
    #bsr = binary_search_recursive(arr, l, r, target, occurance)
    #print(bsr)
    #if bsr != None and bsr != -1:
    #    print(arr[bsr])
    #target_index, i = binary_search(arr,target)
    #print(f"iterations: {i}")
    #print("position:",target_index)
    #print(f"value: {arr[target_index]}")
    