def select_sort(a, i, n):
    if i >= n - 1:
        return
    minpos = i
    for j in range(i + 1, n):
        if a[j] < a[minpos]:
            minpos = j
    a[i], a[minpos] = a[minpos], a[i]
    select_sort(a, i + 1, n)


def insert_sort(a, i, n):
    if i >= n:
        return
    j = i
    while j > 0 and a[j] < a[j - 1]:
        a[j], a[j - 1] = a[j - 1], a[j]
        j = j - 1
    insert_sort(a, i + 1, n)


def merge_sort(a):
    i = len(a)
    if i <= 1:
        return a
    return merge(merge_sort(a[0: i // 2]), merge_sort(a[i // 2:i]))


def merge(a, b):
    c, m, n = [], len(a), len(b)
    i, j = 0, 0

    while i + j < m + n:
        if i == m:
            c.append(b[j])
            j = j + 1
        elif j == n:
            c.append(a[i])
            i = i + 1
        elif a[i] > b[j]:
            c.append(b[j])
            j = j + 1
        elif a[i] <= b[j]:
            c.append(a[i])
            i = i + 1
        else:
            pass
    return c


def quick_sort(a, l, r):
    if r - l <= 1:
        return
    i = l + 1
    for j in range(l + 1, r):
        if a[j] <= a[l]:
            a[i], a[j] = a[j], a[i]
            i = i + 1
    a[i - 1], a[l] = a[l], a[i - 1]
    quick_sort(a, l, i - 1)
    quick_sort(a, i, r)


a = [23, 38, 72, 45, 12, 92, 40, 37, 56, 28]

# insert_sort(a, 1, len(a))
# print(a)

# merge_sort(a)
# print(merge_sort(a))

# select_sort(a, 0, len(a))
# print(a)

quick_sort(a, 0, len(a))
print(a)

# b = [2, 5, 7, 9]
# c = [1, 4, 8, 10]
#
# print(merge(b, c))
