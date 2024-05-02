import pandas as pd
import sys
import getpass
from datetime import date,datetime,timedelta
from abc import ABC, abstractmethod

class Decorate:
    def logindesign(self):
        print("           ---------***---------")
        print("   ","~"*16,"*","~"*16)
        print(" |                                       |")
        print(" |                WELCOME                |")
        print(" |                  TO                   |")
        print(" |             MONEY MANAGER             |")
        print(" |                                       |")
        print("   ","~"*16,"*","~"*16)
        print("           ---------***---------")
    def exitdesign(self):
        print(' -'*20)
        print("|         Exiting MONEY MANAGER          |")
        print("|          ©Emtiaz Ahmed 2024            |")
        print(' -'*20)
    def maindesign(self):
        print(' -'*20)
        print('|             MONEY MANAGER             |')
        print('|              MAIN MENU                |')
        print(' -'*20)
    def saveincomedesign(self):
        print(' -'*20)
        print('|             MONEY MANAGER             |')
        print('|             SAVE INCOME               |')
        print(' -'*20)
    def saveexpensedesign(self):
        print(' -'*20)
        print('|             MONEY MANAGER             |')
        print('|             SAVE EXPENSE              |')
        print(' -'*20)
    def displayincomedesign(self):
        print(' -'*20)
        print('|             MONEY MANAGER             |')
        print('|             INCOME RECORD             |')
        print(' -'*20)
    def allincomedesign(self):
        print(' -'*20)
        print('|              ALL INCOME               |')
        print(' -'*20)
    def dailyincomedesign(self):
        print(' -'*20)
        print("|             TODAY'S INCOME             |")
        print(' -'*20)
    def weeklyincomedesign(self):
        print(' -'*20)
        print('|             WEEKLY INCOME             |')
        print(' -'*20)
    def monthlyincomedesign(self):
        print(' -'*20)
        print('|             MONTHLY INCOME            |')
        print(' -'*20)
    def yearlyincomedesign(self):
        print(' -'*20)
        print('|             YEARLY INCOME             |')
        print(' -'*20)
    def displayexpensedesign(self):
        print(' -'*20)
        print('|             MONEY MANAGER             |')
        print('|             EXPENSE RECORD            |')
        print(' -'*20)
    def allexpensedesign(self):
        print(' -'*20)
        print('|              ALL EXPENSE              |')
        print(' -'*20)
    def dailyexpensedesign(self):
        print(' -'*20)
        print("|            TODAY'S EXPENSE            |")
        print(' -'*20)
    def weeklyexpensedesign(self):
        print(' -'*20)
        print('|            WEEKLY EXPENSE             |')
        print(' -'*20)
    def monthlyexpensedesign(self):
        print(' -'*20)
        print('|           MONTHLY EXPENSE             |')
        print(' -'*20)
    def yearlyexpensedesign(self):
        print(' -'*20)
        print('|            YEARLY EXPENSE             |')
        print(' -'*20)
    def searchedesign(self):
        print(' -'*20)
        print('|           SEARCHING RECORDS           |')
        print(' -'*20)
    def deleteincomedesign(self):
        print(' -'*20)
        print('|         DELETE INCOME RECORDS         |')
        print(' -'*20)
    def deleteexpensedesign(self):
        print(' -'*20)
        print('|        DELETE EXPENSE RECORDS         |')
        print(' -'*20)

