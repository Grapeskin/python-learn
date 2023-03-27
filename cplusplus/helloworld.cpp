
#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <memory>
#include <unordered_map>
#include <algorithm>
#include <random>
#include "helloworld.h"
using namespace std;

int main()
{
    vector<string> msg{"Hello", "C++", "World", "from", "VS Code", "and the C++ extension!"};
    // 1. 遍历vector容器
    // for (const string &word : msg)
    // {
    //     cout << word << " ";
    // }
    // cout << endl;
    // for (auto i = msg.begin(); i < msg.end(); i++)
    // {
    //     cout << *i << " ";
    // }
    // cout << endl;

    // 2. 初始化、遍历int类容器
    // vector<int> v(10, 1);
    // for (auto item : v)
    // {
    //     cout << item << " ";
    // }
    // cout << endl;

    // 3. 初始化、遍历string类容器
    // vector<string> v1{10, "hello"};
    // for (auto item : v1)
    // {
    //     cout << item << " ";
    // }
    // cout << endl;

    // 4. 位运算符
    // unsigned long stu = 0;
    // stu |= (1UL << 12);
    // cout << stu << endl;
    // int a[] = {1,
    //            2,
    //            3};
    // cout << "sizeof(a): " << sizeof(a) << "sizeof(*a): " << sizeof(*a) << endl;

    // 5. 标准库pair
    // pair<string, int> p;
    // p = {"key", 1};
    // cout << "first:" << p.first << ", second:" << p.second << endl;

    // 6. 异常处理
    // try
    // {
    //     int flag = 0;
    //     if (flag == 0)
    //     {
    //         throw runtime_error("accur error");
    //     }
    // }
    // catch (runtime_error e)
    // {
    //     std::cerr << "出错了" << e.what() << '\n';
    // }

    // 7. 测试变长参数
    // fun1(999, {1, 2});

    // 8. 测试函数指针
    // fun2(20, calc);
    // fun2(50, calc);

    // 9. 测试函数指针数组
    // double a[3] = {12.1, 3.4, 4.5};
    // const double *(*p1)(const double *, int) = f1;
    // cout << "Pointer 1 : " << p1(a, 3) << " : " << *(p1(a, 3)) << endl;
    // cout << "Pointer 1 : " << (*p1)(a, 3) << " : " << *((*p1)(a, 3)) << endl;
    // const double *(*parray[3])(const double *, int) = {f1, f2, f3}; // 声明一个指针数组，存储三个函数的地址
    // cout << "Pointer array : " << parray[0](a, 3) << " : " << *(parray[0](a, 3)) << endl;
    // cout << "Pointer array : " << parray[1](a, 3) << " : " << *(parray[1](a, 3)) << endl;
    // cout << "Pointer array : " << (*parray[2])(a, 3) << " : " << *((*parray[2])(a, 3)) << endl;

    // 10. 局部静态变量
    // for (int i = 0; i < 10; i++)
    // {
    //     cout << "count_add=" << count_add(i) << endl;
    // }

    // 11. 面向对象
    // Student stu("lisi", 20); //有参构造创建对象
    // Student stu; //无参构造创建对象
    // cout << "stu_name: " << stu.getName() << ", stu_age: " << stu.getAge() << endl;
    // displayPoint(Point(11));
    // Point p(44, 99);
    // cout << p.x << "," << p.y << endl;

    // 12. lambda函数
    // int a = 1, b = 2, c = 3;
    // cout << [&](int x, int y) -> int // 使用当前函数的局部变量
    // { return a + b + x + y + c; }(4, 5)
    //                                  << endl;
    // vector<int> list{1, 2, 3, 4, 5};
    // //遍历
    // for_each(list.begin(), list.end(), [](const int &item)
    //          { cout << item << endl; });
    // // 查找
    // auto iter = std::find_if(list.begin(), list.end(), [](const int &item)
    //                          { return item > 2; });
    // if (iter != list.end())
    // {
    //     cout << *iter << endl;
    // }
    // 13. 文件读写操作
    // 写文件
    // ofstream ostrm;
    // ostrm.open("target/test.txt", ios_base::out);
    // ostrm << "My first text file!" << endl; //输入字符串
    // ostrm << "Hello file!";                 //输入字符串
    // ostrm.close();
    // //读文件
    // ifstream istrm;
    // istrm.open("target/test.txt", ios_base::in);
    // string str;=
    // while (istrm.good())
    // {
    //     getline(istrm, str);
    //     cout << str << endl;
    // }

    // 14. 集合操作
    // Vector 集合
    // vector<int> v1{1, 2, 3, 4};
    // vector<int> v5{1, 2, 3, 4};
    // vector<int> v6{1, 2, 3, 4};
    // cout << v1.back() << endl;
    // cout << v1.front() << endl;
    // cout << v1.at(3) << endl;
    // v1.push_back(999);
    // v1.insert(v1.begin(), 10);
    // v1.insert(v1.begin() + 2, 10);

    // for (auto i = v1.rbegin(); i != v1.rend(); i++)
    // {
    //     cout << *i << endl;
    // }
    // vector<int> v2(v1);
    // v2.assign({3, 4});
    // for (auto i : v2)
    // {
    //     cout << i << endl;
    // }
    // string str = "hello, world.";
    // cout << str.substr(0, 3) << endl;

    // Map 集合
    // map<string, int> word_count = {{"a", 1}, {"b", 2}};
    // 增
    // auto r1 = word_count.insert(pair<string, int>("c", 3));
    // auto r2 = word_count.insert(pair<string, int>("c", 4));            //重复key不会插入
    // auto r3 = word_count.insert(map<string, int>::value_type("c", 4)); //重复key不会插入
    // cout << "r1 insert result = " << r1.second << endl;
    // cout << "r2 insert result = " << r2.second << endl;
    // cout << "r3 insert result = " << r3.second << endl;
    // for (auto item : word_count)
    // {
    //     cout << item.first << " " << item.second << endl;
    // }
    // // 查
    // auto f_item = word_count.find("ab");
    // if (f_item != word_count.end())
    // {
    //     cout << f_item->first << f_item->second << endl;
    // }
    // else
    // {
    //     cout << "not found." << endl;
    // }
    // // 改
    // auto update_res = word_count.find("a");
    // update_res->second = 999;
    // for (auto item : word_count)
    // {
    //     cout << item.first << " " << item.second << endl;
    // }
    // 删
    // auto item_a = word_count.find("a");
    // word_count.erase(item_a);

    // auto res = word_count.erase("a");
    // cout << "erase a result = " << res << endl;
    // for (auto item : word_count)
    // {
    //     cout << item.first << " " << item.second << endl;
    // }
    // unordered_map<string, int> hashmap{{"k", 1}};
    // hashmap.insert({"k1", 2});
    // for (auto item : hashmap)
    // {
    //     cout << item.first << " " << item.second << endl;
    // }

    // 15. 动态内存与智能指针
    // auto stu = make_shared<Student>();
    // stu->getName();
    // // auto p(stu); // 初始化另一个对象，引用计数+1
    // // stu = nullptr; //没有引用之后会自动析构
    // cout << stu.use_count() << endl;

    // 16. 模板
    // cout << compare(1, 3) << "," << compare('c', 'b') << "," << compare(3.14, 3.14) << endl;

    // 17. 随机数
    // default_random_engine e;

    // uniform_int_distribution<unsigned> u(0, 10);
    // for (size_t i = 0; i < 10; i++)
    // {
    //     cout << u(e) << endl;
    // }
}

bool s_is_empty(string &s)
{
    return s.empty();
}

int count_add(int n) // n是形参
{
    static int ctr = 0; // ctr 是局部静态变量
    ctr += n;
    return ctr;
}
void fun1(int i, initializer_list<int> args, int j)
{
    cout << "i:" << i << "j:" << j << endl;
    for (auto item : args)
    {
        cout << "item:" << item << endl;
    }
}

void fun2(int n, double (*fp)(int num))
{
    cout << "result: " << fp(n) << endl;
}

double calc(int num)
{
    return num * 0.5;
}

const double *f1(const double arr[], int n)
{
    return arr; // 首地址
}

const double *f2(const double arr[], int n)
{
    return arr + 1;
}

const double *f3(const double *arr, int n)
{
    return arr + 2;
}