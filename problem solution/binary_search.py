def binary_search(item_list,item):
    low=0
    high=len(item_list)-1
    found=False
    while (low<=high and not found):
        mid=(low+high)//2
        if item_list[mid] == item:
            found=True
        else:
            if item_list[mid]<item:
                 low=mid+1
            else:
                 high=mid-1
    return found

print(binary_search([1,2,3,5,8], 3))
