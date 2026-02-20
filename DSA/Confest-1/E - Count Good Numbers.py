n = int(input())
numbers = list(map(int,input().split()))
good_count = 0
    
for x in numbers:
        # Condition 1: Factor of 18 (x must not be 0)
    is_factor = (x != 0 and 18 % x == 0)
        
        # Condition 2: Multiple of 45
    is_multiple = (x % 45 == 0)
        
    if is_factor or is_multiple:
        good_count += 1
            
print(good_count)