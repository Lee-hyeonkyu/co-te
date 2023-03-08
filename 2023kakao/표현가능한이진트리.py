def check(arr: list, level: int):
    mid = len(arr) // 2
    if not level:
        return True
    elif arr[mid] == "0":
        if arr[mid - level] == "1" or arr[mid + level] == "1":
            return False

    side = check(arr[:mid], level//2) * check(arr[mid+1:], level//2)
    return side


def solution(numbers):
    answer = []
    for i in numbers:
        # 현재 이진트리
        number = str(bin(i)[2:])
        x = len(number)
        # 최소 크기의 완전이진트리
        fbt = 2**len(str(bin(x)[2:]))-1
        lack = fbt-x
        if lack:
            number = ('0'*lack)+number
        answer.append(1 if check(number, (len(number)+1) // 4) else 0)

    return answer
