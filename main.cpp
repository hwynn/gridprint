// Example program
#include <iostream>
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
	return Bindex[f_v][f_w];
}

void shortPrintAlignment(std::string v,std::string w, std::vector<std::vector<int> > path)
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

std::vector<std::vector<int> > bRecBacktrace(std::vector<std::vector<int> > s, std::string v, std::string w, std::vector<std::vector<char> > bs, std::vector<std::vector<char> > bu, std::vector<std::vector<char> > bl, int x, int y, char mode, std::vector<std::vector<int> > CPath={})
{
	std::string V = ' ' + v;
	std::string W = ' ' + w;
	//we will append the current position to this
	std::vector<std::vector<int> > pathList = CPath;
	pathList.insert(pathList.begin(),{x,y});
	if(mode=='s')
	{
		if(x==0 && y==0)
		{return pathList;
		}
		else if(x==0)
		{
			//did we come from above?
			if(bs[y][x] == '|')
			{pathList = bRecBacktrace(s, v, w, bs, bu, bl, x, y-1, 'u', pathList);}
			else
			{std::cout << "error: cannot traceback above" << std::endl;}
			//did we come diagonally?
			if(bs[y][x] == '\\')
			{pathList = bRecBacktrace(s, v, w, bs, bu, bl, x-1, y-1, 's', pathList);}
		}
		else if(y==0)
		{
			//did we come from the left?
			if(bs[y][x] == '-')
			{pathList = bRecBacktrace(s, v, w, bs, bu, bl, x-1, y, 'l', pathList);}
			else
			{std::cout << "error: cannot traceback left" << std::endl;}
			//did we come diagonally?
			if(bs[y][x] == '\\')
			{pathList = bRecBacktrace(s, v, w, bs, bu, bl, x-1, y-1, 's', pathList);}
		}
		else if(y<1 || x<1)
		{std::cout << "error: unidentified traceback error" << std::endl;}
		else
		{
			//did we come from above?
			if(bs[y][x] == '|')
			{pathList = bRecBacktrace(s, v, w, bs, bu, bl, x, y-1, 'u', pathList);}
			//did we come from the left?
			if(bs[y][x] == '-')
			{pathList = bRecBacktrace(s, v, w, bs, bu, bl, x-1, y, 'l', pathList);}
			//did we come diagonally?
			if(bs[y][x] == '\\')
			{pathList = bRecBacktrace(s, v, w, bs, bu, bl, x-1, y-1, 's', pathList);}
			if(bs[y][x] == ' ')
			{std::cout << "error: blank cell in traceback(s);" << x << " " << y << std::endl;}
		}
	}
	else if(mode=='l')
	{
		if(x==0 && y==0)
		{return pathList;}
		else if(x==0)
		{
			//did we come from above?
			if(bl[y][x] == '|')
			{
				std::cout << "error: this shouldn't happen" << std::endl;
				pathList = bRecBacktrace(s, v, w, bs, bu, bl, x, y-1, 'u', pathList);
			}
			else
			{std::cout << "error: cannot traceback above" << std::endl;}
			//did we come diagonally?
			if(bl[y][x] == '\\')
			{pathList = bRecBacktrace(s, v, w, bs, bu, bl, x-1, y-1, 's', pathList);}
		}
		else if(y==0)
		{
			//did we come from the left?
			if(bl[y][x] == '-')
			{pathList = bRecBacktrace(s, v, w, bs, bu, bl, x-1, y, 'l', pathList);}
			else
			{std::cout << "error: cannot traceback left" << std::endl;}
			//did we come diagonally?
			if(bl[y][x] == '\\')
			{pathList = bRecBacktrace(s, v, w, bs, bu, bl, x-1, y-1, 's', pathList);}
		}
		else if(y<1 || x<1)
		{std::cout << "error: unidentified traceback error" << std::endl;}
		else
		{
			//did we come from above?
			if(bl[y][x] == '|')
			{
				std::cout << "error: this shouldn't happen" << std::endl;
				pathList = bRecBacktrace(s, v, w, bs, bu, bl, x, y-1, 'u', pathList);
			}
			//did we come from the left?
			if(bl[y][x] == '-')
			{pathList = bRecBacktrace(s, v, w, bs, bu, bl, x-1, y, 'l', pathList);}
			//did we come diagonally?
			if(bl[y][x] == '\\')
			{pathList = bRecBacktrace(s, v, w, bs, bu, bl, x-1, y-1, 's', pathList);}
			if(bl[y][x] == ' ')
			{std::cout << "error: blank cell in traceback(l);" << x << " " << y << std::endl;}
		}
	}
	else if(mode=='u')
	{
		if(x==0 && y==0)
		{
			return pathList;
		}
		else if(x==0)
		{
			//did we come from above?
			if(bu[y][x] == '|')
			{pathList = bRecBacktrace(s, v, w, bs, bu, bl, x, y-1, 'u', pathList);}
			else
			{std::cout << "error: cannot traceback above" << std::endl;}
			//did we come diagonally?
			if(bu[y][x] == '\\')
			{pathList = bRecBacktrace(s, v, w, bs, bu, bl, x-1, y-1, 's', pathList);}
		}
		else if(y==0)
		{
			//did we come from the left?
			if(bu[y][x] == '-')
			{
				std::cout << "error: this shouldn't happen" << std::endl;
				pathList = bRecBacktrace(s, v, w, bs, bu, bl, x-1, y, 'l', pathList);
			}
			else
			{std::cout << "error: cannot traceback left" << std::endl;}
			//did we come diagonally?
			if(bu[y][x] == '\\')
			{pathList = bRecBacktrace(s, v, w, bs, bu, bl, x-1, y-1, 's', pathList);}
		}
		else if(y<1 || x<1)
		{std::cout << "error: unidentified traceback error" << std::endl;}
		else
		{
			//did we come from above?
			if(bu[y][x] == '|')
			{pathList = bRecBacktrace(s, v, w, bs, bu, bl, x, y-1, 'u', pathList);}
			//did we come from the left?
			if(bu[y][x] == '-')
			{	
				std::cout << "error: this shouldn't happen" << std::endl;
				pathList = bRecBacktrace(s, v, w, bs, bu, bl, x-1, y, 'l', pathList);
			}
			//did we come diagonally?
			if(bu[y][x] == '\\')
			{pathList = bRecBacktrace(s, v, w, bs, bu, bl, x-1, y-1, 's', pathList);}
			if(bu[y][x] == ' ')
			{std::cout << "error: blank cell in traceback(u);" << x << " " << y << std::endl;}
		}
	}
	return pathList;
}

