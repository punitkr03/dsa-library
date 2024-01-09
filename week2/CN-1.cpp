// Search In Rotated Sorted Array

int search(vector<int>& arr, int n, int k)
{
    int getPivot(vector<int> arr, int n);
    int binarySearch(vector<int> arr, int s, int e, int k);
    // Write your code here.
    // Return the position of K in ARR else return -1.
    int s = 0, e = arr.size()-1;
    int pivot = getPivot(arr, n);
    if(k >= arr[pivot] && k <= arr[n-1])
        return binarySearch(arr, pivot, n-1, k);
    else
        return binarySearch(arr, 0, pivot, k);
}

int getPivot(vector<int> arr, int n) {
    int s = 0, e = arr.size()-1;

    while(s < e) {
        int mid = s + (e-s)/2;
        if (arr[mid] >= arr[0])
            s = mid + 1;
        else
            e = mid;
    }
    return s;
}

int binarySearch(vector<int> arr, int s, int e, int k) {
    
    while (s <= e) {
        int mid = s + (e-s)/2;
        if(arr[mid] == k)
            return mid;
        else if (arr[mid] > k)
            e = mid -1;
        else
            s = mid + 1;
    }
    return -1;
}