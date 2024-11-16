#include <cstdio>
#include <queue>
#include <vector>
#include <cmath>

using namespace std;
#define MAX 51

int N, L, R, arr[MAX][MAX];
bool visited[MAX][MAX];
int dx[] = {0, 0, 1, -1};
int dy[] = {1, -1, 0, 0};

queue<pair<int, int>> q;
vector<pair<int, int>> v;

bool flag = true;
int sum = 0;

void bfs(pair<int, int> start)
{
    q.push(start);
    visited[start.first][start.second] = true;

    while (!q.empty())
    {
        pair<int, int> temp = q.front();
        q.pop();

        for (int i = 0; i < 4; i++)
        {
            int nx = dx[i] + temp.first;
            int ny = dy[i] + temp.second;

            if (0 <= nx && nx < N && 0 <= ny && ny < N && !visited[nx][ny])
            {
                if (abs(arr[nx][ny] - arr[temp.first][temp.second]) >= L &&
                    abs(arr[nx][ny] - arr[temp.first][temp.second]) <= R)
                {
                    q.push({nx, ny});
                    visited[nx][ny] = true;
                    v.push_back({nx, ny});
                    sum += arr[nx][ny];
                }
            }
        }
    }
}
void clear()
{
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            visited[i][j] = false;
        }
    }
}

int main()
{
    int days = 0;
    scanf("%d %d %d", &N, &L, &R);

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            scanf("%d", &arr[i][j]);
        }
    }

    while (flag)
    {
        flag = false;
        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < N; j++)
            {
                if (!visited[i][j])
                {
                    v.clear();
                    v.push_back({i, j});
                    sum = arr[i][j];
                    bfs({i, j});
                }

                if (v.size() >= 2)
                {
                    flag = true;
                    for (int i = 0; i < v.size(); i++)
                    {
                        arr[v[i].first][v[i].second] = sum / v.size();
                    }
                }
            }
        }

        if (flag)
            days++;

        clear();
    }
    printf("%d\n", days);
}