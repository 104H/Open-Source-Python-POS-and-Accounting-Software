
from terminalFrontEnd import terminalPanel
import newCust as nc

class cashSalePanel (terminalPanel):
	def __init__ (self, parent, transactionButtonName):
		terminalPanel.__init__(self, parent, transactionButtonName)

	def CheckOutFunc( self, event ):
		self.clearCartGrid()
		self.t.checkout()
		#self.m_balanceST.SetFocus()
	
	def refundFunc( self, event ):
		self.clearCartGrid()
		self.t.returnProducts()
		#self.m_balanceST.SetFocus()
