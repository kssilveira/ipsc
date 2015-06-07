#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

vector< vector<int> > g;
int go(int a, int pr) {
  int ret = pr;

  int k = ceil(log2(g[a].size()));
  for (int i = 0; i < g[a].size(); ++i) {
    ret += go(g[a][i], pr+k);
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

    int ret = go(0 /*root*/, 0 /*current prefix*/);
    cout << ret << endl;
  }
}
