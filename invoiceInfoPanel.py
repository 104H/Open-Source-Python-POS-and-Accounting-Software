# 26th May, 2018 5:05pm

import wx
import wx.grid
import wx.xrc
import wx.dataview

from connectToDb import connectToDB
import updateInvoiceMoney as uim

class invoiceInfoPanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__( self, parent, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		self.m_invoiceGrid = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,700 ), 0 )
		
		p = self.populateTable()
		lenP = len(p)
		
		# Grid
		self.m_invoiceGrid.CreateGrid( lenP, 10 )
		self.m_invoiceGrid.EnableEditing( False )
		self.m_invoiceGrid.EnableGridLines( True )
		self.m_invoiceGrid.EnableDragGridSize( False )
		self.m_invoiceGrid.SetMargins( 0, 0 )
		
		# Populate Table
		col=0
		for x in p:
			row=0
			# if amount of invoice is smaller than the amount recieved yet, colour the cell red
			if float(x['amount']) > float(x['amountRecieved']):
				self.m_invoiceGrid.SetCellTextColour(row, 4, wx.Colour(255, 128, 128))
			for y in list(x.values()):
				self.m_invoiceGrid.SetCellValue(col, row, str(y))
				row = row+1
			col = col+1
		
		# Columns
		self.m_invoiceGrid.SetColSize( 0, 30 )
		self.m_invoiceGrid.SetColSize( 1, 100 )
		self.m_invoiceGrid.SetColSize( 2, 120 )
		self.m_invoiceGrid.SetColSize( 3, 140 )
		self.m_invoiceGrid.SetColSize( 4, 160 )
		self.m_invoiceGrid.SetColSize( 5, 210 )
		self.m_invoiceGrid.SetColSize( 6, 230 )
		self.m_invoiceGrid.SetColSize( 7, 250 )
		self.m_invoiceGrid.SetColSize( 8, 270 )
		self.m_invoiceGrid.SetColSize( 9, 300 )
		#self.m_invoiceGrid.AutoSizeColumns()
		self.m_invoiceGrid.EnableDragColMove( True )
		self.m_invoiceGrid.EnableDragColSize( True )
		self.m_invoiceGrid.SetColLabelSize( 30 )
		self.m_invoiceGrid.SetColLabelValue( 0, u"ID" )
		self.m_invoiceGrid.SetColLabelValue( 1, u"Date" )
		self.m_invoiceGrid.SetColLabelValue( 2, u"Time" )
		self.m_invoiceGrid.SetColLabelValue( 3, u"Amount" )
		self.m_invoiceGrid.SetColLabelValue( 4, u"Amount Recieved" )
		self.m_invoiceGrid.SetColLabelValue( 5, u"Bilty" )
		self.m_invoiceGrid.SetColLabelValue( 6, u"Agency" )
		self.m_invoiceGrid.SetColLabelValue( 7, u"Customer ID" )
		self.m_invoiceGrid.SetColLabelValue( 8, u"Customer Name" )
		self.m_invoiceGrid.SetColLabelValue( 9, u"Customer Contact" )
		self.m_invoiceGrid.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_invoiceGrid.EnableDragRowSize( False )
		self.m_invoiceGrid.SetRowLabelSize( 1 )
		self.m_invoiceGrid.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_invoiceGrid.SetDefaultCellAlignment( wx.ALIGN_CENTRE, wx.ALIGN_TOP )
		bSizer11.Add( self.m_invoiceGrid, 0, wx.ALIGN_CENTRE|wx.ALL, 5 )
		
		self.SetSizer( bSizer11 )
		self.Layout()
		bSizer11.Fit( self )
		
		self.m_invoiceGrid.Bind( wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.updateCollectedMoney )
		
	def populateTable (self):
		qry = 'select i.id, SUBSTRING(i.timeStamp, 1, 11), SUBSTRING(i.timeStamp, 12), i.amount, i.amountRecieved, i.transportKey, i.transportAgency, c.id, c.name, c.contact from customer c, invoice i where i.buyerId = c.id ORDER BY i.id'
		
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
		
	def updateInvoices (self):
		self.m_invoiceGrid.DeleteRows(numRows=self.m_invoiceGrid.GetNumberRows())
		
		p = self.populateTable()
		lenP = len(p)
		
		self.m_invoiceGrid.InsertRows(numRows=lenP)
		
		# Populate Table
		col=0
		for x in p:
			row=0
			x = list(x.values())
			if float(x[3]) > float(x[4]):
				self.m_invoiceGrid.SetCellBackgroundColour(x[0], 4, wx.Colour(255, 128, 128))
			for y in x:
				self.m_invoiceGrid.SetCellValue(col, row, str(y))
				row = row+1
			col = col+1
	
	def updateCollectedMoney (self, event):
		iid = self.m_invoiceGrid.GetCellValue(event.GetRow(), 0)
		cid = self.m_invoiceGrid.GetCellValue(event.GetRow(), 6)
		dlg = uim.GetData(self, iid, cid) 
		dlg.ShowModal()
		self.updateInvoices()
