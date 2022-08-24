import re
new_id = "abcdefghijklmn.p"

def solution(new_id):
    # 1.
    new_id = new_id.lower()
    # 2.
    new_id = re.sub('[^a-z-_\.0-9]', '', new_id)
    # 3.
    new_id = re.sub('[\.]+', '.', new_id)
    # 4.
    new_id = new_id.strip(".")
    # 5.
    if len(new_id) == 0:
        new_id = "a"
    # 6.
    elif len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == ".":
            new_id = new_id.rstrip(".")
    # 7.
    while len(new_id) <3:
        new_id += new_id[-1]

    return new_id

print(solution(new_id))

