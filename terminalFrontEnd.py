
import wx
import wx.xrc
import wx.grid
import wx.adv

from cart import terminal

import newProd as np
import newCust as nc
from connectToDb import connectToDB

class terminalPanel ( wx.Panel ):
	
	def __init__( self, parent, transactionButtonName ):
		# input stream
		self.inputStream = ''
		self.t = terminal()
		
		wx.Panel.__init__ ( self, parent, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.Size( -1,-1 ), wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_CAPTIONTEXT ) )
		
		bSizerMyFrame1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.papa = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
		self.papa.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		
		bSizerMain = wx.BoxSizer( wx.VERTICAL )

		########### Cart Grid Start
		self.productsGrid = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.productsGrid.CreateGrid( 99, 6 )
		self.productsGrid.EnableEditing( True )
		self.productsGrid.EnableGridLines( True )
		self.productsGrid.EnableDragGridSize( False )
		self.productsGrid.SetMargins( 0, 0 )
		self.productsGrid.SetRowLabelSize( 20 )
		
		self.productsGrid.SetColSize( 0, 60 )
		self.productsGrid.SetColSize( 1, 120 )
		self.productsGrid.SetColSize( 2, 180 )
		self.productsGrid.SetColSize( 3, 240 )
		self.productsGrid.SetColSize( 4, 300 )
		self.productsGrid.SetColSize( 5, 360 )
		
		self.productsGrid.SetColLabelValue( 0, u"ID" )
		self.productsGrid.SetColLabelValue( 1, u"Name" )
		self.productsGrid.SetColLabelValue( 2, u"Quantity" )
		self.productsGrid.SetColLabelValue( 3, u"Unit Price" )
		self.productsGrid.SetColLabelValue( 4, u"Total Discount" )
		self.productsGrid.SetColLabelValue( 5, u"Total Price" )
		
		self.productsGrid.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		self.productsGrid.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		########### Cart Grid End
		
		self.bSizerPG = wx.BoxSizer( wx.HORIZONTAL )
		self.bSizerPG.Add( self.productsGrid, 1, wx.EXPAND|wx.ALL, 5 )
		
		self.inputTC = wx.SearchCtrl( self.papa, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0 )
		#self.inputTC.SetEditable( False )
		self.inputTC.SetDescriptiveText( "Search for Customer or Product" )

		'''
		searchSize = self.inputTC.GetSize()
		x, y = self.inputTC.GetScreenPosition()
		y = searchSize[1] + y
		'''
		self.suggestionList = wx.ListBox ( self.papa, choices=self.suggestionCandidatesAsList( self.inputTC.GetValue() ), pos=(30, 60),  size=(-1, -1) )
		self.suggestionList.SetTransparent(wx.IMAGE_ALPHA_OPAQUE)
		self.suggestionList.Hide()
		
		self.customerHeading = wx.StaticText( self.papa, wx.ID_ANY, u"Customer Information", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.customerName = wx.StaticText( self.papa, wx.ID_ANY, u"Name:   ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.customerContact = wx.StaticText( self.papa, wx.ID_ANY, u"Contact:   ", wx.DefaultPosition, wx.DefaultSize, 0 )
		#self.customerBalance = wx.StaticText( self.papa, wx.ID_ANY, u"Balance:   ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.newCustomerButton = wx.Button( self.papa, wx.ID_ANY, u"Select Customer", wx.DefaultPosition, wx.DefaultSize, 0 )
		
		self.bSizerTopSecondRowCustInfo = wx.BoxSizer( wx.VERTICAL )
		self.bSizerTopSecondRowCustInfo.Add( self.customerHeading, 1, wx.EXPAND|wx.ALL, 5 )
		self.bSizerTopSecondRowCustInfo.Add( self.customerName, 1, wx.EXPAND|wx.ALL, 5 )
		self.bSizerTopSecondRowCustInfo.Add( self.customerContact, 1, wx.EXPAND|wx.ALL, 5 )
		#self.bSizerTopSecondRowCustInfo.Add( self.customerBalance, 1, wx.EXPAND|wx.ALL, 5 )
		self.bSizerTopSecondRowCustInfo.Add( self.newCustomerButton, 1, wx.EXPAND|wx.ALL, 5 )
		
		self.totalBill = wx.StaticText( self.papa, wx.ID_ANY, u"Total:   0000000", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.discountTC = wx.StaticText( self.papa, wx.ID_ANY, u"Discount:   0000000", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.billAfterDiscount = wx.StaticText( self.papa, wx.ID_ANY, u"After Discount:   0000000", wx.DefaultPosition, wx.DefaultSize, 0 )
		
		self.totalBill.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.discountTC.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.billAfterDiscount.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		
		self.bSizerTopSecondRowCartInfo = wx.BoxSizer( wx.VERTICAL )
		self.bSizerTopSecondRowCartInfo.Add( self.totalBill, 1, wx.EXPAND|wx.ALL|wx.ALIGN_CENTRE_VERTICAL, 5 )
		self.bSizerTopSecondRowCartInfo.Add( self.discountTC, 1, wx.EXPAND|wx.ALL, 5 )
		self.bSizerTopSecondRowCartInfo.Add( self.billAfterDiscount, 2, wx.ALIGN_CENTRE_VERTICAL, 5 )
		
		self.transactionButton = wx.Button( self.papa, wx.ID_ANY, transactionButtonName, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.returnButton = wx.Button( self.papa, wx.ID_ANY, u"Return", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cleanCartButton = wx.Button( self.papa, wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.DefaultSize, 0 )
		
		self.transactionButton.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		
		self.bSizerTopSecondRowControls = wx.BoxSizer( wx.VERTICAL )
		self.bSizerTopSecondRowControls.Add( self.transactionButton, 3, wx.EXPAND|wx.ALL, 5 )
		self.bSizerTopSecondRowControls.Add( self.returnButton, 2, wx.EXPAND|wx.ALL, 5 )
		self.bSizerTopSecondRowControls.Add( self.cleanCartButton, 2, wx.EXPAND|wx.ALL, 5 )
		
		self.bSizerTopSecondRow = wx.BoxSizer( wx.HORIZONTAL )
		self.bSizerTopSecondRow.Add ( self.bSizerTopSecondRowCustInfo, 3, wx.EXPAND|wx.ALL, 5 )
		self.bSizerTopSecondRow.Add ( self.bSizerTopSecondRowCartInfo, 3, wx.EXPAND|wx.ALL, 5 )
		self.bSizerTopSecondRow.Add ( self.bSizerTopSecondRowControls, 4, wx.EXPAND|wx.ALL, 5 )
		
		self.bSizerTop = wx.BoxSizer( wx.VERTICAL )
		self.bSizerTop.Add ( self.inputTC, 1, wx.EXPAND|wx.ALL, 5 )
		#self.bSizerTop.Add ( self.suggestionList, 0, wx.EXPAND|wx.ALL, 5 )
		self.bSizerTop.Add ( self.bSizerTopSecondRow, 4, wx.EXPAND|wx.ALL, 5 )
		
		bSizerMain.Add( self.bSizerTop, 4, wx.EXPAND|wx.ALL, 5 )
		bSizerMain.Add( self.bSizerPG, 6, wx.EXPAND|wx.ALL, 5 )
		
		self.papa.SetSizer( bSizerMain )
		self.papa.Layout()
		bSizerMain.Fit( self.papa )
		bSizerMyFrame1.Add( self.papa, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.SetSizer( bSizerMyFrame1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.inputTC.Bind( wx.EVT_TEXT, self.search )
		self.inputTC.Bind( wx.EVT_SET_FOCUS, self.showSearchSuggestion )
		self.inputTC.Bind( wx.EVT_KILL_FOCUS, self.hideSearchSuggestion )
		
		self.suggestionList.Bind (wx.EVT_SET_FOCUS, self.search )
		
		self.transactionButton.Bind( wx.EVT_BUTTON, self.CheckOutFunc )
		self.returnButton.Bind( wx.EVT_BUTTON, self.refundFunc )
		self.cleanCartButton.Bind( wx.EVT_BUTTON, self.clearEverything )
		
		self.productsGrid.Bind(wx.grid.EVT_GRID_CELL_CHANGED, self.cartChange)
		
		self.newCustomerButton.Bind ( wx.EVT_BUTTON, self.determineParty )

		# Collect barcode input
		#self.papa.Bind( wx.EVT_TEXT, self.barcodeInput )
		self.inputTC.Bind(wx.EVT_CHAR_HOOK, self.barcodeInput)
		#self.inputTC.SetFocus()
		
	def __del__( self ):
		pass

	def determineParty (self, event):
		dlg = nc.GetData(self.papa, self.t)
		dlg.ShowModal()
		
		if (self.t.customerId != 0):
			self.customerName.SetLabel("Name:  " + self.t.customerName)
			self.customerContact.SetLabel("Contact:  "+self.t.customerContact)
	
	def showSearchSuggestion (self, event):
		self.suggestionList.Show()
		self.Layout()
		
	def hideSearchSuggestion (self, event):
		if (self.suggestionList.HasFocus() == False):
			self.suggestionList.Hide()
			self.Layout()
		
	def search (self, event):
		self.suggestionList.SetItems( self.suggestionCandidatesAsList( self.inputTC.GetValue() ) )
		self.suggestionList.Show()
		self.suggestionList.SetSelection(0)
		self.Layout()
		
	def cartChange (self, event):
		# this function deals with all types in changes in the cart
		r = event.GetRow()
		if (event.GetCol() == 2):
			# if quantity was changed
			x = self.t.increaseQty( int(self.productsGrid.GetCellValue(r, 0)), int(self.productsGrid.GetCellValue(r, 2))-self.t.getCartProducts()[r].qty )
			if x == True:
				self.productsGrid.SetCellValue(r, 5, str( self.t.getCartProducts()[r].qty * self.t.getCartProducts()[r].price ))
				self.productsGrid.SetCellValue(r, 4, str( self.t.getCartProducts()[r].qty * ( self.t.getCartProducts()[r].origPrice - self.t.getCartProducts()[r].price ) ))
			if type(x) == type(int()):
				self.alert("Only "+str(x)+" are available", '')
				self.productsGrid.SetCellValue(r, 2, event.GetString())
		
		if (event.GetCol() == 3):
			# if unit price was changed
			self.t.getCartProducts()[r].price = int(self.productsGrid.GetCellValue(r, 3))
			
			self.productsGrid.SetCellValue(r, 4, str( self.t.getCartProducts()[r].qty * ( self.t.getCartProducts()[r].origPrice - self.t.getCartProducts()[r].price ) ))
			self.productsGrid.SetCellValue(r, 5, str( self.t.getCartProducts()[r].qty * self.t.getCartProducts()[r].price ))
			
		if (event.GetCol() == 4):
			# if discount was changed
			self.t.getCartProducts()[r].price = self.t.getCartProducts()[r].price - ( int(self.productsGrid.GetCellValue(r, 4)) / self.t.getCartProducts()[r].qty )
			
			self.productsGrid.SetCellValue(r, 3, str( self.t.getCartProducts()[r].price ))
			self.productsGrid.SetCellValue(r, 5, str( self.t.getCartProducts()[r].qty * self.t.getCartProducts()[r].price ))
		
		if (event.GetCol() == 5):
			# if total price was changed
			self.t.getCartProducts()[r].price = int(self.productsGrid.GetCellValue(r, 5)) / self.t.getCartProducts()[r].qty
			
			self.productsGrid.SetCellValue(r, 4, str( (self.t.getCartProducts()[r].origPrice - self.t.getCartProducts()[r].price) * self.t.getCartProducts()[r].qty ))
			self.productsGrid.SetCellValue(r, 3, str( self.t.getCartProducts()[r].price ))
		
		self.totalBill.SetLabel( "Total:  " + str( self.t.getCart().computeTotalBill() + self.t.getCart().computeTotalDiscount() ))
		self.discountTC.SetLabel( "Discount:  " + str( self.t.getCart().computeTotalDiscount() ))
		self.billAfterDiscount.SetLabel( "After Discount:  " + str( self.t.getCart().computeTotalBill() ))
	
	def suggestionCandidates (self, searchString):
		qry = 'SELECT products.name, products.codeName, products.costPrice, products.sellingPrice, products.barcode FROM `currentinventory`, `products` WHERE products.id = currentinventory.productId AND codeName LIKE "%'+str(searchString)+'%"'
		conn = connectToDB()
		curs = conn.cursor()
		curs.execute(qry)
		r = curs.fetchall()
		menu = wx.Menu()
		for x in r:
			help = "Rs. " + str(x['costPrice']) + "   Rs. " + str(x['sellingPrice']) + "   " + str(x['barcode'])
			menu.Append(wx.ID_NEW, x['codeName'], helpString=help)
		return menu
	
	def suggestionCandidatesAsList (self, searchString):
		qry = 'SELECT DISTINCT products.name, products.codeName, products.costPrice, products.sellingPrice, products.barcode FROM `currentinventory`, `products` WHERE products.id = currentinventory.productId AND codeName LIKE "%'+str(searchString)+'%" OR BARCODE LIKE "%'+str(searchString)+'%"'
		conn = connectToDB()
		curs = conn.cursor()
		curs.execute(qry)
		r = curs.fetchall()
		sug = []
		for x in r:
			prod = x['codeName'] + "    - "+x['name']+"   Rs. " + str(x['costPrice']) + "   Rs. " + str(x['sellingPrice']) + "   " + str(x['barcode'])
			sug.append(prod)
		sug.append("New Product")
		return sug
	
	def fetchAllCodenames (self):
		qry = 'SELECT codeName FROM products'
		conn = connectToDB()
		curs = conn.cursor()
		curs.execute(qry)
		r = curs.fetchall()
		sug = []
		for x in r:
			sug.append(x['codeName'])
		return sug
		
	def refundFunc( self, event ):
		pass

	def CheckOutFunc( self, event ):
		pass

	def makePopUp(self, prompt, title):
		pp = wx.TextEntryDialog(self, prompt, title)
		pp.ShowModal()
		r = pp.GetValue()
		pp.Destroy()
		pp.Show()
		return r
	
	def makePopUpDate(self, prompt, title):
		pp = wx.TextEntryDialog(self, prompt, title)
		pp.ShowModal()
		r = pp.GetValue()
		pp.Destroy()
		pp.Show()
		return r
	
	def alert(self, msg, title):
		x = wx.MessageDialog(self, msg, title)
		x.ShowModal()
		
	def dumpCartInDvlc (self):
		for x in range(self.t.numberOfItems()):
			self.productsGrid.SetCellValue(x, 0, str( self.t.getCartProducts()[x].pid ))
			self.productsGrid.SetCellValue(x, 1, str( self.t.getCartProducts()[x].name ))
			self.productsGrid.SetCellValue(x, 2, str( self.t.getCartProducts()[x].qty ))
			self.productsGrid.SetCellValue(x, 3, str( self.t.getCartProducts()[x].price ))
			self.productsGrid.SetCellValue(x, 4, str( self.t.getCartProducts()[x].origPrice - self.t.getCartProducts()[x].price ))
			self.productsGrid.SetCellValue(x, 5, str( self.t.getCartProducts()[x].qty * self.t.getCartProducts()[x].price ))
		self.totalBill.SetLabel( "Total:  " + str( self.t.getCart().computeTotalBill() + self.t.getCart().computeTotalDiscount() ))
		self.discountTC.SetLabel( "Discount:  " + str( self.t.getCart().computeTotalDiscount() ))
		self.billAfterDiscount.SetLabel( "After Discount:  " + str( self.t.getCart().computeTotalBill() ))

	def clearCartGrid (self):
		for x in range(self.t.numberOfItems()):
			self.productsGrid.SetCellValue(x, 0, '')
			self.productsGrid.SetCellValue(x, 1, '')
			self.productsGrid.SetCellValue(x, 2, '')
			self.productsGrid.SetCellValue(x, 3, '')
			self.productsGrid.SetCellValue(x, 4, '')
			self.productsGrid.SetCellValue(x, 5, '')
		
		self.totalBill.SetLabel('Total:   0000000')
		self.discountTC.SetLabel( "Discount:  0000000" )
		self.billAfterDiscount.SetLabel( "After Discount:  0000000" )
		
		self.customerName.SetLabel('Name: ')
		self.customerContact.SetLabel('Contact:  ')
		#self.customerBalance.SetLabel('Balance:  ')
	
	def clearEverything (self, event=None):
		self.clearCartGrid()
		self.t.refresh()
	
	def newProd(self, bc):
		dlg = np.GetData(self.papa, bc)
		dlg.ShowModal()
	
	def identifyParty (self, inS):
		if self.t.fetchCustomerId(inS):
			self.customerName.SetLabel(self.t.customerName)
			self.customerContact.SetLabel(self.t.customerContact)
		else:
			dlg = nc.GetData(self.papa, inS)
			dlg.ShowModal()
			
			self.t.fetchCustomerId(inS)
			self.customerST.SetLabel(self.t.customerName)
	
	def barcodeInput (self, event):
		if event.GetKeyCode() == wx.WXK_UP:
			self.suggestionList.SetSelection( self.suggestionList.GetSelection() -1 )
			return
		elif event.GetKeyCode() == wx.WXK_DOWN:
			self.suggestionList.SetSelection( self.suggestionList.GetSelection() +1 )
			return
		c = event.GetUnicodeKey()
		if c is 8:
			# backspace
			self.inputStream = self.inputStream[:-1]
		if c is 27:
			# esc key
			self.inputStream = ''
		if c in range(48, 91):
			# number or alphabet
			self.inputStream = self.inputStream + chr(c)
		if c is 13:
			# enter key
			listSelection = self.suggestionList.GetString( self.suggestionList.GetSelection() )
			print (listSelection)
			if listSelection == "New Product":
				self.newProd( self.inputTC.GetValue() )
			else:
				x = self.t.findProduct( listSelection.split()[0] , 1)
				
				if x == True:
					self.dumpCartInDvlc()
					self.inputStream = ''
					self.hideSearchSuggestion(None)
		self.inputTC.SetValue(self.inputStream)
	


'''
class terminalPanel ( wx.Panel ):
	
	def __init__( self, parent, transactionButtonName ):
		# input stream
		self.inputStream = ''
		self.t = terminal()
		
		wx.Panel.__init__ ( self, parent, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.Size( -1,-1 ), wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_CAPTIONTEXT ) )
		
		bSizerMyFrame1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_papa = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
		
		bSizer231 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer5.SetMinSize( wx.Size( 150,20 ) ) 
		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer13.SetMinSize( wx.Size( 150,5 ) ) 
		bSizer15 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_customerST = wx.StaticText( self.m_papa, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_customerST.Wrap( -1 )
		self.m_customerST.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.m_customerST.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTIONTEXT ) )
		
		bSizer15.Add( self.m_customerST, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer13.Add( bSizer15, 1, wx.ALL|wx.EXPAND, 5 )
		
		#------------
		bSizerTS = wx.BoxSizer( wx.VERTICAL )
		
		self.m_searchProd = ACTextControl( self.m_papa, self.suggestionCandidates() )
		#self.m_searchProd.Wrap( -1 )
		#self.m_searchProd.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		#self.m_searchProd.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTIONTEXT ) )
		
		bSizerTS.Add( self.m_searchProd, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer13.Add( bSizerTS, 1, wx.ALL|wx.EXPAND, 5 )
		#--------------
		
		bSizer16 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_balanceST = wx.StaticText( self.m_papa, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_balanceST.Wrap( -1 )
		self.m_balanceST.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.m_balanceST.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTIONTEXT ) )
		
		bSizer16.Add( self.m_balanceST, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer13.Add( bSizer16, 1, wx.EXPAND, 5 )
		
		bSizer17 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer13.Add( bSizer17, 1, wx.EXPAND, 5 )
		
		
		bSizer5.Add( bSizer13, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer231.Add( bSizer5, 0, wx.EXPAND, 5 )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer301 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer23 = wx.BoxSizer( wx.VERTICAL )
		
		########### Cart Grid Start
		self.m_productsGrid = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_productsGrid.CreateGrid( 99, 6 )
		self.m_productsGrid.EnableEditing( True )
		self.m_productsGrid.EnableGridLines( True )
		self.m_productsGrid.EnableDragGridSize( False )
		self.m_productsGrid.SetMargins( 0, 0 )
		self.m_productsGrid.SetRowLabelSize( 20 )
		
		self.m_productsGrid.SetColSize( 0, 40 )
		self.m_productsGrid.SetColSize( 1, 80 )
		self.m_productsGrid.SetColSize( 2, 120 )
		self.m_productsGrid.SetColSize( 3, 140 )
		self.m_productsGrid.SetColSize( 4, 160 )
		
		self.m_productsGrid.SetColLabelValue( 0, u"ID" )
		self.m_productsGrid.SetColLabelValue( 1, u"Name" )
		self.m_productsGrid.SetColLabelValue( 2, u"Quantity" )
		self.m_productsGrid.SetColLabelValue( 3, u"Unit Price" )
		self.m_productsGrid.SetColLabelValue( 4, u"Total Discount" )
		self.m_productsGrid.SetColLabelValue( 5, u"Total Price" )
		
		self.m_productsGrid.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		self.m_productsGrid.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		########### Cart Grid End
		
		bSizer23.Add( self.m_productsGrid, 1, wx.EXPAND|wx.ALL, 5 )
		
		
		bSizer301.Add( bSizer23, 1, wx.ALIGN_BOTTOM|wx.ALL|wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 5 )
		
		bSizer32 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer32.SetMinSize( wx.Size( -1,60 ) ) 
		bSizer31 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer31.SetMinSize( wx.Size( -1,60 ) ) 
		self.m_TotalST = wx.StaticText( self.m_papa, wx.ID_ANY, u"Total", wx.DefaultPosition, wx.Size( -1,60 ), 0 )
		self.m_TotalST.Wrap( -1 )
		self.m_TotalST.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		
		bSizer31.Add( self.m_TotalST, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer32.Add( bSizer31, 1, wx.EXPAND, 5 )
		
		bSizer33 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer33.SetMinSize( wx.Size( -1,60 ) ) 
		self.m_TotalAmtST = wx.StaticText( self.m_papa, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( -1,60 ), 0 )
		self.m_TotalAmtST.Wrap( -1 )
		self.m_TotalAmtST.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		
		bSizer33.Add( self.m_TotalAmtST, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer32.Add( bSizer33, 1, wx.EXPAND, 5 )
		
		
		bSizer301.Add( bSizer32, 0, wx.ALIGN_BOTTOM|wx.ALL|wx.FIXED_MINSIZE|wx.EXPAND, 5 )
		
		
		bSizer6.Add( bSizer301, 1, wx.EXPAND, 5 )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer24 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer9.Add( bSizer24, 1, wx.ALL|wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 5 )
		
		
		bSizer8.Add( bSizer9, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer41 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_transactionB = wx.Button( self.m_papa, wx.ID_ANY, transactionButtonName, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_transactionB.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.m_transactionB.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_CAPTIONTEXT ) )
		
		bSizer41.Add( self.m_transactionB, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer12.Add( bSizer41, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer88 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_returnB = wx.Button( self.m_papa, wx.ID_ANY, u"Return", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_returnB.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		
		bSizer88.Add( self.m_returnB, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizerCC = wx.BoxSizer( wx.VERTICAL )
		
		self.m_cleanCartB = wx.Button( self.m_papa, wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_cleanCartB.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		
		bSizerCC.Add( self.m_cleanCartB, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer12.Add( bSizerCC, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer12.Add( bSizer88, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer10.Add( bSizer12, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer30 = wx.BoxSizer( wx.HORIZONTAL )
		
		''
		bSizer40 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer40.SetMinSize( wx.Size( -1,200 ) ) 
		self.m_prodSuggest = wx.dataview.DataViewListCtrl( self.m_papa, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_prodSuggest.SetMinSize( wx.Size( -1,200 ) )
		
		self.m_prodSuggest.AppendTextColumn('Name')
		self.m_prodSuggest.AppendTextColumn('Price')
		
		bSizer40.Add( self.m_prodSuggest, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer30.Add( bSizer40, 1, wx.EXPAND, 5 )
		''
		
		bSizer10.Add( bSizer30, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer8.Add( bSizer10, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer6.Add( bSizer8, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer231.Add( bSizer6, 1, wx.EXPAND, 5 )
		
		
		self.m_papa.SetSizer( bSizer231 )
		self.m_papa.Layout()
		bSizer231.Fit( self.m_papa )
		bSizerMyFrame1.Add( self.m_papa, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizerMyFrame1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_transactionB.Bind( wx.EVT_BUTTON, self.CheckOutFunc )
		self.m_returnB.Bind( wx.EVT_BUTTON, self.refundFunc )
		self.m_cleanCartB.Bind( wx.EVT_BUTTON, self.clearEverything )
		self.m_productsGrid.Bind(wx.grid.EVT_GRID_CELL_CHANGED, self.cartChange)
		
		# Collect barcode input
		#self.m_papa.Bind(wx.EVT_CHAR_HOOK, self.barcodeInput)
		self.m_papa.SetFocus()
		
	def __del__( self ):
		pass
		
	def cartChange (self, event):
		# this function deals with all types in changes in the cart
		r = event.GetRow()
		if (event.GetCol() == 2):
			# if quantity was changed
			x = self.t.increaseQty( int(self.m_productsGrid.GetCellValue(r, 0)), int(self.m_productsGrid.GetCellValue(r, 2))-self.t.getCartProducts()[r].qty )
			if x == True:
				self.m_productsGrid.SetCellValue(r, 5, str( self.t.getCartProducts()[r].qty * self.t.getCartProducts()[r].price ))
				self.m_productsGrid.SetCellValue(r, 4, str( self.t.getCartProducts()[r].qty * ( self.t.getCartProducts()[r].origPrice - self.t.getCartProducts()[r].price ) ))
			if type(x) == type(int()):
				self.alert("Only "+str(x)+" are available", '')
				self.m_productsGrid.SetCellValue(r, 2, event.GetString())
		
		if (event.GetCol() == 3):
			# if unit price was changed
			self.t.getCartProducts()[r].price = int(self.m_productsGrid.GetCellValue(r, 3))
			
			self.m_productsGrid.SetCellValue(r, 4, str( self.t.getCartProducts()[r].qty * ( self.t.getCartProducts()[r].origPrice - self.t.getCartProducts()[r].price ) ))
			self.m_productsGrid.SetCellValue(r, 5, str( self.t.getCartProducts()[r].qty * self.t.getCartProducts()[r].price ))
			
		if (event.GetCol() == 4):
			# if discount was changed
			self.t.getCartProducts()[r].price = self.t.getCartProducts()[r].price - ( int(self.m_productsGrid.GetCellValue(r, 4)) / self.t.getCartProducts()[r].qty )
			
			self.m_productsGrid.SetCellValue(r, 3, str( self.t.getCartProducts()[r].price ))
			self.m_productsGrid.SetCellValue(r, 5, str( self.t.getCartProducts()[r].qty * self.t.getCartProducts()[r].price ))
		
		if (event.GetCol() == 5):
			# if total price was changed
			self.t.getCartProducts()[r].price = int(self.m_productsGrid.GetCellValue(r, 5)) / self.t.getCartProducts()[r].qty
			
			self.m_productsGrid.SetCellValue(r, 4, str( (self.t.getCartProducts()[r].origPrice - self.t.getCartProducts()[r].price) * self.t.getCartProducts()[r].qty ))
			self.m_productsGrid.SetCellValue(r, 3, str( self.t.getCartProducts()[r].price ))
		
		self.m_TotalAmtST.SetLabel(str( self.t.getCart().computeTotalBill() ))
	
	def suggestionCandidates (self):
		qry = 'select codeName from products'
		conn = connectToDB()
		curs = conn.cursor()
		curs.execute(qry)
		r = curs.fetchall()
		cand = []
		for x in r:
			cand.append(x['codeName'])
		return cand
		
	def refundFunc( self, event ):
		pass

	def CheckOutFunc( self, event ):
		pass

	def makePopUp(self, prompt, title):
		pp = wx.TextEntryDialog(self, prompt, title)
		pp.ShowModal()
		r = pp.GetValue()
		pp.Destroy()
		pp.Show()
		return r
	
	def makePopUpDate(self, prompt, title):
		pp = wx.TextEntryDialog(self, prompt, title)
		pp.ShowModal()
		r = pp.GetValue()
		pp.Destroy()
		pp.Show()
		return r
	
	def alert(self, msg, title):
		x = wx.MessageDialog(self, msg, title)
		x.ShowModal()
		
	def dumpCartInDvlc (self):
		for x in range(self.t.numberOfItems()):
			self.m_productsGrid.SetCellValue(x, 0, str( self.t.getCartProducts()[x].pid ))
			self.m_productsGrid.SetCellValue(x, 1, str( self.t.getCartProducts()[x].name ))
			self.m_productsGrid.SetCellValue(x, 2, str( self.t.getCartProducts()[x].qty ))
			self.m_productsGrid.SetCellValue(x, 3, str( self.t.getCartProducts()[x].price ))
			self.m_productsGrid.SetCellValue(x, 4, str( self.t.getCartProducts()[x].origPrice - self.t.getCartProducts()[x].price ))
			self.m_productsGrid.SetCellValue(x, 5, str( self.t.getCartProducts()[x].qty * self.t.getCartProducts()[x].price ))
		self.m_TotalAmtST.SetLabel(str( self.t.getCart().computeTotalBill() ))

	def clearCartGrid (self):
		for x in range(self.t.numberOfItems()):
			self.m_productsGrid.SetCellValue(x, 0, '')
			self.m_productsGrid.SetCellValue(x, 1, '')
			self.m_productsGrid.SetCellValue(x, 2, '')
			self.m_productsGrid.SetCellValue(x, 3, '')
			self.m_productsGrid.SetCellValue(x, 4, '')
			self.m_productsGrid.SetCellValue(x, 5, '')
		self.m_TotalAmtST.SetLabel('0')
		self.m_customerST.SetLabel('')
	
	def clearEverything (self, event=None):
		self.clearCartGrid()
		self.t.refresh()
	
	def newProd(self, bc):
		dlg = np.GetData(self.m_papa, bc)
		dlg.ShowModal()
	
	def identifyParty (self, inS):
		if self.t.fetchCustomerId(inS):
			self.m_customerST.SetLabel(self.t.customerName)
		else:
			dlg = nc.GetData(self.m_papa, inS)
			dlg.ShowModal()
			
			self.t.fetchCustomerId(inS)
			self.m_customerST.SetLabel(self.t.customerName)
	
	def barcodeInput (self, event):
		c = event.GetUnicodeKey()
		if c is 8:
			# backspace
			self.inputStream = self.inputStream[:-1]
		if c is 27:
			# esc key
			self.inputStream = ''
		if c in range(48, 91):
			# number or alphabet
			self.inputStream = self.inputStream + chr(c)
		if c is 13:
			# enter key
			inS = self.inputStream
			self.inputStream = ''
			
			#checking for custom commands first
			if inS[:5] == 'SWINC':
				# increase quantity of last entered product
				return
			
			if inS[:5] == 'SWDEC':
				# decrease quantity of last entered product
				return
				
			if inS == 'SWPRNTRCPT':
				# print reciept
				return
			
			if inS[:2] == '03' and len(inS) == 11:
				# identify customer using the entered mobile number or register one
				self.identifyParty(inS)
				return
			
			# otherwise check if the entered string was a barcode number
			x = self.t.findProduct(inS, 1)
			
			''
			if x == False:
				self.alert("Already in the cart", '')
		
			if type(x) == type(int()):
				self.alert("Only "+str(x)+" are available", '')
			''
			
			if x == True:
				self.dumpCartInDvlc()
			
			if x is None:
				self.newProd(inS)
				x = self.t.findProduct(inS, 1)
				if x == True:
					self.dumpCartInDvlc()
				''
				if type(x) == type(int()):
					self.alert("Only "+str(x)+" are available", '')
				''
			
				# unfinished business here
		self.m_balanceST.SetLabel(self.inputStream)
'''
