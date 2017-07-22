// Example program
#include <iostream>
#include <tuple>
#include <string>
#include <fstream>
#include <vector>

int maximum(int a, int b)
{
	if(a > b)
	{return a;}
	else 
	{return b;}
}
int maximum(int a, int b, int c)
{return maximum(maximum(a,b), c);}

int minimum(int a, int b)
{
	if(a < b)
	{return a;}
	else 
	{return b;}
}
int minimum(int a, int b, int c)
{return minimum(minimum(a,b), c);}

const int Bindex[24][24] = {{4, -1, -2, -2, 0, -1, -1, 0, -2, -1, -1, -1, -1, -2, -1, 1, 0, -3, -2, 0, -2, -1, 0, -4},
{-1, 5, 0, -2, -3, 1, 0, -2, 0, -3, -2, 2, -1, -3, -2, -1, -1, -3, -2, -3, -1, 0, -1, -4},
{-2, 0, 6, 1, -3, 0, 0, 0, 1, -3, -3, 0, -2, -3, -2, 1, 0, -4, -2, -3, 3, 0, -1, -4},
{-2, -2, 1, 6, -3, 0, 2, -1, -1, -3, -4, -1, -3, -3, -1, 0, -1, -4, -3, -3, 4, 1, -1, -4},
{0, -3, -3, -3, 9, -3, -4, -3, -3, -1, -1, -3, -1, -2, -3, -1, -1, -2, -2, -1, -3, -3, -2, -4},
{-1, 1, 0, 0, -3, 5, 2, -2, 0, -3, -2, 1, 0, -3, -1, 0, -1, -2, -1, -2, 0, 3, -1, -4},
{-1, 0, 0, 2, -4, 2, 5, -2, 0, -3, -3, 1, -2, -3, -1, 0, -1, -3, -2, -2, 1, 4, -1, -4},
{0, -2, 0, -1, -3, -2, -2, 6, -2, -4, -4, -2, -3, -3, -2, 0, -2, -2, -3, -3, -1, -2, -1, -4}, 
{-2, 0, 1, -1, -3, 0, 0, -2, 8, -3, -3, -1, -2, -1, -2, -1, -2, -2, 2, -3, 0, 0, -1, -4},
{-1, -3, -3, -3, -1, -3, -3, -4, -3, 4, 2, -3, 1, 0, -3, -2, -1, -3, -1, 3, -3, -3, -1, -4},
{-1, -2, -3, -4, -1, -2, -3, -4, -3, 2, 4, -2, 2, 0, -3, -2, -1, -2, -1, 1, -4, -3, -1, -4}, 
{-1, 2, 0, -1, -3, 1, 1, -2, -1, -3, -2, 5, -1, -3, -1, 0, -1, -3, -2, -2, 0, 1, -1, -4},
{-1, -1, -2, -3, -1, 0, -2, -3, -2, 1, 2, -1, 5, 0, -2, -1, -1, -1, -1, 1, -3, -1, -1, -4},
{-2, -3, -3, -3, -2, -3, -3, -3, -1, 0, 0, -3, 0, 6, -4, -2, -2, 1, 3, -1, -3, -3, -1, -4},
{-1, -2, -2, -1, -3, -1, -1, -2, -2, -3, -3, -1, -2, -4, 7, -1, -1, -4, -3, -2, -2, -1, -2, -4},
{1, -1, 1, 0, -1, 0, 0, 0, -1, -2, -2, 0, -1, -2, -1, 4, 1, -3, -2, -2, 0, 0, 0, -4},
{0, -1, 0, -1, -1, -1, -1, -2, -2, -1, -1, -1, -1, -2, -1, 1, 5, -2, -2, 0, -1, -1, 0, -4},
{-3, -3, -4, -4, -2, -2, -3, -2, -2, -3, -2, -3, -1, 1, -4, -3, -2, 11, 2, -3, -4, -3, -2, -4},
{-2, -2, -2, -3, -2, -1, -2, -3, 2, -1, -1, -2, -1, 3, -3, -2, -2, 2, 7, -1, -3, -2, -1, -4}, 
{0, -3, -3, -3, -1, -2, -2, -3, -3, 3, 1, -2, 1, -1, -2, -2, 0, -3, -1, 4, -3, -2, -1, -4}, 
{-2, -1, 3, 4, -3, 0, 1, -1, 0, -3, -4, 0, -3, -3, -2, 0, -1, -4, -3, -3, 4, 1, -1, -4},
{-1, 0, 0, 1, -3, 3, 4, -2, 0, -3, -3, 1, -1, -3, -1, 0, -1, -3, -2, -2, 1, 4, -1, -4},
{0, -1, -1, -1, -2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -2, 0, 0, -2, -1, -1, -1, -1, -1, -4},
{-4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, 1}};

