#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int n;
    bool check = false;
    cin >> n;
    vector<int> x(n);

    for (int &v : x)
    {
        cin >> v;
    }

    sort(x.begin(), x.end());

    int num = 1;

    for (int v : x)
        if (num >= v)
        {
            num += v;
        }

    cout << num << endl;

    return 0;
}