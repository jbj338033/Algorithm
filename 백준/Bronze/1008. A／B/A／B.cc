#include <iostream>

using namespace std;

int main() {
    int a, b;

    cin >> a >> b;

    cout.precision(10);
    cout << a / (double) b;

    return 0;
}
