#include<iostream>
#include<vector>
using namespace std;

void bubbleSort(vector<int> &arr, int len)
{
    bool notSorted = true;
    while(true)
    {
        notSorted = false;
        for(int i=0; i<len-1; i++)
        {
            if(arr[i]>arr[i+1])
            {
                swap(arr[i],arr[i+1]);
                notSorted = true;
            }
        }
        if(!notSorted)
        {
            break;
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
    bubbleSort(arr, len);
    cout<<"sorted:";
    for(int i=0; i<len; i++)
    {
        cout<<arr[i]<<" ";
    }
    return 0;
}