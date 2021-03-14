#include <iostream>
#include <set>
#include <string>
#include <assert.h> 

using namespace std;

bool allUnique(string s) {
    string sSeen;
    for (auto const& e : s) { 
        if (sSeen.find(e) != std::string::npos) {
            return false;
        }
        else {
            sSeen += e;
        }
    }
    return true;
}

int main() {
    assert(allUnique("") == true);
    assert(allUnique(" ") == true);
    assert(allUnique("Hello, world!") == false);
    assert(allUnique("  ") == false);
    assert(allUnique("Python") == true);
    return 0;
}