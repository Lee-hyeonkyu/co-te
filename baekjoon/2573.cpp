#include <cstdio>
#include <vector>
#include <queue>
#include <cstring>

#define MAX 301
using namespace std;

int n, m, board[MAX][MAX];
int dx[] = {1, 0, 0, -1};
int dy[] = {0, -1, 1, 0};
int year = 0;
bool check = true;

void bfs(pair<int, int> pos, bool visited[MAX][MAX])
{
    queue<pair<int, int>> q;
    q.push(pos);
    while (!q.empty())
    {
        pair<int, int> cur = q.front();
        q.pop();

        for (int k = 0; k < 4; k++)
        {
            int nx = cur.first + dx[k];
            int ny = cur.second + dy[k];

            if (0 <= nx && nx < n && 0 <= ny && ny < m && board[nx][ny] != 0 && !visited[nx][ny])
            {
                visited[nx][ny] = 1;
                q.push({nx, ny});
            }
        }
    }
}

int countIceberg()
{
    bool visited[MAX][MAX] = {0};
    int isol = 0;
    check = false;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (board[i][j] != 0 && visited[i][j] == 0)
            {
                check = true;
                visited[i][j] = 1;
                bfs({i, j}, visited);
                isol++;
            }
        }
    }
    return isol;
}

void meltingIceberg()
{
    bool visited_[MAX][MAX] = {0};
    int Nboard[MAX][MAX] = {0};

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {

            if (board[i][j] != 0 && !visited_[i][j])
            {
                int tmp = 0;
                visited_[i][j] = 1;
                for (int k = 0; k < 4; k++)
                {
                    int nx = i + dx[k];
                    int ny = j + dy[k];

                    if (0 <= nx && nx < n && 0 <= ny && ny < m && board[nx][ny] == 0)
                    {
                        tmp++;
                    }
                }
                int nxtIce = board[i][j] - tmp;
                if (nxtIce < 0)
                {
                    nxtIce = 0;
                }
                Nboard[i][j] = nxtIce;
            }
        }
    }
    memcpy(board, Nboard, sizeof(Nboard));
    year++;
}

bool noIceberg()
{
    bool chk = true;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (board[i][j] != 0)
            {
                chk = false;
            }
        }
    }
    return chk;
}

int main()
{
    int cnt = 0;
    scanf("%d %d", &n, &m);

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            int t;
            scanf("%d", &t);
            board[i][j] = t;
        }
    }
    while (check)
    {
        cnt = countIceberg();
        if (cnt >= 2)
        {
            check = false;
        }
        else if (check)
        {
            meltingIceberg();
        }
    }
    if (noIceberg())
    {
        year = 0;
    }

    printf("%d\n", year);
}