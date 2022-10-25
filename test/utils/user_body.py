def create_valid_user():
    return {
        "email": "teste@tester.com",
        "senha": "teste123"
    }
    
def create_user_admin():
    return {
        "email": "admin@tester.com",
        "senha": "teste123",
        "ativo": True,
        "admin": True
    }
    
def create_invalid_user_deactivated():
    return {
        "email": "deactivated@tester.com",
        "senha": "teste123",
        "ativo": False,
        "admin": False
    }

def create_invalid_user_email():
    return {
        "email": "teste@",
        "senha": "teste123"
    }