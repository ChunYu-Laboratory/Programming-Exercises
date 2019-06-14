#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int main()
{
    string X;
    cin >> X;

    int sign = 1, Y = 0;
    for(int i = 0; i < X.size(); i++)
    {
        Y += sign*(X[i]-'0');
        sign = -sign;
    }

    cout << abs(Y) << endl;

    cout << endl;
    system("pause");
}