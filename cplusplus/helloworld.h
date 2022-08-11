#include <iostream>
#include <vector>
#include <string>

using namespace std;
const double *f1(const double arr[], int n);
const double *f2(const double[], int);
const double *f3(const double *, int);

void fun1(int i, initializer_list<int> args, int j = 8);
void fun2(int n, double (*fp)(int num));
double calc(int num);
int count_add(int n);
bool s_is_empty(string &s);

class Student
{
public:
    Student();
    Student(string name, int age);
    ~Student()
    {
        cout << "执行析构函数" << endl;
    };

    string getName()
    {
        return (*this).name;
    }
    int getAge()
    {
        return (*this).age;
    }

private:
    string name;
    int age;
};
Student::Student()
{
    cout << "执行无参构造函数" << endl;
    name = "default_name";
    age = 999;
}
Student::Student(string n, int a) : name(n), age(a)
{

    cout << "执行有参构造函数" << endl;
    cout << name << ", " << age << endl;
    name = "wangwu";
    age = 66;
}