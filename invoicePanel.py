
from terminalFrontEnd import terminalPanel
import newCust as nc

class invoiceSalePanel (terminalPanel):
	def __init__ (self, parent, transactionButtonName):
		terminalPanel.__init__(self, parent, transactionButtonName)
		#self.returnButton.Hide()
	
	def CheckOutFunc( self, event ):
		amt = self.makePopUp("Enter Recieved Amount", "Amount Recieved")
		self.clearCartGrid()
		self.t.prepareInvoice(amt)
	
	def refundFunc( self, event ):
		self.clearCartGrid()
		self.t.returnProducts()
