number_1 = int(input('number_1: '))
number_2 = int(input('number_2: '))
number_3 = int(input('number_3: '))
number_4 = int(input('number_4: '))
number_5 = int(input('number_5: '))
arr = [number_1,number_2,number_3,number_4,number_5]       
DUPLICATES=0    
#Searches for duplicate element    
for i in range(0, len(arr)):    
    for j in range(i+1, len(arr)):    
        if(arr[i] == arr[j]):    
            DUPLICATES=DUPLICATES+1 
if (DUPLICATES==0):
    print("ALL UNIQUE")
else:
    print("DUPLICATES")