# RSA Decryption Script

This Python script demonstrates how to decrypt ciphertext using ElGamal encryption. The decryption process involves using Alice's private key `a` and a prime number `q` to decrypt ciphertext pairs into plaintext messages.

## Features
- **ElGamal Decryption**: The script decrypts each ciphertext pair by applying the ElGamal decryption formula using the private key.
- **Modular Arithmetic**: Uses modular exponentiation to compute intermediate values and modular inverse for decryption.
- **Base-26 Text Conversion**: After decryption, the resulting value is converted to readable text using a base-26 encoding (each block of 6 characters is represented by a number modulo 26).

## Given Values
- **q**: The prime number used in ElGamal encryption.
- **a**: Alice's private key.
- **ciphertext**: List of ciphertext pairs. Each pair contains two integers `c1` and `c2`.

## Functions

### `decryptPair(c1, c2, a, q)`
This function decrypts a pair of ciphertext integers `(c1, c2)` using Alice's private key `a` and the prime number `q`.

- **c1**: First part of the ciphertext pair.
- **c2**: Second part of the ciphertext pair.
- **a**: Alice's private key.
- **q**: The prime number used in the encryption process.

The function computes the shared secret `s` as `s = c1^a % q`, then calculates the modular inverse `s_inv` of `s`, and finally computes `M = (c2 * s_inv) % q` to obtain the decrypted message `M`.

### Process
- Each ciphertext pair is decrypted using the `decryptPair()` function.
- The decrypted result `M` is then converted from a numerical value to a string using a base-26 conversion (each 6-character block is derived from `M`).
- The script outputs each decoded 6-character string on a new line.