char vx[24] = {'A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V', 'B', 'Z', 'X', '-'};
char wx[24] = {'A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V', 'B', 'Z', 'X', '-'};

int DeltaBLOSUM(char i, char j)
{
	//std::cout << "using blosum!" << std::endl;
	int f_v = 23;
	int f_w = 23;
	
	for(int y=0; y<24; y++)
	{
		if(toupper(i)== vx[y])
		{
			f_v = y;
			break;
		}
	}
	for(int x=0; x<24; x++)
	{
		if(toupper(j)== wx[x])
		{
			f_w = x;
			break;
		}
	}
	//tstd::cout << f_v << " " << f_w << std::endl;
	return Bindex[f_v][f_w];
}

void shortPrintAlignment(std::string v,std::string w, std::vector<std::vector<int>> path)
{
	int offset = 60;
	const std::string V = '-' + v;
	const std::string W = '-' + w;
	std::string top = ""; //W
	std::string middle = ""; //relationship
	std::string btm = ""; //V
	std::vector<int> v1;
	v1.push_back(0);
	v1.push_back(1);
	std::vector<int> v2;
	v2.push_back(1);
	v2.push_back(0);
	if(path[1] == v1) //moved down. gap in W
	{
		top = top + "-";
		middle = middle + " ";
		btm = btm + V[path[0][1]];
	}
	else if( path[1] == v2 ) //moved left, gap in V
	{
		top = top + W[path[0][0]];
		middle = middle + " ";
		btm = btm + "-";
	}
	else //moved diagonal, match or mismatch
	{
		top = top + W[path[0][0]];
		if(W[path[0][0]]==V[path[0][1]])
		{
			middle = middle + "|";
		}
		else
		{
			middle = middle + "*";
		}
		btm = btm + V[path[0][1]];
	}	
	for (size_t i=1; i<path.size(); i++)
	{
		if(i%offset == 0)
		{
			std::cout << top << std::endl << middle << std::endl << btm << std::endl << std::endl;
			top = "";
			middle = "";
			btm = "";
		}
		if(path[i][0]==path[i-1][0]) //we didn't move left.
		{ 
			top = top + "-";
			middle = middle + " ";
			btm = btm + V[path[i][1]];
		}
		else if(path[i][1]==path[i-1][1]) //we didn't move down
		{
			top = top + W[path[i][0]];
			middle = middle + " ";
			btm = btm + "-";
		}
		else //we moved diagonally
		{
			top = top + W[path[i][0]];
			if(W[path[i][0]]==V[path[i][1]])
			{
				middle = middle + "|";
			}
			else
			{
				middle = middle + "*";
			}
			btm = btm + V[path[i][1]];
		}
		if(i == path.size()-1)
		{
			std::cout << top << std::endl << middle << std::endl << btm;
		}
	}
	std::cout << std::endl << std::endl;
}


std::vector<std::vector<int>> bRecBacktrace(std::vector<std::vector<int>> s, std::string v, std::string w, std::vector<std::vector<char>> b, int x, int y, std::vector<std::vector<int>> CPath={})
{
	std::string V = ' ' + v;
	std::string W = ' ' + w;
	std::vector<std::vector<int>> pathList = CPath; //we will append the current position to this
	pathList.insert(pathList.begin(),{x,y});
	if(x==0 && y==0)
	{
		return pathList;
	}
	else if(x==0)
	{	
		if(b[y][x] == '|')		//did we come from above?
		{pathList = bRecBacktrace(s, v, w, b, x, y-1, pathList);}
		else
			std::cout << "error: cannot traceback above" << std::endl;
		if(b[y][x] == '\\')	//did we come diagonally?
		{pathList = bRecBacktrace(s, v, w, b, x-1, y-1, pathList);}
	}
	else if(y==0)
	{
		if(b[y][x] == '-')		//did we come from the left?
		{pathList = bRecBacktrace(s, v, w, b, x-1, y, pathList);}
		else
			std::cout << "error: cannot traceback left" << std::endl;
		if(b[y][x] == '\\')	    //did we come diagonally?
		{pathList =  bRecBacktrace(s, v, w, b, x-1, y-1, pathList);}
	}
	else if(y<1 || x<1)
	{
		std::cout << "error: unidentified traceback error" << std::endl;
	}
	else
	{
		if(b[y][x] == '|')		//did we come from above?
		{pathList = bRecBacktrace(s, v, w, b, x, y-1, pathList);}
		if(b[y][x] == '-')	    //did we come from the left?
		{pathList = bRecBacktrace(s, v, w, b, x-1, y, pathList);}		
		if(b[y][x] == '\\')	    //did we come diagonally?
		{pathList = bRecBacktrace(s, v, w, b, x-1, y-1, pathList);}
	}
	return pathList;
}

