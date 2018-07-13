#include<iostream>
using namespace std;

int main()
{
	int abc[3];
	
	for(int i=0;i<3;i++) cin>>abc[i];
	
	int a=abc[0], b=abc[1], c=abc[2];
	
	if(a>0) a=1;
	if(b>0) b=1;
	
	bool impossible=true;
	if((a&b)==c){cout<<"AND"<<'\n'; impossible=false;}
	if((a|b)==c){cout<<"OR"<<'\n'; impossible=false;}
	if((a^b)==c){cout<<"XOR"<<'\n'; impossible=false;}
	if(impossible) cout<<"IMPOSSIBLE";
}
