def solution(nums):
    # 목록 최대 개수
    x = int(len(nums)/2)
    # 중복없이 종류 수
    y = len(set(nums))
    if x-y > 0:
        return y
    else:
        return x
