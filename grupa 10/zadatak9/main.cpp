#include <bits/stdc++.h>

using namespace std;

// OSNOVI ALGORITMI ZA PRONALAZAK NAJKRACEG PUTA IZMEDJU DVA CVORA
/// Grupa 10

// Pretraga u sirinu, koristimo red i vektor sa obradjene cvorove
void bfs(int s, int u, const vector<vector<int>>& adj, vector<int>& d, vector<int>& p) {
    int n = adj.size();
    vector<bool> used(n, false);
    queue<int> q;

    q.push(s);
    used[s] = true;
    p[s] = -1;
    d[s] = 0;

    while (!q.empty()) {
        int v = q.front();
        q.pop();
        for (int to : adj[v]) {
            if (!used[to]) {
                used[to] = true;
                q.push(to);
                d[to] = d[v] + 1;
                p[to] = v;
            }
        }
    }

    // Ispis putanje
    if (!used[u]) {
        cout << "No path from " << s << " to " << u << "!\n";
    } else {
        vector<int> path;
        for (int v = u; v != -1; v = p[v])
            path.push_back(v);
        reverse(path.begin(), path.end());

        cout << "Shortest path from " << s << " to " << u << ": ";
        for (int v : path)
            cout << v << " ";
        cout << "\n";
    }
}

// Rekurzivna predraga u dubinu, koristimo samo vektor za obradjene cvorove
void dfs(int v, const vector<vector<int>>& adj, vector<bool>& visited) {
    visited[v] = true;
    cout << v << " ";
    for (int u : adj[v]) {
        if (!visited[u]) {
            dfs(u, adj, visited);
        }
    }
}


int main()
{
    // Inicijalizujemo graf

    int n = 6;

    vector<vector<int>> adj(n);

    adj[0] = {1, 2};
    adj[1] = {0, 3};
    adj[2] = {0, 3, 4};
    adj[3] = {1, 2, 5};
    adj[4] = {2};
    adj[5] = {3};

    // Pocetni i kranji cvor
    int s = 0;
    int u = 5;


    // Rezultati pretraga

    cout << "BFS: " << endl;

    vector<int> d(n), p(n);
    bfs(s, u, adj, d, p);

    cout << "\nDFS:" << endl;

    vector<bool> visited(n, false);
    cout << "DFS starting from node " << s << ": ";
    dfs(s, adj, visited);
    cout << "\n";

    return 0;
}
