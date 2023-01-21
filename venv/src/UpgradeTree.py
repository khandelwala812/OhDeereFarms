from Currency import *
plantCorn = true;
plantWheat = false;
plantBeans = false;

#returns 1 if successful buy, 0 if not
#                 corn(10)
#        (15)beans - | - wheat(15)
#
#
#


def upgradeCorn():
    if not(plantCorn) & getCurrency >= 10:
        subCurrency(10)
        return 1
    return 0

def upgradeWheat():
    if plantCorn & getCurrency >= 15:
        subCurrency(15)
        return 1
    return 0

def upgradeBeams():
    if plantCorn & getCurrency >= 15:
        subCurrency(15)
        return 1
    return 0