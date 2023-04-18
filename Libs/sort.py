
def quick_sort(array):
  if len(array) <- 1:
    return array
  pivot = array[0]
  left = [x for x in array[1:] if x <= pivot]
  right = [x for x in array[1:] if x > pivot]
  return left + [pivot] + right


def merge_sort(array):
  if len(array) <= 1:
    return array
  mid = len(array) // 2
  left = array[:mid]
  right = array[mid:]
  left = merge_sort(left)
  right = merge_sort(right)
  return merge(left, right)

def merge(left, right):
  l = 0
  r = 0
  result = []
  while l < len(left) and r < (right):
    if left[l] < right[r]:
      result.append(left[l])
      l += 1
    else:
      result.append(right[r])
      r += 1
  result += left[l:]
  result += right[r:]
  return result

def heap_sort(self, nums: List[int]) -> List[int]:
  heap = []
  while nums:
      heappush(heap, nums.pop())
  while heap:
      nums.append(heappop(heap))
  return nums

def bubble_sort(array):
  for i in range(len(array)):
    for j in range(len(array) - 1, i, -1):
      if array[j] < array[j - 1]:
        array[j], array[j - 1] = array[j - 1], array[j]
  return array

def selection_sort(array):
  for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
      if array[min_index] > array[j]:
        min_index = j
    array[i], array[min_index] = array[min_index], array[i]
  return array

def insertion_sort(array):
  for i in range(1, len(array)):
    v = array[i]
    j = i - 1
    while j >= 0 and array[j] > v:
      array[j + 1] = array[j]
      j -= 1
    array[j + 1] = v
  return array

def shell_sort(array):
  n = len(array)
  h = 1
  while h < n:
    h = 3 * h + 1
  while h >= 1:
    for i in range(h, n):
      v = array[i]
      j = i - h
      while j >= 0 and array[j] > v:
        array[j + h] = array[j]
        j -= h
      array[j + h] = v
    h = h // 3
  return array

def counting_sort(array):
  max_value = max(array)
  counts = [0] * (max_value + 1)
  for i in array:
    counts[i] += 1
  result = []
  for i, v in enumerate(counts):
    result += [i] * v
  return result

def radix_sort(array):
  RADIX = 10
  placement = 1
  max_digit = max(array)
  while placement < max_digit:
    buckets = [list() for _ in range(RADIX)]
    for i in array:
      tmp = int((i / placement) % RADIX)
      buckets[tmp].append(i)
    a = 0
    for b in range(RADIX):
      buck = buckets[b]
      for i in buck:
        array[a] = i
        a += 1
    placement *= RADIX
  return array

def bucket_sort(array):
  BUCKET_SIZE = 5
  max_value = max(array)
  size = max_value // BUCKET_SIZE + 1
  buckets = [[] for _ in range(size)]
  for i in array:
    buckets[i // BUCKET_SIZE].append(i)
  result = []
  for bucket in buckets:
    bucket = insertion_sort(bucket)
    result += bucket
  return result
  