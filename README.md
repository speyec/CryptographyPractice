# Assymetric vs Symmetric
| What I learned from watching a tutorial on how to make a cryptographic algorithm |

--- Asymmetric ---

In order to create the public key and private key, we give them size of 1024 bits and this is also where they are generated. Then we save the public key to public.pem and the private key to private.pem. Loading the private key and public key are relatively simple. 
Encrypted the message is easy and then writing the encrypted message into a text file was easy as well. The process to read the encrypted message from the file it was in was easy; and then writing the code in order to decrypt the message, we had to pass two paramters because the funciton decrypt() needs the encrypted message and then they key that needs to be used in order to decrypt the encrypted message. 
We also use 'wb' and 'rb' instead of 'r' and 'b' because since RSA is working in bytes, we cannot use text 'r' and 'w' to read and write bytes.

============================

For the signing part of the video, we first have to sign our message so we encode it into bytes first and then apply the hashing algorithm (in this case SHA-256) and then we sign the hashed message with the private key. We then write the bytes into a file in order to keep track of the original byte sequence so that if the message ever gets altered after, the program is unable to verify that the message was sent by us. rsa.verify() compares the current encoding of signed_message() to the original decrypted encoding of signed_message() and if the current does not equal orignal, it fails to verify. 

--- Symmetric ---

Fernet is used to generate a symmetric key. We generate a key using .generate_key() and then we comment it out after we write the key into a .key secure file so that it cannot be changed once the program is run again. We do f = Fernet(key) so that we are able to use methods like encrypt() and decrypt() which we do use to encrypt and decrypt the CSV file. 
