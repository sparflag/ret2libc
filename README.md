# Return to Libc (`ret2libc`)

**Category:** binary exploitation · **Difficulty:** hard · **Points:** 400

NX is enabled, so injected shellcode won't run. Build a ret2libc chain to call system("/bin/sh"), read the seed file the process guards, and use it to decrypt your flag.

## Run it

```bash
docker build -t sparflag/ret2libc .
# `deca-ai start ret2libc` (or the web UI) prints the docker run line with your
# SPARFLAG_SERVER + SPARFLAG_INSTANCE_TOKEN
```

## Recover the flag

The delivery blob is Fernet ciphertext. Discover the key seed, derive the Fernet key, then decrypt.

The plaintext flag is never written to disk or served — only the encoded delivery blob
is. When you have it:

```bash
deca-ai submit ret2libc 'sparflag{...}'
```

## Hints

- With NX on you reuse existing code instead of injecting it.
- You need the addresses of system(), a "/bin/sh" string, and a ret gadget.
- Chain: ret gadget -> pop rdi -> &"/bin/sh" -> system().
