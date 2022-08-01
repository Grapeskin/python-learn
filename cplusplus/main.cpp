#include <iostream>
using namespace std;

struct Person
{
    /* data */
    string name;
    int age;
    string address = "";
};

extern int func();
int main(int argc, char const *argv[])
{
    int int_var = 123;
    bool bool_var = 'a';
    int int_v1 = true;
    string list_var{"this is a test text"};
    std::cout << "int_var=" << int_var << endl;
    std::cout << "bool_var=" << bool_var << endl;
    std::cout << "int_v1=" << int_v1 << endl;
    std::cout << "list_var=" << list_var << endl;
    int &addr_int_var = int_var;
    std::cout << "addr_int_var=" << addr_int_var << endl;
    int *p = &int_var;
    std::cout << "p=" << p << endl;
    std::cout << "p_val=" << *p << endl;
    std::cout << "p=" << &int_var << endl;
    int *np = nullptr;
    // std::cout << "np=" << *np << endl;
    int *vp = &int_var;
    std::cout << "vp=" << *vp << endl;
    const int a = 12;
    std::cout << "a=" << a << endl;
    // 指针指向常量
    const int *ap = &a;
    std::cout << "ap=" << *ap << endl;
    ap = &int_var;
    std::cout << "ap=" << *ap << endl;
    // 指针是个常量指针
    int *const ptr = &int_var;
    std::cout << "ptr=" << *ptr << endl;

    int i = 12.178, &b = i;
    std::cout << "i=" << i << endl;

    decltype(func()) c = 9;
    std::cout << "c=" << c << endl;

    int x = 3, y = 4;
    decltype(x) z = x;
    decltype((y)) d = x;
    ++z;
    ++d;
    std::cout << "x=" << x << endl;
    std::cout << "y=" << y << endl;

    Person person;
    person.age = 111;
    person.name = "zhangsan";
    std::cout << "person=" << person.age << endl;
    return 0;
}

int func()
{
    return 12;
}