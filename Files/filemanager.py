DIR_PATH = "CSVs/"


def analyzeCompanySheet(fileName):
    print("Analyzing company sheet named: " + str(fileName))
    try:
        f = open(DIR_PATH + fileName, "r")
        trimmed = trimFinancials(f)
        f.close()
        revenue = convertSTRListToFloatList(trimmed[0])
        eps = convertSTRListToFloatList(trimmed[1])
        bvps = convertSTRListToFloatList(trimmed[2])
        opCash = convertSTRListToFloatList(trimmed[3])
        cash = convertSTRListToFloatList(trimmed[4])
        roi = convertSTRListToFloatList(trimmed[5])
        print("\n\nConverted and trimmed results:\n")
        print("Revenue: " + str(revenue))
        print("EPS: " + str(eps))
        print("BVPS: " + str(bvps))
        print("Operating Cash: " + str(opCash))
        print("Cash: " + str(cash))
        print("ROI: " + str(roi))
        print("\n")
        return [revenue, eps, bvps, opCash, cash, roi]
    except FileNotFoundError as e:
        print("File not found")
        return False



def printFile(file):
    for x in file:
        print(x)


def trimFinancials(file):
    print("\nTrimming financial stats...\n")
    revenue = eps = bvps = opCash = cash = roi = ""
    for line in file:
        if "Revenue USD" in line:
            revenue = line
        elif "Earnings Per Share" in line:
            eps = line
        elif "Book Value Per Share" in line:
            bvps = line
        elif "Operating Cash Flow USD" in line:
            opCash = line
        elif "Free Cash Flow USD" in line:
            cash = line
        elif "Return on Invested Capital" in line:
            roi = line

    print("Revenue: " + str(revenue))
    print("EPS: " + str(eps))
    print("BVPS: " + str(bvps))
    print("Operating Cash: " + str(opCash))
    print("Cash: " + str(cash))
    print("ROI: " + str(roi))

    revenue = revenue.split(",", 1)[1]
    revenue = revenue.replace(",", "")
    revenue = revenue.replace("\n", "")
    revenue = revenue.split("\"")
    revenue = list(filter(None, revenue))

    eps = eps.split(",", 1)[1]
    eps = removeUnwantedChars(eps)

    bvps = bvps.split(",", 1)[1]
    bvps = removeUnwantedChars(bvps)

    opCash = opCash.split(",", 1)[1]
    opCash = removeUnwantedChars(opCash)

    cash = cash.split(",", 1)[1]
    cash = removeUnwantedChars(cash)

    roi = roi.split(",", 1)[1]
    roi = removeUnwantedChars(roi)

    # print("Revenue: " + str(revenue))
    # print("EPS: " + str(eps))
    # print("BVPS: " + str(bvps))
    # print("Operating Cash: " + str(opCash))
    # print("Cash: " + str(cash))
    # print("ROI: " + str(roi))
    return [revenue, eps, bvps, opCash, cash, roi]


def removeUnwantedChars(financialStr):
    financialStr = financialStr.replace("\"", "")
    financialStr = financialStr.replace("\n", "")
    financialList = financialStr.split(",")
    return financialList


def convertSTRListToFloatList(aList):
    for i in range(0, len(aList)):
        if aList[i] == '':
            aList[i] = 0
        aList[i] = float(aList[i])
    return aList


def saveDataToFile(analyzedCompany):
    try:
        f = open(DIR_PATH + "/Analyzed/" + analyzedCompany.name + "_Analyzed.txt", "w")
        dataSTR = "\nCOMPANY: " + str(analyzedCompany.name)
        dataSTR += "\n\nGROWTH REPORT 1, 5, AND 10 YEARS IN % :"
        dataSTR += "\nROI: " + str(analyzedCompany.roi)
        dataSTR += "\nBVPS: " + str(analyzedCompany.bvps)
        dataSTR += "\nEPS: " + str(analyzedCompany.eps)
        dataSTR += "\nREVENUE: " + str(analyzedCompany.revenue)
        dataSTR += "\nCASH: " + str(analyzedCompany.cash)
        dataSTR += "\nOPERATING CASH: " + str(analyzedCompany.opCash)
        f.write(dataSTR)
        f.close()
        return True
    except:
        return False


analyzeCompanySheet("FB Key Ratios.csv")

