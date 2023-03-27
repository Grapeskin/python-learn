#include <iostream>
#include <vector>
#include "student.h"
class Teacher
{
private:
    Student *stu;

public:
    Teacher();
    Teacher(const Student &s);
    Teacher &operator=(const Teacher &);
    ~Teacher();
};
