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


Third-party tools
========
makerom, ctrtool: from 3dsguy's project_ctr https://github.com/3DSGuy/Project_CTR

CTR_Decryptor: from VOiD and xerpi http://gbatemp.net/threads/release-3ds_ctr_decryptor-void.370684/

3DS Explorer(fixed romfs.bin extraction): https://code.google.com/p/3dsexplorer/