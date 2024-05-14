# Generate email addresses
    def generate_email(name):
        # Split student name into first name and last name
        parts = name.split()
        first_name = parts[0]
        last_name = parts[-1] if len(parts) > 1 else ""
        # Remove special characters such as ' from last name using regular expressions
        last_name = re.sub(r'[^a-zA-Z]', '', last_name)
        # Generate email address
        email = f"{first_name[0]}{last_name}@gmail.com".lower()
        return email
