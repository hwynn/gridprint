// Example program
#include <iostream>
#include <tuple>
#include <string>
#include <algorithm>    // std::max_element std::max std::find

std::tuple<int, int> f(int a, int b, int c) //returns (sum, max) of three ints
{
    int x = a + b + c;
    int y = a;
    y = std::max(y, b);
    y = std::max(y, c);
    return std::make_tuple(x, y);
}

int maximum(int a, int b)
{
    if(a > b)
        {return a;}
    else 
        {return b;}
}
int maximum(int a, int b, int c)
{return maximum(maximum(a,b), c);}



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
    //std::vector<int> f_vector(m, 0);
    std::vector<std::vector<int>> f_grid(n, std::vector<int>(m, 0));
    return f_grid;
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

std::tuple<std::vector<std::vector<int>>, std::vector<std::vector<int>>> grid(std::string y, std::string x)
{
    const std::string V = ' ' + y;
    const std::string W = ' ' + x;
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
    return std::make_tuple(S, ourPaths);
}


int main()
{
  auto t = f(1, 2, 3);
  std::cout << "hello3" << std::endl;
  std::tuple<std::vector<std::vector<int>>, std::vector<std::vector<int>>> myGrid = grid("hello", "there");
  //std::cout << std::get<0>(t) << std::endl;
  //std::cout << std::get<1>(t) << std::endl;
  //std::vector<std::vector<int>> grid1 = twoVector(3,4);
  std::cout << "hello4" << std::endl;
  print_vi_vector(std::get<0>(myGrid));
  
}

