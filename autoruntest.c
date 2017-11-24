#include <windows.h>
#include <winuser.h>   
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void main()
{
	printf("Hello");
	WinExec("D:\\emu8086\\emu8086.exe", SW_SHOW);
}