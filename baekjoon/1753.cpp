#include <cstdio>
#include <queue>
#include <vector>
#include <functional>

using namespace std;

void dijkstra(int num, const vector<vector<pair<int, int>>> &graph)
{
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    vector<int> distances(graph.size(), 1e9);
    distances[num] = 0;
    pq.push({0, num});

    while (!pq.empty())
    {
        int dist = pq.top().first;
        int current = pq.top().second;
        pq.pop();

        if (dist > distances[current])
            continue;

        for (const auto &edge : graph[current])
        {
            int next = edge.first;
            int weight = edge.second;

            if (dist + weight < distances[next])
            {
                distances[next] = dist + weight;
                pq.push({distances[next], next});
            }
        }
    }

    for (int i = 1; i < distances.size(); i++)
    {
        if (distances[i] == 1e9)
            printf("INF\n");
        else
            printf("%d\n", distances[i]);
    }
}

int main()
{
    int v, e, k;
    scanf("%d %d", &v, &e);
    scanf("%d", &k);
    vector<vector<pair<int, int>>> graph(v + 1);

    for (int i = 0; i < e; i++)
    {
        int x, y, z;
        scanf("%d %d %d", &x, &y, &z);
        graph[x].emplace_back(y, z);
    }
    dijkstra(k, graph);
}