void print_vi_vector(std::vector<std::vector<int> > x)
{
	//std::cout << "target_addresses: ";
	for(size_t i=0; i<x.size(); i++)
	{
		std::cout << "{";
		for(size_t j=0; j<x[i].size(); j++)
		{
			std::cout << x[i][j] << ", ";
		}
		std::cout << "}" << "\n";   
	}
	std::cout << "\n";
	//std::cout << "test6" << std::endl;
}

void print_vs_vector(std::vector<std::vector<char> > x)
{
	for(size_t i=0; i<x.size(); i++)
	{
		std::cout << "{";
		for(size_t j=0; j<x[i].size(); j++)
		{
			std::cout << x[i][j] << ", ";
		}
		std::cout << "}" << "\n";   
	}
	std::cout << "\n";
}

std::vector<std::vector<int>> twoVector(int n, int m)
{
	std::vector<std::vector<int>> f_grid(n, std::vector<int>(m, 0));
	return f_grid;
}

std::vector<std::vector<int>> localAlignment(std::string y, std::string x)
{
	const std::string V = " " + y;
	const std::string W = " " + x;
	std::vector<std::vector<int>> S(V.length(), std::vector<int>(W.length(), 0));
	std::vector<std::vector<int>> L(V.length(), std::vector<int>(W.length(), 0));
	std::vector<std::vector<int>> U(V.length(), std::vector<int>(W.length(), 0));
	std::vector<std::vector<char>> B(V.length(), std::vector<char>(W.length(), ' '));
	const int a = 1;
	const int p = 11;
	//std::cout << "test1" << std::endl;
	for (size_t i=0; i< V.length(); i++) //horizontal
	{
		//std::cout << "test2" << std::endl;
		//S[y,x];
		for (size_t j=0; j< W.length(); j++) //vertical
		{
			if(i==0 && j==0)
			{
				//std::cout << "test3a1" << ", i: " << i << ", j: "<< j << " " << W.length() <<std::endl;
				L[i][j] = 0;
				U[i][j] = 0;
				S[i][j] = 0;
				B[i][j] = ' ';
				//std::cout << "test3a2" << ", i: " << i << ", j: "<< j << " " << W.length() << std::endl;
			}
			else if(j==0) //cannot use [i-1][j]
			{
				//std::cout << "test3b1" << ", i: " << i << ", j: "<< j << " " << W.length() << std::endl;
				L[i][j] = 0;
				U[i][j] = maximum((U[i-1][j] - a), (S[i-1][j]-(p+a)));
				S[i][j] = U[i][j];
				B[i][j] = '|';
				//std::cout << "test3b2" << ", i: " << i << ", j: "<< j << " " << W.length() << std::endl;
			}
			else if(i==0) //cannot use [i][j-1]
			{
				//std::cout << "test3c1" << ", i: " << i << ", j: "<< j << " " << W.length() << std::endl;
				L[i][j] = maximum((L[i][j-1] - a), (S[i][j-1]-(p+a)));
				U[i][j] = 0;
				S[i][j] = L[i][j];
				B[i][j] = '-';
				//std::cout << "test3c2" << ", i: " << i << ", j: "<< j << " " << W.length() << std::endl;
			}
			else
			{	
				//std::cout << "test3d1" << ", i: " << i << ", j: "<< j << " " << W.length() << std::endl;
				//lower level. horizontal edges		gaps in w
				L[i][j] = maximum((L[i][j-1] - a), (S[i][j-1]-(p+a)));
				//upper level. vertical edges		gaps in v
				U[i][j] = maximum((U[i-1][j] - a), (S[i-1][j]-(p+a)));
				//main level. diagonal edges			matches/mismatches
				S[i][j] = maximum((S[i-1][j-1] + DeltaBLOSUM(V[i], W[j])), U[i][j], L[i][j]);
				//std::cout << "test6" << std::endl;
				if(S[i][j] == L[i][j])
				{B[i][j] = '-';}
				if(S[i][j] == U[i][j])
				{B[i][j] = '|';}
				if(S[i][j] == (S[i-1][j-1] + DeltaBLOSUM(V[i], W[j])))
				{B[i][j] = '\\';}
				//std::cout << "test3d2" << ", i: " << i << ", j: "<< j << " " << W.length() << std::endl;
			}
			//std::cout << "test5" << std::endl;
		}
		//std::cout << "test4" << std::endl;
	}
	//std::cout << "test6" << std::endl;
	std::vector<std::vector<int>> ourPaths = bRecBacktrace(S, y, x, B, x.length(), y.length());
	if(ourPaths.size() > 0)
	{ourPaths.erase(ourPaths.begin());}
	//print_vi_vector(ourPaths);
	shortPrintAlignment(y, x, ourPaths);
	
	return S;
}

