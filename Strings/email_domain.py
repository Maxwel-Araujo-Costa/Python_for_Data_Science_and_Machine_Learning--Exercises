#Create a function that grabs the email website domain from a string in the form:

#user@domain.com

#So for example, passing "user@domain.com" would return: domain.com

email = 'user@domain.com'
def domainGet(e):
    domain = e.split('@')
    return domain[-1]
print(domainGet(email))