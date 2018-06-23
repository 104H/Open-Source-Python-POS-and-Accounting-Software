from connectToDb import connectToDB

conn = connectToDB()

import wx
import wx.xrc

class GetData(wx.Dialog):
    def __init__(self, parent, terminalObj):
        self.t = terminalObj
    	
        wx.Dialog.__init__(self, parent, wx.ID_ANY, "Name Input", size= (650,260))
        self.panel = wx.Panel(self,wx.ID_ANY)

        self.lblName = wx.StaticText(self.panel, label="Name", pos=(20,20))
        self.name = wx.TextCtrl(self.panel, value="", pos=(110,20), size=(500,-1))
        
        self.lblPhone = wx.StaticText(self.panel, label="Phone", pos=(20,60))
        self.phone = wx.TextCtrl(self.panel, value="", pos=(110,60), size=(500,-1))
        
        self.lblAdd = wx.StaticText(self.panel, label="Address", pos=(20,100))
        self.address = wx.TextCtrl(self.panel, value="", pos=(110,100), size=(500,-1))
        
        self.lblPrevB = wx.StaticText(self.panel, label="Previous Balance\n(if any)", pos=(20,140))
        self.previousBal = wx.TextCtrl(self.panel, value="", pos=(110,140), size=(500,-1))
        
        self.saveButton =wx.Button(self.panel, label="Save", pos=(110,200))
        self.closeButton =wx.Button(self.panel, label="Cancel", pos=(250,200))
        
        self.saveButton.Bind(wx.EVT_BUTTON, self.SaveConnString)
        self.closeButton.Bind(wx.EVT_BUTTON, self.OnQuit)
        
        self.Bind(wx.EVT_CLOSE, self.OnQuit)
        self.phone.Bind(wx.EVT_TEXT, self.findInfo)
        
        self.phone.SetFocus()
        
        self.Show()	

    def findInfo (self, event):
        if self.t.fetchCustomerId(self.phone.GetValue()):
                self.name.SetValue(self.t.customerName)
                self.name.SetEditable(False)
                self.saveButton.Disable()
                #self.customerContact.SetLabel(self.t.customerContact)
        else:
                self.name.SetValue("")
                self.name.SetEditable(True)
                self.saveButton.Enable()
                self.t.customerId = 0
	
    def OnQuit(self, event):
        self.result_name = None
        self.Destroy()

    def SaveConnString(self, event):
        name = self.name.GetValue()
        phone = self.phone.GetValue()
        add = self.address.GetValue()
        bal = self.previousBal.GetValue()
        
        if bal == "":
        	bal = 0
        
        qry = "INSERT INTO `customer` (name, contact, address, balance) VALUES ('%s', '%s', '%s', '%s')" % (name, phone, add, bal)
        conn.cursor().execute(qry)
        
        qry = "INSERT INTO `headOfAccounts` (description, computation) VALUES ('Customer%s-R', '1')" % (conn.insert_id())
        conn.cursor().execute(qry)
        conn.commit()
        
        self.Destroy()

