#include <iostream>
#include <vector>
#include <cstring>
using namespace std;

extern void print(string *args)
{
    cout << *args << endl;
}

int main(int argc, char const *argv[])
{
    string str = "this is a test line";
    cout << str << endl;
    cout << str.size() << endl;
    bool equals = str == "this is a test line";
    string str_add = "hello"s + "world"s;
    cout << str_add << endl;
    cout << equals << endl;
    for (auto x : str)
    {
        cout << x << endl;
    }
    vector<int> v1;
    v1.push_back(444);
    for(auto item : v1) {
        cout << item << endl;
    }
    cout << v1.size() << "," << v1.capacity()<< endl;

    const char * c_str = str.c_str();
    
    cout << strlen(c_str) << endl;
    return 0;
}
