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
	cout << "Start\n";


	int array0[24][24] = {};////Declare 2D array to match size of Process Chart and fill with 0s
	//Begin assigning 1's to 2D array. Start of adjacency matrix.
	//Will be hardcoding Process Map - Enteric Negative Screening (ENS) 1 for now
	//Hardocded for now. Something dynamic later?
	cout << "  1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4\n";

	int x=0, y=0;
	for (x = 0; x <= 23; x++) {
		cout << x << " ";
		for (y= 0; y <= 23; y++) {
			array0[x][y] = { 1 };
			cout << array0[x][y];
			cout <<" ";
		}
		cout << "\n";

	}









	std::cin.get();
}