from cryptography.fernet import Fernet

# --- GENERATED KEY IN mykey.key HERE --- 
# key = Fernet.generate_key()
# with open('mykey.key', 'wb') as mykey:
#     mykey.write(key)

 # --- This is when someone shares a key with you ---
with open("mykey.key", 'rb') as mykey:
    key = mykey.read()


with open('grades.csv', 'rb') as original_file:
    original = original_file.read()

# Encrypts the file
# f is the way we are able to encrypt the original csv file
f = Fernet(key)
encrypted_csv = f.encrypt(original)

# Writes the encrypted file into a csv called enc_grades.csv
with open('enc_grades.csv', 'wb') as encrypted_file:
    encrypted_file.write(encrypted_csv)

# Decrypts enc_grades.csv using the generated public key 'key'

with open('enc_grades.csv', 'rb') as encrypted:
    encryptedCSV = encrypted.read()
    
decryped_csv = f.decrypt(encryptedCSV)

with open('dec_grades.csv', 'wb') as dec_grades:
    dec_grades.write(decryped_csv)