n = 2
queries = ["desktop1 request", "desktop2 request", "desktop3 request",
           "desktop3 request", "desktop1 release", "desktop3 request"]


def solution(n, queries):
    answer = list()
    available_ip = [i for i in range(1, n+1)]

    for i, j in enumerate(queries):
        key = j.split()[0]
        value = j.split()[1]

        target = [s for s in answer if s.startswith(key)]

        if value == 'request' and available_ip:
            if target and [s for s in target if s.split()[1] != 'reject']:
                ip = '192.168.0.{}'.format(
                    int([i for i in answer if i.startwith(key)[-1][-1]]))

            else:
                ip = '192.168.0.{}'.format(min(available_ip))

            answer.append('{} {}'.format(key, ip))
            available_ip.remove(min(available_ip))

        elif value == 'request' and not available_ip:
            answer.append('{} {}'.format(key, 'reject'))
        else:
            available_ip.append(int(target[-1][-1]))

    return answer


print(solution(n, queries))
