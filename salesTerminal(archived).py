import wx
import wx.xrc
import wx.grid

class salesPanel ( wx.Panel ):
	
	def __init__( self, parent ):
		# input stream
		self.inputStream = ''

		wx.Panel.__init__ ( self, parent, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		
		self.mainSizer = wx.BoxSizer(wx.VERTICAL)
		
		self.topInfoSizer = wx.BoxSizer (wx.HORIZONTAL)
		
		self.topInfoSizerLeftSide = wx.BoxSizer (wx.VERTICAL)
		
		self.customerNoST = wx.StaticText( self, wx.ID_ANY, u"Customer ID: 99999")
		self.customerNoST.SetFont( wx.Font( 20, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.topInfoSizerLeftSide.Add (self.customerNoST, wx.EXPAND|wx.ALL)
		
		self.supplierNoST = wx.StaticText( self, wx.ID_ANY, u"Supplier ID: 99999")
		self.supplierNoST.SetFont( wx.Font( 20, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.topInfoSizerLeftSide.Add (self.supplierNoST, wx.EXPAND|wx.ALL)
		
		self.operatorNoST = wx.StaticText( self, wx.ID_ANY, u"Operator ID: 99999", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.operatorNoST.SetFont( wx.Font( 20, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.topInfoSizerLeftSide.Add (self.operatorNoST, wx.EXPAND|wx.ALL)
		
		self.topInfoSizerRightSide = wx.BoxSizer (wx.VERTICAL)
		
		self.inputStringST = wx.StaticText( self, wx.ID_ANY, u"Input String")
		self.inputStringST.SetFont( wx.Font( 20, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.topInfoSizerRightSide.Add (self.inputStringST, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER)
		
		self.topInfoSizer.Add (self.topInfoSizerLeftSide, wx.EXPAND|wx.ALIGN_LEFT)
		self.topInfoSizer.Add (self.topInfoSizerRightSide, wx.EXPAND|wx.ALIGN_RIGHT)
		
		self.bottomSizer = wx.BoxSizer (wx.HORIZONTAL)
		
		self.cartSizer = wx.BoxSizer (wx.HORIZONTAL)
		########### Cart Grid Start
		self.productsGrid = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.productsGrid.CreateGrid( 99, 6 )
		self.productsGrid.EnableEditing( True )
		self.productsGrid.EnableGridLines( True )
		self.productsGrid.EnableDragGridSize( False )
		self.productsGrid.SetMargins( 0, 0 )
		self.productsGrid.SetRowLabelSize( 20 )
		
		self.productsGrid.SetColSize( 0, 30 )
		self.productsGrid.SetColSize( 1, 60 )
		self.productsGrid.SetColSize( 2, 90 )
		self.productsGrid.SetColSize( 3, 120 )
		self.productsGrid.SetColSize( 4, 150 )
		self.productsGrid.SetColSize( 5, 180 )
		
		self.productsGrid.SetColLabelValue( 0, u"ID" )
		self.productsGrid.SetColLabelValue( 1, u"Name" )
		self.productsGrid.SetColLabelValue( 2, u"Quantity" )
		self.productsGrid.SetColLabelValue( 3, u"Unit Price" )
		self.productsGrid.SetColLabelValue( 4, u"Total Discount" )
		self.productsGrid.SetColLabelValue( 5, u"Total Price" )
		
		self.productsGrid.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		self.productsGrid.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		########### Cart Grid End
		self.cartSizer.Add (self.productsGrid)
		
		self.bottomRight = wx.BoxSizer (wx.VERTICAL)
		
		self.controlsSizer = wx.BoxSizer (wx.HORIZONTAL)
		
		self.cashSaleB = wx.Button( self, wx.ID_ANY, u"Cash Sale", wx.DefaultPosition, (200,200), 0 )
		self.cashSaleB.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.cashSaleB.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_CAPTIONTEXT ) )
		
		self.controlsSizer.Add (self.cashSaleB, 1, wx.ALL|wx.EXPAND, 5)
		
		self.returnB = wx.Button( self, wx.ID_ANY, u"Return", wx.DefaultPosition, (200,200), 0 )
		self.returnB.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.returnB.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_CAPTIONTEXT ) )
		
		self.controlsSizer.Add (self.returnB, 1, wx.ALL|wx.EXPAND, 5)
		
		self.clearB = wx.Button( self, wx.ID_ANY, u"Clear", wx.DefaultPosition, (200,200), 0 )
		self.clearB.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.clearB.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_CAPTIONTEXT ) )
		
		self.controlsSizer.Add (self.clearB, 1, wx.ALL|wx.EXPAND, 5)
		
		self.bottomRight.Add (self.controlsSizer, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER)
		
		self.billST = wx.StaticText( self, wx.ID_ANY, u"Bill: 99999")
		self.billST.SetFont( wx.Font( 20, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.bottomRight.Add (self.billST, wx.EXPAND|wx.ALL)
		
		self.DiscountTC = wx.TextCtrl( self, wx.ID_ANY, u"0", size=(200, 40))
		self.DiscountTC.SetFont( wx.Font( 20, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.bottomRight.Add (self.DiscountTC, wx.ALL)
		
		self.billAfterDiscountST = wx.StaticText( self, wx.ID_ANY, u"Bill After Discount: 99999")
		self.billAfterDiscountST.SetFont( wx.Font( 20, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.bottomRight.Add (self.billAfterDiscountST, wx.EXPAND|wx.ALL)
		
		self.bottomSizer.Add (self.cartSizer)
		self.bottomSizer.Add (self.bottomRight)
		
		self.mainSizer.Add (self.topInfoSizer, wx.EXPAND|wx.ALL)
		self.mainSizer.Add (self.bottomSizer, wx.EXPAND|wx.ALL)
		
		self.SetSizer( self.mainSizer )
		self.Layout()
		
		self.Bind(wx.EVT_CHAR_HOOK, self.keyInput)
		
	def keyInput(self, event):
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
			inS = self.inputStream
			self.inputStream = ''
			
			# checking for custom commands first
			# change to new supplier
			if inS[:2] == '03' and len(inS) == 11:
				# fetch or create new customer or supplier
				return
			
			# assume input is a barcode and look for a matching product in the database
			
			
		self.inputStringST.SetLabel(self.inputStream)
		
