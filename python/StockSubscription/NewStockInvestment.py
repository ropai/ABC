import random
from numpy import mean, var, std
import matplotlib.pyplot as plt
'''
  ****************  新股申购模拟程序     *****************
  **                Ver: 0.1                            **
  **                Author: Vincent                     **
  **                Data:   2017-Dec-23                 **
  ********************************************************  
'''
class CNewStockInvest:
    def __init__(self, initCapital):
        self.week = 0   #周数
        self.issuePrice = 0     #发行价
        self.lotRate = 0        #中签率
        self.subscribeNum = 0   #申购数量
        self.ticketNum = 0      #中签数量
        self.V = 0              #V
        self.marketPrice = 0    #上市价
        self.WeeklyStockIncome = [] #每周打中新股的收益（5周后才能抛出）
        if initCapital>0:
            self.InitialCapital = initCapital
        else:
            self.InitialCapital = 1000000
        self.CurrentCapital = self.InitialCapital 
        self.Profit = 0     #利润
        self.ProfitRate = 0 #利润率

    def reset(self):
        self.week = 0;
        self.WeeklyStockIncome.clear()

    def setInitCapital(self, initCapital):
        if initCapital>0:
            self.InitialCapital = initCapital
        else:
            self.InitialCapital = 1000000
        self.CurrentCapital = self.InitialCapital  
    
    def genRandIssuePrice():  #产生随机的新股发行价(5~10元)
        return 5+5*random.random()

    def genRandLotRate():#产生随机的新股中签率(0,001~0.025)
        return 0.001+0.024*random.random() 
   
    def refreshWeeklyData(self): #每周进行打新
        self.issuePrice = CNewStockInvest.genRandIssuePrice()
        self.lotRate = CNewStockInvest.genRandLotRate()
        if 3<self.week< 52:  #第5周到52周可以抛出5周前的股票回笼资金
            self.CurrentCapital += self.WeeklyStockIncome[self.week-4]
        self.subscribeNum = self.CurrentCapital/self.issuePrice
        self.ticketNum = round((self.subscribeNum * self.lotRate)/1000)*1000  #一手1000股
        self.V = 0.5*random.random()
        self.marketPrice = (0.8+0.5/(self.lotRate*100) + self.V)*self.issuePrice
        self.WeeklyStockIncome.append(self.ticketNum*self.marketPrice)
        self.CurrentCapital -= self.issuePrice * self.ticketNum #扣去打新费用 
        weeklyData = (1 + self.week,self.issuePrice,self.lotRate,self.subscribeNum,self.ticketNum,self.V,self.marketPrice,self.CurrentCapital)
        self.week += 1
        #print(weeklyData)
         
    def getLastFourWeekIncome(self):#最后四周的新股收益要一年后才能到账
        sum = 0
        for x in range(48,52):
            sum += self.WeeklyStockIncome[x]
        return sum

    def runOneYearTest(self):#测试一年的数据
        #print(" 周         发行价             中签率            申购数         中签数         V            上市价               剩余资金")
        for x in range(0,52):
            self.refreshWeeklyData()
        self.CurrentCapital += self.getLastFourWeekIncome()
        self.Profit = self.CurrentCapital - self.InitialCapital
        self.ProfitRate = self.Profit/self.InitialCapital
        #print("【年初资金】：%d 【年末资金】： %d 【利润】：%d 【利润率】：%0.2f%%" % (self.InitialCapital,self.CurrentCapital,self.Profit, self.ProfitRate*100))
        return self.ProfitRate*100


#主函数    
def main():
    
    invest1 = CNewStockInvest(0)
    X =[] #利润率-投入图 X轴
    Y =[] #利润率-投入图 Y轴
    #测试初始资金10W 到 300W
    profitRateResults = [] 
    for x in range(0,60):#投入5W~250W,增幅为5W
        initCapital = 50000*(x+1)
        X.append(initCapital)
        for t in range(0,1000): #每组测试1000次取平均值
            invest1.reset()
            invest1.setInitCapital(initCapital)
            profitRateResults.append(invest1.runOneYearTest())
        meanProfitRate = mean(profitRateResults)
        Y.append(meanProfitRate)
        print("投入资金:%d 利润率均值:%0.2f%% 方差:%0.2f 标准差:%0.2f" % (initCapital,meanProfitRate,var(profitRateResults),std(profitRateResults)))
        print("------------------------------------------------------------");
        profitRateResults.clear()
        
    plt.figure()
    plt.plot(X,Y)
    plt.title("New Stock Investment")
    plt.xlabel("Invested Capital(Yuan)")
    plt.ylabel("Rate of Profit(%)")
    plt.show()
main()
