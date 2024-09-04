#include "UserInterface.h"
#include <stdio.h>
#include <stdlib.h>

UI* createUI(Controller* ctrl)
{
	UI* ui = (UI*)malloc(sizeof(UI));

	//make sure that the space was allocated
	if (ui == NULL)
		return NULL;

	//make sure controller exists exists
	if (ctrl == NULL)
		return NULL;

	ui->controller = ctrl;
	return ui;
}

void destroyUI(UI* ui)
{

	if (ui == NULL)
		return;

	destroyController(ui->controller);
	ui->controller = NULL;

	//free the space allocated for the UI
	free(ui);
}

/// <summary>
/// Prints the app menu
/// </summary>
void printMenu()
{
	printf("1. Add a product\n");
	printf("2. Delete a product\n");
	printf("3. Update a product\n");
	printf("4. Filter by name\n");
	printf("5. Filter by category\n");
	printf("6. Undo\n");
	printf("7. Redo\n");
	printf("0. Exit\n");
	printf("Input the option: ");
}

/// <summary>
/// Add a new product to the repository
/// </summary>
/// <param name="ui">UI object</param>
void addProductUI(UI* ui)
{
	char name[50];
	char category[50];
	int quantity = 0;
	int day, month, year;

	// read product name
	printf("Input the name: ");
	scanf("%50s", name);

	// read product category
	printf("Input the category: ");
	scanf("%50s",  category);

	// read product quantity
	printf("Input the quantity: ");
	if (scanf("%d", &quantity) != 1)
	{
		printf("Invalid quantity\n");
		// Clearing the input buffer
		int c;
		while ((c = getchar()) != '\n' && c != EOF);
		return;
	}

	// read product expiration date
	printf("Input the expiration date\n");

	printf("Day: ");
	if (scanf("%d", &day) != 1 || day  < 0)
	{
		printf("\nInvalid day\n\n");
		// Clearing the input buffer
		int c;
		while ((c = getchar()) != '\n' && c != EOF);
		return;
	}

	printf("Month: ");
	if (scanf("%d", &month) != 1 || month < 0)
	{
		printf("\nInvalid month\n\n");
		// Clearing the input buffer
		int c;
		while ((c = getchar()) != '\n' && c != EOF);
		return;
	}

	printf("Year: ");
	if (scanf("%d", &year) != 1 || year < 0)
	{
		printf("\nInvalid year\n\n");
		// Clearing the input buffer
		int c;
		while ((c = getchar()) != '\n' && c != EOF);
		return;
	}

	// pass input to the controller
	int ret_val = addProduct(ui->controller, name, category, quantity, day, month, year);
	if (ret_val == -1)
		printf("\nInvalid category!\n\n");
	else
		printf("\nProduct added successfully\n\n");
}

/// <summary>
/// Remove a product from the repository
/// </summary>
/// <param name="ui">A pointer to an ui object</param>
void removeProductUI(UI* ui)
{
	char name[50];
	char category[50];

	// read product name
	printf("Input the name: ");
	scanf("%50s", name);

	// read product category
	printf("Input the category: ");
	scanf("%50s", category);

	//pass input to the controller
	int ret_val = removeProduct(ui->controller, name, category);
	if (ret_val == -1)
		printf("\nInvalid input or product does not exist!\n\n");
	else
		printf("\nProduct removed successfully\n\n");
}

/// <summary>
/// Update a product from the repository
/// </summary>
/// <param name="ui">A pointer to an ui object</param>
void updateProductUI(UI* ui)
{
	char name[50];
	char category[50];
	int quantity = 0;
	int day, month, year;

	// read product name
	printf("Input the name: ");
	scanf("%50s", name);

	// read product category
	printf("Input the category: ");
	scanf("%50s", category);

	// read product quantity
	printf("Input the new quantity: ");
	if (scanf("%d", &quantity) != 1)
	{
		printf("Invalid quantity\n");
		// Clearing the input buffer
		int c;
		while ((c = getchar()) != '\n' && c != EOF);
		return;
	}

	// read product expiration date
	printf("Input the new expiration date\n");

	printf("Day: ");
	if (scanf("%d", &day) != 1 || day < 0)
	{
		printf("\nInvalid day\n\n");
		// Clearing the input buffer
		int c;
		while ((c = getchar()) != '\n' && c != EOF);
		return;
	}

	printf("Month: ");
	if (scanf("%d", &month) != 1 || month < 0)
	{
		printf("\nInvalid month\n\n");
		// Clearing the input buffer
		int c;
		while ((c = getchar()) != '\n' && c != EOF);
		return;
	}

	printf("Year: ");
	if (scanf("%d", &year) != 1 || year < 0)
	{
		printf("\nInvalid year\n\n");
		// Clearing the input buffer
		int c;
		while ((c = getchar()) != '\n' && c != EOF);
		return;
	}

	// pass input to the controller
	int ret_val = updateProduct(ui->controller, name, category, quantity, day, month, year);
	if (ret_val == -1)
		printf("\nInvalid category or product does not exist!\n\n");
	else
		printf("\nProduct updated successfully\n\n");
}

