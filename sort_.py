# Selection sort (선택 정렬)

# 정렬되지 않은 리스트에서 0번쨰 인덱스를 기준으로 잡고 기준 이후의 인덱스를 돌면서 제일 작은 것을 찾고 스왑한다.
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array


# Insertion sort (삽입 정렬)
# (오름차순으로 정렬 시)
# n번째 인덱스부터 n-1번째 인덱스와 비교하여 더 작은 것과 위치를 바꾼다. 이후로 n-1번째가 현재 자신보다 작다면 멈춤.
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


def insertion_sort(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
            else:
                break

    return array


# Quick sort (퀵 정렬)

# 0번째 인덱스를 기준으로 잡고 리스트의 왼쪽은 기준보다 큰 값, 리스트의 오른쪽은 기준보다 작은 값을 찾으며 큰 값이 왼쪽, 작은 값이 오른쪽에 있다면 위치 스왑을 시키고
# 만약 작은 값이 왼쪽 큰 값이 오른 쪽에 있다면 (크로스된 상황) 작은 값의 위치와 기준의 위치를 스왑한다. 그럼 기준으로부터 왼쪽과 오른쪽으로 나뉘어지는데
# 이 떄 분할하여 위와 같은 방식으로 정렬을 진행한다.

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]
    # pivot보다 작은 값을 (왼쪽)으로 모은다.
    left_side = [x for x in tail if x <= pivot]
    # pivot보다 큰 값을 (오른쪽)으로 모은다.
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


# Count sort (계수 정렬)

# 정돈되지 않은 리스트의 가장 큰 값에 + 1 한 빈 리스트를 초기화한 뒤, 리스트 전체를 돌며 나온 값을 빈 리스트의 인덱스 위치에 +1 해주고
# 빈 리스트의 길이만큼 루프를 돌며 그 위치의 값만큼 반복하여 출력한다.
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]


def count_sort(array):
    new_array = []
    count = [0] * (max(array)+1)

    for i in range(len(array)):
        count[array[i]] += 1

    for i in range(len(count)):
        for _ in range(count[i]):
            new_array.append(i)
    return new_array
