# while-else
lst = [2, 3, 3, -2, -2, -2]
idx = 0

while idx < len(lst):
    if lst[idx] == -12:
        print ("found the target")
        break
    idx +=1
else:
    print("didn't find it")
    
