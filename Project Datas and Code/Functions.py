import khayyam 
import datetime
import pandas as pd

df=pd.read_excel('data1.xlsx')
df.index +=1
df.drop(['name','floor'],inplace=True,axis=1)
df.columns=['vahed','tedad_sakenin','masahat','tedad_parking']

df_transaction=pd.read_csv('transaction.csv')


# for understanding the category
def sub_cat(a):
        if a[2]=='bill':
            return a[3];
        else:
            return a[2];
# equal division
def e(a,i):
    return 1/df.vahed.count()*int(a[1]);
# division based on resident 
def r(a,i):
    return df.loc[i,'tedad_sakenin']/df.tedad_sakenin.sum()*int(a[1]);
#  division based on area 
def s(a,i):
    return df.loc[i,'masahat']/df.masahat.sum()*int(a[1]);
# division based on parking 
def p(a,i):
    return df.loc[i,'tedad_parking']/df.tedad_parking.sum()*int(a[1]);

     
# a function that realises which type of division must be used
def operation(a,i):
    if a[4]=='d':
        if sub_cat(a) in ['water','electricity']:
            return r(a,i)
        elif sub_cat(a) in ['city_hall','elevator','cleaning','repairing','charge','others']:
            return e(a,i)
        elif sub_cat(a)=='parking':
            return p(a,i)
        elif sub_cat(a)=='gas':
            return s(a,i)               
    else:
        if a[4]=='r':
            return r(a,i)
        if a[4]=='s':
            return s(a,i)
        if a[4]=='p':
            return p(a,i)
        if a[4]=='e':
            return e(a,i)
# for announcing the codition of budget        
def budget(df_transaction,a):
    budget=df_transaction[df_transaction['category']=='charge'].amount.sum()-df_transaction[df_transaction['category']!='charge'].amount.sum()
    if budget<=-a:
        print('your budget is :')
        print(budget)
        print('condition is red')
    elif (budget>-a/2) & (budget<0):
        print('your budget is :')
        print(budget)
        print('condition is yellow')
    else:
        print('your budget is :')
        print(budget)
        print('condition is green')