# all functions defined make entries in the general journal

'''
1	A/C Recievable
2	A/C Payable
3	Purchase
4	Sale
5	Cash
6	Bank
21 	SalesDiscount
22 	PurchaseDiscount
23	SalesReturn
24	PurchaseReturn
'''

from connectToDb import connectToDB

conn = connectToDB()

def determineCustHoA (cust, typ):
	qry = 'SELECT id FROM headOfAccounts WHERE description = "%s"' % ('Customer'+str(cust)+'-'+typ)
	curs = conn.cursor()
	curs.execute(qry)
	r = curs.fetchone()
	return r['id']

def determineSuppHoA (cust, typ):
	qry = 'SELECT id FROM headOfAccounts WHERE description = "%s"' % ('Supplier'+str(cust)+'-'+typ)
	curs = conn.cursor()
	curs.execute(qry)
	r = curs.fetchone()
	return r['id']

def cashSaleEntry (amt, discount, saleId):
	saleId = "Sle-" + str(saleId)
	qry = 'INSERT INTO generalLedger (headOfAc, transactionType, Debit, Credit) VALUES (5, "%s", %s, 0), (21, "%s", %s, 0), (4, "%s", 0, %s)' % (saleId, amt, saleId, discount, saleId, str( int(amt) + int(discount) ))
	curs = conn.cursor()
	curs.execute(qry)
	conn.commit()

def invoiceEntry (amt, discount, amtRecieved, cust, invoiceId, cheque=1):
	#compute hoa using cust number from argument
	hoa = determineCustHoA(cust, 'R')
	invoiceId = 'Inv-'+str(invoiceId)

	c='6'
	if not(cheque):
		c = '5'

	qry = 'INSERT INTO generalLedger (headOfAc, transactionType, Debit, Credit) VALUES (%s, "%s", %s, 0), (21, "%s", %s, 0), (%s, "%s", %s, 0), (4, "%s", 0, %s)' % (c, invoiceId, amtRecieved, invoiceId, discount, hoa, invoiceId, str(int(amt) - int(amtRecieved)), invoiceId, str( int(amt)+int(discount) ))

	curs = conn.cursor()
	curs.execute(qry)
	conn.commit()
	
	'''
	curs = conn.cursor()
	qry = 'INSERT INTO generalLedger (headOfAc, Debit, Credit) VALUES (%s, %s, 0)' % (c, amt)
	curs.execute(qry)
	conn.commit()
	
	curs = conn.cursor()
	qry = 'INSERT INTO generalLedger (headOfAc, Debit, Credit) VALUES (%s, %s, 0)' % (str(hoa), str(int(amt) - int(amtRecieved)))
	curs.execute(qry)
	conn.commit()
	
	curs = conn.cursor()
	qry = 'INSERT INTO generalLedger (headOfAc, Debit, Credit) VALUES (4, 0, %s)' % (amtRecieved)
	curs.execute(qry)
	conn.commit()
	'''

def invoiceMoneyUpdateEntry (amt, cust, invoiceId, chequeNo, cheque=1):
	#compute hoa using cust number from argument
	hoa = determineCustHoA(cust, 'R')
	invoiceId = 'Inv-'+str(invoiceId)
	
	curs = conn.cursor()
	
	c=6
	if not(cheque):
		c = '5'
	
	qry = 'INSERT INTO generalLedger (headOfAc, transactionType, chequeNo, Debit, Credit) VALUES (%s, "%s", "%s", %s, 0), (%s, "%s", "%s", 0, %s)' % (c, invoiceId, chequeNo, amt, hoa, invoiceId, chequeNo, amt)
	curs.execute(qry)
	conn.commit()


def purchaseEntry (amt, discount, amtPaid, sup, purchaseId, cheque=1):
	#compute hoa using cust number from argument
	hoa = determineSuppHoA(sup, 'P')
	purchaseId = 'Pur-'+str(purchaseId)
	
	curs = conn.cursor()
	
	c=6
	if not(cheque):
		c = '5'
	
	qry = 'INSERT INTO generalLedger (headOfAc, transactionType, Debit, Credit) VALUES (3, "%s", %s, 0), (%s, "%s", 0, %s), (%s, "%s", 0, %s), (22, "%s", 0, %s)' % (purchaseId, str( int(amt)+int(discount) ), c, purchaseId, amtPaid, hoa, purchaseId, str( int(amt) - int(amtPaid) ), purchaseId, discount)
	curs.execute(qry)
	conn.commit()


def purchaseMoneyUpdateEntry (amt, cust, purchaseId, chequeNo, cheque=1):
	#compute hoa using cust number from argument
	hoa = determineSuppHoA(cust, 'P')
	purchaseId = 'Pur-'+str(purchaseId)
	
	curs = conn.cursor()
	
	c=6
	if not(cheque):
		c = '5'
	
	qry = 'INSERT INTO generalLedger (headOfAc, transactionType, chequeNo, Debit, Credit) VALUES (%s, "%s", "%s", %s, 0), (%s, "%s", "%s", 0, %s)' % (hoa, purchaseId, chequeNo, amt, c, purchaseId, chequeNo, amt)
	print('here')
	curs.execute(qry)
	conn.commit()

def returnEntry (amt, discount, refundId):
	# cash sale return
	refundId = "Rfd-" + str(refundId)
	qry = 'INSERT INTO generalLedger (headOfAc, transactionType, Debit, Credit) VALUES (23, "%s", %s, 0), (5, "%s", 0, %s), (21, "%s", 0, %s)' % (refundId, str( int(amt) + int(discount) ), refundId, amt, refundId, discount)
	curs = conn.cursor()
	curs.execute(qry)
	conn.commit()


def invoiceReturnEntry (invoiceId, refundId):
	invoiceId = "Inv-" + str(invoiceId)
	refundId = "Rfd-"+str(refundId)
	
	qry = 'INSERT INTO generalLedger (headOfAc, transactionType, Debit, Credit) SELECT IF (headOfAc = 4, 23, headOfAc), "%s", Credit, Debit FROM generalLedger WHERE transactionType = "%s" ORDER BY id DESC' % (refundId, invoiceId)
	
	curs = conn.cursor()
	curs.execute(qry)
	conn.commit()


def purchaseReturnEntry (purchaseId):
	# called by return prod
	refundId = "RPr-"+str(purchaseId)
	purchaseId = "Pur-" + str(purchaseId)
	
	qry = 'INSERT INTO generalLedger (headOfAc, transactionType, Debit, Credit) SELECT IF (headOfAc = 3, 24, headOfAc), "%s", Credit, Debit FROM generalLedger WHERE transactionType = "%s" ORDER BY id DESC' % (refundId, purchaseId)
	
	curs = conn.cursor()
	curs.execute(qry)
	conn.commit()

def manualEntry (hoa, transcType, cheque, debit, credit):
	qry = 'INSERT INTO generalLedger (headOfAc, transactionType, chequeNo, Debit, Credit) VALUES ("%s", "%s", "%s", "%s", "%s")' % (hoa, transcType, cheque, debit, credit)
	
	curs = conn.cursor()
	curs.execute(qry)
	conn.commit()
