#include<iostream>
#include<vector>
using namespace std;

void insertionSort(vector<int> &arr, int len)
{
    int j = 0;
    for(int i=0; i<len; i++)
    {
        j = i;
        while(j>0 && arr[j]<arr[j-1])
        {
            swap(arr[j], arr[j-1]);
            j--;
        }
    }
}

int main()
{
    int len,temp;
    vector<int> arr;
    cin>>len;
    for(int i=0; i<len; i++)
    {
        cin>>temp;
        arr.push_back(temp);
    }
    insertionSort(arr, len);
    cout<<"sorted:";
    for(int i=0; i<len; i++)
    {
        cout<<arr[i]<<" ";
    }
    return 0;
}