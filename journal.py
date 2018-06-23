
import wx
import wx.xrc
import wx.grid
import wx.adv
import re

import manualJournalEntryPanel as mjep
from connectToDb import connectToDB
conn = connectToDB()

class journalPanel ( wx.Panel ):
	
	def __init__( self, parent ):
		
		wx.Panel.__init__ ( self, parent, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		
		bSizerMain = wx.BoxSizer( wx.VERTICAL )
		
		bSizerDate = wx.BoxSizer( wx.HORIZONTAL )
		bSizerGrid = wx.BoxSizer( wx.HORIZONTAL )
		
		########### Date Picker Start
		self.m_startDate = wx.adv.DatePickerCtrl(self, size=(60,-1), style = wx.adv.DP_DROPDOWN | wx.adv.DP_SHOWCENTURY | wx.adv.DP_ALLOWNONE)
		self.m_endDate = wx.adv.DatePickerCtrl(self, size=(60,-1), style = wx.adv.DP_DROPDOWN | wx.adv.DP_SHOWCENTURY | wx.adv.DP_ALLOWNONE)
		
		self.m_manEntryB = wx.Button( self, wx.ID_ANY, u"New Entry", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_manEntryB.Bind(wx.EVT_BUTTON, self.manEntry)
		########### Date Picker End
		
		bSizerDate.Add (self.m_startDate, 1, wx.ALL|wx.EXPAND, 5 )
		bSizerDate.Add (self.m_endDate, 1, wx.ALL|wx.EXPAND, 5 )
		bSizerDate.Add (self.m_manEntryB, 1, wx.ALL|wx.EXPAND, 5 )
		
		########### Cart Grid Start
		self.m_journalGrid = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_journalGrid.CreateGrid( 500, 9 )
		self.m_journalGrid.EnableEditing( True )
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
		'''
		
		self.m_journalGrid.SetColSize( 0, 30 )
		self.m_journalGrid.SetColSize( 1, 60 )
		self.m_journalGrid.SetColSize( 2, 90 )
		self.m_journalGrid.SetColSize( 3, 120 )
		self.m_journalGrid.SetColSize( 4, 150 )
		self.m_journalGrid.SetColSize( 5, 180 )
		self.m_journalGrid.SetColSize( 6, 210 )
		self.m_journalGrid.SetColSize( 7, 240 )
		self.m_journalGrid.SetColSize( 8, 270 )
		
		self.m_journalGrid.SetColLabelValue( 0, u"ID" )
		self.m_journalGrid.SetColLabelValue( 1, u"Date" )
		self.m_journalGrid.SetColLabelValue( 2, u"Time" )
		self.m_journalGrid.SetColLabelValue( 3, u"Head of A/C" )
		self.m_journalGrid.SetColLabelValue( 4, u"Folio Number" )
		self.m_journalGrid.SetColLabelValue( 5, u"Transaction ID" )
		self.m_journalGrid.SetColLabelValue( 6, u"Cheque Number" )
		self.m_journalGrid.SetColLabelValue( 7, u"Debit" )
		self.m_journalGrid.SetColLabelValue( 8, u"Credit" )
		
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
		self.m_journalGrid.Bind(wx.grid.EVT_GRID_CELL_CHANGED, self.journalChange)
	
	def journalChange (self, event):
		r = event.GetRow()
		
		qry = 'UPDATE `generalLedger` SET dateTime = "%s", headOfAc = "%s", transactionType = "%s", chequeNo = "%s", Debit = "%s", Credit = "%s" WHERE id = %s' % (self.m_journalGrid.GetCellValue(r, 1) + " " + self.m_journalGrid.GetCellValue(r, 2), self.m_journalGrid.GetCellValue(r, 4), self.m_journalGrid.GetCellValue(r, 5), self.m_journalGrid.GetCellValue(r, 6), self.m_journalGrid.GetCellValue(r, 7), self.m_journalGrid.GetCellValue(r, 8), self.m_journalGrid.GetCellValue(r, 0))
		print(qry)
		curs = conn.cursor()
		curs.execute(qry)
		conn.commit()
		
		#self.reloadJournal()
		
	def manEntry (self, event):
		dlg = mjep.GetData(self) 
		dlg.ShowModal()
		
		self.reloadJournal()
	
	def dateChangeHandler (self, event):
		self.reloadJournal()
	
	def reloadJournal (self):
		self.m_journalGrid.DeleteRows(numRows=self.m_journalGrid.GetNumberRows())
		self.m_journalGrid.InsertRows(numRows=500)
		
		self.populateTable()
	
	def populateTable (self):
		#print(type(self.m_startDate.GetValue()))
		#print(type(self.m_endDate.GetValue().Format("%F")))
		qry = 'SELECT gl.id, gl.dateTime, hoa.description, gl.headOfAc, gl.transactionType, gl.chequeNo, gl.Debit, gl.Credit FROM generalLedger gl, headOfAccounts hoa where gl.headOfAc = hoa.id and gl.dateTime BETWEEN "%s" AND "%s" ORDER BY gl.dateTime LIMIT 500' % ( self.m_startDate.GetValue().Format("%F") + " 00:00:00", self.m_endDate.GetValue().Format("%F") + " 23:59:59")
		curs = conn.cursor()
		curs.execute(qry)
		
		row = 0
		while (1):
			r = curs.fetchone()
			if (r is not None):
				x = re.search ("(?<=Customer)[0-9]*", r['description'])
				if x is not None:
					q = 'SELECT name FROM customer WHERE id = %s' % (x.group(0))
					c = conn.cursor()
					c.execute(q)
					cust = c.fetchone()
					r['description'] = cust['name'] + " A/C Recievable"
				
				x = re.search ("(?<=Supplier)[0-9]*", r['description'])
				if x is not None:
					q = 'SELECT name FROM supplier WHERE id = %s' % (x.group(0))
					c = conn.cursor()
					c.execute(q)
					cust = c.fetchone()
					r['description'] = cust['name'] + " A/C Payable"
				
				self.m_journalGrid.SetCellValue(row, 0, str(r['id']))
				self.m_journalGrid.SetCellValue(row, 1, str(r['dateTime'])[:10])
				self.m_journalGrid.SetCellValue(row, 2, str(r['dateTime'])[11:])
				
				if (r['Credit'] > 0):
					self.m_journalGrid.SetCellValue(row, 3, "        "+r['description'])
					self.m_journalGrid.SetCellValue(row, 8, str(r['Credit']))
				else:
					self.m_journalGrid.SetCellValue(row, 3, r['description'])
					self.m_journalGrid.SetCellValue(row, 7, str(r['Debit']))
				self.m_journalGrid.SetCellValue(row, 4, str(r['headOfAc']))
				self.m_journalGrid.SetCellValue(row, 5, r['transactionType'])
				if (r['chequeNo'] is not None):
					self.m_journalGrid.SetCellValue(row, 6, r['chequeNo'])
				#self.m_journalGrid.SetCellValue(row, 7, str(r['Debit']))
				#self.m_journalGrid.SetCellValue(row, 8, str(r['Credit']))
				
				row = row+1
			else:
				break
