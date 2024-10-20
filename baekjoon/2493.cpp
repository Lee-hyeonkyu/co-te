#include <cstdio>
#include <vector>
using namespace std;

int main()
{
    int n;
    scanf("%d", &n);
    vector<int> array(n);
    vector<int> answer(n, 0);

    for (int i = 0; i < n; i++)
    {
        scanf("%d", &array[i]);
    }

    for (int i = 1; i < n; i++)
    {
        int tmp = i - 1;
        while (1)
        {
            if (array[tmp] < array[i])
            {
                if (answer[tmp] == 0)
                {
                    answer[i] = 0;
                    break;
                }
                tmp = answer[tmp] - 1;
            }
            else
            {
                answer[i] = tmp + 1;
                break;
            }
        }
    }

    for (int i = 0; i < n; i++)
    {
        printf("%d ", answer[i]);
    }
    printf("\n");

    return 0;
}
