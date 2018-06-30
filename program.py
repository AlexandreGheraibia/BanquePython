from Account import Account
from Customer import Customer

if __name__=="__main__":
    account=Account(0)
    account.setCustomer(Customer(0,"alex"))
    account.depose(1100,"salaire")
    account.drawBack(50,"mutuelle")
    account.depose(150,"prime à l'emploi")
    account.drawBack(60,"gaz éléctricite")
    account.drawBack(100,"retrait distributeur")
    print("%s"%((account.getCustomer()).getName()))
    for t in account.getTransactions():
        print("%s"%{t.getDate()},"|",f"%.2f"%t.getMontant(),"\t|\t",t.getLabel())

