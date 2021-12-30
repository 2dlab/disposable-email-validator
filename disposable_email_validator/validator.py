import pickle


def is_disposable_email(email: str) -> bool:
    email = email.split('@')[-1]

    with open('disposable_email_validator/disposable_emails', 'rb') as file:
        return email in pickle.load(file)
