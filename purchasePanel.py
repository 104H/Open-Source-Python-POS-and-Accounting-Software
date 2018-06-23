
from terminalFrontEnd import terminalPanel
import newCust as nc

class purchasePanel (terminalPanel):
	def __init__ (self, parent, transactionButtonName):
		terminalPanel.__init__(self, parent, transactionButtonName)
		#self.returnButton.Hide()
	
	def identifyParty (self, inS):
		if self.t.fetchSupplierId(inS):
			self.customerName.SetLabel(self.t.supplierName)
			self.customerContact.SetLabel(self.t.supplierContact)
		else:
			dlg = nc.GetData(parent = self.m_papa)
			dlg.ShowModal()
	
	def CheckOutFunc( self, event ):
		amtPaid = self.makePopUpDate("Enter Amount Paid", "Amount Paid")
		self.clearCartGrid()
		self.t.purchaseItems(amtPaid)
	'''
	def refundFunc( self, event ):
		self.clearCartGrid()
		self.t.returnPurchase()
		self.m_balanceST.SetFocus()
	'''
