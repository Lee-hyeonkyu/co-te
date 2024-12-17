#include <cstdio>

using namespace std;
typedef unsigned long long ll;

ll factorial(int num)
{
    if (num)
    {
        return num * factorial(num - 1);
    }
    else
        return 1;
}

int main()
{
    int N;
    ll x;
    scanf("%d", &N);
    x = factorial(N);
    printf("%llu", x);
}