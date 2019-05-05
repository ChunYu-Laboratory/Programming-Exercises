#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{
    int NM[2];
    for(int i = 0; i < 2; i++)
    {
        cin >> NM[i];
    }

    int N = NM[0], M = NM[1];

    int cluster[N][M];
    for(int i = 0; i < N; i++)
    {
        for(int j = 0; j < M; j++)
        {
            cin >> cluster[i][j];
        }
    }

    int max_num[N], temp[M];
    for(int i = 0; i < N; i++)
    {
        for(int j = 0; j < M; j++)
        {
            temp[j] = cluster[i][j];
        }

        reverse(temp, temp+M);
        max_num[i] = temp[0];
    }

    int S = 0;
    for(int i = 0; i < N; i++)
    {
        S += max_num[i];
    }
    cout << S << endl;

    vector<int> select_num;
    for(int i = 0; i < N; i++)
    {
        if(S % max_num[i] == 0)
        {
            select_num.push_back(max_num[i]);
        }
    }

    if(select_num.size() == 0)
    {
        cout << -1 << endl;
    }
    else
    {
        for(int i = 0; i < select_num.size(); i++)
        {
            if(i < select_num.size()-1)
            {
                cout << select_num[i] << " ";
            }
            else
            {
                cout << select_num[i];
            }
            
        }
    }

    cout << endl;
    system("pause");
}