void print_vi_vector(std::vector<std::vector<int> > x)
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

std::vector<std::vector<int> > twoVector(int n, int m)
{
	std::vector<std::vector<int> > f_grid(n, std::vector<int>(m, 0));
	return f_grid;
}

std::vector<std::vector<int> > localAlignment(std::string y, std::string x)
{
	const std::string V = " " + y;
	const std::string W = " " + x;
	std::vector<std::vector<int> > S(V.length(), std::vector<int>(W.length(), 0));
	std::vector<std::vector<int> > L(V.length(), std::vector<int>(W.length(), 0));
	std::vector<std::vector<int> > U(V.length(), std::vector<int>(W.length(), 0));
	std::vector<std::vector<char> > Bs(V.length(), std::vector<char>(W.length(), ' '));
	std::vector<std::vector<char> > Bl(V.length(), std::vector<char>(W.length(), ' '));
	std::vector<std::vector<char> > Bu(V.length(), std::vector<char>(W.length(), ' '));
	
	const int a = 1;
	const int p = 11;
	
	
	//horizontal
	for (size_t i=0; i< V.length(); i++)
	{
		//S[y,x];
		//vertical
		for (size_t j=0; j< W.length(); j++)
		{
			if(i==0 && j==0)
			{
				L[i][j]=0;
				U[i][j]=0;
				S[i][j]=0;
				Bl[i][j]=' ';
				Bu[i][j]=' ';
				Bs[i][j]=' ';
			}
			else if(i==0 || j==0)
			{
				if(j==0)
				{
					L[i][j]=0;
					Bl[i][j]=' ';
					if(i==1)
					{U[i][j] = (S[i-1][j]-(p+a));}
					else
					{U[i][j] = maximum((U[i-1][j] - a), (S[i-1][j]-(p+a)));}
					Bu[i][j] = '|';
					S[i][j]=U[i][j];
					Bs[i][j] = '|';
				}
				else if(i==0)
				{
					U[i][j]=0;
					Bu[i][j]=' ';
					if(j==1)
					{L[i][j] = (S[i][j-1]-(p+a));}
					else
					{L[i][j] = maximum((L[i][j-1] - a), (S[i][j-1]-(p+a)));}
					Bl[i][j]='-';
					S[i][j]=L[i][j];
					Bs[i][j] = '-';
				}
			}
			else 
			{
				//finding L
				if(Bl[i][j-1]==' ')
				{
					L[i][j] = (S[i-1][j-1] + DeltaBLOSUM(V[i], W[j]));
					Bl[i][j] ='\\';
				}
				else if(Bl[i][j-1]=='\\')
				{
					L[i][j] = (S[i][j-1]-(p+a));
					Bl[i][j] = '-';
				}
				else if(Bl[i][j-1]=='-')
				{
					L[i][j] = maximum((L[i][j-1] - a), (S[i][j-1]-(p+a)));
					Bl[i][j] = '-';
				}
				else
				{std::cout << "Error: no direction for l found" << std::endl;}
				//check if diagonal is good enough to change our minds;
				if(((S[i-1][j-1] + DeltaBLOSUM(V[i], W[j]))-L[i][j])>=12)
				{
					L[i][j] = (S[i-1][j-1] + DeltaBLOSUM(V[i], W[j]));
					Bl[i][j] = '\\';
				}
				//finding U
				if(Bu[i-1][j]==' ')
				{
					U[i][j] = (S[i-1][j-1] + DeltaBLOSUM(V[i], W[j]));
					Bu[i][j] = '\\';
				}
				else if(Bu[i-1][j]=='\\')
				{
					U[i][j] = (S[i-1][j]-(p+a));
					Bu[i][j] = '|';
				}
				else if(Bu[i-1][j]=='|')
				{
					U[i][j] = maximum((U[i-1][j] - a), (S[i-1][j]-(p+a)));
					Bu[i][j] = '|';
				}
				else
				{std::cout << "Error: no direction for u found" << std::endl;}
				//check if diagonal is good enough to change our minds;
				if(((S[i-1][j-1] + DeltaBLOSUM(V[i], W[j]))-U[i][j])>=12)
				{
					U[i][j] = (S[i-1][j-1] + DeltaBLOSUM(V[i], W[j]));
					Bu[i][j] = '\\';
				}
				if((i==(V.length()-1) && j!=(W.length()-1)) or (i!=(V.length()-1) && j==(W.length()-1)))
				{
					if(i==(V.length()-1))
					{
						U[i][j] = (S[i-1][j-1] + DeltaBLOSUM(V[i], W[j]));
						Bu[i][j] = '\\';
					}
					else if(j==(W.length()-1))
					{
						L[i][j] = (S[i-1][j-1] + DeltaBLOSUM(V[i], W[j]));
						Bl[i][j] ='\\';
					}
					else
					{std::cout << "Error: no direction for endzone found" << std::endl;}
				}
				S[i][j] = maximum((S[i-1][j-1] + DeltaBLOSUM(V[i], W[j])), U[i][j], L[i][j]);
				if(S[i][j] == L[i][j])
				{Bs[i][j] = '-';}
				if(S[i][j] == U[i][j])
				{Bs[i][j] = '|';}
				if(S[i][j] == (S[i-1][j-1] + DeltaBLOSUM(V[i], W[j])))
				{Bs[i][j] = '\\';}
			}
		}
	}
	std::vector<std::vector<int> > ourPaths = bRecBacktrace(S, y, x, Bs, Bu, Bl, x.length(), y.length(), 's');
	
	if(ourPaths.size() > 0)
	{ourPaths.erase(ourPaths.begin());}
	std::cout << "pathsize: " << ourPaths.size() << std::endl;
	//print_vi_vector(ourPaths);
	
	
	shortPrintAlignment(y, x, ourPaths);
	
	return (S);
}

