
stg = input()
srch = input()
step, cnt = 0,0
while step <= len(stg)- len(srch):
    if stg[step:step+ len(srch)] == srch:
        cnt +=1
        step += len(srch)
    else:
        step+=1
    
print(cnt)

# doc = input().strip()
# word = input().strip()
# count, start = 0, 0

# while start <= len(doc) - len(word):
#     if doc[start:start + len(word)] == word:
#         count += 1
#         start += len(word)
#     else:
#         start += 1
# print (count)
