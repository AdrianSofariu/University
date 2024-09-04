#pragma once
#include <time.h>

typedef struct {
	int day;
	int month;
	int year;
}Date;


Date createDate(int day, int month, int year);
int getDay(Date* date);
int getMonth(Date* date);
int getYear(Date* date);

/// <summary>
/// Get current date
/// </summary>
/// <returns>a Date object storing the current date</returns>
Date getCurrentDate();

/// <summary>
/// Compute the difference in days between two dates
/// </summary>
/// <param name="a">Date</param>
/// <param name="b">Date</param>
/// <returns>(Double) days between the two dates. 
/// If the date b is smaller than date a, the value will be negative</returns>
double dayDifference(Date a, Date b);

//tests
void testDate();