std::vector<std::vector<int> > globalAlignment(std::string word1, std::string word2)
{
	const std::string V = " " + word1;
	const std::string W = " " + word2;
	std::vector<std::vector<int> > S(V.length(), std::vector<int>(W.length(), 0));
	std::vector<std::vector<int> > L(V.length(), std::vector<int>(W.length(), 0));
	std::vector<std::vector<int> > U(V.length(), std::vector<int>(W.length(), 0));
	std::vector<std::vector<char> > Bl(V.length(), std::vector<char>(W.length(), ' '));
	std::vector<std::vector<char> > Bu(V.length(), std::vector<char>(W.length(), ' '));
	std::vector<std::vector<char> > Bs(V.length(), std::vector<char>(W.length(), ' '));
	
	
	const int a = 1;
	const int p = 11;
	//k is constant. we'll make it 3 for no particular reason.
	unsigned int k = 20;
	if(word2.length() > word1.length())
	{k = k + (word2.length() - word1.length());}
	else if(word2.length() < word1.length())
	{k = k + (word1.length() - word2.length());}
	unsigned const int N = word1.length();
	unsigned const int M = word2.length();
	//for point [0][0]
	L[0][0] = 0;
	U[0][0] = 0;
	S[0][0] = 0;
	Bl[0][0] = ' ';
	Bu[0][0] = ' ';
	Bs[0][0] = ' ';
	for (size_t i=1; i< k+1; i++)
	{
		L[i][0]=0;
		Bl[i][0]=' ';
		if(i==1)
		{U[i][0] = (S[i-1][0]-(p+a));}
		else
		{U[i][0] = maximum((U[i-1][0] - a), (S[i-1][0]-(p+a)));}
		Bu[i][0] = '|';
		S[i][0]=U[i][0];
		Bs[i][0] = '|';
	}
	for (size_t j=1; j< k+1; j++)
	{
		U[0][j]=0;
		Bu[0][j]=' ';
		if(j==1)
		{L[0][j] = (S[0][j-1]-(p+a));}
		else
		{L[0][j] = maximum((L[0][j-1] - a), (S[0][j-1]-(p+a)));}
		Bl[0][j]='-';
		S[0][j]=L[0][j];
		Bs[0][j] = '-';
	}
	for (size_t i=1; i< N+1; i++)
	{
		for (size_t j=maximum(1,i-k); j< minimum(M,i+k)+1; j++)
		{
			//...
			if((j-i)==k) //cannot use [i-1][j]
			{
				U[i][j] = (S[i-1][j-1] + DeltaBLOSUM(V[i], W[j]));
				Bu[i][j] = '\\';
			}
			else
			{
				//finding U
				if(Bu[i-1][j]==' ')
				{
					U[i][j] = (S[i-1][j-1] + DeltaBLOSUM(V[i], W[j]));
					Bu[i][j] = '\\';
				}
				else if(Bu[i-1][j]=='\\')
				{
					U[i][j] = (S[i-1][j]-(p+a));
					Bu[i][j] = '|';
				}
				else if(Bu[i-1][j]=='|')
				{
					U[i][j] = maximum((U[i-1][j] - a), (S[i-1][j]-(p+a)));
					Bu[i][j] = '|';
				}
				else
				{std::cout << "Error: no direction for u found" << std::endl;}
				//check if diagonal is good enough to change our minds;
				if(((S[i-1][j-1] + DeltaBLOSUM(V[i], W[j]))-U[i][j])>=12)
				{	
					U[i][j] = (S[i-1][j-1] + DeltaBLOSUM(V[i], W[j]));
					Bu[i][j] = '\\';
				}
			}
			//...
			if((i-j)==k) //cannot use [i][j-1]
			{
				L[i][j] = (S[i-1][j-1] + DeltaBLOSUM(V[i], W[j]));
				Bl[i][j] ='\\';
			}
			else
			{
				//finding L
				if(Bl[i][j-1]==' ')
				{
					L[i][j] = (S[i-1][j-1] + DeltaBLOSUM(V[i], W[j]));
					Bl[i][j] ='\\';
				}
				else if(Bl[i][j-1]=='\\')
				{
					L[i][j] = (S[i][j-1]-(p+a));
					Bl[i][j] = '-';
				}
				else if(Bl[i][j-1]=='-')
				{
					L[i][j] = maximum((L[i][j-1] - a), (S[i][j-1]-(p+a)));
					Bl[i][j] = '-';
				}
				else
				{std::cout << "Error: no direction for l found" << std::endl;}
				//check if diagonal is good enough to change our minds;
				if(((S[i-1][j-1] + DeltaBLOSUM(V[i], W[j]))-L[i][j])>=12)
				{
					L[i][j] = (S[i-1][j-1] + DeltaBLOSUM(V[i], W[j]));
					Bl[i][j] = '\\';
				}
			}
			//are we on the edge of the grids?
			if((i==(V.length()-1) and j!=(W.length()-1)) or (i!=(V.length()-1) and j==(W.length()-1)))
			{
				if(i==(V.length()-1))
				{
					U[i][j] = (S[i-1][j-1] + DeltaBLOSUM(V[i], W[j]));
					Bu[i][j] = '\\';
				}
				else if(j==(W.length()-1))
				{
					L[i][j] = (S[i-1][j-1] + DeltaBLOSUM(V[i], W[j]));
					Bl[i][j] ='\\';
				}
				else
				{	
					std::cout << "Error: no direction for endzone found" << std::endl;
				}
			}
			S[i][j] = maximum((S[i-1][j-1] + DeltaBLOSUM(V[i], W[j])), U[i][j], L[i][j]);
			if(S[i][j] == L[i][j])
			{Bs[i][j] = '-';}
			if(S[i][j] == U[i][j])
			{Bs[i][j] = '|';}
			if(S[i][j] == (S[i-1][j-1] + DeltaBLOSUM(V[i], W[j])))
			{Bs[i][j] = '\\';}
		}
	}
	std::vector<std::vector<int> > ourPaths = bRecBacktrace(S, word1, word2, Bs, Bu, Bl,word2.length(),word1.length(), 's');
	if(ourPaths.size() > 0)
	{ourPaths.erase(ourPaths.begin());}
	//std::cout << "pathsize: " << ourPaths.size() << std::endl;
	//print_vi_vector(ourPaths);
	shortPrintAlignment(word1, word2, ourPaths);
	return (S);
}

