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

class controlAccountPanel ( wx.Panel ):
	
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
		
		self.m_journalGrid.SetColLabelValue( 0, u"Head Of Account" )
		self.m_journalGrid.SetColLabelValue( 1, u"Amount" )
		
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
		row = 0
		# 1 -- debit - credit
		# 0 -- credit - debit
		for x in range(2):
			if x == 0:
				computation = "SUM(gl.Credit) - SUM(gl.Debit)"
			elif x == 1:
				computation = "SUM(gl.Debit) - SUM(gl.Credit)"
				
			qry = 'SELECT hoa.description, %s as amt FROM generalLedger gl, headOfAccounts hoa WHERE gl.headOfAc = hoa.id AND gl.dateTime BETWEEN "%s" AND "%s" AND hoa.computation = %s GROUP BY gl.headOfAc' % (computation, self.m_startDate.GetValue().Format("%F") + " 00:00:00", self.m_endDate.GetValue().Format("%F") + " 23:59:59", str(x))
			curs = conn.cursor()
			curs.execute(qry)
		
			while (1):
				r = curs.fetchone()
				if (r is not None):
					self.m_journalGrid.SetCellValue(row, 0, r['description'])
					self.m_journalGrid.SetCellValue(row, 1, str(r['amt']))
					row = row + 1
				else:
					break
				
				
				
				
