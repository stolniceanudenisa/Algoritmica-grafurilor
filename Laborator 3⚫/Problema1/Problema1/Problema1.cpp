#include <iostream>
#include <fstream>
#include <utility>
#include <vector>
#include <algorithm>
using namespace std;
ifstream file;

//Initializare matricea costurilor
void initCost(int w[30][30], int n) {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			w[i][j] = INT_MAX;
		}
	}
}

//Citirea din fisier, extremitatile muchiei + ponderea
void citire(int &n, pair <int, int> muchie[30], int w[30][30], int &m) {
	file >> n;
	initCost(w, n);
	int i = 0;
	while (!file.eof()) {
		file >> muchie[i].first >> muchie[i].second;
		file >> w[muchie[i].first - 1][muchie[i].second - 1];
		i++;
	}
	m = i;
}

//creeare lista de vecini
void vecini(vector<int> v[30], pair <int, int> muchie[30], int m) {
	int vf1, vf2;
	for (int i = 0; i < m; i++) {
		vf1 = muchie[i].first;
		vf2 = muchie[i].second;
		v[vf1 - 1].push_back(vf2);
	}
}

//initializare informatii despre varf: distanta de la start la varf + parintele varfului 
void initializare_info(int n, int start, pair <int, int> info[30]) {
	for (int i = 0; i < n; i++) {
		info[i].first = INT_MAX;
		info[i].second = NULL;
	}
	info[start - 1].first = 0;
}

//vectorului Q i se atribuie initial toate varfurile grafului
void init_Q(vector <int> &Q,int n) {
	for (int i = 0; i < n; i++) {
		Q.push_back(i+1);
	}
}

//elimina minimul din vector
int extract_min( vector <int> &Q, pair <int, int> info[30]) {
	int poz=0, varf= Q.at(0),min = info[Q.at(0)-1].first;
	for (unsigned i = 1; i < Q.size(); i++)
		if (info[Q.at(i)-1].first < min)
		{
			varf = Q.at(i);
			min = info[Q.at(i)-1].first;
			poz = i;
		}
	Q.erase(Q.begin() + poz);
	return varf;
}

//functia actualizeaza drumul minim dintre doua varfuri
void relax(int parinte, pair <int, int> &u_pereche, pair <int, int> & v_pereche, int  cost) {
	if (v_pereche.first > u_pereche.first + cost) {
		v_pereche.first = u_pereche.first + cost;
		v_pereche.second = parinte;
	}
}

//algoritmul determina drumul minim de la un varf start la celelalte varfuri
void Dijkstra(int n, vector<int> v[30], int start, int w[30][30], pair <int, int> info[30]) {
	vector <int> Q, S;
	int u, vf;
	initializare_info(n, start, info);
	init_Q(Q, n);
	while (Q.size()>0) {
		u = extract_min(Q,info);
		S.push_back(u);
		if(info[u-1].first!=INT_MAX){
			for (unsigned i = 0; i < v[u - 1].size(); i++) {
				vf = v[u - 1].at(i);
				relax(u, info[u - 1], info[vf - 1], w[u - 1][vf - 1]);
			}
		}
	}
}

//afisare drum minim
void afisareDrum(int n, int start, pair <int, int> info[30]) {
	for (int i = 0; i < n; i++) {
		cout << "Drumul minim " << start << "-" << i + 1 << ": ";
		if (info[i].first != INT_MAX)
			cout << info[i].first << endl;
		else cout << "nedeterminat" << endl;
	}
}

/*void afisareMuchii(pair <int, int> muchie[30], int m) {
	for (int i = 0; i < m; i++) {
		cout << muchie[i].first << " " << muchie[i].second << endl;
	}
}*/

/*void afisareCost(int w[30][30], int n) {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cout << w[i][j] << " ";
		}
		cout << endl;
	}
}*/

void afisareVecini(vector<int> v[30], int n) {
	for (int i = 0; i < n; i++) {
		cout << i + 1 << ": ";
		for (unsigned  j = 0; j < v[i].size(); j++) {
			cout << v[i].at(j) << " ";
		}
		cout<<endl;
	}
}

int main() {
	vector<int> v[30];
	pair <int, int> info[30], muchie[30];
	int n, w[30][30], m, start, cmd;
	file.open("input.txt");
	citire(n, muchie, w, m);
	vecini(v, muchie, m);

	//afisareMuchii(muchie, m);
	//cout << n << endl;
	//afisareCost(w, n);
	//afisareVecini(v,n);
	while (1) {
		cout << "1. Aplicati algoritmul Dijkstra" << endl;
		cout << "0. Exit" << endl;
		cout << "Comanda: ";
		cin >> cmd;
		if (cmd == 1) {
			cout << "Dati un varf de start: "; cin >> start;
			if (start<1 || start >n)
				cout << "Nu exista acest nod!" << endl;
			else {
				Dijkstra(n, v, start,w, info);
				afisareDrum(n, start, info);
			}
			continue;
		}
		if (cmd == 0) {
			cout << "Multumit ca ati utilizat aplicatia!" << endl;
			break;
		}
		if (cmd != 0 || cmd != 1) {
			cout << "Comanda gresita!" << endl;
		}
	}
	file.close();
	return 0;
}
