QEMU		= qemu-system-i386
QEMU_ARGS	= -L . -m 32 -rtc base=localtime -vga std -drive file=fdimage0.bin,index=0,if=floppy,format=raw

default:
	$(QEMU) $(QEMU_ARGS)