std::vector<std::vector<int>> globalAlignment(std::string word1, std::string word2)
{
	const std::string V = " " + word1;
	const std::string W = " " + word2;
	std::vector<std::vector<int>> S(V.length(), std::vector<int>(W.length(), 0));
	std::vector<std::vector<int>> L(V.length(), std::vector<int>(W.length(), 0));
	std::vector<std::vector<int>> U(V.length(), std::vector<int>(W.length(), 0));
	std::vector<std::vector<int>> F(V.length(), std::vector<int>(W.length(), 0));
	std::vector<std::vector<char>> B(V.length(), std::vector<char>(W.length(), ' '));
	const int a = 1;
	const int p = 11;
	//k is constant. we'll make it 3 for no particular reason.
	unsigned int k = 3;
	//std::cout << "test4" << std::endl;
	if(word2.length() > word1.length())
	{
		k = k + (word2.length() - word1.length());
	}
	else if(word2.length() < word1.length())
	{
		k = k + (word1.length() - word2.length());
	}
	unsigned const int N = word1.length();
	unsigned const int M = word2.length();
	//d is another constant chosen arbitrarily
	const int d = 2;
	//std::cout << "test5" << std::endl;
	//for point [0][0]
	L[0][0] = 0;
	U[0][0] = 0;
	S[0][0] = 0;
	B[0][0] = ' ';
	F[0][0] = 0;
	//std::cout << "test60" << std::endl;
	for (size_t i=1; i< k+1; i++)
	{
		//std::cout << "test61" << std::endl;
		//std::cout << "test61 " << word1 << L.size() << std::endl;
		//std::cout << "test71" << i << std::endl;
		L[i][0] = 0;
		//std::cout << "test71" << std::endl;
		U[i][0] = maximum((U[i-1][0] - a), (S[i-1][0]-(p+a)));
		//std::cout << "test72" << std::endl;
		S[i][0] = U[i][0];
		//std::cout << "test73" << std::endl;
		B[i][0] = '|';
		//std::cout << "test74" << std::endl;
		F[i][0] = 0; //I have no idea what number these should be initialized to
		//std::cout << "test61a" << std::endl;
	}
	//std::cout << "test62a" << std::endl;
	for (size_t j=1; j< k+1; j++)
	{
		//std::cout << "test62" << std::endl;
		L[0][j] = maximum((L[0][j-1] - a), (S[0][j-1]-(p+a)));
		U[0][j] = 0;
		S[0][j] = L[0][j];
		B[0][j] = '-';
		F[0][j] = 0; //I have no idea what number these should be initialized to
		//std::cout << "test63" << std::endl;
	}
	for (size_t i=1; i< N+1; i++)
	{
		//std::cout << "test10" << std::endl;
		for (size_t j=maximum(1,i-k); j< minimum(M,i+k)+1; j++)
		{
			if((j-i)==k) //cannot use [i-1][j]
			{
				L[i][j] = maximum((L[i][j-1] - a), (S[i][j-1]-(p+a)));	
				U[i][j] = 0;
				S[i][j] = maximum((S[i-1][j-1] + DeltaBLOSUM(V[i], W[j])), L[i][j]);
				if(S[i][j] == (S[i-1][j-1] + DeltaBLOSUM(V[i], W[j])))
				{B[i][j] = ('\\');}
				else if(S[i][j] == L[i][j])
				{B[i][j] = '-';}
				else
				{std::cout << "error: cannot determine backtracing direction1" << std::endl;}
			}
			else if((i-j)==k) //cannot use [i][j-1]
			{
				L[i][j] = 0;
				U[i][j] = maximum((U[i-1][j] - a), (S[i-1][j]-(p+a)));
				S[i][j] = maximum((S[i-1][j-1] + DeltaBLOSUM(V[i], W[j])), U[i][j]);
				if(S[i][j] == (S[i-1][j-1] + DeltaBLOSUM(V[i], W[j])))
					B[i][j] = ('\\');
				else if(S[i][j] == U[i][j])
				{B[i][j] = '|';}
				else
				{std::cout << "error: cannot determine backtracing direction2" << std::endl;}
			}	
			else //we're assuming this is inside the band
			{
				L[i][j] = maximum((L[i][j-1] - a), (S[i][j-1]-(p+a)));
				U[i][j] = maximum((U[i-1][j] - a), (S[i-1][j]-(p+a)));
				S[i][j] = maximum((S[i-1][j-1] + DeltaBLOSUM(V[i], W[j])), U[i][j], L[i][j]);
				if(S[i][j] == L[i][j])
				{B[i][j] = '-';}
				else if(S[i][j] == U[i][j])
				{B[i][j] = '|';}
				else if(S[i][j] == (S[i-1][j-1] + DeltaBLOSUM(V[i], W[j])))
				{B[i][j] = '\\';}
				else
				{std::cout << "error: cannot determine backtracing direction3  " << i << ", " << j << ", " << S[i][j] << ", " << L[i][j] << ", " << U[i][j] << ", "<< std::endl;}
			}	 
			if((i-j)>k)
			{F[i][j] = maximum((F[i][j-1]-d),(F[i-1][j-1] + S[i][j]));}
			else if((j-i)>k)
			{F[i][j] = maximum((F[i-1][j]-d),(F[i-1][j-1] + S[i][j]));}
			else
			{F[i][j] = (F[i-1][j-1] + S[i][j]);}
			//std::cout << "test30" << std::endl;
		}
		//std::cout << "test40" << std::endl;
	}
	//std::cout << "test6" << std::endl;
	std::vector<std::vector<int>> ourPaths = bRecBacktrace(S, word1, word2, B, word2.length(), word1.length());
	//std::cout << "test7" << std::endl;
	if(ourPaths.size() > 0)
	{ourPaths.erase(ourPaths.begin());}
	//std::cout << "test8" << std::endl;
	//print_vi_vector(ourPaths);
	shortPrintAlignment(word1, word2, ourPaths);
	return (S);
}

