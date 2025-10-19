#!/usr/bin/env python3
"""
Simple Password Strength Calculator
Determines if password is WEAK or STRONG based on hash type
"""

import sys                                  # For command-line arguments
from colorama import Fore, Style, init      # For colored terminal output

init(autoreset=True)                        # Initialize colorama

def get_character_pool(password):
    """Calculate character pool and check character types"""
    pool = 0
    has_lower = any(c.islower() for c in password)       # Check for lowercase
    has_upper = any(c.isupper() for c in password)       # Check for uppercase
    has_digit = any(c.isdigit() for c in password)       # Check for digits
    has_special = any(c in '!@#$%^&*()_+-=[]{}|;:,.<>?~`' for c in password) # Check for special chars  
    
    if has_lower: pool += 26    # a-z
    if has_upper: pool += 26    # A-Z
    if has_digit: pool += 10    # 0-9
    if has_special: pool += 32      # Common special characters
    
    return pool, has_lower, has_upper, has_digit, has_special


def calculate_strength(password, hash_type):
    """Determine password strength based on character pool and length"""
    
    pool, has_lower, has_upper, has_digit, has_special = get_character_pool(password)
    
    if pool == 0:
        return None
    
    length = len(password)
    
    # Simple strength criteria (no specific GPU/hash speeds) (soon will add more complex calc)
    # Just based on character diversity and length
    
    char_types = sum([has_lower, has_upper, has_digit, has_special])
    
    # Determine strength
    if length < 8:
        strength = "WEAK"
        color = Fore.RED        # Strong red for weak
        emoji = "❌"
    elif length < 12:
        if char_types < 3:
            strength = "WEAK"
            color = Fore.RED
            emoji = "❌"
        else:
            strength = "MODERATE"
            color = Fore.YELLOW
            emoji = "⚠️"
    else:  # 12+ characters
        if char_types >= 3:
            strength = "STRONG"
            color = Fore.GREEN
            emoji = "✅"
        else:
            strength = "MODERATE"
            color = Fore.YELLOW
            emoji = "⚠️"
    
    return {
        'strength': strength,
        'color': color,
        'emoji': emoji,
        'length': length,
        'pool': pool,
        'has_lower': has_lower,
        'has_upper': has_upper,
        'has_digit': has_digit,
        'has_special': has_special,
        'char_types': char_types
    }





def print_analysis(data, password, hash_type):
    """Pretty print the analysis"""
    
    print(f"\n{Fore.CYAN}{'='*60}")
    print(f"{Fore.CYAN}PASSWORD STRENGTH ANALYSIS")
    print(f"{Fore.CYAN}{'='*60}\n")
    
    print(f"Password: {Fore.YELLOW}{password}{Style.RESET_ALL}")
    print(f"Hash Type: {Fore.LIGHTBLUE_EX}{hash_type.upper()}{Style.RESET_ALL}")
    
    print(f"\n{Fore.WHITE}Analysis:")
    print(f"  • Length: {data['length']} characters")
    print(f"  • Character Types: {data['char_types']}/4")
    
    print(f"\n{Fore.WHITE}Character Variety:")
    chars = [
        ("Lowercase", data['has_lower']),
        ("Uppercase", data['has_upper']),
        ("Digits", data['has_digit']),
        ("Special", data['has_special'])
    ]
    for char_type, present in chars:
        status = f"{Fore.GREEN}✓{Style.RESET_ALL}" if present else f"{Fore.RED}✗{Style.RESET_ALL}"
        print(f"  {status} {char_type}")
    
    print(f"\n{Fore.CYAN}{'='*60}")
    print(f"{data['color']}{data['emoji']} STRENGTH: {data['strength']}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*60}\n")
    
    # Recommendation
    if data['strength'] == "STRONG":
        print(f"{Fore.GREEN}✅ This password is STRONG!{Style.RESET_ALL}")
        print(f"{Fore.GREEN}   Good for important accounts.{Style.RESET_ALL}")
    elif data['strength'] == "MODERATE":
        print(f"{Fore.YELLOW}⚠️  This password is MODERATE.{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}   Consider making it longer or more complex.{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}❌ This password is WEAK!{Style.RESET_ALL}")
        print(f"{Fore.RED}   Make it at least 12 characters with mixed types.{Style.RESET_ALL}")
    
    # Hash type info
    if hash_type == 'bcrypt':
        print(f"\n{Fore.LIGHTGREEN_EX}✅ bcrypt: Good choice for password hashing.{Style.RESET_ALL}")
    else:
        print(f"\n{Fore.LIGHTYELLOW_EX}⚠️  {hash_type.upper()}: Legacy hash. Use bcrypt or Argon2.{Style.RESET_ALL}")
    
    print()


def main():
    if len(sys.argv) < 3:
        print(f"\n{Fore.CYAN}Usage: python3 crack_calculator.py <password> <hash_type>\n")
        print(f"{Fore.WHITE}Hash types: md5, sha256, ntlm, bcrypt\n")
        print(f"{Fore.LIGHTGREEN_EX}Examples:{Style.RESET_ALL}")
        print(f"  python3 crack_calculator.py 'password' md5")
        print(f"  python3 crack_calculator.py 'MyP@ssw0rd!2024' bcrypt")
        print(f"  python3 crack_calculator.py 'abc123' sha256\n")
        sys.exit(1)
    
    password = sys.argv[1]      # Password from command line
    hash_type = sys.argv[2].lower()     # Hash type from command line
    
    # Validate
    valid_types = ['md5', 'sha256', 'ntlm', 'bcrypt']   # Supported hash types
    if hash_type not in valid_types:
        print(f"{Fore.RED}❌ Invalid hash type '{hash_type}'")
        print(f"{Fore.WHITE}Valid types: {', '.join(valid_types)}\n")
        sys.exit(1)
    
    # Calculate
    data = calculate_strength(password, hash_type)
    
    if data is None:
        print(f"{Fore.RED}❌ Error: Password is empty\n")
        sys.exit(1)
    
    # Print
    print_analysis(data, password, hash_type)


if __name__ == '__main__': 
    main()  
