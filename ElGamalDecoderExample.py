from sympy import mod_inverse

#Given
q = 310000037
a = 87543455
ciphertext = [
    (56495539, 72767212),
    (62083516, 76971521),
    (181398440, 263421160),
    (149867850, 72743477),
    (14826439, 190288780),
    (113953407, 197793189),
    (117331466, 185360595),
    (291767686, 140312582),
    (97578813, 288144131),
    (66782213, 277003739),
    (189849901, 192777619),
    (147582903, 21503450),
    (154299245, 242826784),
    (86211909, 200694188),
    (31309028, 293758361),
    (21217580, 3535169),
    (79019712, 49185229),
    (213930082, 159557439),
    (73624006, 229408211),
    (292736574, 18644176),
    (237123292, 168250610),
    (38995570, 306955959),
    (199390530, 176530325),
    (226189829, 196581913),
    (195038651, 170658203)
]

#Decrypt function, c1 is the first of the pair for the block and c2 is the second pair, a is Alice's private key and q is the prime
def decryptPair(c1, c2, a, q):
    #s = c1^a % q
    s = pow(c1, a, q)
    #Finds the modular inverse of s (s^-1 mod q)
    sInverse = mod_inverse(s, q)
    #Finds M (= [c2 * s_inv] mod q)
    M = (c2 * sInverse) % q
    return M

#Process all pairs and output each decrypted block
for c1, c2 in ciphertext:
    #Decrypts each ciphertext pair to get M
    M = decryptPair(c1, c2, a, q)

    #Converts M from base-26 to a set of 6-character strings
    blockText = ""
    for i in range(6):
        blockText = chr((M % 26) + ord('a')) + blockText
        M //= 26

    #Print each string on a new line
    print(blockText)
