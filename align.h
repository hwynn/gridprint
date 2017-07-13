// Example program
#include <iostream>
#include <tuple>
#include <string>
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

std::tuple<int, int> f(int a, int b, int c) //returns (sum, max) of three ints
{
    int x = a + b + c;
    int y = a;
    y = maximum(y, b);
    y = maximum(y, c);
    return std::make_tuple(x, y);
}

int DeltaBLOSUM(char i, char j)
{
    return 3;
}

std::vector<std::vector<int>> grid(std::string y, std::string x)
{
    const std::string V = ' ' + y;
    const std::string W = ' ' + x;
    std::vector<std::vector<int>> S(V.length(), std::vector<int>(W.length(), 0));
    std::vector<std::vector<int>> L(V.length(), std::vector<int>(W.length(), 0));
    std::vector<std::vector<int>> U(V.length(), std::vector<int>(W.length(), 0));
    std::vector<std::vector<char>> B(V.length(), std::vector<char>(W.length(), ' '));
    const int a = 1;
    const int p = 11;
    for (size_t i=0; i < V.length(); i++) //horizontal
    {
		//S[y,x];
		for (size_t j=0; j < W.length(); j++) //vertical
		{
			if(i==0 && j==0)
			{
				L[i][j] = 0;
				U[i][j] = 0;
				S[i][j] = 0;
				B[i][j] = ' ';
			}
			else if(j==0) //cannot use [i-1][j]
			{
				L[i][j] = 0;
				U[i][j] = maximum((U[i-1][j] - a), (S[i-1][j]-(p+a)));
				S[i][j] = U[i][j];
				B[i][j] = '|';
            }
			else if(i==0) //cannot use [i][j-1]
			{
				L[i][j] = maximum((L[i][j-1] - a), (S[i][j-1]-(p+a)));
				U[i][j] = 0;
				S[i][j] = L[i][j];
				B[i][j] = '-';
			}
			else
			{	
			    //lower level. horizontal edges		gaps in w
				L[i][j] = maximum((L[i][j-1] - a), (S[i][j-1]-(p+a)));
				//upper level. vertical edges		gaps in v
				U[i][j] = maximum((U[i-1][j] - a), (S[i-1][j]-(p+a)));
				//main level. diagonal edges			matches/mismatches
				S[i][j] = maximum((S[i-1][j-1] + DeltaBLOSUM(V[i], W[j])), U[i][j], L[i][j]);
				
				if(S[i][j] == L[i][j])
					{B[i][j] = '-';}
				if(S[i][j] == U[i][j])
					{B[i][j] = '|';}
				if(S[i][j] == (S[i-1][j-1] + DeltaBLOSUM(V[i], W[j])))
					{B[i][j] = '\\';}
		    }
		}
    }
    return S;
}

std::vector<int> passVector(int n)
{
    std::vector<int> f_vector(n, 0);
    return f_vector;
}

std::vector<std::vector<int>> twoVector(int n, int m)
{
    //std::vector<int> f_vector(m, 0);
    std::vector<std::vector<int>> f_grid(n, std::vector<int>(m, 0));
    return f_grid;
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
}



int main()
{
  std::string s1 = "MVLSPADKTNVKAAWGKVGAHAGEYGAEALERMFLSFPTTKTYFPHFDLSHGSAQVKGHGKKVADALTNA";
  std::string s2 = "MVLSGEDKSNIKAAWGKIGGHGAEYGAEALERMFASFPTTKTYFPHFDVSHGSAQVKGHGKKVADALASA";
  auto t = f(1, 2, 3);

  std::vector<std::vector<int>> dumb = grid("hello","there");
  std::cout << std::get<0>(t) << std::endl;
  std::cout << std::get<1>(t) << std::endl;
  print_vi_vector(dumb);
  
  std::vector<int> myVector1 = passVector(5);
  for (std::vector<int>::iterator it = myVector1.begin(); it != myVector1.end(); ++it)
    std::cout << ' ' << *it;
  std::cout << '\n';
  std::vector<std::vector<int>> myVector2 = twoVector(5, 3);
  print_vi_vector(myVector2);
}