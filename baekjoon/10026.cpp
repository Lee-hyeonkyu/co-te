#include <cstdio>
#include <vector>
#include <queue>
#include <string.h>
using namespace std;

int N;
char board[100][101], board_blind[100][101];
bool visited[100][101];
int dx[] = {0, 0, -1, 1};
int dy[] = {-1, 1, 0, 0};

void bfs(int x, int y, char board_[100][101])
{
    queue<pair<int, int>> q;
    visited[x][y] = 1;
    char color = board_[x][y];
    q.push({x, y});

    while (!q.empty())
    {
        pair<int, int> cur = q.front();
        q.pop();

        for (int i = 0; i < 4; i++)
        {
            int nx = cur.first + dx[i];
            int ny = cur.second + dy[i];

            if (0 <= nx && nx < N && 0 <= ny && ny < N && !visited[nx][ny] && board_[nx][ny] == color)
            {
                visited[nx][ny] = 1;
                q.push({nx, ny});
            }
        }
    }
}

int cnt_regions(char board_[100][101])
{
    int regions = 0;

    memset(visited, 0, sizeof(visited));

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            if (!visited[i][j])
            {
                bfs(i, j, board_);
                regions++;
            }
        }
    }
    return regions;
}

int main()
{
    scanf("%d", &N);

    for (int i = 0; i < N; i++)
    {
        scanf("%s", board[i]);
    }

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            if (board[i][j] == 'G')
            {
                board_blind[i][j] = 'R';
            }
            else
            {
                board_blind[i][j] = board[i][j];
            }
        }
    }

    int normal_r = cnt_regions(board);
    int blind_r = cnt_regions(board_blind);

    printf("%d %d\n", normal_r, blind_r);
}
