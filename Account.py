#un compte
#    un client
#   des transactions
#   appartient a une banque et un client
import sys
from datetime import datetime

from Transaction import Transaction


class Account:
    transCount=0

    """
    si id generer à l'exterieur
    """
    def setId(this,id):
        this.id=id

    def getId(this):
        return this.id

    def getDate(this):
        return this.createThe

    """def getName(this):
        return this.name

    def setName(this,name):
        return this.name
    """
    def getSold(this):
        return this.sold
    """
    
    def setSold(this,sold):
        this.sold=sold
    """
    def getTransactions(this):
        return this.transactions

    def setCustomer(this,customer):
        this.customer=customer

    def getCustomer(this):
        return this.customer

    def __init__(this):
        return

    def __init__(this,id):
        this.id=id
        this.sold=0
        this.custumer=None
        this.bank=None
        this.transactions=[]
        this.createThe=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    def __repr__(this):
        return f"{name}"

    def drawBack(this,montant,label):
        if this.getSold()-montant>0 and montant>0:
            this.sold-=montant
            id=transCount=+1
            t=Transaction(id,label,-montant,this,this)
            this.getTransactions().append(t)
            return montant
        else:
            if montant<0 :
                sys.stderr.write('-- transaction not allowed by retire opeation--')
            else:
                sys.stderr.write('-- transaction was refused by retire --not enougth found on account id'+this.getId())
            return 0

    def depose(this,montant,label):
        if montant>0:
            this.sold+=montant
            id=transCount=+1
            t=Transaction(id,label,montant,None,this)
            this.getTransactions().append(t)
            return montant
        else:
            sys.stderr.write('--transaction was refused by depose--negative montant')
            return 0
