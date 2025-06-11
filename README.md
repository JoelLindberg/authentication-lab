# Authentication lab


## 01_linux_hashes - Hashes in Linux /etc/passwd file

A small experiment to explore password hashes by looking at the hash created in Ubuntu for a user and then using python passlib to verify that the password and the hash verifies.

### Hash Prefixes and Their Algorithms

The hashed passwords in /etc/shadow follow a specific structure: $(id)$..., where the id indicates the hashing algorithm. Common identifiers include:
    
    $1$: MD5-crypt
    $2y$ or $2b$: bcrypt
    $5$: SHA256-crypt
    $6$: SHA512-crypt (default for modern Ubuntu systems)

Ubuntu 24.04 uses yescrypt and apparently passlib doesn't support this.

So for this experiment I temporarily changed what algorithm to be used:

1. `sudo vim /etc/pam.d/common-password`
2. Find the line looking like the below:
    password   [success=1 default=ignore]   pam_unix.so obscure **yescrypt**
3. Replace yescrypt with sha512:
    password   [success=1 default=ignore]   pam_unix.so obscure **sha512**
4. `passwd <user>`
5. Now open `/etc/passwd` and find the user and password you changed.
    After you set a new password you should now see that it starts with **$6**. Copy this hash and use it in the script to verify the password is matching the hash.
6. Don't forget to **revert** the changes back to **yescrypt** in the **/etc/pam.d/common-password** file after you copied the hash.


## 02_fastapi_auth

We will be using fastapi and argon2.

* argon2: https://pypi.org/project/argon2-cffi/
    - https://argon2-cffi.readthedocs.io/en/stable/
    - Source for this package is also referenced here: https://docs.djangoproject.com/en/5.2/topics/auth/passwords/
* fastapi docs as reference:
    - https://fastapi.tiangolo.com/advanced/security/http-basic-auth/
    - https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
        - In case I would like to play with JTW next time: https://jwt.io/


Why use password hasing?

    "If your database is stolen, the thief won't have your users' plaintext passwords, only the hashes.

    So, the thief won't be able to try to use that password in another system (as many users use the same password everywhere, this would be dangerous)."

    - Source: https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#password-hashing


1. python3 -m venv venv
2. source venv/bin/activate
3. python3 -m pip install -r requirements.txt
4. `fastapi dev fastapi_auth.py`
5. Add to header: `Authorization: supersecrettoken` when sending your request:
    - `curl -H 'Authorization: supersecrettoken' http://127.0.0.1:8000/secure-data`



*OAuth 2.0 (OAuth2) is an open standard protocol that allows users to grant third-party applications access to their protected resources without sharing their usernames and passwords*

*OAuth 2.0 is an authorization framework, not an authentication protocol itself.*




