# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Mar  6 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

import functions as f
#import bcr as bcr
#import printer as pr
import newCust as nc
import newProd as np

###########################################################################
## Class MyFrame1
###########################################################################

class salesPanel ( wx.Panel ):
	
	def __init__( self, parent ):
		# input stream
		self.inputStream = ''
		self.cartItems = 0
		self.custNo = 0
		
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
		
		self.m_checkoutB = wx.Button( self.m_papa, wx.ID_ANY, u"Cash Sale", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkoutB.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.m_checkoutB.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_CAPTIONTEXT ) )
		
		bSizer41.Add( self.m_checkoutB, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer12.Add( bSizer41, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer29 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_pInvoiceB = wx.Button( self.m_papa, wx.ID_ANY, u"Print Invoice", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_pInvoiceB.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		
		bSizer29.Add( self.m_pInvoiceB, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer12.Add( bSizer29, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer88 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_refundB = wx.Button( self.m_papa, wx.ID_ANY, u"Return", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_refundB.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		
		bSizer88.Add( self.m_refundB, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizerCC = wx.BoxSizer( wx.VERTICAL )
		
		self.m_cleanCartB = wx.Button( self.m_papa, wx.ID_ANY, u"Clean Cart", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_cleanCartB.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		
		bSizerCC.Add( self.m_cleanCartB, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer12.Add( bSizerCC, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer12.Add( bSizer88, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer10.Add( bSizer12, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer30 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer40 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer40.SetMinSize( wx.Size( -1,200 ) ) 
		self.m_prodSuggest = wx.dataview.DataViewListCtrl( self.m_papa, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_prodSuggest.SetMinSize( wx.Size( -1,200 ) )
		
		self.m_prodSuggest.AppendTextColumn('Name')
		self.m_prodSuggest.AppendTextColumn('Price')
		
		bSizer40.Add( self.m_prodSuggest, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer30.Add( bSizer40, 1, wx.EXPAND, 5 )
		
		
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
		self.m_checkoutB.Bind( wx.EVT_BUTTON, self.CheckOutFunc )
		self.m_pInvoiceB.Bind( wx.EVT_BUTTON, self.printInvoice )
		self.m_refundB.Bind( wx.EVT_BUTTON, self.refundFunc )
		self.m_cleanCartB.Bind( wx.EVT_BUTTON, self.clearCart )
		self.m_productsGrid.Bind(wx.grid.EVT_GRID_CELL_CHANGED, self.cartChange)
		
		# Collect barcode input
		self.m_papa.Bind(wx.EVT_CHAR_HOOK, self.barcodeInput)
		self.m_papa.SetFocus()
		
	def __del__( self ):
		pass
		
	def cartChange (self, event):
		# this function deals with all types in changes in the cart
		r = event.GetRow()
		if (event.GetCol() == 2):
			# if quantity was changed
			x = f.incQty( int(self.m_productsGrid.GetCellValue(r, 0)), int(self.m_productsGrid.GetCellValue(r, 2))-f.cart['qty'][r] )
			if x == True:
				self.m_productsGrid.SetCellValue(r, 5, str(f.cart['totalPrice'][r]))
				self.m_productsGrid.SetCellValue(r, 4, str( (f.cart['origPrice'][r] - f.cart['price'][r]) * f.cart['qty'][r] ))
			if type(x) == type(int()):
				self.alert("Only "+str(x)+" are available", '')
				self.m_productsGrid.SetCellValue(r, 2, event.GetString())
		
		if (event.GetCol() == 3):
			# if unit price was changed
			#f.cart['discount'][r] = f.cart['discount'][r] + int( f.cart['price'][r] - int(self.m_productsGrid.GetCellValue(r, 3)) )
			f.cart['price'][r] = int(self.m_productsGrid.GetCellValue(r, 3))
			f.cart['totalPrice'][r] = f.cart['qty'][r] * f.cart['price'][r]
			
			self.m_productsGrid.SetCellValue(r, 4, str( (f.cart['origPrice'][r] - f.cart['price'][r]) * f.cart['qty'][r] ))
			self.m_productsGrid.SetCellValue(r, 5, str(f.cart['totalPrice'][r]))
			
		if (event.GetCol() == 4):
			# if discount was changed
			#f.cart['discount'][r] = int(self.m_productsGrid.GetCellValue(r, 4))
			f.cart['price'][r] = f.cart['price'][r] - int(self.m_productsGrid.GetCellValue(r, 4))
			f.cart['totalPrice'][r] = f.cart['qty'][r] * f.cart['price'][r]
			
			self.m_productsGrid.SetCellValue(r, 3, str(f.cart['price'][r]))
			self.m_productsGrid.SetCellValue(r, 5, str(f.cart['totalPrice'][r]))
		
		if (event.GetCol() == 5):
			# if total price was changed
			f.cart['totalPrice'][r] = int(self.m_productsGrid.GetCellValue(r, 5))
			#f.cart['discount'][r] = f.cart['discount'][r] + f.cart['price'][r] - f.cart['totalPrice'][r] / f.cart['qty'][r]
			f.cart['price'][r] = f.cart['totalPrice'][r] / f.cart['qty'][r]
			
			self.m_productsGrid.SetCellValue(r, 4, str( (f.cart['origPrice'][r] - f.cart['price'][r]) * f.cart['qty'][r] ))
			self.m_productsGrid.SetCellValue(r, 3, str(f.cart['price'][r]))
		
		self.m_TotalAmtST.SetLabel(str(f.computeTotalBill()))
	
	
	def refundFunc( self, event ):
		try:
			f.refundProd(self.custNo)
			self.clearEverything()
		except ValueError:
			self.alert("Cart is Empty", "Alert")
		else:
			pass
		self.m_balanceST.SetFocus()

	def CheckOutFunc( self, event ):
		try:
			bill=str(f.computeTotalBill())
			f.checkout(self.custNo)
			self.clearEverything()
			
		except ValueError:
			self.alert("Cart is Empty", "Alert")
		else:
			pass
		self.m_balanceST.SetFocus()

	def printInvoice(self, event):
		amt = self.makePopUp("Enter Recieved Amount", "Amount Recieved")
		try:
			f.prepareInvoice (self.custNo, amt)
			self.clearEverything()
		except ValueError:
			self.alert("Cart is Empty", "Alert")
		else:
			pass
		self.m_balanceST.SetFocus()

	def makePopUp(self, prompt, title):
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
		for x in range(self.cartItems):
			self.m_productsGrid.SetCellValue(x, 0, str( f.cart['pid'][x] ))
			self.m_productsGrid.SetCellValue(x, 1, str( f.cart['name'][x] ))
			self.m_productsGrid.SetCellValue(x, 2, str( f.cart['qty'][x] ))
			self.m_productsGrid.SetCellValue(x, 3, str( f.cart['price'][x] ))
			self.m_productsGrid.SetCellValue(x, 4, str( f.cart['origPrice'][x] - f.cart['price'][x] ))
			self.m_productsGrid.SetCellValue(x, 5, str( f.cart['totalPrice'][x] ))
		self.m_TotalAmtST.SetLabel(str(f.computeTotalBill()))
	
	def cleanCart (self):
		for x in range(self.cartItems):
			self.m_productsGrid.SetCellValue(x, 0, '')
			self.m_productsGrid.SetCellValue(x, 1, '')
			self.m_productsGrid.SetCellValue(x, 2, '')
			self.m_productsGrid.SetCellValue(x, 3, '')
			self.m_productsGrid.SetCellValue(x, 4, '')
			self.m_productsGrid.SetCellValue(x, 5, '')
		self.m_TotalAmtST.SetLabel('0')
	
	def clearCart (self, event):
		self.cleanCart()
		f.releaseAllProducts()
	
	def clearEverything (self):
		self.cleanCart()
		self.custNo = 0
		self.m_customerST.SetLabel('')
		self.cartItems = 0
	
	def newCust(self):
		dlg = nc.GetData(parent = self.m_papa)
		dlg.ShowModal()
		
	def newProd(self, bc):
		dlg = np.GetData(self.m_papa, bc)
		dlg.ShowModal()
		
	def barcodeInput (self, event):
		c = event.GetUnicodeKey()
		#print(c)
		if c is 8:
			#backspace
			self.inputStream = self.inputStream[:-1]
		if c is 27:
			# esc key
			self.inputStream = ''
		if c in range(48, 91):
			# number or alphabet
			self.inputStream = self.inputStream + chr(c)
		if c is 13:
			# enter key
			print(self.inputStream)
			inS = self.inputStream
			self.inputStream = ''
			
			#checking for custom commands first
			print(inS[:5])
			if inS[:5] == 'SWINC':
				x = f.incQty(f.cart['pid'][-1:][0], int(inS[5:]))
				if x == True:
					self.dumpCartInDvlc()
				if type(x) == type(int()):
					self.alert("Only "+str(x)+" are available", '')
				return
			
			if inS[:5] == 'SWDEC':
				f.incQty(f.cart['pid'][-1:][0], -int(inS[5:]))
				self.dumpCartInDvlc()
				return
				
			if inS == 'SWPRNTRCPT':
				self.CheckOutFunc(1)
				return
			
			if inS[:2] == '03' and len(inS) == 11:
				customer = f.fetchClientId(inS)
				self.m_customerST.SetLabel(customer['name'])
				self.custNo = customer['id']
				return
			
			if inS == 'NEWCUST':
				self.newCust()
				return
			
			qty = 1
			x = f.findBarcode(inS, qty)
		
			if x == False:
				self.alert("Already in the cart", '')
		
			if x == True:
				self.cartItems = self.cartItems+1
				self.dumpCartInDvlc()
		
			if type(x) == type(int()):
				self.alert("Only "+str(x)+" are available", '')
			
			if x is None:
				self.newProd(inS)
				x = f.findBarcode(inS, qty)
				if x == True:
					self.cartItems = self.cartItems+1
					self.dumpCartInDvlc()
					self.m_TotalAmtST.SetLabel(str(f.computeTotalBill()))
				if type(x) == type(int()):
					self.alert("Only "+str(x)+" are available", '')
			
				# unfinished business here
				
			
		self.m_balanceST.SetLabel(self.inputStream)
