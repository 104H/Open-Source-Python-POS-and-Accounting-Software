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
import wx.adv
import re

from connectToDb import connectToDB

conn = connectToDB()

###########################################################################
## Class MyFrame1
###########################################################################

class incomeStatementPanel ( wx.Panel ):
	
	def __init__( self, parent ):
		
		wx.Panel.__init__ ( self, parent, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		
		bSizerMain = wx.BoxSizer( wx.VERTICAL )
		
		bSizerDate = wx.BoxSizer( wx.HORIZONTAL )
		bSizerGrid = wx.BoxSizer( wx.HORIZONTAL )
		
		########### Date Picker Start
		self.m_startDate = wx.adv.DatePickerCtrl(self, size=(60,-1), style = wx.adv.DP_DROPDOWN | wx.adv.DP_SHOWCENTURY | wx.adv.DP_ALLOWNONE)
		self.m_endDate = wx.adv.DatePickerCtrl(self, size=(60,-1), style = wx.adv.DP_DROPDOWN | wx.adv.DP_SHOWCENTURY | wx.adv.DP_ALLOWNONE)
		########### Date Picker End
		
		bSizerDate.Add (self.m_startDate, 1, wx.ALL|wx.EXPAND, 5 )
		bSizerDate.Add (self.m_endDate, 1, wx.ALL|wx.EXPAND, 5 )
		
		########### Cart Grid Start
		self.m_journalGrid = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_journalGrid.CreateGrid( 50, 2 )
		self.m_journalGrid.EnableEditing( False )
		self.m_journalGrid.EnableGridLines( True )
		self.m_journalGrid.EnableDragGridSize( False )
		self.m_journalGrid.SetMargins( 0, 0 )
		self.m_journalGrid.SetRowLabelSize( 1 )
		#self.m_journalGrid.AutoSizeColLabelSize( True )
		
		'''
		self.m_journalGrid.SetColSize( 0, 20 )
		self.m_journalGrid.SetColSize( 1, 40 )
		self.m_journalGrid.SetColSize( 2, 60 )
		self.m_journalGrid.SetColSize( 3, 80 )
		self.m_journalGrid.SetColSize( 4, 90 )
		self.m_journalGrid.SetColSize( 5, 110 )
		self.m_journalGrid.SetColSize( 6, 130 )
		self.m_journalGrid.SetColSize( 7, 150 )
		self.m_journalGrid.SetColSize( 8, 170 )
		
		self.m_journalGrid.SetColSize( 0, 30 )
		self.m_journalGrid.SetColSize( 1, 60 )
		self.m_journalGrid.SetColSize( 2, 90 )
		self.m_journalGrid.SetColSize( 3, 120 )
		self.m_journalGrid.SetColSize( 4, 150 )
		self.m_journalGrid.SetColSize( 5, 180 )
		self.m_journalGrid.SetColSize( 6, 210 )
		self.m_journalGrid.SetColSize( 7, 240 )
		self.m_journalGrid.SetColSize( 8, 270 )
		self.m_journalGrid.SetColSize( 9, 300 )
		'''
		
		self.m_journalGrid.SetColSize( 0, 50 )
		self.m_journalGrid.SetColSize( 1, 100 )
		
		#self.m_journalGrid.SetColLabelValue( 0, u"Head Of Account" )
		#self.m_journalGrid.SetColLabelValue( 1, u"Amount" )
		
		self.m_journalGrid.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		self.m_journalGrid.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		self.populateTable()
		########### Cart Grid End
		
		bSizerGrid.Add (self.m_journalGrid, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizerMain.Add( bSizerDate, 1, wx.ALL|wx.EXPAND, 5 )
		bSizerMain.Add( bSizerGrid, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.SetSizer( bSizerMain )
		self.Layout()
		bSizerMain.Fit( self )
		
		self.m_startDate.Bind(wx.adv.EVT_DATE_CHANGED, self.dateChangeHandler)
		self.m_endDate.Bind(wx.adv.EVT_DATE_CHANGED, self.dateChangeHandler)
		
	def dateChangeHandler (self, event):
		self.reloadJournal()
	
	def reloadJournal (self):
		self.m_journalGrid.DeleteRows(numRows=self.m_journalGrid.GetNumberRows())
		self.m_journalGrid.InsertRows(numRows=500)
		
		self.populateTable()
	
	def populateTable (self):
		curs = conn.cursor()
		
		##### Sales
		qry = 'SELECT SUM(Credit) - SUM(Debit) as sales from generalLedger WHERE headOfAc = 4'
		curs.execute(qry)
		sales = curs.fetchone()['sales']
		
		qry = 'SELECT SUM(Debit) - SUM(Credit) as salesDisc from generalLedger WHERE headOfAc = 21'
		curs.execute(qry)
		salesDisc = curs.fetchone()['salesDisc']
		
		qry = 'SELECT SUM(Debit) - SUM(Credit) as salesReturn from generalLedger WHERE headOfAc = 23'
		curs.execute(qry)
		salesReturn = curs.fetchone()['salesReturn']
		
		netSales = sales - salesDisc - salesReturn
		
		qry = 'SELECT SUM(Debit) - SUM(Credit) as expenses from generalLedger WHERE headOfAc = 25'
		curs.execute(qry)
		expn = curs.fetchone()['expenses']
		
		qry = 'SELECT SUM(Debit) - SUM(Credit) as tax from generalLedger WHERE headOfAc = 26'
		curs.execute(qry)
		tax = curs.fetchone()['tax']
		
		###### Cost of Goods
		qry = 'SELECT inventory from inventoryVal WHERE dateTime BETWEEN "%s" AND "%s"' % (self.m_startDate.GetValue().Format("%F") + " 00:00:00", self.m_startDate.GetValue().Format("%F") + " 23:59:59")
		curs.execute(qry)
		openInv = curs.fetchone()['inventory']
		
		qry = 'SELECT inventory from inventoryVal WHERE dateTime BETWEEN "%s" AND "%s"' % (self.m_endDate.GetValue().Format("%F") + " 00:00:00", self.m_endDate.GetValue().Format("%F") + " 23:59:59")
		curs.execute(qry)
		clsInv = curs.fetchone()['inventory']
		
		####### Purchases
		qry = 'SELECT SUM(Debit) - SUM(Credit) as purchase from generalLedger WHERE headOfAc = 3'
		curs.execute(qry)
		purchase = curs.fetchone()['purchase']
		
		qry = 'SELECT SUM(Credit) - SUM(Debit) as purcDisc from generalLedger WHERE headOfAc = 22'
		curs.execute(qry)
		purchaseDisc = curs.fetchone()['purcDisc']
		
		qry = 'SELECT SUM(Credit) - SUM(Debit) as purcReturn from generalLedger WHERE headOfAc = 24'
		curs.execute(qry)
		purchaseReturn = curs.fetchone()['purcReturn']
		
		netPurchase = purchase - purchaseDisc - purchaseReturn
		
		##### Cost of Goods Sold
		cogs = openInv + netPurchase - clsInv
		
		grossProfit = sales - cogs
		
		netProfit = grossProfit - expn
		
		profitAfterTax = netProfit - tax
		
		###### Displaying in Grid
		self.m_journalGrid.SetCellValue(0, 0, "Sales")
		self.m_journalGrid.SetCellValue(0, 1, str( sales ))
		
		self.m_journalGrid.SetCellValue(2, 0, "Cost of Goods Sold")
		self.m_journalGrid.SetCellValue(2, 1, str( cogs ))
		
		self.m_journalGrid.SetCellValue(4, 0, "Gross Profit")
		self.m_journalGrid.SetCellValue(4, 1, str( grossProfit ))
		
		self.m_journalGrid.SetCellValue(6, 0, "Less")
		self.m_journalGrid.SetCellValue(7, 0, "     Expenses")
		self.m_journalGrid.SetCellValue(7, 1, str( expn ))
		
		self.m_journalGrid.SetCellValue(9, 0, "Net Profit")
		self.m_journalGrid.SetCellValue(9, 1, str( netProfit ))
		
		self.m_journalGrid.SetCellValue(11, 0, "Tax")
		self.m_journalGrid.SetCellValue(11, 1, str( tax ))
		
		self.m_journalGrid.SetCellValue(13, 0, "Profit After Tax")
		self.m_journalGrid.SetCellValue(13, 1, str( profitAfterTax ))
		
		#self.m_journalGrid.SetCellValue(, 0, "")
		#self.m_journalGrid.SetCellValue(, 1, str(  ))
		
		
		
				
