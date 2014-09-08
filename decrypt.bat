cd workdir
ren *.exh.xorpad exh.xor
ren *.exefs.xorpad exefs.xor
ren *.romfs.xorpad romfs.xor
..\xor exh.enc.bin exh.xor
..\xor exefs.enc.bin exefs.xor
..\xor romfs.enc.bin romfs.xor
ren exh.enc.bin.out exh.bin
ren exefs.enc.bin.out exefs.bin
ren romfs.enc.bin.out romfs.bin
cd ..