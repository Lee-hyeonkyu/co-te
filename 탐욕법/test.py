def gcd(w,h):
    if h == 0:
        return w
    mod = w % h
    if mod != 0:
        w, h = h, mod
        return gcd(w, h)
    else:
        return h

def solution(w,h):
    answer =(w*h) - (w+h-gcd(w,h))
    return answer
