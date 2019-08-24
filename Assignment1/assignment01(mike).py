class Bank:

    def __init__(self, bank = 'Unnamed'):
        self.bank = bank
        self.clients = []
        self.status = {'bank': self.bank, 'clients': self.clients}
        self.anon_counter=0

    def deposit(self, name = None, amount = 200):
        self.name = name
        self.amount = amount

        if self.name is None:
            self.anon_counter += 1
            self.name = "client" + str(self.anon_counter);
            self.clients.append((self.name, self.amount))
        else:
            self.clients.append((self.name, self.amount))

    def __str__(self):
        return str(self.status)

def consult(bank, name):
    length = len(bank.status['clients'])
    for account in range(0, length):
        if bank.status['clients'][account][0] == name:
            savings = bank.status['clients'][account][1]
            print(name + " has " + str(savings) + " in its BBVA savings account")
            break
    else:
        print("Error: " + name + " is not a client of " + bank.status['bank'] + " bank")

def withdraw(bank, name, withdraw):
    length = len(bank.status['clients'])
    for account in range(0, length):
        if bank.status['clients'][account][0] == name:
            savings = bank.status['clients'][account][1]
            update = savings - withdraw
            bank.status['clients'][account] = (name, update)
            print(name + " withdrew " + str(withdraw) + " from its " + bank.status['bank'] + " savings account")
            break
    else:
        print("Error: " + name + " is not a client of " + bank.status['bank'] + " bank")

def cancel(bank, name):
    length = len(bank.status['clients'])
    for account in range(0, length):
        if bank.status['clients'][account][0] == name:
            del bank.status['clients'][account]
            print(name + " canceled its " + bank.status['bank'] + " savings account")
            break
    else:
        print("Error: " + name + " is not a client of " + bank.status['bank'] + " bank")

def report(bank, lt = None, gt = None, clients = None):
    length = len(bank.status['clients'])
    total = 0
    filter = []
    if clients is not None:
        for name in clients:
            for account in range(0, length):
                if name == bank.status['clients'][account][0]:
                    filter.append(bank.status['clients'][account])
                    break
            else:
                print("Error: " + name + " is not a client of " + bank.status['bank'] + " bank")
        filter.sort(key=lambda x: x[1], reverse=True)
    else:
        filter = bank.status['clients']
    length = len(filter)

    import locale
    locale.setlocale(locale.LC_ALL, '')
    print("----------------------------------")
    print("| * BBVA bank savings accounts * |")
    print("----------------------------------")
    print("| Client             | Balance   |")
    print("----------------------------------")
    for account in range (0, length):
        name = filter[account][0]
        savings = filter[account][1]
        if lt is None and gt is None:
            total += savings
            print("| " + '{:<7}'.format(name) + "            | $" + '{:>8}'.format(f'{savings:n}') + " |")
        elif lt is not None:
            if savings < lt:
                total += savings
                print("| " + '{:<7}'.format(name) + "            | $" + '{:>8}'.format(f'{savings:n}') + " |")
        elif gt is not None:
            if savings > gt:
                total += savings
                print("| " + '{:<7}'.format(name) + "            | $" + '{:>8}'.format(f'{savings:n}') + " |")
    print("----------------------------------")
    print("|              Total | $" + '{:>8}'.format(f'{total:n}')+ " |")
    print("----------------------------------")

def add_clients(bank, clients):
    length = len(bank.status['clients'])
    new = 0
    deposits = 0
    for account in clients:
        if type(account) == tuple:
            for tup in range (0, length):
                if account[0] == bank.status['clients'][tup][0]:
                    update = account[1] + bank.status['clients'][tup][1]
                    bank.status['clients'][tup] = (account[0], update)
                    deposits += 1
                    break
            else:
                bank.clients.append(account)
                new += 1
        else:
            bank.anon_counter += 1
            bank.clients.append(("client" + str(bank.anon_counter), account))
            new += 1
    print("Added " + str(new) + " new clients and " + str(deposits) + " deposit to " + bank.status['bank'] + " bank")
    print(bank)

def cancel_clients(bank, clients):
    for name in clients:
        length = len(bank.status['clients'])
        for account in range (0, length):
            if name == bank.status['clients'][account][0]:
                del bank.status['clients'][account]
                print(name + " canceled its " + bank.status['bank'] + " savings account")
                break
        else:
            print("Error: " + name + " is not a client of " + bank.status['bank'] + " bank")

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
    main() #yields expected output as seen in assignment01(template).py
