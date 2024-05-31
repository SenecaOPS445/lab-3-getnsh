#!/usr/bin/env python3
'''Lab 3 - Running System Commands From Python'''
# Author ID: gchawla4@myseneca.ca

import subprocess

def free_space():
    # Launch the Linux command: df -h | grep '/$' | awk '{print $4}' as a new process
    p = subprocess.Popen(['df', '-h'], stdout=subprocess.PIPE)
    p1 = subprocess.Popen(['grep', '/$'], stdin=p.stdout, stdout=subprocess.PIPE)
    p2 = subprocess.Popen(['awk', '{print $4}'], stdin=p1.stdout, stdout=subprocess.PIPE)
    
    # Retrieve output
    output = p2.communicate()[0]
    
    # Convert stdout to a string and strip off the newline characters
    free_space = output.decode('utf-8').strip()
    
    return free_space

if __name__ == '__main__':
    print(free_space())
