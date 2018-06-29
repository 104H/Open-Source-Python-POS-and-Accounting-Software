import wx
import wx.grid

class numOnlyValidator(wx.Validator):
	def __init__(self):
		super(numOnlyValidator, self).__init__()
		
		self.Bind(wx.EVT_CHAR, self.Validate)
	# --------------------------------------------------------------------------
	def Clone(self):
		return numOnlyValidator()

	# --------------------------------------------------------------------------
	def Validate(self, event):
		k = event.GetKeyCode()
		if not(k >= 48 and k <= 57):
			#wx.MessageBox("Please enter numbers only", "Invalid Input", wx.OK | wx.ICON_ERROR)
			return False
			
		#self.GetWindow().SetValue( self.GetWindow().GetValue() + chr(k) )
		event.Skip()
		return True

	# --------------------------------------------------------------------------
	def TransferToWindow(self):
		return True

	# --------------------------------------------------------------------------
	def TransferFromWindow(self):
		return True
'''
class numOnlyGridEditor (wx.grid.GridCellTextEditor):
	def __init__ (self):
		super(numOnlyGridEditor, self).__init__()
		
		self.SetValidator(numOnlyValidator())
	
	def EndEdit (self, row, col, grid, oldval):
		print ("asdasd")
		if not self.Validate():
			return None
'''
