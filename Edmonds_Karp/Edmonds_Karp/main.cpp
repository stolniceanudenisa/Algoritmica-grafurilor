#include<iostream>
#include<vector>
#include<queue>
#include<stack>
#include<fstream>
#include<string>
using namespace std;
int n, m, nrp,s,t;
vector<vector<int>> c, f;//matricea capacitatii a fluxurilor
vector<string> color;//vector viz/neviz
vector<int> parinte;
typedef struct arc {
	int ex1, ex2;
};
stack<arc> S;//pt memorarea arcelor in drumul de crestere
queue<int> Q;//pentru bfs

ifstream in("input.txt");


int min(int x, int y) {
	return x < y ? x: y;
}

//cautare bfs pentru un drum de crestere
int bfs(int sursa, int dest) {
	int u, v;
	color.assign(n + 1, "alb");
	parinte.assign(n + 1, 0);
	Q.push(sursa);
	color[sursa] = "gri";

	while (!Q.empty()) {
		u = Q.front();
		Q.pop();
		for (v = 1; v <= n; v++) {
			if (color[v] == "alb" && c[u][v] - f[u][v] > 0) {//capacitatea arcului in graful rezidual este pozitiva 
				Q.push(v);
				color[v] = "gri";
				parinte[v] = u;
			}
		}
		color[u] = "negru";
	}
	return color[dest] == "negru";//am parcurs un drum de crestere
}

//Ford Fulkerson
int FluxMaxim(int sursa, int dest) {
	int u;
	//init flux maxim
	int flux_max = 0;
	vector<int> aux;
	aux.assign(n + 1, 0);
	f.assign(n + 1, aux);

	//cat timp exista un drum de crestere, incrementeaza fluxul de-a lungul acestui drum
	while (bfs(sursa, dest)) {
		int flux = INT_MAX;
		nrp++;
		arc w;
		for (u = n; parinte[u] > 0; u = parinte[u]) {
			flux = min(flux, c[parinte[u]][u] - f[parinte[u]][u]);
			w.ex1 = parinte[u];
			w.ex2 = u;
			S.push(w);
		}
		cout << "Drumul de crestere " << nrp << endl;
		while (!S.empty())
		{
			w = S.top();
			cout << "(" << w.ex1 << "," << w.ex2 << ")";
			S.pop();
		}
		cout <<endl<< "Fluxul pompat: " << flux << endl;
		//adaugam flux la flux_max
		for (u = n; u > parinte[u]; u = parinte[u]) {
			f[parinte[u]][u] += flux;
			f[u][parinte[u]] -= flux;
		}
		flux_max += flux;
	}
	return flux_max;
}

void citire() {
	int a, b, p;
	vector<int> aux;//vector de initializari
	in >> n >> m >>s>>t;

	//initializari
	aux.assign(n + 1, 0);
	parinte.assign(n + 1, 0);
	c.assign(n + 1, aux);
	f.assign(n + 1, aux);

	//citire capacitati
	while (!in.eof())
	{
		in >> a >> b >> p;
		c[a][b] = p;
		c[b][a] = p;
	}
	in.close();
}
int main() {
	citire();
	int flux_max = FluxMaxim(1, n);
	cout << "Flux maxim " << flux_max <<" pe "<<nrp<<" cai."<< endl;
	return 0;
}

