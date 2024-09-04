#include <stdio.h>
#include <math.h>

void print_menu() {
	/*
	*Void procedure to print menu entries.
	*No parameters.
	*No return value.
	*/
	printf("\n1. Read a vector of numbers\n");
	printf("2. Functionality 1\n");
	printf("3. Functionality 2\n");
	printf("4. Exit\n");
}

void read_vector(int vector[], int *len) {
	/*
	*Void procedure to read a vector of integers. Stops on reading 0. 0 is not included in the vector.
	*:vector: int vector
	*:len: int pointer which will store the length of the vector
	*return -
	*/
	int element = 1, i = 0;
	*len = 0;
	while(1)
	{
		printf("Input next element: ");
		scanf("%d", &element);
		if (element == 0)
			return;
		vector[i] = element;
		i += 1;
		*len += 1;
	}
}

int prime(int n){
	/*
	*Function that checks if a number is prime.
	*:n: integer
	* returns 1 if n is prime, 0 if not
	*/
	if(n < 2)
		return 0;
	else 
	{
		if (n == 2) 
		{
			return 1;
		}
		else 
		{
			if (n % 2 == 0) 
			{
				return 0;
			}
			else
			{
				for (int i = 3; i <= sqrt(n); i += 2)
				{
					if (n % i == 0)
						return 0;
				}
			}
		}
	}
	return 1;
}

int exponent_of_p(int p, int n) {
	/*
	* Finds the exponent of a given number p if it appears in the decomposition of a given nr. n
	* :p, n: integer numbers
	* Returns number of occurences of p in the decomposition of n, if p does not appear in the decomposition, 0 will be returned
	* If p is not prime, a warning will be printed and -1 will be returned
	*/

	//Check if p is prime
	if (prime(p) == 0)
	{
		printf("P is not prime!");
		return -1;
	}

	//If p is prime, check how many times it appears
	int counter = 0;
	while (n % p == 0 && n > 1)
	{
		counter += 1;
		n /= p;
	}

	//Return result
	return counter;
	
}

void functionality_1() {
	/*  This function reads the input for the first functionality and displays the results 
		obtained after calling exponent_of_p
	*/
	int p, n;
	printf("Choose a number n to decompose: ");
	scanf("%d", &n);
	printf("Choose the prime factor p:");
	scanf("%d", &p);

	int nr_occurences = exponent_of_p(p, n);
	if(nr_occurences >= 0)
		printf("%d appears %d times in the prime decomposition of %d\n", p, nr_occurences, n);
	
}


int relative_prime(int a, int b) {
	/*
	* Function to check if 2 numbers are realtive primes.
	* It actually compuutes the greatest common divisor of a and b.
	* If it is 1 then the function returns 1, 0 else.
	* :a,b: integers
	*/
	while (b != 0)
	{
		int r = a % b;
		a = b;
		b = r;
	}
	if (a == 1)
		return 1;
	return 0;
}

int longest_subsequence_of_relative_primes(int v[], int len, int* maxstart, int* maxlength){
	/*
	* Function to find and the longest subsequence of relative primes in a vector.
	* If the vector was not inputed before, a warning is printed and the function returns -1.
	* If execution was successful 0 will be returned.
	* :v: vector of integers
	* :len: length of the vector v
	* :maxstart: int* where the start of the longest subsequence that satisfies the condition will be stored
	* :maxlength: int* where the length of the longest subsequence that satisfies the condition will be stored
	*/
	if (len == 0)
	{
		printf("Vector not available!\n");
		return -1;
	}

	int start = 0, current_len = 1;
	*maxstart = 0;
	*maxlength = 1;

	for (int i = 1; i < len; i += 1)
	{
		if (relative_prime(v[i], v[i - 1]))
		{
			current_len += 1;
			if (current_len > *maxlength)
			{
				*maxstart = start;
				*maxlength = current_len;
			}
		}
		else
		{
			current_len = 1;
			start = i;
		}
	}
	return 0;
	
}

void functionality_2(int v[],  int len) {
	/*  This function is used to execute the second functionality of the program and displays the results
		obtained after calling longest_subsequence_of_relative_primes
		:v: vector of integers
		:len: length of the vector v
	*/
	int maxstart, maxlength;
	int check = longest_subsequence_of_relative_primes(v, len, &maxstart, &maxlength);

	if (check == 0)
		for (int i = maxstart; i < (maxstart + maxlength); i += 1)
			printf("%d ", v[i]);
}

int main() {
	/*
		Main function used to read option of the user and call the corresponding functions.
	*/

	int v[100];
	int option, len = 0;

	while (1) {
		print_menu();
		printf("Choose an option: ");
		scanf("%d", &option);
		switch (option) {
			case 1:
				read_vector(v, &len);
				break;
			case 2:
				functionality_1();
				break;
			case 3:
				functionality_2(v, len);
				break;
			case 4:
				exit(0);
			default:
				printf("Invalid option");
		}
	}
	return 0;
}