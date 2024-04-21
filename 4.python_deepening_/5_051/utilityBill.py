income = 0
waterPrice = 0; electricPrice = 0; gasPrice = 0

def setIncome(ic):
    global income
    income = ic

def getIncome():
    return income


def setWaterPrice(wp):
    global waterPrice
    waterPrice = wp


def getWaterPrice():
    return waterPrice


def setElectricPrice(ep):
    global electricPrice
    electricPrice = ep


def getElectricPrice():
    return electricPrice


def setGasPrice(gp):
    global gasPrice
    gasPrice = gp


def getGasPrice():
    return gasPrice

def getUitliltyBill():
    result = waterPrice + electricPrice + gasPrice
    return result

def getUtilityBillRate():
    result = getUitliltyBill() / getIncome() * 100
    return result

def formatedNumber(n):
    return format(n, ',')