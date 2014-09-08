arm-none-eabi-gcc -g payload.s -c -mcpu=arm946e-s -march=armv5te -mlittle-endian -o payload.o -fshort-wchar

arm-none-eabi-objcopy --adjust-vma 0x111110 -I elf32-little -O binary payload.o payload.bin