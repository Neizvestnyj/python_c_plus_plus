#pragma warning(disable : 4996)

#include "date.h"
#include <iostream>
#include <ctime>


// Date constructor
Date::Date(int year, int month, int day)
{
    SetDate(year, month, day);
}

// Date member function
void Date::SetDate(int year, int month, int day)
{
    m_month = month;
    m_day = day;
    m_year = year;
}

void Date::print_all(){
    cout << "A certain date: " << getYear() << "." << getMonth() << "." << getDay() << endl;
}

char* Date::getCurrentDate() {
    time_t rawtime;
    time(&rawtime); // текущая дата в секундах
    char* current_time;

    current_time = ctime(&rawtime);
    return current_time;
}
