
from terminalFrontEnd import terminalPanel
import newCust as nc

class quotationPanel (terminalPanel):
	def __init__ (self, parent, transactionButtonName):
		terminalPanel.__init__(self, parent, transactionButtonName)
		self.returnButton.Hide()
	
	def CheckOutFunc( self, event ):
		expDate = self.makePopUpDate("Enter Expiry Date", "Expiry Date")
		self.clearCartGrid()
		self.t.saveQuote(expDate)
	
	def refundFunc( self, event ):
		self.clearCartGrid()
		self.t.returnProducts()
