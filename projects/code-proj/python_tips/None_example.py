print(type(None)) # <class 'NoneType'>

def email(subject, content, to, cc=None, bcc=None):
    print(f" {subject}, {content}, {to}, {cc}, {bcc}")

email(None, "great work", "test@gmail.com") # None, great work, test@gmail.com, None, None

var = None
if var is None:
    print("do something") # do something
