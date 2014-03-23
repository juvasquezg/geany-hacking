#include <stdio.h>

int main(int argc, char **argv) {
	void *p;
	(void)argc; (void)argv;
	p=(void*)(fgetpos);
	return 0;
}
