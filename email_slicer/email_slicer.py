#!/usr/bin/env python3

def main():
    print("Email Slicer")
    print("")

    # collect email from user
    email_input = input("Input your email address: ")

    # split the email using the @
    # the first part as the username
    # the second part is going to be saved as domain
    (username, domain) = email_input.split("@")

    # split domain using '.'
    (domain, extension) = domain.split(".")

    print("USername: ", username)
    print("Domain: ", domain)
    print("Extension: ", extension)


while True:
    main()
