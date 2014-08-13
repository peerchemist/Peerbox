## paxctl

 paxctl  is  a tool that allows PaX flags to be modified on a per-binary
       basis.  PaX is part of common  security-enhancing  kernel  patches  and
       secure  distributions,  such  as  GrSecurity  or Adamantix and Hardened
       Gentoo, respectively.  Your system  needs  to  be  running  a  properly
       patched and configured kernel for this program to have any effect.

       -P     enforce paging based non-executable pages (PAGEEXEC)

       -p     do not enforce paging based non-executable pages (NOPAGEEXEC)

       -E     emulate trampolines (EMUTRAMP)

       -e     do not emulate trampolines (NOEMUTRAMP)

       -M     enforce secure memory protections (MPROTECT)

       -m     do not enforce secure memory protections (NOMPROTECT)

       -R     randomize memory regions (RANDMMAP)

       -r     do not randomize memory regions (NORANDMMAP)

       -X     randomize   base   address   of   normal  (ET_EXEC)  executables
              (RANDEXEC)

       -x     do not randomize base address of  normal  (ET_EXEC)  executables
              (NORANDEXEC)

       -S     enforce segmentation based non-executable pages (SEGMEXEC)

       -s     do   not   enforce   segmentation   based  non-executable  pages
              (NOSEGMEXEC)

       -v     view flags

       -z     restore default flags (further flags still apply)

       -c     create the PT_PAX_FLAGS program header if it does not exist  but
              PT_GNU_STACK does by converting the latter into the former

       -q     suppress error messages

       -Q     report flags in short format

