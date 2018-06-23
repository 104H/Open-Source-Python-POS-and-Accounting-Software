from datetime import datetime, date
from pyinvoice.models import InvoiceInfo, ServiceProviderInfo, ClientInfo, Item, Transaction
from pyinvoice.templates import SimpleInvoice

def imaker(fName, id, duedate, clientId, clientName, clientMobileNumber, prods, discountNo):

	#fname: filename
	#id: invoice id, type: str or int or unicode
	#duedate: invoice duedate: str or int or unicode
	#clientId: passed in client_info. type: str or int or unicode
	#clientName: type is str ot unicode
	#clientMobileNumber. type: int or str or unicode
	#prods is a list which makes the item table
	#prods -> name, description price, quantity
	#discountNo: passes into the function which sets the discount rate. type: int
	

	doc = SimpleInvoice(fName)

	# Paid stamp, optional
	doc.is_paid = False

	doc.invoice_info = InvoiceInfo(id, datetime.now(), duedate)  # Invoice info, optional

	# Service Provider Info, optional
	doc.service_provider_info = ServiceProviderInfo(
		name='Salman Wholeseller',
		mobileNumber= '03362510211'
		
		
	)

	# Client info, optional
	doc.client_info = ClientInfo(
		client_id = clientId,
		name = clientName, 
		mobileNumber = clientMobileNumber,
		
		
	)

	# Add Item
	for x in prods:
		doc.add_item(Item(x[0], x[1], x[2], x[3]))
		

	# Tax rate, optional

	doc.set_item_discount_rate(discountNo)  # 20%


	doc.finish()
#test run
#imaker('sabih5.pdf','12356', '12-13-1997', '1234', 'john Doe', '03312097073', [['toothpick', 'tooth desc', 1.1, 3] ,['brush', 'brush desc', 2.2, 3] ,['brush', 'brush desc', 2.2, 3] ,['brush', 'brush desc', 2.2, 3] ,['brush', 'brush desc', 2.2, 3] ,['brush', 'brush desc', 2.2, 3] ,['brush', 'brush desc', 2.2, 3] ,['brush', 'brush desc', 2.2, 3] ,['brush', 'brush desc', 2.2, 3] ,['brush', 'brush desc', 2.2, 3] ,['brush', 'brush desc', 2.2, 3] ,['brush', 'brush desc', 2.2, 3] ,['brush', 'brush desc', 2.2, 3] ,['brush', 'brush desc', 2.2, 3] ,['brush', 'brush desc', 2.2, 3] ,['brush', 'brush desc', 2.2, 3] ,['brush', 'brush desc', 2.2, 3] ,['brush', 'brush desc', 2.2, 3] ,['brush', 'brush desc', 2.2, 3] ,['brush', 'brush desc', 2.2, 3] ,['brush', 'brush desc', 2.2, 3] ,['brush', 'brush desc', 2.2, 3] ,['brush', 'brush desc', 2.2, 3] ,['brush', 'brush desc', 2.2, 3]], 20)
