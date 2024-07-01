#include <iostream>

using namespace std;

int main() {
    int a, b;

    cin >> a >> b;

    cout << a * (b % 10) << "\n";
    cout << a * (b % 100 / 10) << "\n";
    cout << a * (b / 100) << "\n";
    cout << a * b;

    return 0;
}
