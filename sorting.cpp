#include <cstdio>
#include <ctime>
#include <iostream>

using namespace std;

void print_arr(int arr[], int n) {
  cout << "[ ";
  for (int i = 0; i < n; i++) {
    cout << arr[i] << ' ';
  }
  cout << "]\n";
}

// buuble sort
// void bubble_sort(int arr[], int n) {
//   for (int i = 0; i < n - 1; i++) {
//     for (int j = 0; j < n - i - 1; j++) {
//       if (arr[j] > arr[j + 1]) {
//         int temp = arr[j];
//         arr[j] = arr[j + 1];
//         arr[j + 1] = temp;
//       }
//     }
//   }
// }
//

void bubble_sort(int arr[], int n) {
  for (int i = n - 1; i > 0; i--) {
    bool swapped = false;
    for (int j = 0; j < n - 1; j++) {
      if (arr[j] > arr[j + 1]) {
        int temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
        swapped = true;
      }
    }
    if (!swapped)
      break;
  }
}

int main() {
  int arr[] = {64, 34, 25, -12, 22, 11, 90};
  int arr2[] = {3, 6, 11, 25, 39};
  int n = sizeof(arr) / sizeof(arr[0]);
  print_arr(arr, n);
  clock_t begin = clock();
  bubble_sort(arr, n);
  print_arr(arr, n);
  printf("%.12fs\n", (double)(clock() - begin) / CLOCKS_PER_SEC);
  return 0;
}