void alignmentProcess(std::string word1, std::string word2)
{
	std::cout << "Using Local Alignment: " << std::endl;
	std::vector<std::vector<int>> grid1 = localAlignment(word1, word2);
	
	std::cout << "Using Banded Global Alignment: " << std::endl;
	std::vector<std::vector<int>> grid2 = globalAlignment(word1, word2);
}

std::string proteinFromFile(std::string filename)
{
	std::string sequence = "";
	std::ifstream file (filename);
	if (file.is_open())
	{
		std::string line;
		getline(file, line);
		line = "";
		while(getline(file, line, '\n'))
		{
			sequence = sequence + line;
		}
	}
	file.close();
	return sequence;
}

int main ( int argc, char *argv[] )
{
	std::string s1;
	std::string s2;
	if(argc > 2)
	{
		s1 = proteinFromFile(argv[1]);
		s2 = proteinFromFile(argv[2]);
	}
	else
	{
		std::cout << "No file given. Using sample protein sequences." << std::endl;
		s1 = "MVLSPADKTNVKAAWGKVGAHAGEYGAEALERMFLSFPTTKTYFPHFDLSHGSAQVKGHGKKVADALTNAVAHVDDMPNALSALSDLHAHKLRVDPVNFKLLSHCLLVTLAAHLPAEFTPAVHASLDKFLASVSTVLTSKYR";
		s2 = "MVLSGEDKSNIKAAWGKIGGHGAEYGAEALERMFASFPTTKTYFPHFDVSHGSAQVKGHGKKVADALASAAGHLDDLPGALSALSDLHAHKLRVDPVNFKLLSHCLLVTLASHHPADFTPAVHASLDKFLASVSTVLTSKYR";
	}

	alignmentProcess(s1, s2);
	//print_vi_vector(myGrid);
	//shortPrintAlignment("hello", "there", std::get<1>(myGrid));
}
