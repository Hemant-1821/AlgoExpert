#include<iostream>
#include<vector>
using namespace std;

void selectionSort(vector<int> &arr, int len)
{
    int smallest = 0;
    for(int i=0; i<len; i++)
    {
        smallest = i;
        for(int j=i+1; j<len; j++)
        {
            if(arr[j]<arr[smallest])
            {
                smallest = j;
            }
        }
        swap(arr[i],arr[smallest]);
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
    selectionSort(arr, len);
    cout<<"sorted:";
    for(int i=0; i<len; i++)
    {
        cout<<arr[i]<<" ";
    }
    return 0;
}