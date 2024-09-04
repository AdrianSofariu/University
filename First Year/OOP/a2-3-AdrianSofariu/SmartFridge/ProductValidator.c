#include "ProductValidator.h"
#include <stdlib.h>
#include <string.h>

int validCategory(char* cat)
{
	if (cat != NULL)
	{
		if (strcmp(cat, "dairy") == 0)
			return 0;
		if (strcmp(cat, "sweets") == 0)
			return 0;
		if (strcmp(cat, "meat") == 0)
			return 0;
		if (strcmp(cat, "fruit") == 0)
			return 0;
	}
	return -1;
}
