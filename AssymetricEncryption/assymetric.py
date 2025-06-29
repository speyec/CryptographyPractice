import rsa
from pathlib import Path
base_directory = Path(__file__).parent

# --- CREATES PUBLIC AND PRIVATE KEY ---

# public_key, private_key = rsa.newkeys(1024)
# with open(base_directory / 'public.pem', 'wb') as f:
#     f.write(public_key.save_pkcs1("PEM"))
# with open(base_directory / 'private.pem', 'wb') as f:
#     f.write(private_key.save_pkcs1("PEM"))

# ------------------------------------------------------

with open(base_directory / 'public.pem', 'rb') as f:
    public_key = rsa.PublicKey.load_pkcs1(f.read())

with open(base_directory / 'private.pem', 'rb') as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())

message = "Hello my password is jumping_jacks"

encrypted_message = rsa.encrypt(message.encode(), public_key)

with open(base_directory / 'encrypted.message', 'wb') as f:
    f.write(encrypted_message)

# encrypt_message = open(base_directory / 'encrypted.message', 'rb').read()
with open(base_directory / 'encrypted.message', 'rb') as e:
    encrypt_message = e.read()

clear_message = rsa.decrypt(encrypt_message, private_key)
with open(base_directory / 'clear.message', 'wb') as c:
    c.write(clear_message)


# ----------------------------------------------------------

# SIGNING A MESSAGE

signed_message = "I am verifying his message"
sig_signed_message = rsa.sign(signed_message.encode(), private_key, 'SHA-256')

# If you remove this with open() and change signed_message and run the program again
# the program will fail to verify since the message has been altered
with open(base_directory / 'signature', 'wb') as f:
    f.write(sig_signed_message)

with open(base_directory / 'signature', 'rb') as f:
    verified_sig = f.read()

print(rsa.verify(signed_message.encode(), verified_sig, public_key))
 