"""This module contains a code example related to

   the assignment 1 of the CS4000 Intelligent Systems course
   
   Date: August .., 2019
   Authors: A0... ... Campus: ...
            A0... ... Campus: ...
"""

class Bank:
    """Represents a savings bank, a financial institution for savings accounts.

    attributes: ..."""

    # add methods ...
    

# add some additional functions ...


def main():
    # create an unnamed bank
    b1 = Bank()
    print(b1)
    # add a client ... by depositing an amount in the bank
    b1.deposit('pedro',100)
    print(b1)
    # create a BBVA bank
    bbva = Bank("BBVA")
    print(bbva)
    # add an unnamed client
    bbva.deposit(amount = 2000)
    print(bbva)
    # add another unnamed client
    bbva.deposit(amount = 500)
    print(bbva)
    # add Juan as a client ... by default it will deposit 200 pesos
    bbva.deposit('juan')
    print(bbva)
    # consult the balance for Lupita
    consult(bbva, 'lupita')
    # consult the balance for Juan
    consult(bbva, 'juan')
    # withdraw 50 pesos from Pedro's account
    withdraw(b1, 'pedro', 50)
    print(b1)
    # withdraw 100 pesos from Juan's account
    withdraw(b1, 'juan', 100)
    withdraw(bbva, 'juan', 100)
    print(bbva)
    # cancel the unnamed client2 account
    cancel(b1, 'client2')
    cancel(bbva, 'client2')
    print(bbva)
    # generate a full report for BBVA bank ... all clients
    report(bbva)
    # generate a report of clients that have less than 400 pesos at BBVA bank
    report(bbva, 400)
    # generate a report of clients that have more than 1000 pesos at BBVA bank
    report(bbva, gt=1000)
    # add a list of clients to BBVA bank
    add_clients(bbva, [450,('hugo',3000),1500,('isabel',750),('juan',250)])
    report(bbva)
    # cancel the accounts of a list of clients
    cancel_clients(bbva,['juan','roberto','isabel'])
    report(bbva)
    # report a list of specific clients
    report(bbva,clients=['juan','hugo','client1'])
    print("*** End ***")


if __name__ == '__main__':
    main()

