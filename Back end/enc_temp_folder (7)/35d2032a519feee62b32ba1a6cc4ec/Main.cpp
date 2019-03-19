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
	
	//For loop for quick adding of edges 1-15
	for (int y = 0; y <= 14; y++) { //Cycle through Y dimension till 14th
		for (int x= 0; x <= 14; x++) { //Cycle through X dimension till 14th
			if (y == (x+1)) { //If next node is increment of current node
				array0[x][y] = { 1 }; //Mark adjacency
			}
		}
	}

	//Manually spec other edges
	array0[1][15] = { 1 };
	array0[15][14] = { 1 };
	array0[2][19] = { 1 };
	array0[19][20] = { 1 };
	array0[20][14] = { 1 };
	array0[2][16] = { 1 };
	array0[16][17] = { 1 };
	array0[17][18] = { 1 };
	array0[18][14] = { 1 };
	array0[12][22] = { 1 };
	array0[22][14] = { 1 };
	array0[11][23] = { 1 };
	array0[23][14] = { 1 };
	array0[9][21] = { 1 };
	array0[21][14] = { 1 };



	/////Display Matrix for reference
	cout << "    1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24\n";
	cout << "--------------------------------------------------------------------------\n";
	for (int y = 0; y <= 23; y++) {
		cout << y + 1 << " ";
		if ((y + 1) <= 9) {
			cout << " ";
		}
		cout << "|";
		for (int x = 0; x <= 23; x++) {
			cout << array0[x][y];
			cout << "  ";
		}
		cout << "\n";
	}

	int A = 0; //Number of arcs/edges
	for (int y = 0; y <= 23; y++) {
		for (int x = 0; x <= 23; x++) {
			if(array0[x][y] == 1)
			{
				A = (A + 1);
			}
		}
	}
	cout << "There are " << A << " arcs\n";
	
	int N = sizeof array0 / sizeof array0[0];
	cout << "There are " << N << " nodes\n";

	int S = A - N + 1;
	cout << "The cyclonic number is " << S << " \n";


		int V = 24;
	//void printSolution(int reach[][V]);
	// Prints transitive closure of graph[][] using Floyd Warshall algorithm 

		/* reach[][] will be the output matrix that will finally have the
		shortest distances between every pair of vertices */
		int reach[24][24] = {};
		int i, j, k;

		/* Initialize the solution matrix same as input graph matrix. Or
		we can say the initial values of shortest distances are based
		on shortest paths considering no intermediate vertex. */
		for (i = 0; i < V; i++)
			for (j = 0; j < V; j++)
				reach[i][j] = array0[i][j];

		/* Add all vertices one by one to the set of intermediate vertices.
		---> Before start of a iteration, we have reachability values for
		all pairs of vertices such that the reachability values
		consider only the vertices in set {0, 1, 2, .. k-1} as
		intermediate vertices.
		----> After the end of a iteration, vertex no. k is added to the
		set of intermediate vertices and the set becomes {0, 1, .. k} */
		for (k = 0; k < V; k++)
		{
			// Pick all vertices as source one by one 
			for (i = 0; i < V; i++)
			{
				// Pick all vertices as destination for the 
				// above picked source 
				for (j = 0; j < V; j++)
				{
					// If vertex k is on a path from i to j, 
					// then make sure that the value of reach[i][j] is 1 
					reach[i][j] = reach[i][j] || (reach[i][k] && reach[k][j]);
				}
			}
		}



		cout << "    1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24\n";
		cout << "--------------------------------------------------------------------------\n";
		for (int y = 0; y <= 23; y++) {
			cout << y + 1 << " ";
			if ((y + 1) <= 9) {
				cout << " ";
			}
			cout << "|";
			for (int x = 0; x <= 23; x++) {
				cout << reach[x][y];
				cout << "  ";
			}
			cout << "\n";
		}

	std::cin.get();
}