class create_login:
    @staticmethod
    def create_account():
        try:
            name = input(" Enter your name: ")
            __pin = int(getpass.getpass(" Enter your PIN: "))
        except:
            print(" Please enter valid inputs")
            return
        # Load existing data from Excel file
        try:
            df = pd.read_excel("user_accounts.xlsx")
        except FileNotFoundError:
            print(" user_accounts.xlsx file not found")

        # Check if name and id already exist together
        check = df[(df['Name'] == name)]
        if not check.empty:
            print(" Account with the same name already exists.")
        else:
            # Add new user to DataFrame using loc
            df.loc[len(df)] = [name, __pin]
            # Write updated DataFrame to Excel file
            df.to_excel("user_accounts.xlsx", index=False)
            print(" Account created successfully.")
    @staticmethod
    def login():
        # Load existing data from Excel file (if exists)
        try:
            df = pd.read_excel("user_accounts.xlsx")
        except FileNotFoundError:
            print(" user_accounts.xlsx file not found")
        try:
            name = input(" Enter your name: ")
            pin = int(getpass.getpass(" Enter your Password: "))
        except:
            print(" Please enter valid inputs")
            return

        # Check if name and id exist together in the DataFrame
        check = df[(df['Name'] == name) & (df['PIN'] == pin)]
        # print(check)
        if not check.empty:
            print(f" Login successful. Logging in {name}'s account")
            Menu.MainMenu(name)
        else:
            print(" Invalid name or PIN. Please try again.")
            Menu.LoginMenu()

class Entry:
    def __init__(self, name, category, amount):
        self.time = date.today()
        self.category = category
        self.amount = amount
        self.name = name
    def SaveEntry(self,filename):
        try:
            df = pd.read_excel(filename,sheet_name=self.name)
        except:
            df=pd.DataFrame(columns=["Date", "Category", "Amount"])
            with pd.ExcelWriter(filename, mode='w') as writer:
                df.to_excel(writer, sheet_name=self.name, index=False)
        df.loc[len(df)]=[self.time,self.category,self.amount]
        with pd.ExcelWriter(filename,mode='a',if_sheet_exists='overlay') as writer:
            df.to_excel(writer,sheet_name=self.name,index=False)

class SaveIncome(Entry): #inherit from Entry class
    def __init__(self, name, category, amount): #overriding Entry class __init__() method
        super().__init__(name, category, amount)
        super().SaveEntry('income_record.xlsx')
        print(" Income record updated successfully")

class SaveExpense(Entry):
    def __init__(self, name, category, amount):
        super().__init__(name, category, amount)
        super().SaveEntry('expense_record.xlsx')
        print(" Expense record updated successfully")

class Goal:
    def set_goal(self, name, goal):
        try:
            df = pd.read_excel('goal.xlsx')
        except FileNotFoundError:
            df = pd.DataFrame(columns=['Name', 'Goal'])
        # Check if the name already exists in the DataFrame
        if name in df['Name'].values:
            # Update the goal for the existing name
            df.loc[df['Name'] == name, 'Goal'] = goal
        else:
            # Add a new row with the provided name and goal
            df = df.append({'Name': name, 'Goal': goal}, index=False)
        # Write the DataFrame back to the file
        df.to_excel('goal.xlsx', index=False)
    def get_goal(self, name):
        try:
            df = pd.read_excel('goal.xlsx')
        except FileNotFoundError:
            print(" The goal file doesn't exist.")

        check = df[df['Name'] == name]
        if not check.empty:
            print(f" Your present Goal is: {check.iloc[0, 1]}")
        else:
            print(" The user still hasn't set any goal yet.")

class Display(ABC):
    def __init__(self,name,filename):
        self.name=name
        self.filename=filename
    @abstractmethod
    def all(self):
        pass
    @abstractmethod
    def daily(self):
        pass
    @abstractmethod
    def weekly(self):
        pass
    @abstractmethod
    def monthly(self):
        pass
    @abstractmethod
    def yearly(self):
        pass

