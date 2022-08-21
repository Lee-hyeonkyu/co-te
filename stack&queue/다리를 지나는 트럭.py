def solution(bridge_length, weight, truck_weights):
    time_required = 0
    dis = [0] * bridge_length
    
    while dis:
        time_required += 1
        dis.pop(0)
        if truck_weights:
            if sum(dis) + truck_weights[0] <= weight:
                dis.append(truck_weights.pop(0))
            else:
                dis.append(0)
    
    return time_required

bridge_length = 100
weight = 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]

print(solution(bridge_length, weight, truck_weights))

