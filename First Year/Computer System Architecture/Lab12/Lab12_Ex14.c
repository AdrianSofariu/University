#include <stdio.h>
#include <stdlib.h>

int display_in_octal(char*);


int main() {
    long num;
    char binary[33] = { 0 };

    printf("Enter the number of binary numbers: ");
    scanf("%u", &num);

    for (int i = 0; i <= num; i++) {
	binary[33] = { 0 };
        printf("Enter a binary number: ");
        scanf("%s", binary);

        int octal = display_in_octal(binary);
        printf("In octal: %o\n", octal);
    }

    return 0;
}

