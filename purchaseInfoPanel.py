# 26th May, 2018 5:05pm

import wx
import wx.grid
import wx.xrc
import wx.dataview

from connectToDb import connectToDB
import updatePurchaseMoney as upm

class purchaseInfoPanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__( self, parent, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		self.m_purchaseGrid = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,700 ), 0 )
		
		p = self.populateTable()
		lenP = len(p)
		
		# Grid
		self.m_purchaseGrid.CreateGrid( lenP, 9 )
		self.m_purchaseGrid.EnableEditing( False )
		self.m_purchaseGrid.EnableGridLines( True )
		self.m_purchaseGrid.EnableDragGridSize( False )
		self.m_purchaseGrid.SetMargins( 0, 0 )
		
		# Populate Table
		col=0
		for x in p:
			row=0
			# if amount of invoice is smaller than the amount recieved yet, colour the cell red
			if float(x['totalBill']) > float(x['amountPaid']):
				self.m_purchaseGrid.SetCellBackgroundColour(row, 4, wx.Colour(255, 128, 128))
			for y in list(x.values()):
				self.m_purchaseGrid.SetCellValue(col, row, str(y))
				row = row+1
			col = col+1
		
		# Columns
		self.m_purchaseGrid.SetColSize( 0, 30 )
		self.m_purchaseGrid.SetColSize( 1, 100 )
		self.m_purchaseGrid.SetColSize( 2, 120 )
		self.m_purchaseGrid.SetColSize( 3, 140 )
		self.m_purchaseGrid.SetColSize( 4, 160 )
		self.m_purchaseGrid.SetColSize( 5, 210 )
		self.m_purchaseGrid.SetColSize( 6, 230 )
		self.m_purchaseGrid.SetColSize( 7, 250 )
		self.m_purchaseGrid.SetColSize( 8, 270 )
		#self.m_purchaseGrid.AutoSizeColumns()
		self.m_purchaseGrid.EnableDragColMove( True )
		self.m_purchaseGrid.EnableDragColSize( True )
		self.m_purchaseGrid.SetColLabelSize( 30 )
		self.m_purchaseGrid.SetColLabelValue( 0, u"ID" )
		self.m_purchaseGrid.SetColLabelValue( 1, u"Date Time" )
		self.m_purchaseGrid.SetColLabelValue( 2, u"Amount" )
		self.m_purchaseGrid.SetColLabelValue( 3, u"Amount Paid" )
		self.m_purchaseGrid.SetColLabelValue( 4, u"Supplier ID" )
		self.m_purchaseGrid.SetColLabelValue( 5, u"Supplier Name" )
		self.m_purchaseGrid.SetColLabelValue( 6, u"Supplier Contact" )
		self.m_purchaseGrid.SetColLabelValue( 7, u"Supplier Address" )
		self.m_purchaseGrid.SetColLabelValue( 8, u"Supplier IBAN" )
		self.m_purchaseGrid.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_purchaseGrid.EnableDragRowSize( False )
		self.m_purchaseGrid.SetRowLabelSize( 1 )
		self.m_purchaseGrid.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_purchaseGrid.SetDefaultCellAlignment( wx.ALIGN_CENTRE, wx.ALIGN_TOP )
		bSizer11.Add( self.m_purchaseGrid, 0, wx.ALIGN_CENTRE|wx.ALL, 5 )
		
		self.SetSizer( bSizer11 )
		self.Layout()
		bSizer11.Fit( self )
		
		self.m_purchaseGrid.Bind( wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.updateCollectedMoney )
		
	def populateTable (self):
		qry = 'SELECT p.id, p.dateTime, p.totalBill, p.amountPaid, s.id, s.name, s.contact, s.iban FROM purchase p, supplier s where s.id=p.supplier ORDER BY p.id'
		
		con = connectToDB()
		curs = con.cursor()
		curs.execute(qry)
		
		inv = []
		
		while (1):
			r = curs.fetchone()
			if (r is not None):
				inv.append(r)
			else:
				return inv
		
	def updatePurchases (self):
		self.m_purchaseGrid.DeleteRows(numRows=self.m_purchaseGrid.GetNumberRows())
		
		p = self.populateTable()
		lenP = len(p)
		
		self.m_purchaseGrid.InsertRows(numRows=lenP)
		
		# Populate Table
		col=0
		for x in p:
			row=0
			x = list(x.values())
			if x[3] > x[4]:
				self.m_purchaseGrid.SetCellBackgroundColour(row, 4, wx.Colour(255, 128, 128))
			for y in x:
				self.m_purchaseGrid.SetCellValue(col, row, str(y))
				row = row+1
			col = col+1
	
	def updateCollectedMoney (self, event):
		iid = self.m_purchaseGrid.GetCellValue(event.GetRow(), 0)
		sid = self.m_purchaseGrid.GetCellValue(event.GetRow(), 4)
		dlg = upm.GetData(self, iid, sid)
		dlg.ShowModal()
		self.updatePurchases()
