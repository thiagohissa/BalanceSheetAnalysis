import math


class Financial:
    @staticmethod
    def calcROI(roi):
        print("Calculating ROI...")
        avg1 = roi[1]
        avg5 = avg10 = 0

        for i in range(1, (len(roi)-1)//2):
            avg5 += roi[i]
        for i in range(1, len(roi)):
            avg10 += roi[i]

        avg1 = round(avg1)
        avg5 = round(avg5/5)
        avg10 = round(avg10/len(roi))
        print("ROI: " + str([avg1, avg5, avg10]) + "\n")
        return [avg1, avg5, avg10]

    @staticmethod
    def calcGrowthRate(financials, financialsName):
        print("Calculating " + financialsName + "'s Growth Rate...")
        current = financials[1]

        # Last Year (1 year):
        initial = financials[2]
        years = 1
        if initial != 0:
            if current / initial > 0:
                avg1 = math.pow(current / initial, 1 / years) - 1
                avg1 = round(avg1 * 100)
            else:
                avg1 = -1
        else:
            avg1 = 100

        # Half (5 years usually):
        initial = financials[len(financials)//2]
        years = len(financials)//2
        if initial != 0:
            if current / initial > 0:
                avg5 = math.pow(current / initial, 1 / years) - 1
                avg5 = round(avg5 * 100)
            else:
                avg5 = -1
        else:
            avg5 = 100

        # Total (10 years usually):
        initial = financials[len(financials)-1]
        years = len(financials)-1
        if initial != 0:
            if current / initial > 0:
                avg10 = math.pow(current / initial, 1 / years) - 1
                avg10 = round(avg10 * 100)
            else:
                avg10 = -1
        else:
            print("AVG10: " + str(initial))
            avg10 = 100

        print(financialsName + "'s Growth Rate: " + str([avg1, avg5, avg10]) + "\n")
        return [avg1, avg5, avg10]




