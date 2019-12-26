import schedule
import time
from random import *
elements = 10
class Bet:
    def __init__(self,home,away,bet1,bet2,bet3):
        self.home=home
        self.away=away
        self.bet1=bet1
        self.bet2=bet2
        self.bet3=bet3
teams=['Arsenal','Liverpool','ManchesterCity','Leicester','Chelesea','Totenham','Brighton' , 'Everton','Shefield','Wolves','Burnley','Newcastle','Watford','Norwich']
initalmatch = []
updatedmatch=[]
result={}   
def writeInFile():
    global initalmatch
    f=open("meciuri.txt","w+")
    i=0
    while i<elements:
        i=i+1
        home=randint(1,13)
        away=randint(1,13)
        bet1=uniform(1,5)
        bet2=uniform(2,3.5)
        bet3=uniform(1,5)
        match=Bet(teams[home],teams[away],bet1,bet2,bet3)
        initalmatch.append(match)
        bet=teams[home] +" "+teams[away] + " " + str(bet1) +" "+str(bet2)+" "+ str(bet3) +"\n"
        f.write(bet)
    f.close()
def split(line):
    global updatedmatch
    sp=line.split(" ");
    matchupdated=Bet(sp[0],sp[1],uniform(1,5),uniform(1,5),uniform(1,5))
    updatedmatch.append(matchupdated)
    newbet=sp[0]+" "+ sp[1] + " " +str(uniform(1,5))+" " +str(uniform(1,5))+" " +str(uniform(1,5))+"\n"
    return newbet
def readAndSplit():
    mUp=[]
    f=open("meciuri.txt","r")
    for line in f:
        mUp.append(split(line))
    f.close()
    f=open("meciuri.txt","w+")
    for meci in mUp:
        f.write(meci)
    f.close()
def pronostic(value,el1,el2,el3):
    pron=''
    if(value==el1 and el1 > 0):
        pron='1'
    if(value==el2 and el2 > 0):
        pron='x'
    if(value==el3 and el3 >0 ):
        pron='2'
    return pron
def compare(initalmatch,updatedmatch):
 
    for i in range(elements):
        el1=initalmatch[i].bet1-updatedmatch[i].bet1
        el2=initalmatch[i].bet2-updatedmatch[i].bet2
        el3=initalmatch[i].bet3-updatedmatch[i].bet3
        value=max(el1,el2,el3)
        pron=pronostic(value,el1,el2,el3)
        result.update({value:pron})
def safeBet(result):
   global initalmatch
   temp=max(result.keys())
   ind=list(result.items())
   res=[idx for idx, key in enumerate(ind) if key[0] == temp]
   index=res[0]
   concatMatch=initalmatch[index].home + " " +initalmatch[index].away+" ==>" +result.get(temp)
   print(concatMatch)
writeInFile()
def reset():
    global initalmatch
    global updatedmatch
    global result
    result={}
    initalmatch=[]
    for el in updatedmatch:
        initalmatch.append(el)
    updatedmatch=[]
def doSomething():
    readAndSplit()
    compare(initalmatch,updatedmatch)
    safeBet(result)
    reset()
schedule.every(10).seconds.do(doSomething)
while 1:
    schedule.run_pending()
    time.sleep(1)