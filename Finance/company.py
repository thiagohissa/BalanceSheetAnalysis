class Company:
    def __init__(self, name, data):
        self.name = name
        self.revenue = data[0]
        self.eps = data[1]
        self.bvps = data[2]
        self.opCash = data[3]
        self.cash = data[4]
        self.roi = data[5]

