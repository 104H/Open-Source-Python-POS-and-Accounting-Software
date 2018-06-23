from connectToDb import connectToDB

conn = connectToDB()

import wx
import wx.xrc

import gLedgerFunctions as af

class GetData(wx.Dialog):
    def __init__(self, parent, iid, sid):
        self.iid = iid
        self.sid = sid
        
        wx.Dialog.__init__(self, parent, wx.ID_ANY, "Purchase "+iid, size= (650,400))
        self.panel = wx.Panel(self,wx.ID_ANY)

        self.m_cartDV = wx.dataview.DataViewListCtrl( self.panel, wx.ID_ANY, (20,20), wx.Size( 600, 180 ), 0 )
        self.m_cartDV.SetMinSize( wx.Size( -1,400 ) )
        
        self.m_cartDV.AppendTextColumn('Name')
        self.m_cartDV.AppendTextColumn('Quantity')
        self.m_cartDV.AppendTextColumn('Price')
        self.m_cartDV.AppendTextColumn('Total Price')
        
        qry = 'select p.name, pp.quantity, pp.price from productpurchase pp, products p where pp.product = p.id and purchaseId = %s' % (iid)
        curs = conn.cursor()
        curs.execute(qry)
        r = curs.fetchone()
        while (1):
        	if r is not None:
        		self.m_cartDV.AppendItem([ r['name'], str(r['quantity']), str(r['price']), str(int(r['quantity']) * int(r['price'])) ])
        		r = curs.fetchone()
        	else:
        		break

        self.lblRecMoney = wx.StaticText(self.panel, label="Paid Money", pos=(20,220))
        self.recMoney = wx.TextCtrl(self.panel, value="", pos=(130,220), size=(90,-1))
        
        self.lblcheque = wx.StaticText(self.panel, label="Cheque Number", pos=(20,270))
        self.chequeNum = wx.TextCtrl(self.panel, value="", pos=(130,270), size=(90,-1))
        
        self.saveButton =wx.Button(self.panel, label="Save", pos=(110,320))
        self.closeButton =wx.Button(self.panel, label="Cancel", pos=(250,320))
        self.returnButton =wx.Button(self.panel, label="Return", pos=(390,320))
        
        self.saveButton.Bind(wx.EVT_BUTTON, self.SaveConnString)
        self.closeButton.Bind(wx.EVT_BUTTON, self.OnQuit)
        self.returnButton.Bind(wx.EVT_BUTTON, self.OnReturn)
        
        self.Bind(wx.EVT_CLOSE, self.OnQuit)
        
        self.Show()    
    
    def returnPurchase (purchaseId):
        qry = 'UPDATE purchase SET returned=1 WHERE id = %s' % (purchaseId)
        curs = conn.cursor()
        curs.execute(qry)
	
        af.purchaseReturnEntry(purchaseId)
    
    def OnReturn (self, event):
    	returnPurchase(self.iid)
    	self.Destroy()

    def OnQuit(self, event):
        self.result_name = None
        self.Destroy()
    
    def updateMoney (self, iid, amt, supp, chequeNo):
    	qry = 'UPDATE `purchase` SET amountPaid = amountPaid+%s WHERE id = %s' % (amt, iid)
    	curs = conn.cursor()
    	curs.execute(qry)
    	
    	qry = 'INSERT INTO `purchasePayment` (purchaseId, amount) VALUES (%s, %s)' % (iid, amt)
    	curs = conn.cursor()
    	curs.execute(qry)
    	
    	conn.commit()
    	
    	af.purchaseMoneyUpdateEntry (amt, supp, iid, chequeNo)

    def SaveConnString(self, event):
        recMoney = self.recMoney.GetValue()
        if (recMoney == ''):
                self.updateMoney(self.iid, recMoney, self.sid, self.chequeNum.GetValue())
        self.Destroy()

