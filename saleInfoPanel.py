# 26th May, 2018 5:05pm

import wx
import wx.grid
import wx.xrc
import wx.dataview

from connectToDb import connectToDB

class saleInfoPanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__( self, parent, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		self.m_invoiceGrid = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		
		p = self.populateTable()
		lenP = len(p)
		
		# Grid
		self.m_invoiceGrid.CreateGrid( lenP, 8 )
		self.m_invoiceGrid.EnableEditing( False )
		self.m_invoiceGrid.EnableGridLines( True )
		self.m_invoiceGrid.EnableDragGridSize( False )
		self.m_invoiceGrid.SetMargins( 0, 0 )
		
		# Populate Table
		col=0
		for x in p:
			row=0
			for y in list(x.values()):
				self.m_invoiceGrid.SetCellValue(col, row, str(y))
				row = row+1
			col = col+1
		
		# Columns
		self.m_invoiceGrid.SetColSize( 0, 30 )
		self.m_invoiceGrid.SetColSize( 1, 60 )
		self.m_invoiceGrid.SetColSize( 2, 90 )
		#self.m_invoiceGrid.AutoSizeColumns()
		self.m_invoiceGrid.EnableDragColMove( True )
		self.m_invoiceGrid.EnableDragColSize( True )
		self.m_invoiceGrid.SetColLabelSize( 30 )
		self.m_invoiceGrid.SetColLabelValue( 0, u"ID" )
		self.m_invoiceGrid.SetColLabelValue( 1, u"Date Time" )
		self.m_invoiceGrid.SetColLabelValue( 2, u"Amount" )
		self.m_invoiceGrid.SetColLabelValue( 3, u"Employee ID" )
		self.m_invoiceGrid.SetColLabelValue( 4, u"Refund" )
		self.m_invoiceGrid.SetColLabelValue( 5, u"Customer Name" )
		self.m_invoiceGrid.SetColLabelValue( 6, u"Customer Contact" )
		self.m_invoiceGrid.SetColLabelValue( 7, u"Customer Address" )
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
		
	def populateTable (self):
		qry = 'select s.id, s.dateTime, s.totalBill, s.preparedBy, s.refund, c.name, c.contact, c.address from sales s, customer c where s.customer = c.id'
		
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
		
	def updateStocks (self):
		self.m_invoiceGrid.DeleteRows(numRows=self.m_invoiceGrid.GetNumberRows())
		
		p = self.populateTable()
		lenP = len(p)
		
		self.m_invoiceGrid.InsertRows(numRows=lenP)
		
		# Populate Table
		col=0
		for x in p:
			row=0
			for y in list(x.values()):
				self.m_invoiceGrid.SetCellValue(col, row, str(y))
				row = row+1
			col = col+1
	
	def refundSale (self, event):
		iid = self.m_custInfoGrid.GetCellValue(event.GetRow(), 0)
		dlg = uim.GetData(self, iid) 
		dlg.ShowModal()
		self.updateInvoices()
