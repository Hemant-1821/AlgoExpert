#include<iostream>
#include<vector>
using namespace std;

int binarySearch( vector<int> &arr, int start, int end, int target)
{
    if(start>end)
    {
        return -1;
    }
    int mid = ((end+start)/2);
    if(arr[mid]>target)
    {
        binarySearch(arr, start, mid-1, target);
    }
    else if(arr[mid]<target)
    {
        binarySearch(arr, mid+1, end, target);
    }
    else if(arr[mid]==target)
    {
        return mid;
    }
}

int main()
{
    int len, temp, target;
    vector<int> arr;
    cin>>len;
    for(int i=0; i<len; i++)
    {
        cin>>temp;
        arr.push_back(temp);
    }
    cout<<"enter target";
    cin>>target;
    int idx = binarySearch(arr, 0, len-1, target);
    if(idx>=0)
    {
        cout<<"element at:"<<idx;
    }
    else
    {
        cout<<"element not in this list!";
    }
    return 0;
}