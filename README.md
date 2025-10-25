# Password Strength Analyzer

Simple password strength analysis tool for cybersecurity learners and professionals.  
Checks password complexity and gives real-time feedback on strength and hash security.

---

## Features
- Detects password strength: **WEAK / MODERATE / STRONG**
- Checks character diversity (lowercase, uppercase, digits, special)
- Supports hash types: **MD5, SHA-256, NTLM, bcrypt**
- Gives recommendations based on hash security level
- Clean, color-coded terminal output

---

## Installation
```
# Clone the repository
git clone https://github.com/E2xCoder/Password-Strength-Control.git
cd Password-Strength-Control

# Install required package
pip install colorama


python3 crack_calculator.py "<password>" "<hash_type>"
Example Commands

python3 crack_calculator.py "password" "md5"
python3 crack_calculator.py "MyP@ssw0rd!2024" "bcrypt"
python3 crack_calculator.py "abc123" "sha256"
Supported Hash Types
Hash Type	Status	Note
md5	❌ Legacy	Very weak, avoid
sha256	⚠️ Common	Not safe for password storage
ntlm	⚠️ Windows	Obsolete, crackable
bcrypt	✅ Recommended	Strong and modern

https://ibb.co/1JTc3jNQ

Example Output

============================================================
PASSWORD STRENGTH ANALYSIS
============================================================

Password: MyP@ssw0rd!2024
Hash Type: BCRYPT

Analysis:
  • Length: 13 characters
  • Character Types: 4/4

Character Variety:
  ✓ Lowercase
  ✓ Uppercase
  ✓ Digits
  ✓ Special

============================================================
✅ STRENGTH: STRONG
============================================================

✅ This password is STRONG!
   Good for important accounts.

✅ bcrypt: Good choice for password hashing.
Strength Rules
Strength	Criteria
WEAK	< 8 chars or < 3 character types
MODERATE	8–12 chars with 2–3 types, or 12+ chars with < 3 types
STRONG	≥12 chars with 3+ character types

Security Tips
Always use bcrypt or Argon2 for password hashing.

Avoid MD5, SHA-1, NTLM for password storage.

Use unique passwords for each account.

Consider using a password manager.

Enable 2FA/MFA whenever possible.

Future Plans
Add GPU cracking time estimation

Add Argon2 and PBKDF2 support

Integrate password breach API

Add web version and batch mode

Author
Emre Eren (E2xCoder)
Cybersecurity & Programming Student — Berlin, 2025

License
MIT License


