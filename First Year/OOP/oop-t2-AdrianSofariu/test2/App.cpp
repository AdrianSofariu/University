#include "UI.h"
#include "Device.h"


int main(){

	Device d;
	UI user_int{ d };
	user_int.run();
	return 0;
}