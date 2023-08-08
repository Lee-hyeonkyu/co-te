import sys
sys.setrecursionlimit(10000)

nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]

def preorder(array, lst):
    node = array[0]

    arr1 = []
    arr2 = []

    for i in range(1, len(array)):
        if node[0] > array[i][0]:
            arr1.append(array[i])
        else:
            arr2.append(array[i])
    
    lst.append(node[2])

    if len(arr1)>0:
        preorder(arr1, lst)
    if len(arr2)>0:
        preorder(arr2,lst)

def postorder(array, lst):
    node = array[0]

    arr1 = []
    arr2 = []

    for i in range(1, len(array)):
        if node[0] > array[i][0]:
            arr1.append(array[i])
        else:
            arr2.append(array[i])

    if len(arr1)>0:
        postorder(arr1,lst)
    if len(arr2)>0:
        postorder(arr2,lst)
    lst.append(node[2])


def solution(nodeinfo):
    preorder_answer = []
    postorder_answer = []

    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)
    
    nodeinfo.sort(key=lambda x: [x[1],x[0]], reverse = True)
    
    preorder(nodeinfo,preorder_answer)
    postorder(nodeinfo, postorder_answer)

    return [postorder_answer,postorder_answer]
print(solution(nodeinfo))