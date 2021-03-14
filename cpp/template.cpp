#include <iostream>
#include <assert.h> 

using namespace std;

int functionName() {
    // ...
    return 0;
}

int main() {
    cout << "Hello, world!" << endl;
    assert(functionName() == 0);
    return 0;
}