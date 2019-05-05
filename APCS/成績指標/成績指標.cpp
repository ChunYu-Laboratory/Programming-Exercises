#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main()
{
    int num;
    cin>>num;

    int score[num];
    for(int i=0;i<num;i++)
    {
        cin>>score[i];
    }

    sort(score, score+num);

    for(int i=0;i<num;i++)
    {
        if(i<num-1)
        {
            cout<<score[i]<<" ";
        }
        else
        {
            cout<<score[i];
        }
    }

    cout<<endl;

    vector<int> f;
    vector<int> p;

    for(int i=0;i<num;i++)
    {
        if(score[i]<60)
        {
            f.push_back(score[i]);
        }
        else
        {
            p.push_back(score[i]);
        }
        
    }

    reverse(f.begin(), f.end());
    sort(p.begin(), p.end());

    if(f.size()==0)
    {
        cout<<"best case"<<endl;
    }
    else
    {
        cout<<f[0]<<endl;
    }
    if(p.size()==0)
    {
        cout<<"worst case"<<endl;
    }
    else
    {
        cout<<p[0]<<endl;
    }
    
    cout<<endl;
    system("pause");
}