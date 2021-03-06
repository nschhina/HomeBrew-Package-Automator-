#!/usr/bin/python
import homebrew_install
import ansible_install
import sys
import platform

def main():
    if(platform.system()=='Darwin'):
        homebrew_install.homebrewinstaller()
        print("installed Homebrew")
    ansible_install.pipinstaller()
    print("installed Pip")
    ansible_install.ansibleinstaller()
    print("installed Ansible")


if __name__ == "__main__":
    main()
