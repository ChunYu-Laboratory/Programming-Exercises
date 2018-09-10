#include<iostream>
using namespace std;

int main()
{
	int N;
	cin>>N;
	
	int friend_index[N];
	
	for(int i=0;i<N;i++)
	{
		cin>>friend_index[i];
	}
	
	bool track[N];
	
	for(int i=0;i<N;i++)
	{
		track[i] = false;
	}
	
	int count = 0;
	
	for(int i=0;i<N;i++)
	{
		if(track[i]) continue;
		
		int next = i;
		
		while(not track[next])
		{
			track[next] = true;
			next = friend_index[next];
		}
		
		count++;
	}
	
	cout<<count<<endl;
}
