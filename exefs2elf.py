# convert exefs to elf
import sys
import os
import glob
import struct

CC = "arm-none-eabi-gcc"
CP = "arm-none-eabi-g++"
OC = "arm-none-eabi-objcopy" 
LD = "arm-none-eabi-ld"


def allFile(pattern):
    s = "";
    for file in glob.glob(pattern):
        s += file + " ";
    return s;
	
def run(cmd):
	os.system(cmd)

def writefile(path, s):
	with open(path, "wb") as f:
		f.write(s);

with open("workdir/exh.bin", "rb") as f:
	exh = f.read(64);



(textBase, textPages, roPages, rwPages, bssSize) =struct.unpack(
'16xii4x4x4xi4x4x4xi4xi', exh);
textSize = textPages * 0x1000;
roSize = roPages * 0x1000;
rwSize = rwPages * 0x1000;
bssSize = ( (bssSize / 0x1000) + 1 ) * 0x1000;
print("textBase: %08x\ntextSize: %08x\nroSize: %08x\nrwSize: %08x\nbssSize: %08x\n" % (textBase, textSize, roSize, rwSize, bssSize))
if (textBase != 0x100000):
	print('textBase mismatch, might be an encrypted exheader file.');
	exit(0);

exefsPath = 'workdir/exefs/';
with open(exefsPath + 'code.bin', "rb") as f:
	text = f.read(textSize);
	ro = f.read(roSize);
	rw = f.read(rwSize);
	
with open('e2elf.ld', 'r') as f:
	ldscript = f.read();
ldscript = ldscript.replace('%bsssize%', str(bssSize));

with open('workdir/e2elf.ld', 'wb') as f:
	f.write(ldscript);

writefile(exefsPath + 'text.bin', text);
writefile(exefsPath + 'ro.bin', ro);
writefile(exefsPath + 'rw.bin', rw);

objfiles = '';
for i in (('text', 'text'), ('ro', 'rodata'), ('rw', 'data')):
	a, b = i;
	run(OC + ' -I binary -O elf32-littlearm --rename-section .data=.' + b + ' ' 
		+ exefsPath + a + '.bin ' + exefsPath + a + '.o');
	objfiles += exefsPath + a + '.o' + ' ';
	
print objfiles;
run (LD + ' --accept-unknown-input-arch -T workdir/e2elf.ld -o workdir/exefs.elf ' + objfiles);