# convert exefs to elf
import sys
import os
import glob
import struct

CC = "arm-none-eabi-gcc"
CP = "arm-none-eabi-g++"
OC = "arm-none-eabi-objcopy" 
LD = "arm-none-eabi-ld"

with open('../../workdir/exefs/symbols.txt', 'r') as f:
	db = eval(f.read());
	
def ref(sym):
	global db;
	t = int(db[sym], 0);
	if (t == 0):
		print('***ERROR*** Symbol %s not located, please edit symbols.txt manually.' % t);
		exit();
	return t;

def loadRef(str):
	global db;
	for k in db:
		t = '%' + k + '%';
		if (str.find(t) != -1):
			str = str.replace(t, hex(ref(k)));
	return str;
	
def run(cmd):
	os.system(cmd)

def writefile(path, s):
	with open(path, "wb") as f:
		f.write(s);

with open('payload_template.s', "r") as f:
	payload = f.read();
	
mountRomPtr = ref('mountRom');
payload = loadRef(payload);

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

	