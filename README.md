![Header](https://github.com/Moody0101-X/HEDShell/raw/main/img/scr.png)

# HEDShell

## Description

A python based reple that supports hashing and encoding given pieces of text.

## Quick start

```console
$ git clone https://github.com/Moody0101-X/HEDShell
$ cd HEDShell
$ python -m venv venv && ./venv/Scripts/activate
$ pip install -r requirements.txt
$ cd src && main.py
```

## Usage examples

- in this example the reple hashes the string HELLOWWORLD using the `sha256` algorithm.
```console
	[*] -> hash HELLOWWORLD sha256

	0b21b7db59cd154904fac6336fa7d2be1bab38d632794f281549584068cdcb74
```
- to see available hashing algorithms just write hash.

- in the following example the reple encodes the string hello `base16`
```console
	[*] -> encode hello base16
	
	68656C6C6F
```

- to see available hashing algorithms just write encode.
- to decode strings use the decode command as follows
```console
	[*] -> decode 68656C6C6F base16
	
	hello
```

- other commands: `exit`, `help`


