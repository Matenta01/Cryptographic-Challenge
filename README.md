# 📚 Block Cipher Coursework — Solution

This repository contains my implementation and solution for a custom block cipher exercise.
The task was to implement a simple block cipher that operates on blocks of four decimal digits using a specific permutation and digit-wise addition, then break the cipher using a known plaintext-ciphertext pair to recover the encryption key and decrypt a challenge.

## 📁 Repository Structure

```
Q1/
 ├── encipher.py   # Implements the apprentice's block cipher
 ├── break.py      # Recovers the key using known plaintext and solves the challenge
 ├── challenge.txt # Provided encrypted challenge message
 ├── Key.txt       # Recovered key written as required
```

## ✅ How it works

* **`encipher.py`** — Defines the `encipher()` function that encrypts a 4-digit block using the specified permutation and key-based digit addition.
* **`break.py`** — Implements `breakcipher()` to reverse-engineer the key using the given plaintext-ciphertext pair and decrypt the provided challenge.
* **`Key.txt`** — Contains the recovered key for the apprentice’s cipher.

## 🗝️ How to use

1. **Encrypt** — Run `encipher.py` to test the encryption logic on custom inputs.
2. **Break** — Run `break.py` to recover the key and decrypt the challenge.
3. **Verify** — Check `Key.txt` for the recovered key used to solve the challenge.

## ⚙️ Requirements

* Python 3
* No additional libraries required — follow the constraints (no extra imports).
