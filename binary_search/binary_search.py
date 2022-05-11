def bimnary_search(l, k):
    left = 0
    right = len(l)-1
    while right >= left:
        mid = int(left+(right-left)/2)
        if l[mid] == k:
            return mid
        elif l[mid] > k:
            right = mid - 1
        elif l[mid] < k:
            left = mid + 1

a = [1,3,5,5,7,9,12]
print(bimnary_search(a, 5))




