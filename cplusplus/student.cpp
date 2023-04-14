#include "student.h"
Student::Student()
{
    std::cout << "Student 无参构造" << std::endl;
}
Student::Student(std::string &name, int age) : name(name), age(age)
{
    std::cout << "Student 有参构造" << std::endl;
}
Student &Student::operator=(Student &stu)
{
    std::cout << "Student 拷贝赋值" << std::endl;
    name = stu.getName();
    age = stu.getAge();
    return *this;
}

Student::~Student()
{
    std::cout << "Student 析构函数" << std::endl;
}
std::string Student::getName() const
{
    return name;
}
int Student::getAge() const
{
    return age;
}
