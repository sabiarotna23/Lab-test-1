number=[12,5,8,3,17,1,9]
smallest = number[0]
for num in number:
    if num < smallest:
        smallest = num
        print("smallest number is:",smallest)