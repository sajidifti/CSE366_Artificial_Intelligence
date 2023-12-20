// Assignment 1

// This assignment was done in C++ as I do not have a good grasp on Python yet.
// In further assignments, I will try to code in python.

// The code is not complete. It can only print minimum cost and the path from S to D.
// I added the course pretty late. I missed multiple classes. This was my first Lab of CSE366.
// I will try to be more vigilant from next class and lab.



#include <bits/stdc++.h>
using namespace std;

void add_edge(vector<int> adj[], int src, int dest)
{
    adj[src].push_back(dest);
    adj[dest].push_back(src);
}

bool BFS(vector<int> adj[], int src, int dest, int v,
         int pred[], int dist[])
{
    list<int> queue;

    bool visited[v];

    for (int i = 0; i < v; i++)
    {
        visited[i] = false;
        dist[i] = INT_MAX;
        pred[i] = -1;
    }

    visited[src] = true;
    dist[src] = 0;
    queue.push_back(src);

    while (!queue.empty())
    {
        int u = queue.front();
        queue.pop_front();
        for (int i = 0; i < adj[u].size(); i++)
        {
            if (visited[adj[u][i]] == false)
            {
                visited[adj[u][i]] = true;
                dist[adj[u][i]] = dist[u] + 1;
                pred[adj[u][i]] = u;
                queue.push_back(adj[u][i]);

                if (adj[u][i] == dest)
                    return true;
            }
        }
    }

    return false;
}

void minimumCost(vector<int> adj[], int s,
                           int dest, int v)
{
    int pred[v], dist[v];

    if (BFS(adj, s, dest, v, pred, dist) == false)
    {
        cout << "INF";
        return;
    }

    vector<int> path;
    int crawl = dest;
    path.push_back(crawl);
    while (pred[crawl] != -1)
    {
        path.push_back(pred[crawl]);
        crawl = pred[crawl];
    }

    cout << "Minimum Cost Is: "
         << dist[dest];

    cout << "\nPath is::\n";
    for (int i = path.size() - 1; i >= 0; i--)
        cout << path[i] + 1 << " ";
}

int main()
{
    int V, E, S, D, x, y;
    

    cout << "Enter V and E: ";
    cin >> V >> E;

    vector<int> adj[V];

    cout << endl
         << "Enter The Edges: \n\n";

    for (int i = 0; i < E; i++)
    {
        cout << "Enter x and y (" << i + 1 << "): ";
        cin >> x >> y;
        x = x - 1;
        y = y - 1;
        add_edge(adj, x, y);
    }

    cout << "\nEnter S and D: ";
    cin >> S >> D;
    S = S - 1;
    D = D - 1;

    minimumCost(adj, S, D, V);
    cout << endl;
    return 0;
}
