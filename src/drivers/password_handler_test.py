from .password_handler import PasswordHandler

def test_encrypt():
    new_password = "test_password"
    password_handler = PasswordHandler()

    hashed_password = password_handler.encrypt_password(new_password)
    password_checked = password_handler.check_password(new_password, hashed_password)
    assert password_checked
