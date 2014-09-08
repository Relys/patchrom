# convert exefs to elf
import sys
import os
import glob
import struct

CC = "arm-none-eabi-gcc"
CP = "arm-none-eabi-g++"
OC = "arm-none-eabi-objcopy" 
LD = "arm-none-eabi-ld"


	
def run(cmd):
	os.system(cmd)

def writefile(path, s):
	with open(path, "wb") as f:
		f.write(s);

with open('payload_template.s', "r") as f:
	payload = f.read();
	
mountRomPtr = int(raw_input("mountRomFunction (0xXXXX): "), 0);
mountArchivePtr = raw_input("mountArchiveFunction (0xXXXX): ");
regArchivePtr = raw_input("regArchiveFunction (0xXXXX): ");
romPath = raw_input("romPath ('rom:' if not sure): ");

payload = payload.replace("%mountarchive%", mountArchivePtr);
payload = payload.replace("%regarchive%", regArchivePtr);
payload = payload.replace("%rompath%", romPath);

with open('payload.s', 'w') as f:
	f.write(payload);

run("del *.o *.bin *.out");
run(CC + " -g payload.s -c -mcpu=arm946e-s -march=armv5te -mlittle-endian -o payload.o -fshort-wchar");
run(LD + ' -Ttext ' + hex(mountRomPtr) + ' payload.o');
run(OC + " -I elf32-little -O binary a.out payload.bin");

with open('payload.bin', "rb") as f:
	payload = f.read();

with open('../../workdir/exefs/code.bin', 'rb') as f:
	code = f.read();
	
t = mountRomPtr-0x100000;
code = code[0:t] + payload + code[t + len(payload):];
print(len(code));

with open('../../workdir/exefs/code.bin', 'wb') as f:
	f.write(code);

print('done. don\'t forget to rebuild the elf file');

	