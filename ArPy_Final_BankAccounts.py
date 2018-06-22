

# by Arash, modified date: 22-06-2018 / 20:07

class Account:

    account_counter=0
    
    def __init__(self,number,owner,balance=0.0):
        self.number=number
        self.owner=owner
        self.balance=balance


    def __repr__(self):
        return '{},{},{}'.format(self.number,self.owner,self.balance)
    

    def create(owner,init_balance,accounts):
        if  len(accounts)==0:
            #if first account
            Account.account_counter =1
            number='A'+str(Account.account_counter)
        else:
            #if there is some previous accounts
            number='A'+str(Account.newAccountIndex(accounts))
            

        new_account=Account(number,owner)
        new_account.deposit(init_balance)
        return new_account

    def deposit(self,amount):
        if amount <= 0.0:
            return False       
        self.balance +=amount
        return True

    def withdraw(self,amount):
        if amount>self.balance:
            return False
        self.balance -=amount
        return True

    def newAccountIndex(accounts):
        indx=[]
        for i in accounts:
            a,o,b=repr(i).split(',')
            indx.append(int(a.strip('A')))        
        return(max(indx)+1)        



class GUI:
    accounts_file='c:\\tmp\\accounts.txt'

    def __init__(self):
        self.accounts=GUI.load(GUI.accounts_file)        

    
    def __repr__(self):
        return \
