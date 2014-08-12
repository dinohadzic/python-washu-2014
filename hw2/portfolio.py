import random

class Portfolio():
	def __init__(self):
		self.cash = 0.00
		self.investments = {"stock" : {}, "mutual funds" : {}, "bonds" : {}}
		self.history = "Portfolio:\n"
		
	def addCash(self, cash):
		self.cash += float(cash)
		self.history += "Contributes $%.2f\n" % float(cash)
		
	def withdrawCash(self, cash):
		self.cash -= float(cash)
		self.history += "Withdraws $%.2f\n" % float(cash)
		
	def invest(self, shares, investment):
		self.withdrawCash(shares * investment.price)
		if investment in self.investments[investment.investType()]:
			self.investments[investment.investType()][investment] += shares
		else: 
			self.investments[investment.investType()][investment] = shares
		self.history += "Purchases %d shares of %s in %s" % (shares, investment.investType(), investment.name)
		
	def divest(self, shares, investment):
		self.investments[investment.investType()][investment] -= shares
		self.addCash(shares * investment.Selling_Price())
		self.history += "Sells %d shares of %s in %s" % (shares, investment.investType(), investment.name)
	
	def buyStock(self, shares, investment): self.invest(int(shares), investment)
	
	buyMutualFund = invest
	
	def sellStock(self, shares, investment): self.divest(int(shares), investment)
	
	sellMutualFund = divest
	
	def history(self): print self.history

	def __str__(self):
		product = "Cash:\t$%.2f \n" % self.cash
		for investment in self.investments:
			product += "%s: \n" % investment
			if not self.investments[investment]: 
				product += "\t None \n"
			for i in self.investments[i]: 
				product += "\t" + str(self.investments[investment][i]) + "\t" + str(i.name) + "\n"
		return product	
		
class Investment(object):
	def __init__(self, price, name):
		self.price = price
		self.name = name
			
	def Selling_Price(self):
		return random.uniform(.9 * self.price, 1.2 * self.price)
			
class Stock(Investment):
	def __init__(self, price, name):
		Investment.__init__(self, price, name)
			
	def investType(self): return "stock"
	
	def Selling_Price(self):
		return random.uniform(0.5 * self.price, 1.5 * self.price)
		
class MutualFund(Investment):
	def __init__(self, name):
		Investment.__init__(self, 1.0, name)
			
	def investType(self): return "mutual funds"
		
portfolio = Portfolio()
portfolio.addCash(300.50)
s = Stock(20, "HFH")
portfolio.buyStock(5, s)
mf1 = MutualFund("BRT")
mf2 = MutualFund("GHT")
portfolio.buyMutualFund(10.3, mf1)
portfolio.buyMutualFund(2, mf2)
portfolio.withdrawCash(50)

#Unfortunately, when I run the bottom tests I receive an error.

#print(portfolio) 
#portfolio.sellMutualFund("BRT", 3)
#portfolio.sellStock("HFH", 1)
#portfolio.history()


			
	
				
	
		
		
	
		
		