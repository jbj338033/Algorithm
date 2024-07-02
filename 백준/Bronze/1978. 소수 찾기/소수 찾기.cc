#include <iostream>

#define ll long long

using namespace std;

bool isPrime(int n) {
    if (n == 1) return false;
    
    for (int i = 2; i < n / 2 + 1; i++) {
        if (n % i == 0) {
            return false;
        }
    }

    return true;
}

int main() {
    int n;

    cin >> n;

    int count = 0;

    for (int i = 0; i < n; i++) {
        int a;

        cin >> a;

        if (isPrime(a)) {
            count += 1;
        }
    }

    cout << count;

    return 0;
}
