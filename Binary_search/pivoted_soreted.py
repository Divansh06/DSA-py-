arr = [7,8,9,1,2,3,4,5,6]

low = 0
high = len(arr)-1
target = 7
while low<=high:
    mid = (low + high) // 2
    if arr[mid] == target:
        print(mid)
        break
    if arr[low] <= arr[mid]:
        if arr[mid] > target and arr[low] <= target:
            high = mid - 1
        else:
            low = mid + 1
    else: 
        if arr[mid] < target <= arr[high]:
            low = mid + 1
        else:
            high = mid - 1