
#include <iostream>
#ifndef __STU__
#define __STU__
class Student
{
private:
    std::string name;
    int age;

public:
    Student();
    Student(std::string &, int);
    Student &operator=(Student &);
    ~Student();

public:
    std::string getName() const;
    int getAge() const;
};
#endif