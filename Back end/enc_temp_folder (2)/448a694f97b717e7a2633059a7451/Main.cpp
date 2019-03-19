#include "Main.h"
#include <iostream>
using namespace std;

Main::Main()
{
}


Main::~Main()
{
}

int main(int argc, char *argv[])
{
	cout << "Adjacency Matrix for Process Map - Enteric Negative Screening (ENS) 1\n";


	int array0[24][24] = {};////Declare 2D array to match size of Process Chart and fill with 0s
	//Begin assigning 1's to 2D array. Start of adjacency matrix.
	//Will be hardcoding Process Map - Enteric Negative Screening (ENS) 1 for now
	//Hardocded for now. Something dynamic later?
	//Directed graphs so X=Start Node
	for (int x = 0; x <= 14; x++) {
		for (int y= 0; y <= 14; y++) {
			if (x == (y+1)) {
				array0[x][y] = { 1 };
			}
		}
	}

	array0[2][16] = { 1 };
	array0[16][15] = { 1 };
	array0[3][20] = { 1 };
	array0[20][21] = { 1 };
	array0[21][15] = { 1 };
	array0[3][17] = { 1 };
	array0[17][18] = { 1 };
	array0[18][19] = { 1 };
	array0[19][15] = { 1 };
	array0[13][23] = { 1 };
	array0[23][15] = { 1 };
	array0[12][24] = { 1 };
	array0[24][15] = { 1 };
	array0[10][22] = { 1 };
	array0[22][15] = { 1 };


	/////Display Matrix for reference
	cout << "    1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 10 11 12 13 14\n";
	cout << "--------------------------------------------------------------------------\n";
	for (int x = 0; x <= 23; x++) {
		cout << x + 1 << " ";
		if ((x + 1) <= 9) {
			cout << " ";
		}
		cout << "|";
		for (int y = 0; y <= 23; y++) {
			cout << array0[x][y];
			cout << "  ";
		}
		cout << "\n";
	}









	std::cin.get();
}
