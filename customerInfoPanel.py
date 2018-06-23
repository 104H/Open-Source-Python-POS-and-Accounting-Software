# 26th May, 2018 5:05pm

import wx
import wx.grid
import wx.xrc
import wx.dataview

from connectToDb import connectToDB

class customerInfoPanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__( self, parent, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		self.m_custInfoGrid = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,700 ), 0 )
		
		p = self.populateTable()
		lenP = len(p)
		
		# Grid
		self.m_custInfoGrid.CreateGrid( lenP, 5 )
		self.m_custInfoGrid.EnableEditing( False )
		self.m_custInfoGrid.EnableGridLines( True )
		self.m_custInfoGrid.EnableDragGridSize( False )
		self.m_custInfoGrid.SetMargins( 0, 0 )
		
		# Populate Table
		col=0
		for x in p:
			row=0
			# if amount of invoice is smaller than the amount recieved yet, colour the cell red
			if float(x['balance']) > 0:
				self.m_custInfoGrid.SetCellTextColour(row, 4, wx.Colour(255, 128, 128))
			for y in list(x.values()):
				self.m_custInfoGrid.SetCellValue(col, row, str(y))
				row = row+1
			col = col+1
		
		# Columns
		self.m_custInfoGrid.SetColSize( 0, 30 )
		self.m_custInfoGrid.SetColSize( 1, 100 )
		self.m_custInfoGrid.SetColSize( 2, 120 )
		self.m_custInfoGrid.SetColSize( 3, 140 )
		#self.m_custInfoGrid.AutoSizeColumns()
		self.m_custInfoGrid.EnableDragColMove( True )
		self.m_custInfoGrid.EnableDragColSize( True )
		self.m_custInfoGrid.SetColLabelSize( 30 )
		self.m_custInfoGrid.SetColLabelValue( 0, u"ID" )
		self.m_custInfoGrid.SetColLabelValue( 1, u"Name" )
		self.m_custInfoGrid.SetColLabelValue( 2, u"Contact" )
		self.m_custInfoGrid.SetColLabelValue( 3, u"Address" )
		self.m_custInfoGrid.SetColLabelValue( 4, u"Balance" )
		self.m_custInfoGrid.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_custInfoGrid.EnableDragRowSize( False )
		self.m_custInfoGrid.SetRowLabelSize( 1 )
		self.m_custInfoGrid.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_custInfoGrid.SetDefaultCellAlignment( wx.ALIGN_CENTRE, wx.ALIGN_TOP )
		bSizer11.Add( self.m_custInfoGrid, 0, wx.ALIGN_CENTRE|wx.ALL, 5 )
		
		self.SetSizer( bSizer11 )
		self.Layout()
		bSizer11.Fit( self )
		
		#self.m_custInfoGrid.Bind( wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.updateCollectedMoney )
		
	def populateTable (self):
		qry = 'select c.id, c.name, c.contact, c.address, sum(i.amount - i.amountRecieved) as balance from customer c, invoice i where i.buyerId = c.id group by c.id'
		
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
		
	def updateCustomers (self):
		self.m_custInfoGrid.DeleteRows(numRows=self.m_custInfoGrid.GetNumberRows())
		
		p = self.populateTable()
		lenP = len(p)
		
		self.m_custInfoGrid.InsertRows(numRows=lenP)
		
		# Populate Table
		col=0
		for x in p:
			row=0
			x = list(x.values())
			if float(x[4]) > 0:
				self.m_custInfoGrid.SetCellBackgroundColour(x[0], 4, wx.Colour(255, 128, 128))
			for y in x:
				self.m_custInfoGrid.SetCellValue(col, row, str(y))
				row = row+1
			col = col+1
	
	def updateCollectedMoney (self, event):
		iid = self.m_custInfoGrid.GetCellValue(event.GetRow(), 0)
		dlg = uim.GetData(self, iid) 
		dlg.ShowModal()
		self.updateInvoices()
