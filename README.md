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
