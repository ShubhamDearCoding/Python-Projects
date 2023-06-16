master_pwd = input("What is the master password? ")

def view() :
     pass

 def add():
       name = input('Account name: ') 
       pwd = input("Password: ")  

       with open('passwords.txt', 'w') as f:
             f.write(name + " " + pwd)