/// <summary>
/// Filter all products by name.
/// If the name is empty, all will be considered
/// </summary>
/// <param name="ui">A pointer to an ui object</param>
void filterByNameUI(UI* ui)
{
	char name[50];
	int length = 0;

	// Clearing the input buffer
	int c;
	while ((c = getchar()) != '\n' && c != EOF);
	printf("Input the name: ");

	fgets(name, sizeof(name), stdin);
	name[strlen(name) - 1] = '\0';

	// get as strings all the products that contain the given string
	Product* list = filterProductsByName(ui->controller, name, &length);

	if(length == 0)
	{
		free(list);
		printf("\nNo products found\n\n");
		return;
	}
	else
	{
		printf("\n");
		for (int i = 0; i < length; i++)
		{
			char p[200];
			toString(list[i], p);
			printf("%s\n", p);
		}
		free(list);
	}
}

/// <summary>
/// Filter all products of a given category that expire in the following x days
/// X is a value provided by the user
/// </summary>
/// <param name="ui">A pointer to an UI object</param>
void filterByCategory(UI* ui)
{
	char category[50];
	int length = 0;
	int days = 0;

	// Clearing the input buffer
	int c;
	while ((c = getchar()) != '\n' && c != EOF);
	printf("Input the category: ");

	// Read category
	fgets(category, sizeof(category), stdin);
	category[strlen(category) - 1] = '\0';

	// Read days
	printf("Input the number of days: ");
	if (scanf("%d", &days) != 1 || days < 0)
	{
		printf("\nInvalid number of days\n\n");
		// Clearing the input buffer
		int c;
		while ((c = getchar()) != '\n' && c != EOF);
		return;
	}

	// get as strings all the products that satisfy the given conditions
	Product* list = filterProductsByCategory(ui->controller, category, &length, days);

	if (length == 0)
	{
		free(list);
		printf("\nNo products found\n\n");
		return;
	}
	else
	{
		printf("\n");
		for (int i = 0; i < length; i++)
		{
			char p[200];
			toString(list[i], p);
			printf("%s\n", p);
		}
		free(list);
	}
}

/// <summary>
/// Undo the last operation that modified the repository
/// </summary>
/// <param name="ui">Pointer to ui object</param>
void undoUI(UI* ui)
{
	int success = undo(ui->controller);
	if(success != 0)
		printf("No more undos available\n");
	else
		printf("Undo successful\n");
}

/// <summary>
/// Redo the last operation that was undone
/// </summary>
/// <param name="ui">Pointer to ui object</param>
void redoUI(UI* ui)
{
	int success = redo(ui->controller);
	if (success != 0)
		printf("No more redos available\n");
	else
		printf("Redo successful\n");
}

void startUI(UI* ui)
{
	int option = 0;
	while (1)
	{
		printMenu();
		int ret_val = scanf("%d", &option);
		switch (option)
		{
			case 1:
			// Add a product
				addProductUI(ui);
				break;
			case 2:
			// Delete a product
				removeProductUI(ui);
				break;
			case 3:
			// Update a product
				updateProductUI(ui);
				break;
			case 4:
			// Filter by name
				filterByNameUI(ui);
				break;
			case 5:
			// Filter by category
				filterByCategory(ui);
				break;
			case 6:
				// Undo
				undoUI(ui);
				break;
			case 7:
				// Redo
				redoUI(ui);
				break;
			case 0:
			// Exit
				return;
		default:
			printf("Invalid option\n");
		}
	}
}