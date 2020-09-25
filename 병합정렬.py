n = int(input())

list = []
for _ in range(n):
    list.append(int(input()))


def merge_sort(list):
    
    if (len(list) == 1):
        return list
          
    else:

        middle = len(list)//2

        left = list[:middle]
        right = list[middle:]

        left = merge_sort(left)
        right = merge_sort(right)
        
        return merge(left, right)

def merge(left, right):
    ans = []

    while (len(left)>0 or len(right)>0):

        if (len(left) == 0):
            ans.append(right[0])
            right = right[1:]

        elif (len(right) == 0):
            ans.append(left[0])
            left = left[1:]

        else:
            if left[0] <= right[0]:
                ans.append(left[0])
                left = left[1:]

            else:
                ans.append(right[0])
                right = right[1:]
    
    return ans


print(merge_sort(list))