class DisplayIncome(Display):
    def all(self):
        try:
            df=pd.read_excel(self.filename,sheet_name=self.name)
            if len(df)!=0:
                print(df) #to remove index use df.to_string(index=False)
                print(f" {self.name}'s Total Amount of Income: {df.iloc[:,2].sum()}")
            else:
                print(f" There has no income record for {self.name}")
        except:
            print(f" There has no income record for {self.name}")
    def daily(self):
        try:
            df=pd.read_excel(self.filename,sheet_name=self.name)
            if len(df)!=0:
                df['Date'] = pd.to_datetime(df['Date'])
                self.targetdate = datetime.now().strftime("%Y-%m-%d")
                df=df.loc[df["Date"]>=self.targetdate]
                if len(df)!=0:
                    print(df.to_string(index=False))
                    self.daily_total= df.loc[df['Date']>=self.targetdate,'Amount'].sum()
                    print(f" {self.name}'s Total Amount of Today's Income : {self.daily_total}")
                else:
                    print(f" There has no daily income record for {self.name}")
            else:
                print(f" There has no income record for {self.name}")
        except:
            print(f" There has no income record for {self.name}")
    def weekly(self):
        try:
            df=pd.read_excel(self.filename,sheet_name=self.name)
            if len(df)!=0:
                df['Date'] = pd.to_datetime(df['Date'])
                self.current_date = datetime.now()
                self.targetdate= self.current_date - timedelta(weeks=1)
                df=df.loc[df["Date"]>=self.targetdate]
                if len(df)!=0:
                    print(df.to_string(index=False))
                    self.weekly_total= df.loc[df['Date']>=self.targetdate,'Amount'].sum()
                    print(f" {self.name}'s Total Amount of Weekly Income from {self.targetdate.strftime('%Y-%m-%d')} to {self.current_date.strftime('%Y-%m-%d')} : {self.weekly_total}")
                else:
                    print(f" There has no weekly income record for {self.name}")
            else:
                print(f" There has no income record for {self.name}")
        except:
            print(f" There has no income record for {self.name}")
    def monthly(self):
        try:
            df=pd.read_excel(self.filename,sheet_name=self.name)
            if len(df)!=0:
                df['Date'] = pd.to_datetime(df['Date'])
                self.current_date = datetime.now()
                self.targetdate= self.current_date - timedelta(days=30)
                df=df.loc[df["Date"]>=self.targetdate]
                if len(df)!=0:
                    print(df.to_string(index=False))
                    self.monthly_total= df.loc[df['Date']>=self.targetdate,'Amount'].sum()
                    print(f" {self.name}'s Total Amount of Monthly Income from {self.targetdate.strftime('%Y-%m-%d')} to {self.current_date.strftime('%Y-%m-%d')} : {self.monthly_total}")
                else:
                    print(f" There has no monthly income record for {self.name}")
            else:
                print(f" There has no income record for {self.name}")
        except:
            print(f" There has no income record for {self.name}")
    def yearly(self):
        try:
            df=pd.read_excel(self.filename,sheet_name=self.name)
            if len(df)!=0:
                df['Date'] = pd.to_datetime(df['Date'])
                self.current_date = datetime.now()
                self.targetdate= self.current_date - timedelta(days=365)
                df=df.loc[df["Date"]>=self.targetdate]
                if len(df)!=0:
                    print(df.to_string(index=False))
                    self.yearly_total= df.loc[df['Date']>=self.targetdate,'Amount'].sum()
                    print(f" {self.name}'s Total Amount of Yearly Income from {self.targetdate.strftime('%Y-%m-%d')} to {self.current_date.strftime('%Y-%m-%d')} : {self.yearly_total}")
                else:
                    print(f" There has no yearly income record for {self.name}")
            else:
                print(f" There has no income record for {self.name}")
        except:
            print(f" There has no income record for {self.name}")

