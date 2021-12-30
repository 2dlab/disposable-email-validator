import os
import pickle


def is_disposable_email(email: str) -> bool:
    email = email.split('@')[-1]

    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    with open(os.path.join(__location__, "disposable_emails"), 'rb') as file:
        return email in pickle.load(file)