'''
                    Welcome to this Arash Corebanking(:-D) system!

                                     Main Menu
(S)how Accounts
(C)reate Account
(R)emove Account
(F)ind an Account Number
(L)ooking for any String(Full Serach)
(E)dit Account
(D)eposit Cash
(W)ithdraw Cash
(T)ransfer Cash
(M)ain Menu (Back to Menu List)
(Q)uit


'''

    
    def run(self):
        print(self)
        while True:
            op=input('select your operation:')
            lst_accounts=GUI.load(GUI.accounts_file)
            
            #******* Show Accounts            
            if op.upper()=='S':
                print('\n\nlist of accounts')
                print('----------------')
                GUI.show(lst_accounts)
                
            #******* Create an account
            elif op.upper()=='C':
                ow=input('\nEnter the owner name:')
                bl=float(input('\nEnter the initial balance value:'))
                newaccount=Account.create(ow,bl,lst_accounts)
                if newaccount is not None:
                    GUI.change(GUI.accounts_file,newaccount)
                    print('\n\nAccount created successfully!')                    
                else:
                    print('\n\nAn error occured!')
                print('\n\n')

            #******* Remove Accounts            
            if op.upper()=='R':
                while True:
                    a=input('\nEnter the "Account Number" to remove:')
                    if a =='':
                        continue
                    s=GUI.find(lst_accounts,a.upper())
                    if s=='-1':
                        print('\nInvalid Account Number')
                    else:
                        r=input('\nDo you want to remove this account: '+repr(s)+ '\nEnter Y/N ?')
                        if r.upper()=='Y':
                            if GUI.remove(lst_accounts,s.number):
                                print('Account removed successfully!')
                            else:
                                print('An error was ccoured!')
                        print('\n\n')
                        break
            
            #******* Find an Account Number
            elif op.upper()=='F':
                while True:
                    st=input('\nEnter the "Account Number":')
                    if st =='':
                        continue
                    print('\n\nFind an Account Number')
                    print('Search result:')
                    print('----------------')
                    k=GUI.find(lst_accounts,st)
                    if k =='-1':
                        print('Account Number not exist!')
                    else:
                        print(k)          
                    break
                print('\n\n')

            #******* Looking for any String(Full Serach)
            elif op.upper()=='L':
                st=input('\nEnter the string which you are looking for:')
                print('\n\nFull Text Search')
                print('Search result:')
                print('----------------')
                for i in GUI.look(lst_accounts,st):
                    print(i, end='\n')
                print('\n\n')                      

            #******* Edit Account
            elif op.upper()=='E':
                while True:
                    a=input('\nEnter the "Account Number" to edit:')
                    if a =='':
                        continue
                    s=GUI.find(lst_accounts,a.upper())
                    if s=='-1':
                        print('\nInvalid Account Number')
                    else:
                        print('\nCurrent Account info is:',s)
                        
                        ow=input('\nEnter the new "Owner":')
                        bl=float(input('\nEnter the new "Balance":'))
                        print('\nEdit operation result:')
                        print('----------------')
                        if GUI.edit(lst_accounts,s.number,ow,bl):
                            print('Account edited successfully!')
                        else:
                            print('An error was ccoured!')
                    print('\n\n')
                    break
                                
                
            elif op.upper()=='D':
                while True:
                    a=input('\nEnter the "Account Number" to deposit:')
                    if a =='':
                        continue
                    s=GUI.find(lst_accounts,a.upper())
                    if s=='-1':
                        print('\nInvalid Account Number')
                    else:
                        print('\nCurrent Account info is:',s)
                        
                        dv=float(input('\nEnter "Deposit Value":'))
                        print('\nDeposit operation result:')
                        print('----------------')
                        s.deposit(dv)
                        if GUI.edit(lst_accounts,s.number,s.owner,s.balance):
                            print('Deposit is done successfully!')
                        else:
                            print('An error was ccoured!')
                    print('\n\n')
                    break
                
            elif op.upper()=='W':
                while True:
                    a=input('\nEnter the "Account Number" to withdraw:')
                    if a =='':
                        continue
                    s=GUI.find(lst_accounts,a.upper())
                    if s=='-1':
                        print('\nInvalid Account Number')
                    else:
                        print('\nCurrent Account info is:',s)                        
                        dv=float(input('\nEnter "Withdraw Value":'))
                        print('\nWithdraw operation result:')
                        print('----------------')                        
                        if not s.withdraw(dv):
                            print('Insufiecent balance!')                            
                        else:
                            if GUI.edit(lst_accounts,s.number,s.owner,s.balance):
                                print('Withdraw is done successfully!')
                            else:
                                print('An error was ccoured!')
                    print('\n\n')
                    break
                
            elif op.upper()=='T':
                 while True:
                    s=input('\nEnter the Source "Account Number":')
                    d=input('\nEnter the Destination "Account Number":')
                    v=input('\nEnter the "Value" to Transfer:')
                    if s=='' or d =='' or v=='':
                        print('Enter source or destination number or value')
                        continue
                    p=GUI.find(lst_accounts,s.upper())
                    if p=='-1':
                        print('\nInvalid Source Account Number')
                    else:
                        q=GUI.find(lst_accounts,d.upper())
                        if q=='-1':
                            print('\nInvalid destination Account Number')
                        else:
                            r=input('\nTransfer '+str(v)+' from '+p.number +\
                                        ' to '+q.number+ '. is ok? (Y/N)')
                            if r.upper()=='Y':
                                if not p.withdraw(float(v)):
                                    print('Insufiecent source balance!')
                                else:
                                    q.deposit(float(v))
                                    if GUI.edit(lst_accounts,p.number,p.owner,str(p.balance)) \
                                    and GUI.edit(lst_accounts,q.number,q.owner,str(q.balance)):
                                        print('Transfer is done successfully!')
                                    else:
                                        print('An error was ccoured!')                                    
                            print('\n\n')
                            break
                
            elif op.upper()=='M':
                print(self)
                
            elif op.upper()=='Q':
                q=input('\n\nQuit(Y/N)?')
                if q.upper()=='Y':
                    break                
            continue 
      

    def show(accounts):       
        for i in accounts:
            print(i, end='\n')
        print('\n\n')


    def find(accounts,number):
        for i in accounts:           
            p=i.number.find(number.upper())
            if p !=-1:
                return i
        return '-1'

    def look(accounts,string):
        lst_result=[]
        for i in accounts:
            s=repr(i).find(string)
            if s !=-1:
               lst_result.append(i)
        return lst_result

    def remove(accounts,number):
        i=0
        for p in accounts:
            if p.number.lower()==number.lower():
                accounts.pop(i)
                GUI.save(GUI.accounts_file,accounts)                
                return True
            i +=1
        return False

    def edit(accounts,number,owner,balance):
        i=0
        for p in accounts:
            if p.number.lower()==number.lower():
                accounts[i]=Account(number,owner,float(balance))
                GUI.save(GUI.accounts_file,accounts)                
                return True
            i +=1
        return False
      
    def load(filename):
        accounts=[]
        f=open(filename,'r')
        for a in f:
            name,owner,balance=a.split(',')
            accounts.append(Account(name,owner,float(balance)))
        f.close()
        return accounts


    def save(filename,account):
        f=open(filename,'w')
        for i in account:
            f.write(repr(i).rstrip())
            f.write('\n')
        f.close()


    def change(filename,account):
        f=open(filename,'a')
        f.write(repr(account)+'\n')            
        f.close()


##b=Account('A01','Arash',100.0)
##s=input('value:')
##
##print(b)
##b.deposit(s)
##print(b)

   
g=GUI()
g.run()


     

    
    

    
