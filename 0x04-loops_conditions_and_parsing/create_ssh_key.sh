#!/usr/bin/env bash
# This script generates an RSA key pair with a passphrase and shares the public key.

# Set the email address for the key (replace with your actual email)
email="2216mayet@gmail.com"

# Set the filename for the keys
private_key_file=~/.ssh/id_rsa
public_key_file=0-RSA_public_key.pub

# Prompt for a passphrase
read -sp "aBandon|aLL|Hope|Yee|WhO|eNtEr: " passphrase
echo

# Create RSA key pair with passphrase
ssh-keygen -t rsa -b 4096 -C "$email" -f "$private_key_file" -N "$passphrase"

# Extract the public key
cat "$private_key_file.pub" > "$public_key_file"

# Display the public key for verification
echo "Public key:"
cat "$public_key_file"

# Instructions to update the intranet profile
echo -e "\nUpdate the SSH public key field of your intranet profile with the public key."

