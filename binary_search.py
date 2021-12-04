print('Hello World!')

global debug
debug = 0

def binary_search(arr, n):
  beg = 0
  end = len(arr) - 1
  i = 0
  while beg <= end:
    i = i + 1
    mid = beg + int((end - beg) / 2)
    find = arr[mid]
    if debug:
      print(i,' ',beg,' ',end,' ',mid,' ', find)
    if find == n:
      return n
    if find < n:
      beg = mid + 1
    else:
      end = mid - 1
    if i > 10: 
      return 999
  return None

my_arr = [1, 3, 5, 9, 45, 79, 100]
print(binary_search(my_arr, 79))
print(binary_search(my_arr, 44))