//LIBRARIES
#include <iostream>
#include <vector>
#include <stdlib.h>

//*********************
//TEST FOR GITKRSKEN  *
//*********************

//HEADERS
#include "windows.h"
//#include "Employee.h"

//DEFINES
#define GENERATE_SCHED 1
#define ADD_EMPLOY 2
#define UPDATE_AVAIL 3

//PROTOTYPES
LRESULT CALLBACK AvailabiProcedure(HWND hWnd, UINT msg, WPARAM wp, LPARAM lp);
LRESULT CALLBACK ScheduleProcedure(HWND hWnd, UINT msg, WPARAM wp, LPARAM lp);
LRESULT CALLBACK EmployeeProcedure(HWND hWnd, UINT msg, WPARAM wp, LPARAM lp);
LRESULT CALLBACK WindowProcedure(HWND, UINT, WPARAM, LPARAM);
void AddMenus(HWND hWnd); // MAIN MENU FOR START WINDOW
void registerSchedule(HINSTANCE);
void registerEmployee(HINSTANCE);
void registerAvail(HINSTANCE);

//DISPLAY WINDOWS
void displaySchedule(LPSTR, HWND);
//void displayEmployee(HWND);
//void displayAvailabi(HWND):


//CONTROLS FOR WINDOWS
void AddControls(HWND hWNd); // MAIN CONTROLS
void AddControlsSched(HWND hWNd); //SCHEDULE CONTROLS
void AddControlsEmply(HWND hWNd); //EMPLOYEE ADD CONTROLS
void AddControlsAvail(HWND hWNd); //AVAIL UPDATE CONTROLS

//ADD MENUS FOR SPECIFIC DIALOGUES
void AddMenusSched(HWND hWnd);
void AddMenusEmply(HWND hWnd);
void AddMenusAvail(HWND hWnd);

//GLOBAL VAR
HMENU hMenu;


//MAIN FUNCTION-------------------------------------------------------------------------------------------------------------
int WINAPI WinMain(HINSTANCE hInst, HINSTANCE hPrevInst, LPSTR args, int ncmdshow){
	//DECLARE EMPLOYEE VECTOR
	
	//MAKE WINDOWCLASS
	WNDCLASSW mw = {0};
	mw.hbrBackground = (HBRUSH) COLOR_WINDOW;
	mw.hCursor = LoadCursor(NULL, IDC_ARROW);
	mw.hInstance = hInst;
	mw.lpszClassName = L"MainWindow";
	mw.lpfnWndProc = WindowProcedure;
	
	RegisterClassW(&mw);
	
	CreateWindowW(L"MainWindow", L"Jump'n Jammin Schedule", WS_OVERLAPPEDWINDOW | WS_VISIBLE, 100,100,500,500, NULL,NULL,NULL,NULL);
	
	MSG msg = {0};
	
	while(GetMessage(&msg, NULL,0,0)){
		TranslateMessage(&msg);
		DispatchMessage(&msg);
	}
	
	return 0;
}

// WINDOW PROCEDURES----------------------------------------------------------------------------------------------------
LRESULT CALLBACK WindowProcedure(HWND hWnd, UINT msg, WPARAM wp, LPARAM lp){
	//SWITCH CASE FOR ONCLICK & CREATION
	
	switch(msg){
		case WM_CREATE:
			break;
		case WM_COMMAND:
			break;
		case WM_DESTROY:
			break;
		default:
		return DefWindowProcW(hWnd, msg, wp, lp);
	}
	
}

//AVAILABILITY PROCEDURE
LRESULT CALLBACK AvailabiProcedure(HWND hWnd, UINT msg, WPARAM wp, LPARAM lp){ 
	switch(msg){
		case WM_CREATE:
			break;
		case WM_COMMAND:
			break;
		case WM_DESTROY:
			break;
		default:
		return DefWindowProcW(hWnd, msg, wp, lp);
	}
}

//SCHEDULE PROCEDURE
LRESULT CALLBACK ScheduleProcedure(HWND hWnd, UINT msg, WPARAM wp, LPARAM lp){
	switch(msg){
		case WM_CREATE:
			break;
		case WM_COMMAND:
			break;
		case WM_DESTROY:
			break;
		default:
		return DefWindowProcW(hWnd, msg, wp, lp);
	}
}

//EMPLOYEE PROCEDURE
LRESULT CALLBACK EmployeeProcedure(HWND hWnd, UINT msg, WPARAM wp, LPARAM lp){
	switch(msg){
		case WM_CREATE:
			break;
		case WM_COMMAND:
			break;
		case WM_DESTROY:
			break;
		default:
		return DefWindowProcW(hWnd, msg, wp, lp);
	}
}

//REGISTER WINDOWS-------------------------------------------------------------------------------------------------
void registerSchedule(HINSTANCE hInst){

	WNDCLASSW sched = {0};
	sched.hbrBackground = (HBRUSH) COLOR_WINDOW;
	sched.hCursor = LoadCursor(NULL, IDC_ARROW);
	sched.hInstance = hInst;
	sched.lpszClassName = L"SchedWindow";
	sched.lpfnWndProc = WindowProcedure;
	
	RegisterClassW(&sched);	
}

void registerEmployee(HINSTANCE hInst){
	WNDCLASSW empl = {0};
	empl.hbrBackground = (HBRUSH) COLOR_WINDOW;
	empl.hCursor = LoadCursor(NULL, IDC_ARROW);
	empl.hInstance = hInst;
	empl.lpszClassName = L"EmplyWindow";
	empl.lpfnWndProc = WindowProcedure;
	
	RegisterClassW(&empl);		
}

void registerAvail(HINSTANCE hInst){
	WNDCLASSW avail = {0};
	avail.hbrBackground = (HBRUSH) COLOR_WINDOW;
	avail.hCursor = LoadCursor(NULL, IDC_ARROW);
	avail.hInstance = hInst;
	avail.lpszClassName = L"AvailWindow";
	avail.lpfnWndProc = WindowProcedure;
	
	RegisterClassW(&avail);	
	
}

//ADD MENUS TO EACH WINDOW-----------------------------------------------------------------------------------------
void AddMenusSched(HWND hWnd){ //MAIN MENU ADD MENU DIALOG BOX

}

void AddMenusEmply(HWND hWnd){ //ADD EMPLOYEE DIALOG BOX
	
	
}

void AddMenusAvail(HWND hWnd){ //AVAILABILITY UPDATE DIALOG BOX
	
	
}



//ADD CONTROLS TO WINDOWS-------------------------------------------------------------------------------------------
void AddControlsSched(HWND hWNd){ //SCHEDULE CONTROLS

}

void AddControlsEmply(HWND hWNd){ //EMPLOYEE ADD CONTROLS

}

void AddControlsAvail(HWND hWNd){ //AVAIL UPDATE CONTROLS

}

//DISPLAY WINDOWS-----------------------------------------------------------------------------------------------------

void displaySchedule(LPCWSTR x, HWND hWnd){
	CreateWindowW(x, L"Dialogue", WS_VISIBLE | WS_OVERLAPPEDWINDOW, 400,400,200,200, hWnd, NULL, NULL, NULL);
}
/*
void displayEmployee(LPSTR X, HWND hWnd){
	
}

void displayAvailabi(LPSTR x, HWND hWnd){
	
}
*/