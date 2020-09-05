#include<iostream>
#include <vector>
using namespace std;

void quickSort(int start, int end, vector<int> &arr)
{
    if(start>=end)
    {
        return;
    }
    int pivot = start;
    int left = start+1;
    int right = end;
    while(left<=right)
    {
        if(arr[left]>arr[pivot] && arr[right]<arr[pivot])
        {
            swap(arr[left],arr[right]);
        }
        if(arr[left] <= arr[pivot])
        {
            left++;
        }
        if(arr[right] >= arr[pivot])
        {
            right--;
        }
    }
    swap(arr[right],arr[pivot]);
    bool leftIsSmaller = false;
    if((right-1) - start < end - (right+1))
    {
        leftIsSmaller = true;
    }


    if(leftIsSmaller)
    {
        // cout<<start<<right-1<<"if"<<endl;
        quickSort(start,right-1,arr);
        quickSort(right+1,end,arr);
    }
    else
    {
        // cout<<start<<right-1<<"else"<<endl;
        quickSort(right+1,end,arr);
        quickSort(start,right-1,arr);
    }
}

int main()
{
    int len,temp;
    std::vector< int > arr = {8,5,2,9,5,6,3};
    len = arr.size();
    quickSort(0, len-1, arr);
    for(int i=0;i<len;i++)
    {
        cout<<arr[i];
    }
    return 0;
}
