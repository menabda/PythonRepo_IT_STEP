# მოცემულია რიცხვების სია [94, 56, 32, 55, 344, 192, 4832, 2, 9, 0, 1]

# გამოიყენეთ სორტირების ალორითმები: bubble sort, merge sort და insertion sort.

# შედეგები დაბეჭდეთ ეკრანზე.
nums = [94, 56, 32, 55, 344, 192, 4832, 2, 9, 0, 1]

#bubble sort

def bubble_sort(arr):
  n = len(arr)

  for i in range(n-1, 0, -1):
    for j in range(i):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]


# ===============

bubble_sort(nums)

print("Bubble Sorted Numbers:")
print(nums)

#merge sort

def merge_sort(arr):
  n = len(arr)
  middle = n // 2

  if n <= 1:
    return arr
  
  left = merge_sort(arr[:middle])
  right = merge_sort(arr[middle:])

  return merge_two_list(left, right)


def merge_two_list(a, b):
  c = []
  i = j = 0

  while i < len(a) and j < len(b):
    if a[i] < b[j]:
      c.append(a[i])
      i += 1
    else:
      c.append(b[j])
      j += 1
  
  c += a[i:] + b[j:]

  return c


print("Merge Sorted Numbers:")
print(merge_sort(nums))

#insertion sort

def insertion_sort(arr):
  n = len(arr)

  for i in range(1, n):
    j = i

    while j > 0 and arr[j] < arr[j - 1]:
      arr[j-1], arr[j] = arr[j], arr[j-1]

      j -= 1

insertion_sort(nums)

print("Insertion Sorted Numbers")
print(nums)