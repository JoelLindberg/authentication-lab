from passlib.context import CryptContext


# Create a CryptContext with common hash schemes used in /etc/shadow
# Multiple algorithms can be specified as below although we will only be verifying a sha512 hash in this exmaple.
shadow_ctx = CryptContext(schemes=["sha512_crypt", "md5_crypt", "des_crypt"], deprecated="auto")

def verify_shadow_hash(password, hash):
    return shadow_ctx.verify(password, hash)

# Verify your hash
shadow_hash = "$6$MeanX3RxuWcuNMws$Y3ZRatXK/A251fMzQFomdDYh6R7ZVIsWCP4CfHEWJQ/Uxe5SXpBcrViQ95Z7zElK9QgvDuLnFS6GTB..LGY.v0"  # Replace with actual shadow hash
password = "FoxieFoxie1"  # Replace with the password to verify
is_valid = verify_shadow_hash(password, shadow_hash)
print(f"Password is valid: {is_valid}")
