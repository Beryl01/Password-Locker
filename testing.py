#!/usr/bin/env python3.6
from user import User
from credential import Credential
import random
def create_user(fname, lname, phone, email):
    """
    Function to create a new user
    """
    new_user = User(fname, lname, phone, email)
    return new_user

def create_credential(uname, pword, email):
    """
    Function to create new user credentials
    """
    new_credential = Credential(uname, pword, email)
    return new_credential

def save_user(user):
    """
    Function to save user
    """
    user.save_user_details()

def save_cred(credential):
    """
    Function to save user credentials
    """
    credential.save_credential()

