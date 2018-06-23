# 26th May, 2018 5:05pm

import wx
import wx.grid
import wx.xrc
import wx.dataview

from connectToDb import connectToDB

class stockLevelsPanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__( self, parent, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		self.m_productsGrid = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		
		p = self.populateTable()
		lenP = len(p)
		
		# Grid
		self.m_productsGrid.CreateGrid( lenP, 8 )
		self.m_productsGrid.EnableEditing( True )
		self.m_productsGrid.EnableGridLines( True )
		self.m_productsGrid.EnableDragGridSize( False )
		self.m_productsGrid.SetMargins( 0, 0 )
		
		# Populate Table
		col=0
		for x in p:
			row=0
			for y in list(x.values()):
				self.m_productsGrid.SetCellValue(col, row, str(y))
				row = row+1
			col = col+1
		
		# Columns
		self.m_productsGrid.SetColSize( 0, 30 )
		self.m_productsGrid.SetColSize( 1, 60 )
		self.m_productsGrid.SetColSize( 2, 90 )
		self.m_productsGrid.SetColSize( 3, 120 )
		self.m_productsGrid.SetColSize( 4, 150 )
		self.m_productsGrid.SetColSize( 5, 180 )
		self.m_productsGrid.SetColSize( 6, 210 )
		self.m_productsGrid.SetColSize( 7, 240 )
		#self.m_productsGrid.AutoSizeColumns()
		self.m_productsGrid.EnableDragColMove( True )
		self.m_productsGrid.EnableDragColSize( True )
		self.m_productsGrid.SetColLabelSize( 30 )
		self.m_productsGrid.SetColLabelValue( 0, u"ID" )
		self.m_productsGrid.SetColLabelValue( 1, u"Name" )
		self.m_productsGrid.SetColLabelValue( 2, u"Code Name" )
		self.m_productsGrid.SetColLabelValue( 3, u"Cost Price" )
		self.m_productsGrid.SetColLabelValue( 4, u"Selling Price" )
		self.m_productsGrid.SetColLabelValue( 5, u"Minimum Required" )
		self.m_productsGrid.SetColLabelValue( 6, u"Current Quantity" )
		self.m_productsGrid.SetColLabelValue( 7, u"Barcode" )
		self.m_productsGrid.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_productsGrid.EnableDragRowSize( False )
		self.m_productsGrid.SetRowLabelSize( 1 )
		self.m_productsGrid.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_productsGrid.SetDefaultCellAlignment( wx.ALIGN_CENTRE, wx.ALIGN_TOP )
		bSizer11.Add( self.m_productsGrid, 0, wx.ALIGN_CENTRE|wx.ALL, 5 )
		
		self.m_productsGrid.Bind(wx.grid.EVT_GRID_CELL_CHANGED, self.tableChange)
		
		self.SetSizer( bSizer11 )
		self.Layout()
		bSizer11.Fit( self )
		
	def tableChange (self, event):
		r = event.GetRow()
		
		qry = 'UPDATE products, currentinventory SET products.name = "%s", products.codeName = "%s", products.costPrice = "%s", products.sellingPrice = "%s", products.minLevel = "%s", currentinventory.quantity = "%s", products.barcode = "%s" WHERE products.id = currentinventory.productId AND products.id = "%s"' % (self.m_productsGrid.GetCellValue(r, 1), self.m_productsGrid.GetCellValue(r, 2), self.m_productsGrid.GetCellValue(r, 3), self.m_productsGrid.GetCellValue(r, 4), self.m_productsGrid.GetCellValue(r, 5), self.m_productsGrid.GetCellValue(r, 6), self.m_productsGrid.GetCellValue(r, 7), self.m_productsGrid.GetCellValue(r, 0))
		con = connectToDB()
		curs = con.cursor()
		curs.execute(qry)
		con.commit()
		
		#self.reloadJournal()
		
	def populateTable (self):
		#qry = 'SELECT products.id, products.name, products.codeName, products.costPrice, products.sellingPrice, products.minLevel, currentinventory.quantity, products.barcode FROM `currentinventory`, `producttype`, `products` WHERE (producttype.id  = products.type) AND (products.id = currentinventory.productId)'
		qry = 'SELECT products.id, products.name, products.codeName, products.costPrice, products.sellingPrice, products.minLevel, currentinventory.quantity, products.barcode FROM `currentinventory`, `products` WHERE products.id = currentinventory.productId'
		con = connectToDB()
		curs = con.cursor()
		curs.execute(qry)
		
		prods = []
		
		while (1):
			r = curs.fetchone()
			if (r is not None):
				prods.append(r)
			else:
				break
		return prods
		
	def updateStocks (self):
		self.m_productsGrid.DeleteRows(numRows=self.m_productsGrid.GetNumberRows())
		
		p = self.populateTable()
		lenP = len(p)
		
		self.m_productsGrid.InsertRows(numRows=lenP)
		
		# Populate Table
		col=0
		for x in p:
			row=0
			for y in list(x.values()):
				self.m_productsGrid.SetCellValue(col, row, str(y))
				row = row+1
			col = col+1
