#include "Date.h"
#include <time.h>
#include<assert.h>

Date createDate(int day, int month, int year)
{
	Date d;
	d.day = day;
	d.month = month;
	d.year = year;
	return d;
}

/// <summary>
/// Convert a Date struct d into a time_t struct
/// </summary>
/// <param name="d">Date</param>
/// <returns>(time_t) struct built using the information of the Date struct d</returns>
time_t dateToTime(Date d)
{
	struct tm timeinfo = { 0 };
	timeinfo.tm_year = d.year - 1900; // Years since 1900
	timeinfo.tm_mon = d.month - 1;    // Months since January (0-11)
	timeinfo.tm_mday = d.day;         // Day of the month (1-31)
	return mktime(&timeinfo);
}

double dayDifference(Date a, Date b)
{
	time_t start_time = dateToTime(a);
	time_t end_time = dateToTime(b);

	double seconds_diff = difftime(end_time, start_time);
	double days_diff = seconds_diff / (60 * 60 * 24); // Convert seconds to days

	return days_diff;
}

int getDay(Date* d)
{
	return d->day;
}

int getMonth(Date* d)
{
	return d->month;
}

int getYear(Date* d)
{
	return d->year;
}

Date getCurrentDate()
{
	time_t now = time(0);
	struct tm timeinfo;
	localtime_s(&timeinfo, &now);
	Date d = createDate(timeinfo.tm_mday, timeinfo.tm_mon + 1, timeinfo.tm_year + 1900);
	return d;
}

void testDate()
{
	Date d = createDate(10, 10, 2020);
	assert(getDay(&d) == 10);
	assert(getMonth(&d) == 10);
	assert(getYear(&d) == 2020);
	Date d2 = createDate(11, 10, 2020);
	assert(dayDifference(d, d2) == 1);
	Date d3 = createDate(10, 10, 2020);
	assert(dayDifference(d, d3) == 0);
	Date d4 = createDate(9, 10, 2020);
	assert(dayDifference(d, d4) == -1);
	Date d5 = createDate(10, 11, 2020);
	assert(dayDifference(d, d5) == 31);
	Date d6 = createDate(10, 10, 2021);
	assert(dayDifference(d, d6) == 365);
	Date d7 = createDate(10, 10, 2019);
	assert(dayDifference(d, d7) == -366);
}




