def find_uniq(arr):
    for x in arr:
        y = arr.index(x)
        if len(arr[y:]) > 2:
            if arr[y] != arr[y+1] and arr[y] != arr[y+2]:
                return arr[y]
        elif len(arr[y: ]) > 1:
            if arr[y] != arr[y+1]:
                return arr[y]
        else:
                return arr[y]