void alignmentProcess(std::string word1, std::string word2)
{
	std::cout << "Using Local Alignment: " << std::endl;
	std::vector<std::vector<int> > grid1 = localAlignment(word1, word2);
	
	std::cout << "Using Banded Global Alignment: " << std::endl;
	std::vector<std::vector<int> > grid2 = globalAlignment(word1, word2);
}

std::string proteinFromFile(std::string filename)
{
	std::string sequence = "";
	std::ifstream file (filename);
	std::string line;
	if (file.is_open())
	{
		getline(file, line, '\r');
		for(size_t i=0; i<line.length(); i++) //checking to see if getline accidently picked up entire file
			if(line[i] == '\n')
			{
				sequence = line.substr(i, line.length());
				break;
			}
		line = "";
		while(getline(file, line, '\r'))
		{
			//std::cout << "line: " << line << std::endl;
			sequence.append(line);
			//std::cout << "sequence: " << sequence << std::endl;
		}
	}
	else
	{
		std::cout << "Error: file could not be opened" << sequence << std::endl;
	}
	file.close();
	for(size_t i=0; i<sequence.length(); i++)
		if(sequence[i] == ' ' || sequence[i] == '\n' || sequence[i] == '\r' || sequence[i] == '\t') sequence.erase(i,1);
	//std::cout << "sequence: " << sequence << std::endl;
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
		s1 = "LYFIFGAWAGLFGTGLSLLIRTELSQPGTLLGDDQIYNVVVTAHAFVMIFFMVMPIMIGGFGNWLVPLMIGAPDMAFPRMNNMSFWLLPPSFLLLLASAGVEAGAGTGWTVYPPLAGNLAHAGASVDLAIFSLHLAGISSILASINFITTIINMKPPAISQYQTPLFVWSILVTTVLLLLSLPVLAAGITMLLTDRNLNTTFFDPAGGGDPILYQHLFW";
		s2 = "LYLIFVAWAGMVGTGLSLLIRTELSQPGTLLGDDQIYNVVVTAHAFVMIFFMVMPIMIGGFGNWLVPLMIGAPDMAFPRMNNMSFWLLPPSFLLLLASAGVEAGAGTGWTVYPPLAGNLAHAGASVDLAIFSLHLAGISSILASINFITTIINMKPPAISQYQTPLFVWSILVTTILLLLSLPVLAAGITMLLTDRNWNTTFFDPAGGGDPILYQ";
	}
	alignmentProcess(s1, s2);
}