class DisplayExpense(Display):
    def all(self):
        try:
            df=pd.read_excel(self.filename,sheet_name=self.name)
            if len(df)!=0:
                print(df) #to remove index use df.to_string(index=False)
                print(f" {self.name}'s Total Amount of Expense: {df.iloc[:,2].sum()}")
            else:
                print(f" There has no expense record for {self.name}")
        except:
            print(f" There has no expense record for {self.name}")
    def daily(self):
        try:
            df=pd.read_excel(self.filename,sheet_name=self.name)
            if len(df)!=0:
                df['Date'] = pd.to_datetime(df['Date'])
                self.targetdate = datetime.now().strftime("%Y-%m-%d")
                df=df.loc[df["Date"]>=self.targetdate]
                if len(df)!=0:
                    print(df.to_string(index=False))
                    self.daily_total= df.loc[df['Date']>=self.targetdate,'Amount'].sum()
                    print(f" {self.name}'s Total Amount of Today's Expense : {self.daily_total}")
                else:
                    print(f" There has no daily expense record for {self.name}")
            else:
                print(f" There has no expense record for {self.name}")
        except:
            print(f" There has no expense record for {self.name}")
    def weekly(self):
        try:
            df=pd.read_excel(self.filename,sheet_name=self.name)
            if len(df)!=0:
                df['Date'] = pd.to_datetime(df['Date'])
                self.current_date = datetime.now()
                self.targetdate= self.current_date - timedelta(weeks=1)
                df=df.loc[df["Date"]>=self.targetdate]
                if len(df)!=0:
                    print(df.to_string(index=False))
                    self.weekly_total= df.loc[df['Date']>=self.targetdate,'Amount'].sum()
                    print(f" {self.name}'s Total Amount of Weekly Expense from {self.targetdate.strftime('%Y-%m-%d')} to {self.current_date.strftime('%Y-%m-%d')} : {self.weekly_total}")
                else:
                    print(f" There has no weekly expense record for {self.name}")
            else:
                print(f" There has no expense record for {self.name}")
        except:
            print(f" There has no expense record for {self.name}")
    def monthly(self):
        try:
            df=pd.read_excel(self.filename,sheet_name=self.name)
            if len(df)!=0:
                df['Date'] = pd.to_datetime(df['Date'])
                self.current_date = datetime.now()
                self.targetdate= self.current_date - timedelta(days=30)
                df=df.loc[df["Date"]>=self.targetdate]
                if len(df)!=0:
                    print(df.to_string(index=False))
                    self.monthly_total= df.loc[df['Date']>=self.targetdate,'Amount'].sum()
                    print(f" {self.name}'s Total Amount of Monthly Expense from {self.targetdate.strftime('%Y-%m-%d')} to {self.current_date.strftime('%Y-%m-%d')} : {self.monthly_total}")
                else:
                    print(f" There has no monthly expense record for {self.name}")
            else:
                print(f" There has no expense record for {self.name}")
        except:
            print(f" There has no expense record for {self.name}")
    def yearly(self):
        try:
            df=pd.read_excel(self.filename,sheet_name=self.name)
            if len(df)!=0:
                df['Date'] = pd.to_datetime(df['Date'])
                self.current_date = datetime.now()
                self.targetdate= self.current_date - timedelta(days=365)
                df=df.loc[df["Date"]>=self.targetdate]
                if len(df)!=0:
                    print(df.to_string(index=False))
                    self.yearly_total= df.loc[df['Date']>=self.targetdate,'Amount'].sum()
                    print(f" {self.name}'s Total Amount of Yearly Expense from {self.targetdate.strftime('%Y-%m-%d')} to {self.current_date.strftime('%Y-%m-%d')} : {self.yearly_total}")
                else:
                    print(f" There has no yearly expense record for {self.name}")
            else:
                print(f" There has no expense record for {self.name}")
        except:
            print(f" There has no expense record for {self.name}")

class Search:
    def __init__(self,name,filename):
        self.name = name
        self.filename = filename
    def searching(self,data_type,data):
        try:
            df=pd.read_excel(self.filename,sheet_name=self.name)
            df=df.loc[(df['Date']==data) | (df['Category']==data)]
            if len(df)!=0:
                print(df)
            else:
                print(f" No {data_type} record found for {data}")
        except:
            print(" There has no {data_type} record for {self.name}")

class IncomeDelete:
    def __init__(self,name,date):
        self.name=name
        self.date=date
    def deleteprocess(self):
        try:
            df=pd.read_excel('income_record.xlsx',sheet_name=self.name)
            df2=df.loc[(df['Date']==self.date)]
            if len(df2)!=0:
                print(df.loc[df['Date']==self.date])
                index=int(input(" Enter the index number of the row you want to delete: "))
                df=df.drop(index)
                with pd.ExcelWriter('income_record.xlsx',mode='w') as writer:
                    df.to_excel(writer,sheet_name=self.name,index=False)
                    print(" The row deleted successfully")
            else:
                print(" There has no data for the query")
        except:
            print(f" No income record availabe for {self.name}")

