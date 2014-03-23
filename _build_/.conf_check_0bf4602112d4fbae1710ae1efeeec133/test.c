#include <unistd.h>

int main(int argc, char **argv) {
	void *p;
	(void)argc; (void)argv;
	p=(void*)(ftruncate);
	return 0;
}
