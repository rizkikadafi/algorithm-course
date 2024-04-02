/*
Plagiarism Policy:

Associate Professor Steven Halim provides this implementation for his classes
in National University of Singapore (NUS) School of Computing (SoC).

This code is supposed to be studied by his students to understand the technical
details of various time complexities.

Steven does not think that anyone else sets a programming test involving
this..., so feel free to use the code below
*/

#include <bits/stdc++.h>
using namespace std;

int main() {
  long long counter = 0;
  clock_t begin = clock();
  int N = 50000; // try adding a few more zero digitS at the back of this
                 // variable to make your computer hangs...
  for (int i = 0; i < N;
       ++i) { // O(c * N*N) = O(cN^2), c is 'small' if you leave line 14
              // commented, but c is BIG if you uncomment it
    // printf("i = %d\n", i);
    // for (int j = 1; j < N; j*=2) { // O(log N)
    for (int j = 0; j < N; ++j) { // O(N) inner loop, that will be repeated N
                                  // times in the outer loop
      ++counter; // this operation is O(1), and fast, let's say 0.0000000001 s
      // but if you uncomment the next line, the same algorithm will be
      // noticeably much slower printf(" counter = %d\n", counter); // this I/O
      // operation is 'heavy', let's say 0.01s per statement...
    }
  }
  printf("counter = %lld, computed in = %.12fs\n", counter,
         (double)(clock() - begin) / CLOCKS_PER_SEC);
  return 0;
}

// the default setup of this starting SpeedTest.cpp should be around 2-3s
