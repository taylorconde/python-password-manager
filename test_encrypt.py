from encryption_service import EncryptionService

master_key = "MySuperSecretKey123"
service = EncryptionService(master_key)

my_website_password = "my_secret_facebook_password"

encrypted = service.encrypt(my_website_password)
print(f"Original: {my_website_password}")
print(f"Encrypted: {encrypted}")

decrypted = service.decrypt(encrypted)
print(f"Decrypted back: {decrypted}")