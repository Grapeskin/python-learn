#include "teacher.h"
Teacher::Teacher()
{
    std::cout << "Teacher 无参构造" << std::endl;
}
Teacher::Teacher(const Student &stu)
{
    std::cout << "Teacher 有参构造, " << stu.getAge() << std::endl;
    this->stu = new Student(stu);
}

Teacher &Teacher::operator=(const Teacher &t)
{
    std::cout << "Teacher 拷贝赋值" << std::endl;
    this->stu = t.stu;
    return *this;
}
Teacher::~Teacher()
{
    std::cout << "Teacher 析构函数" << std::endl;
    delete stu;
    std::cout << "开始析构stu动态内存" << std::endl;
}