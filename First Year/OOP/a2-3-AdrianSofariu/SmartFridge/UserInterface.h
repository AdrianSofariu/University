#pragma once
#include "Controller.h"

typedef struct {
	Controller* controller;
}UI;

/// <summary>
/// Create a new UI object
/// </summary>
/// <param name="ctrl">Pointer to a Controller type object</param>
/// <returns>A pointer to the created UI object</returns>
UI* createUI(Controller* ctrl);

/// <summary>
/// Destroy a UI object
///</summary>
///<param name="ui">A pointer to the UI object to be destroyed</param>
void destroyUI(UI* ui);


/// <summary>
/// Main procedure of the UI to read user options and execute them
///</summary>/
///<param name="ui"> A pointer to the UI object</param>
void startUI(UI* ui);