class ExpenseDelete:
    def __init__(self,name,date):
        self.name=name
        self.date=date
    def deleteprocess(self):
        try:
            df=pd.read_excel('expense_record.xlsx',sheet_name=self.name)
            df2=df.loc[(df['Date']==self.date)]
            if len(df2)!=0:
                print(df.loc[(df['Date']==self.date)])
                index=int(input(" Enter the index number of the row you want to delete: "))
                df=df.drop(index)
                with pd.ExcelWriter('expense_record.xlsx',mode='w') as writer:
                    df.to_excel(writer,sheet_name=self.name,index=False)
                    print(" The row delted successfully")
            else:
                print(" There has no data for the query")
        except:
            print(f" No expense record availabe for {self.name}")

class Menu:
    d=Decorate()
    g=Goal()
    @staticmethod
    def LoginMenu():
        while(True):
            Menu.d.logindesign()
            print(' 1. Login\n 2. Create a new account\n 3. Exit')
            choice = input(" Enter your choice: ")
            if choice == "1":
                create_login.login()
            elif choice == "2":
                create_login.create_account()
                Menu.LoginMenu()
            elif choice == "3":
                Menu.d.exitdesign()
                sys.exit()
            else:
                print(" Invalid choice. Please enter a valid option.")
    @staticmethod
    def MainMenu(name):
        Menu.d.maindesign()
        Menu.g.get_goal(name)
        print(" 1. Save Income\n 2. Save Expense\n 3. Set Goal\n 4. Get Goal\n 5. Display Income Record\n 6. Display Expense Record")
        print(" 7. Search Income\n 8. Search Expense\n 9. Delete Income Entry\n 10. Delete Expense Entry\n 11. Log Out\n 12. Exit")
        choice = input(" Enter your choice: ")
        if choice == "1":
            while(True):
                Menu.d.saveincomedesign()
                print(" 1. Salary\n 2. Bonus\n 3. Pocket Money\n 4. Other\n 5. Main Menu")
                try:
                    category=input(" Enter your choice: ")
                    if category !='5':
                        amount=float(input(' Enter the amount: '))
                except:
                    print(' Please enter valid inputs')
                if category == "1":
                    s1=SaveIncome(name,'Salary',amount)
                elif category == "2":
                    s1=SaveIncome(name,'Bonus',amount)
                elif category == "3":
                    s1=SaveIncome(name,'Pocket Money',amount)
                elif category == "4":
                    other=input(" Enter the income type: ")
                    s1=SaveIncome(name,other,amount)
                elif category == "5":
                    Menu.MainMenu(name)
                else:
                    print(" Please enter valid choice.")                                
        elif choice == "2":
            while(True):
                Menu.d.saveexpensedesign()
                print(" 1. Food\n 2. Transport\n 3. Health\n 4. Education\n 5. Other\n 6. Main Menu")
                try:
                    category=input(" Enter your choice: ")
                    if category !='6':
                        amount=float(input(' Enter the amount: '))
                except:
                    print(' Please enter valid inputs')
                if category == "1":
                    s1=SaveExpense(name,'Food',amount)
                elif category == "2":
                    s1=SaveExpense(name,'Transport',amount)
                elif category == "3":
                    s1=SaveExpense(name,'Health',amount)
                elif category == "4":
                    s1=SaveExpense(name,'Education',amount)
                elif category =="5":
                    other=input(" Enter the Expense type: ")
                    s1=SaveExpense(name,other,amount)
                elif category == "6":
                    Menu.MainMenu(name)                      
                else:
                    print(" Please enter valid choice.")
        elif choice == "3":
            goal=input(" Enter your goal: ")
            Menu.g.set_goal(name,goal)
            print(" Goal set successfully")
            Menu.MainMenu(name)
        elif choice == "4":
            Menu.g.get_goal(name)
            Menu.MainMenu(name)
        elif choice == "5":
            while(True):
                Menu.d.displayincomedesign()
                check1=DisplayIncome(name, 'income_record.xlsx')
                print(" 1. Check All Record\n 2. Check Daily Record\n 3. Check Weekly Record\n 4. Check Monthly Record\n 5. Check Yearly Record\n 6. Main Menu")
                x=input(" Enter your choice: ")
                if x=="1":
                    Menu.d.allincomedesign()
                    check1.all()
                elif x=="2":
                    Menu.d.dailyincomedesign()
                    check1.daily()
                elif x=="3":
                    Menu.d.weeklyincomedesign()
                    check1.weekly()
                elif x=="4":
                    Menu.d.monthlyincomedesign()
                    check1.monthly()
                elif x=="5":
                    Menu.d.yearlyincomedesign()
                    check1.yearly()
                elif x=="6":
                    Menu.MainMenu(name)
                else:
                    print(" Please enter valid choice")
        elif choice == "6":
            while(True):
                Menu.d.displayexpensedesign()
                check1=DisplayExpense(name, 'expense_record.xlsx')
                print(" 1. Check All Record\n 2. Check Daily Record\n 3. Check Weekly Record\n 4. Check Monthly Record\n 5. Check Yearly Record\n 6. Main Menu")
                x=input(" Enter your choice: ")
                if x=="1":
                    Menu.d.allexpensedesign()
                    check1.all()
                elif x=="2":
                    Menu.d.dailyexpensedesign()
                    check1.daily()
                elif x=="3":
                    Menu.d.weeklyexpensedesign()
                    check1.weekly()
                elif x=="4":
                    Menu.d.monthlyexpensedesign()
                    check1.monthly()
                elif x=="5":
                    Menu.d.yearlyexpensedesign()
                    check1.yearly()
                elif x=="6":
                    Menu.MainMenu(name)
                else:
                    print(" Please enter valid choice")
        elif choice == "7":
            while(True):
                s1=Search(name,'income_record.xlsx')
                print(" 1. Search By Catagory\n 2. Search By Date\n 3. Main Menu")
                x=input(" Enter your choice: ")
                if x=='1':
                    data=input(" Enter the Category Name(Salary/Bonus/Pocket Money/Other): ")
                    Menu.d.searchedesign()
                    s1.searching('income',data)
                elif x=='2':
                    data=input(" Enter the Date(Example: 2024-05-01(Year-Month-Day)): ")
                    Menu.d.searchedesign()
                    s1.searching('income',data)
                elif x=='3':
                    Menu.MainMenu(name)
                else:
                    print(" Please enter valid choice")
        elif choice == "8":
            while(True):
                s1=Search(name,'expense_record.xlsx')
                print(" 1. Search By Catagory\n 2. Search By Date\n 3. Main Menu")
                x=input(" Enter your choice: ")
                if x=='1':
                    data=input(" Enter the Category Name(Food/Transport/Health/Education/Other): ")
                    Menu.d.searchedesign()
                    s1.searching('expense',data)
                elif x=='2':
                    data=input(" Enter the Date(Example: 2024-05-01(Year-Month-Day)): ")
                    Menu.d.searchedesign()
                    s1.searching('expense',data)
                elif x=='3':
                    Menu.MainMenu(name)
                else:
                    print(" Please enter valid choice")
        elif choice == "9":
            while(True):
                Menu.d.deleteincomedesign()
                date=input(" Enter the date(Example: 2024-05-01(Year-Month-Day)): ")
                s1=IncomeDelete(name,date)
                s1.deleteprocess()
                y=input(" 1. Main Menu\n 2. Delete Again\n Enter your choiche: ")
                if y=='1':
                    Menu.MainMenu(name)
                elif y=='2':
                    continue
                else:
                    print(" Please enter valid choice")
        elif choice == "10":
            while(True):
                Menu.d.deleteexpensedesign()
                date=input(" Enter the date(Example: 2024-05-01(Year-Month-Day)): ")
                s1=ExpenseDelete(name,date)
                s1.deleteprocess()
                y=input(" 1. Main Menu\n 2. Delete Again\n Enter your choiche: ")
                if y=='1':
                    Menu.MainMenu(name)
                elif y=='2':
                    continue
                else:
                    print(" Please enter valid choice")
        elif choice == "11":
            print(f" Logging out from {name} account")
            Menu.LoginMenu()
        elif choice == "12":
            Menu.d.exitdesign()
            sys.exit()
        else:
            print(" Invalid choice. Please enter a valid option.")
            Menu.MainMenu(name)
Menu.LoginMenu()

