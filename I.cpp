#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

vector< vector<int> > g;
vector<int> tsize;

// just get size of subtree.
int go_size(int a) {
  int ret = 1;
  for (int i = 0; i < g[a].size(); ++i)
    ret += go_size(g[a][i]);
  return tsize[a] = ret;
}

bool my_sort(int i,int j) { return tsize[i] < tsize[j]; }

int go(int a, int pr) {
  int ret = pr;

  // order by size of subtree.
  sort(g[a].begin(), g[a].end(), my_sort);

  int x = g[a].size();
  int k = ceil(log2(x));
  int t = x - (pow(2.0f, k) - x);  // +1 size

  for (int i = 0; i < g[a].size(); ++i) {
    ret += go(g[a][i], pr+k-(i>=t));
  }
  return ret;
}

int main() {
  int t; cin >> t;
  while (t--) {
    int n; cin >> n;
    g.clear(); g.resize(n);
    for (int i = 0; i < n-1; ++i) {
      int k; cin >> k; k--;
      g[k].push_back(i+1);
    }

    tsize.clear(); tsize.resize(n, 0);
    go_size(0);

    int ret = go(0 /*root*/, 0 /*current prefix*/);
    cout << ret << endl;
  }
}
