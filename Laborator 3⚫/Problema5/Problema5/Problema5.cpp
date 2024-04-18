// Problema5.cpp : Defines the entry point for the console application.
//
#include<iostream>
#include<fstream>
using namespace std;
ifstream file;

//citire matricea de adiacenta
void citire(int &n, int a[30][30]) {
	int i, j;
	file >> n;
	for (i = 0; i < n; i++)
		for (j = 0; j < n; j++)
			file >> a[i][j];
}

//algoritumul de determinare a numarului de drumuri
void Floyd_Warshall(int n, int a[30][30]) {
	int k, i, j;
	for (k = 0; k < n; k++)
		for (i = 0; i < n; i++)
			for (j = 0; j < n; j++)
				a[i][j] = a[i][j] + a[i][k] * a[k][j];
}

void afisare(int n, int a[30][30]) {
	int i,j;
	for (i = 0; i < n; i++) {
		cout << "Numar drumuri:" << endl;
		for (j = 0; j < n; j++)
			cout <<i+1<<"-"<< j + 1 << ": " << a[i][j] <<",  ";
		cout << endl;
	}

}

int main()
{
	int n, a[30][30];
	file.open("input.txt");
	citire(n, a);
	Floyd_Warshall(n, a);
	afisare(n, a);
	file.close();
    return 0;
}