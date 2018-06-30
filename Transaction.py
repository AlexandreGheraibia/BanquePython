from datetime import datetime
class Transaction:
    def __init__(this):
        return
    def __init__(this,id,label,montant,fromTo,goTo):
        this.id=id
        this.label=label
        this.montant=montant
        this.date=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        this.fomTo=fromTo
        this.goTo=goTo

    """ def setId(this,id):
        this.id=id
    """

    def getId(this):
        return this.id

    def setLabel(this,label):
        this.label=label

    def getLabel(this):
        return this.label

    def getFromTo(this):
        return this.fomTo

    def getGoTo(this):
        return this.goTo

    def getDate(this):
        return this.date

    def getMontant(this):
        return this.montant
