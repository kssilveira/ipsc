#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <queue>
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

vector<pair<int, int> > huffmann(vector<int> &v) {
  if (v.size() == 0) return vector<pair<int, int> >();

  int total = 0;
  for (int i = 0; i < v.size(); ++i) total += tsize[v[i]];

  priority_queue<pair<float, vector<pair<int, int> > >,
     vector<pair<float, vector<pair<int, int> > > >,
     greater<pair<float, vector<pair<int, int> > > > > pq;
  for (int i = 0; i < v.size(); ++i) {
    vector<pair<int,int> > vv;
    vv.push_back(make_pair(v[i], 1));
    pq.push(make_pair(1.0*tsize[v[i]]/total, vv));
  }

  while (pq.size() > 1) {
    pair<float, vector<pair<int, int> > > p1 = pq.top(); pq.pop();
    pair<float, vector<pair<int, int> > > p2 = pq.top(); pq.pop();

    vector<pair<int, int> > pv = p1.second;
    pv.insert(pv.end(), p2.second.begin(), p2.second.end());
    for (int i = 0; i < pv.size(); ++i) {
      pv[i].second++;
    }
    pq.push(make_pair(p1.first+p2.first, pv));
  }
  return pq.top().second;
}

int go(int a, int pr) {
  int ret = pr;

  //cout << endl << "go " << a << " " << g[a].size() << endl;
  vector<pair<int, int> > vh = huffmann(g[a]);
  //for (int i = 0; i < vh.size(); ++i)
  //  cout << vh[i].first << " " << vh[i].second << endl;

  for (int i = 0; i < vh.size(); ++i) {
    ret += go(vh[i].first, pr+vh[i].second-1);
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
