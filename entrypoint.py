#!/usr/bin/env python3
"""Return to Libc — a ROP chain into system() reads the guarded seed (fernet delivery)."""
import os, sys
sys.path.insert(0, "/challenge/_shared")
from fetch_material import fetch_material

CHALLENGE_KEY = os.environ.get("CHALLENGE_KEY", "system-binsh")

def main():
    mat = fetch_material()
    with open("/challenge/flag.enc", "w") as f:
        f.write(mat["delivery_blob"])
    with open("/challenge/shell.log", "w") as f:
        f.write(f"$ ropchain -> system(\"/bin/sh\")\n$ cat /seed\n{CHALLENGE_KEY}\n")
    print('flag.enc is Fernet ciphertext. shell.log is the transcript of your ret2libc shell.')
    print('Decrypt flag.enc with the seed you read (Fernet).')

if __name__ == "__main__":
    main()
