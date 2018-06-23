from connectToDb import connectToDB

conn = connectToDB()

import wx
import wx.xrc
import gLedgerFunctions as af

class GetData(wx.Dialog):
    def __init__(self, parent, iid):
        self.iid = iid
        wx.Dialog.__init__(self, parent, wx.ID_ANY, "Quotation "+self.iid, size= (650,320))
        self.panel = wx.Panel(self,wx.ID_ANY)

        self.m_cartDV = wx.dataview.DataViewListCtrl( self.panel, wx.ID_ANY, (20,20), wx.Size( 600, 180 ), 0 )
        self.m_cartDV.SetMinSize( wx.Size( -1,400 ) )
        
        self.m_cartDV.AppendTextColumn('Name')
        self.m_cartDV.AppendTextColumn('Quantity')
        self.m_cartDV.AppendTextColumn('Price')
        self.m_cartDV.AppendTextColumn('Total Price')
        
        qry = 'select p.name, pq.quantity, pq.price from products p, productquotes pq, quotations q where p.id = pq.product and  q.id = pq.quoteId and pq.quoteId = %s' % (iid)
        curs = conn.cursor()
        curs.execute(qry)
        r = curs.fetchone()
        while (1):
            if r is not None:
                self.m_cartDV.AppendItem([ r['name'], str(r['quantity']), str(r['price']), str(int(r['quantity']) * int(r['price'])) ])
                r = curs.fetchone()
            else:
                break
	
        self.lblRecMoney = wx.StaticText(self.panel, label="Recieved Money", pos=(20,220))
        self.recMoney = wx.TextCtrl(self.panel, value="", pos=(130,220), size=(90,-1))
	
        self.convertButton =wx.Button(self.panel, label="Convert to Invoice", pos=(110,260))
        self.closeButton =wx.Button(self.panel, label="Cancel", pos=(250,260))
        
        self.convertButton.Bind(wx.EVT_BUTTON, self.convertToInvoice)
        #self.convertButton.Bind(wx.EVT_BUTTON, self.asd)
        self.closeButton.Bind(wx.EVT_BUTTON, self.OnQuit)
        
        self.Bind(wx.EVT_CLOSE, self.OnQuit)
        
        self.Show()    

    def OnQuit(self, event):
        self.result_name = None
        self.Destroy()
    
    def setToConverted (self):
        qry = 'UPDATE `quotations` SET converted = 1 WHERE id = %s' % (self.iid)
        curs = conn.cursor()
        curs.execute(qry)
        conn.commit()

    def saveInvoice (self):
        qry = 'select customer, preparedBy, totalBill, discount from quotations where id = %s' % (self.iid)
        curs = conn.cursor()
        curs.execute(qry)
        r = curs.fetchone()
        
        #amountRecieved = self.makePopUp("Enter Recieved Amount", "Convert to Invoice")
        amountRecieved = self.recMoney.GetValue()
        
        qry = 'INSERT INTO invoice (employeeId, amount, amountRecieved, discount, buyerId) VALUES (%d, "%d", "%s", %s, "%d")' % (r['preparedBy'], r['totalBill'], amountRecieved, r['discount'], r['customer'])
        curs.execute(qry)
        iId = conn.insert_id()
        print(iId)
        conn.commit()
        
        af.invoiceEntry (r['totalBill'], r['discount'], amountRecieved, r['customer'], iId) #save discount in quotations and pass it here
        
        qry = 'select pq.product, pq.quantity, pq.price from products p, productquotes pq, quotations q where p.id = pq.product and  q.id = pq.quoteId and pq.quoteId = %s' % (self.iid)
        curs = conn.cursor()
        curs.execute(qry)
        r = curs.fetchone()
        
        insCurs = conn.cursor()
        
        while (1):
            if r is not None:
                insQry = 'INSERT INTO productinvoice (invoiceId, product, quantity, price) values (%s, %s, %s, %s)' % (iId, r['product'], r['quantity'], r['price'])
                insCurs.execute(insQry)
                r = curs.fetchone()
            else:
                break
        #im.imaker(str(iId), iId, '0', clientId, c['name'], c['contact'], prods, discountNo=0) print invoice
        conn.commit()

    def convertToInvoice(self, event):
        self.setToConverted()
        self.saveInvoice()
        self.Destroy()

    def makePopUp(self, prompt, title):
        pp = wx.TextEntryDialog(self, prompt, title)
        pp.ShowModal()
        r = pp.GetValue()
        pp.Destroy()
        pp.Show()
        return r
	
