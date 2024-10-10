#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int partition(vector<int> &arr, int low, int high)
{
    int pivot = arr[high];
    int i = low - 1;

    for (int j = low; j < high; j++)
    {
        if (arr[j] < pivot)
        {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return i + 1;
}

void quicksort(vector<int> &arr, int low, int high)
{
    if (low < high)
    {
        int pivot_point = partition(arr, low, high);
        quicksort(arr, low, pivot_point - 1);
        quicksort(arr, pivot_point + 1, high);
    }
}

int main()
{
    vector<int> arr1;
    vector<int> arr2;
    int length, num;
    int answer = 0;
    cin >> length;
    for (int i = 0; i < length; i++)
    {
        cin >> num;
        arr1.push_back(num);
    }

    for (int i = 0; i < length; i++)
    {
        cin >> num;
        arr2.push_back(num);
    }

    quicksort(arr1, 0, length - 1);
    quicksort(arr2, 0, length - 1);

    for (int i = 0; i < length; i++)
    {

        answer += arr1[i] * arr2[(length - 1) - i];
    }
    cout << answer << endl;
}