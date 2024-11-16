#include <cstdio>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

int dx[] = {0, 0, 1, -1};
int dy[] = {1, -1, 0, 0};
int apt = 0;

bool visited[26][26];
queue<pair<int, int>> q;
vector<int> apt_cnt;

int N;

void bfs(vector<vector<int>> board, pair<int, int> start)
{
    q.push(start);
    int tmp = 1;

    while (!q.empty())
    {
        pair<int, int> cur = q.front();
        q.pop();

        for (int i = 0; i < 4; i++)
        {
            int nx = dx[i] + cur.first;
            int ny = dy[i] + cur.second;

            if (0 <= nx && nx < N && 0 <= ny && ny < N && !visited[nx][ny] && board[nx][ny] == 1)
            {
                visited[nx][ny] = 1;
                tmp++;
                q.push({nx, ny});
            }
        }
    }
    apt_cnt.push_back(tmp);
}

int main()
{
    scanf("%d", &N);
    vector<vector<int>> board(N, vector<int>(N));

    for (int i = 0; i < N; i++)
    {
        char row[26];
        scanf("%s", row);
        for (int j = 0; j < N; j++)
        {
            board[i][j] = row[j] - '0';
        }
    }

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            if (!visited[i][j] && board[i][j] == 1)
            {
                visited[i][j] = 1;
                bfs(board, {i, j});
            }
        }
    }

    sort(apt_cnt.begin(), apt_cnt.end());
    printf("%ld\n", apt_cnt.size());

    for (int i = 0; i < apt_cnt.size(); i++)
    {
        printf("%d\n", apt_cnt[i]);
    }
}