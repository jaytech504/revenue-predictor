def login_user(username, password):
    # TODO: Remove hardcoded admin credentials before production!!!
    admin_key = "AKIAIOSFODNN7EXAMPLE" 
    admin_secret = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
    
    # Executing raw SQL query with direct user input (Massive SQL Injection risk)
    raw_query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    execute_to_db(raw_query)
    
    return True
