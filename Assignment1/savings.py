# -*- coding: utf-8 -*-
"""This module contains a code example related to

   the assignment 1 of the CS4000 Intelligent Systems course

   Date: August 19th, 2019
   Authors: A01137566 Campus: Monterrey
            A0... ... Campus: ...
"""

class Bank:
    def __init__(self, name = 'Unnamed'):
        self.name = name
        self.clients = []
        self.unnamedClients = 0
    def report(self, name):
        for
    def findClient(self, client = None):
        if not client:
            return None

        for account in self.clients:
            if account[0] == client:
                return account

        return None

    def deposit(self, client = None, amount = 200):
        '''
        function that deposits certain amount on a clients account
        if the client doesnt exist in the clients list, it creates a new one

        Parameters:
            client (str): The client is used to identify the account

        Returns:
            none,
        '''
        if client == None:
            self.unnamedClients += 1
            client = "client" + str(self.unnamedClients)

        account = self.findClient(client)

        if not account:
            self.clients.append((client, amount))
        else:
            account_to_list = list(account)
            account_to_list[1] += amount
            account = tuple(account_to_list)

def consult(bank = None, client = None):
    if bank == None or client == None:
        print("Please specify the name of the bank and client")
        return

    account = bank.findClient(client)
    if account:
        print(account[0] + " has " + str(account[1]) + " in its " + bank.name + " savings account")
        return
    else:
        print("Error: " + client + " is not a client of " + bank.name + " bank.")
        return

def withdraw(bank, client, amount):
    account = bank.findClient(client)

    if not account:
        print("Error: " + client + " is not a client of " + bank.name + " bank.")
        return
    else:
        if amount > account[1]:
            print(client + " has insufficient funds on its " + bank.name + " savings account.")
            return
        else:
            account_to_list = list(account)
            account_to_list[1] -= amount
            account = tuple(account_to_list)
            print(client + " withdrew " + str(amount) + " from its " + bank.name + " savings account.")
            return

def cancel(bank, client):
    account = bank.findClient(client)

    if not account:
        print("Error: " + client + " is not a client of " + bank.name + " bank.")
        return
    else:
        print(client + " canceled its " + bank.name + " savings account.")
        bank.clients.remove(account)
        return
def report(bank):
    for clients in bank.clients:
        arrayformat[] = s
    return """
            ----------------------------------
            | * {0} bank savings accounts * |
            ----------------------------------
            | Client             | Balance   |
            ----------------------------------
            | {1}                 | $   {2}|
            | {3}                | $     {4}  |
            | {5}             | $     {6}  |
            | {7}                | $   {8}  |
            | {9}             | $   {10} |
            | {11}              | $     {12}  |
            ----------------------------------
            |              Total | $   {13}  |
            ----------------------------------
         """.format(bank)
        return
def cancel_clients(bank, clients):
    for client in clients:
        cancel(bank, client)

def main():
    # create an unnamed bank
    b1 = Bank()
    #print(b1)
    print(b1.name)
    print(b1.clients)
    # add a client ... by depositing an amount in the bank
    b1.deposit('pedro',100)
    #print(b1)
    print(b1.name)
    print(b1.clients)
    # create a BBVA bank
    bbva = Bank("BBVA")
    #print(bbva)
    print(bbva.name)
    print(bbva.clients)
    # add an unnamed client
    bbva.deposit(amount = 2000)
    #print(bbva)
    print(bbva.name)
    print(bbva.clients)
    # add another unnamed client
    bbva.deposit(amount = 500)
    #print(bbva)
    print(bbva.name)
    print(bbva.clients)
    # add Juan as a client ... by default it will deposit 200 pesos
    bbva.deposit('juan')
    #print(bbva)
    print(bbva.name)
    print(bbva.clients)
    # consult the balance for Lupita
    consult(bbva, 'lupita')
    # consult the balance for Juan
    import pdb; pdb.set_trace()
    consult(bbva, 'juan')
    # withdraw 50 pesos from Pedro's account
    withdraw(b1, 'pedro', 50)
    #print(b1)
    print(b1.name)
    print(b1.clients)
    # withdraw 100 pesos from Juan's account
    withdraw(b1, 'juan', 100)
    withdraw(bbva, 'juan', 100)
    #print(bbva)
    print(bbva.name)
    print(bbva.clients)
    # cancel the unnamed client2 account
    cancel(b1, 'client2')
    cancel(bbva, 'client2')
#    print(bbva)
#    # generate a full report for BBVA bank ... all clients
#    report(bbva)

#    # generate a report of clients that have less than 400 pesos at BBVA bank
#    report(bbva, 400)
#    # generate a report of clients that have more than 1000 pesos at BBVA bank
#    report(bbva, gt=1000)
#    # add a list of clients to BBVA bank
#    add_clients(bbva, [450,('hugo',3000),1500,('isabel',750),('juan',250)])
#    report(bbva)
    # cancel the accounts of a list of clients
    cancel_clients(bbva,['juan','roberto','isabel'])
#    report(bbva)
#    # report a list of specific clients
#    report(bbva,clients=['juan','hugo','client1'])
#    print("*** End ***")
#

if __name__ == '__main__':
    main()
