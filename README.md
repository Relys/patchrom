patchrom
========
quick and dirty scripts to patch 3ds roms.

devkitARM is required for most tools.


Usage
========
exefs2elf.py: convert exefs to elf file.

unpack-exefs.bat: unpack exefs.bin.

build-rom.bat: rebuild .3ds roms.

patches/romfsredirect: patching code.bin to redirect romfs access to sdcard, some reverse-engineering works is needed to locate sdk function addresses.
