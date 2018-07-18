#include<iostream>
#include<math.h>
#include<algorithm>
using namespace std;

int main()
{
	int input, side[3];
	
	for(int i=0;i<3;i++)
	{
		cin>>side[i];
	}
	
	sort(side,side+3);
	
	for(int i=0;i<3;i++)
	{
		cout<<side[i];
		if(i<2) cout<<" ";
	}
	
	cout<<'\n';
	
	int a=side[0], b=side[1], c=side[2];
	
	if(a+b<=c) cout<<"No";
	else if(pow(a,2)+pow(b,2)<pow(c,2)) cout<<"Obtuse";
	else if(pow(a,2)+pow(b,2)==pow(c,2)) cout<<"Right";
	else if(pow(a,2)+pow(b,2)>pow(c,2)) cout<<"Acute";
}
