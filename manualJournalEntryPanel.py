from connectToDb import connectToDB

conn = connectToDB()

import wx
import wx.xrc

import gLedgerFunctions as af

class GetData(wx.Dialog):
    def __init__(self, parent):
        
        wx.Dialog.__init__(self, parent, wx.ID_ANY, "Manual Entry", size= (650,400))
        self.panel = wx.Panel(self,wx.ID_ANY)
        
        self.folios = self.fetchFolios()
        self.lblFolio = wx.StaticText(self.panel, label="Folio", pos=(20,70))
        #self.m_folioCombo = wx.ComboBox(self, size=wx.DefaultSize, choices= list(self.folios.keys()), pos=(130,70), size=(90,-1))
        self.folio = wx.TextCtrl(self.panel, value="", pos=(130,70), size=(90,-1))
        
        self.lblTransaction = wx.StaticText(self.panel, label="Transaction Type", pos=(20,120))
        self.transaction = wx.TextCtrl(self.panel, value="", pos=(130,120), size=(90,-1))
        
        self.lblChequeNo = wx.StaticText(self.panel, label="Cheque Number", pos=(20,170))
        self.chequeNo = wx.TextCtrl(self.panel, value="", pos=(130,170), size=(90,-1))
        
        self.lblDebit = wx.StaticText(self.panel, label="Debit", pos=(20,220))
        self.debit = wx.TextCtrl(self.panel, value="", pos=(130,220), size=(90,-1))
        
        self.lblCredit = wx.StaticText(self.panel, label="Credit", pos=(20,270))
        self.credit = wx.TextCtrl(self.panel, value="", pos=(130,270), size=(90,-1))
        
        self.saveButton =wx.Button(self.panel, label="Save", pos=(110,320))
        self.closeButton =wx.Button(self.panel, label="Cancel", pos=(250,320))
        self.returnButton =wx.Button(self.panel, label="Return", pos=(390,320))
        
        self.saveButton.Bind(wx.EVT_BUTTON, self.SaveConnString)
        self.closeButton.Bind(wx.EVT_BUTTON, self.OnQuit)
        self.returnButton.Bind(wx.EVT_BUTTON, self.OnReturn)
        
        self.Bind(wx.EVT_CLOSE, self.OnQuit)
        
        self.Show()    
    
    def fetchFolios (self):
        qry = 'SELECT id, description FROM headOfAccounts'
        curs = conn.cursor()
        curs.execute(qry)
        r = curs.fetchall()

        folios = {}
        for x in r:
            folios.update({x['description'] : x['id']})
        return folios
	
    def OnReturn (self, event):
    	f.returnPurchase(self.iid)
    	self.Destroy()

    def OnQuit(self, event):
        self.result_name = None
        self.Destroy()
    
    def SaveConnString(self, event):
        #hoa = self.m_folioCombo.GetValue()
        hoa = self.folio.GetValue()
        tran = self.transaction.GetValue()
        cheque = self.chequeNo.GetValue()
        debit = self.debit.GetValue()
        credit = self.credit.GetValue()
        
        if ( hoa != "" and (debit != "" or credit != "") ):
            af.manualEntry (hoa, tran, cheque, debit, credit)
        
        self.Destroy()

