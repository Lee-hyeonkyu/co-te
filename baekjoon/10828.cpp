#include <iostream>
using namespace std;

class stack_
{
private:
    int idx = -1;
    int stack_[10000] = {};

public:
    void push(int num)
    {
        stack_[++idx] = num;
    }

    int pop()
    {
        if (idx == -1)
            return -1;
        return stack_[idx--];
    }

    int size()
    {
        return idx + 1;
    }

    bool empty()
    {
        return idx == -1;
    }

    int top()
    {
        if (idx == -1)
            return -1;
        return stack_[idx];
    }
};

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    stack_ stk;

    int a, n;
    string str;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> str;

        if (str == "push")
        {
            cin >> a;
            stk.push(a);
        }
        else if (str == "pop")
        {
            cout << stk.pop() << endl;
        }
        else if (str == "size")
        {
            cout << stk.size() << endl;
        }
        else if (str == "empty")
        {
            cout << stk.empty() << endl;
        }
        else if (str == "top")
        {
            cout << stk.top() << endl;
        }
    }
};

// 200ms printf, scanf로 바꾸면 0ms