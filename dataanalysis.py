import tkinter as tk
import Files.filemanager as filemanager
import Finance.company as company
import Finance.financial as financial

master = tk.Tk()


def analyze():
    print("Company Name: %s\nFile Name: %s" % (e1.get(), e2.get()))

    if e2.get():
        data = filemanager.analyzeCompanySheet(e2.get())
    else:
        data = False

    if data:
        print("Data exists")
        analyzedCompany = company.Company(e1.get(), data)
        analyzedCompany.roi = financial.Financial.calcROI(analyzedCompany.roi)
        analyzedCompany.revenue = financial.Financial.calcGrowthRate(analyzedCompany.revenue, "Revenue")
        analyzedCompany.eps = financial.Financial.calcGrowthRate(analyzedCompany.eps, "EPS")
        analyzedCompany.bvps = financial.Financial.calcGrowthRate(analyzedCompany.bvps, "BVPS")
        analyzedCompany.cash = financial.Financial.calcGrowthRate(analyzedCompany.cash, "Cash")
        analyzedCompany.opCash = financial.Financial.calcGrowthRate(analyzedCompany.opCash, "Operating Cash")
        displayAnalyzedData(analyzedCompany)
    else:
        print("\nData is null")
        displayErrorPopup("Something went wrong! Please make sure the file exists")


def displayAnalyzedData(analyzedCompany):
    newWindow = tk.Toplevel(master)
    newWindow.geometry("450x250")
    lblCompanyName = tk.Label(newWindow, text="Company: " + analyzedCompany.name)
    lblReport = tk.Label(newWindow, text="GROWTH REPORT 1, 5, AND 10 YEARS IN % :")
    lblROI = tk.Label(newWindow, text="ROI: " + str(analyzedCompany.roi))
    lblBVPS = tk.Label(newWindow, text="BVPS: " + str(analyzedCompany.bvps))
    lblEPS = tk.Label(newWindow, text="EPS: " + str(analyzedCompany.eps))
    lblRevenue = tk.Label(newWindow, text="Revenue: " + str(analyzedCompany.revenue))
    lblCash = tk.Label(newWindow, text="Cash: " + str(analyzedCompany.cash))
    lblOpCash = tk.Label(newWindow, text="Operating Cash: " + str(analyzedCompany.opCash))
    if filemanager.saveDataToFile(analyzedCompany):
        confirmationText = "This growth report was saved under the 'Analyzed' folder"
    else:
        confirmationText = "Error! Unable to save report"
    lblConfirmation = tk.Label(newWindow, text=confirmationText)

    lblReport.pack()
    lblCompanyName.pack()
    lblROI.pack()
    lblBVPS.pack()
    lblEPS.pack()
    lblRevenue.pack()
    lblCash.pack()
    lblOpCash.pack()
    lblConfirmation.pack()


def displayErrorPopup(errorMessage):
    print("Displaying error popup...")
    popup = tk.Toplevel(master)
    popup.geometry("400x50")
    lblError = tk.Label(popup, text=errorMessage)
    lblError.pack()


if __name__ == '__main__':
    master.title("Balance Sheet Data Analysis Tool")
    master.geometry("420x230")
    tk.Label(master, text="Welcome!").grid(row=0, columnspan=2)
    tk.Label(master, text="Steps to complete before analysis:").grid(row=1, columnspan=2)
    tk.Label(master, text="1 - Export a company's balance sheet from www.morningstar.ca").grid(row=2, columnspan=2)
    tk.Label(master, text="2 - Drop the csv file in the CSVs folder").grid(row=3, columnspan=2, padx=(0,0))
    tk.Label(master, text="3 - Enter the file name below and tap on 'Analyze'").grid(row=4, columnspan=2)
    tk.Label(master, text="Company Name").grid(row=5)
    tk.Label(master, text="Balance Sheet Name").grid(row=6)

    e1 = tk.Entry(master)
    e2 = tk.Entry(master)
    e1.grid(row=5, column=1)
    e2.grid(row=6, column=1)

    tk.Button(master, text='Quit', command=master.quit, width=15).grid(row=7, column=0, sticky=tk.W, padx=(30,0))
    tk.Button(master, text='Analyze', command=analyze, width=15).grid(row=7, column=1, sticky=tk.W, padx=(10,0))

    tk.mainloop()
