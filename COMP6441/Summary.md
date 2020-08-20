# The puzzle as a whole
So far we've spend alot of time trying solving the age old puzzle of how to communicate while retaining: 

* **C**onfidentiality 
* **I**ntegritiy
* **A**vailability

# Clues to our puzzle
## Confidentiality 

Confidentiality means only the people who we want to read the message can read our message. 

This can be ensured using: 

* Diffie Hellman Key-Exchange 
* Digital Signitures (RSA etc.) 
* AES 
* OTP and other encrpytion methods, but OTP being the strongest 

## Integrity 

Integrity means that the content of the message must remain the same on both ends of the conversation. 

This can be verified using 

* Hashing (e.g.MAC/HMAC, SHA-1, SHA-2) 
* AES

# Combining our clues 

## Diffie Hellman Key Exchange 

..is solely used for an initial key exchange, and is often extended upon by RSA. 

## Digital Signitures 

..verify the sender of a message using public/private keys

* Asymmetric 
* E.g. RSA, where a public and private key is based on the product of two large prime numbers 

## AES 
..is a method of encrypting data using [maths which I mentioned in my previous post](https://jennax-seceng.tumblr.com/post/187300232301/aes-adv-encryption-standard) 

* Symmetric
* uses block ciphers (128bit, 192bit or 256bit) 

## Hashing 

..is a method of quickly map a data on unknown size onto a piece of data of known size. 

* MAC (`H(K| M)` Hashing the key and the message) 
  * Vulnerable to length extension attacks - But can be fixed with a salt 
  * Even with a salt, it is prone to brute-forcing
*