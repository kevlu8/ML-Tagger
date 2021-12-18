#include "window.hpp"

bool createWindow(_In_ HINSTANCE hInstance) {
	const wchar_t CLASS_NAME[] = L"ML-Tagger AI Window";

	WNDCLASS wc = {};

	wc.lpfnWndProc = WindowProcHomemade;
	wc.hInstance = hInstance;
	wc.lpszClassName = CLASS_NAME;
	wc.hCursor = LoadCursor(NULL, IDC_ARROW);
	wc.hbrBackground = (HBRUSH)GetStockObject(WHITE_BRUSH);

	RegisterClass(&wc);
	
	HWND hwnd = CreateWindowExW(
		0,
		CLASS_NAME,
		L"ML-Tagger AI Window",
		WS_OVERLAPPEDWINDOW,
		CW_USEDEFAULT, CW_USEDEFAULT, CW_USEDEFAULT, CW_USEDEFAULT,
		NULL,
		NULL,
		hInstance,
		NULL
	);

	if (hwnd == NULL) {
		return false;
	}

	ShowWindow(hwnd, SW_SHOWNORMAL);


	return true;
}

bool paintWindow(_In_ HWND hwnd) {
	HDC desktop = GetDC(NULL);
	HDC window = GetDC(hwnd);
	BitBlt(window, 0, 0, CW_USEDEFAULT, CW_USEDEFAULT, desktop, 0, 0, SRCCOPY);
	return true;
}

LRESULT CALLBACK WindowProcHomemade(_In_ HWND hwnd, _In_ UINT msg, _In_ WPARAM wp, _In_ LPARAM lp) {
	switch (msg) {
	case WM_PAINT:
		paintWindow(hwnd);
		return 0;
	default:
		return DefWindowProc(hwnd, msg, wp, lp);
	}
}