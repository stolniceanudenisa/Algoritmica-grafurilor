// Problema1.cpp : Implementati rutinele Prufer de codificare si decodificare a unui arbore.
//

#include "stdafx.h"
using namespace std;
#include<fstream> 
#include<vector>
#include<iostream>
#include<queue>
#include<utility>
ifstream f;

//citeste radacina si muchiile arborelui (tata, fiu)
void read_from_file(vector<pair<int,int>>& legatura, int& n, int& root) {
	int father=0, son=0;
	f >> root;
	while (!f.eof()) {
		f >> father >> son;
		legatura.push_back(make_pair(father, son));
		n++;
	}
}

//calculeaza gradul unui nod
void degree(vector<pair<int, int>>& legatura, int& n, vector<int>& d) {
	d.assign(n, 0);
	for (auto l : legatura) {
		d[l.second-1] = d[l.second-1] + 1;
		d[l.first - 1] = d[l.first - 1] + 1;
	}
}

struct CustomCompare
{
	bool operator()(pair<int, int>& lhs, pair<int, int>& rhs)
	{
		return lhs > rhs;
	}
};

//creaza coada cu prioritati
priority_queue<pair<int, int>, vector<pair<int, int>>, CustomCompare> make_queue(vector<int>& d, int& root) {
	priority_queue<pair<int, int>, vector<pair<int, int>>, CustomCompare> q;
	for (int i = 0; i < d.size();i++) {
		//imi un nod daca:
		// - gradul sau e difierit de 0
		// - nodul nu e startul
		if (i+1!=root && d.at(i)!=0) q.push(make_pair(d.at(i),i+1));//gradul nodului i + nodul i
	}
	return q;
}

//cauta tatal unui nod
int find_father(vector<pair<int, int>>& legatura, int& son) {
	for (int i = 0; i < legatura.size(); i++) 
		if (legatura.at(i).second == son) 
			return legatura.at(i).first;

}

//Codificare
vector <int> codare_Prufer(priority_queue<pair<int, int>, vector<pair<int, int>>, CustomCompare> &q, vector<pair<int, int>>& legatura, vector<int>& d, int &root) {
	vector <int> K;
	int son, father;
	q=make_queue(d, root);
	while (!q.empty()) {
		son = q.top().second;
		father = find_father(legatura, son);
		d[father-1]--;
		d[son - 1]--;
		K.push_back(father);
		q=make_queue(d, root);
	}
	return K;
}

//cauta cel mai mic numar !=0 care nu se gaseste in vector
int cel_mai_mic(vector<int>& K, int &n) {
	int min = 1;
	while (min <= n) {
		auto it = find(K.begin(), K.end(), min);
		if (it == K.end()) return min;
		else min++;
	}
}

//Decodificare
vector <pair<int, int>> decodare_Prufer(vector<int>& K, int n) {
	int x, y;
	vector <pair<int, int>> T;
	for (int i = 0; i < n-1; i++) {
		x = K.at(0);
		y = cel_mai_mic(K, n);
		T.push_back(make_pair(x,y));
		K.erase(K.begin());
		K.push_back(y);
	}
	return T;
}

int main()
{
	vector<pair<int, int>> legatura, T;
	vector<int> d, K;
	priority_queue<pair<int, int>, vector<pair<int, int>>, CustomCompare> q;
	int n = 1, root = 0;

	f.open("input.txt");
	read_from_file(legatura, n,root);
	degree(legatura, n, d);

	//codificare Pruffer
	K=codare_Prufer(q, legatura,d, root);
	cout << ">> Codificare Pruffer:" << endl;
	for (int i = 0; i < K.size(); i++) {
		cout << K.at(i) << " ";
	}
	cout << endl;

	//decodificare Pruffer
	cout << ">> Decodificare Pruffer:" << endl;
	
	//vector<int> dd = {2,3,2,1,6,1 };
	T = decodare_Prufer(K, n);
	for (int i = 0; i < T.size(); i++) {
		cout <<"("<< T.at(i).first << ","<< T.at(i).second<<")"<<endl;
	}

	f.close();
    return 0;
}

