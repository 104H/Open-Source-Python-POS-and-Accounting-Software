from escpos.printer import Usb

import usb.core
import usb.util

'''
def connectToPrinter():
	return Usb(0x0416, 0x5011, in_ep=81, out_ep=3)
'''
p = Usb(0x0416, 0x5011, in_ep=81, out_ep=3)
def printReciept(cart, date, invoiceId):
	#p = connectToPrinter()
	
	p.set(align='center', bold=True, double_height=True, double_width=True)
	p.textln('Salman Wholeseller')

	p.set(align='center', bold=True, double_height=False, double_width=False)
	p.textln('Chhadi Lane, Karachi')
	p.textln('Phone: 0336 2510211')
	#p.textln('-------------------------------------------')
	p.textln('===============================================')
	p.ln(1)
	p.textln('Invoice ID: '+str(invoiceId)+'         Date: '+ str(date))
	p.ln(2)

	p.set(align='center', bold=True, double_height=False, double_width=False)

	# width of paper -> 48 chars
	# Product
	p.textln("ID  |Product       |Qty  |Price    |Total Price ")
	p.textln("------------------------------------------------")

	for x in range(len(cart['pid'])):
		p.textln(prepareLine(cart['pid'][x], cart['name'][x], cart['qty'][x], cart['price'][x], cart['totalPrice'][x]))
	#p.textln(prepareLine(4, 'Brush', 10, 200, 10000))
	
	'''
	p.textln("2   | Toothpick    | 50  |    20   |      1000  ")
	p.textln("578 | Battery      | 10  |   100   |      1000  ")
	p.textln("89  | Brush        |  5  |    40   |       200  ")
	'''
	
	p.textln("------------------------------------------------")
	p.textln("                              Total:  "+ str(sum(cart['totalPrice'])))

	p.ln(9)

	p.textln("------------------------------------------------")
	p.textln("                     Notes                      ")

	p.ln(2)

	p.set(align='center', bold=False, double_height=False, double_width=False)
	p.textln("Ganyani, Kirmani and Allahwala IT Consulting")

	#p.image("logo.gif")
	#p.barcode('3422323', 'EAN13', 64, 2, '', '')

	p.cut(mode='PART')
	
def prepareLine (pid, name, qty, price, tPrice):
	ln = ''
	pid = str(pid)
	ln = ln + preparePhrase(pid, 4)
	ln = ln + preparePhrase(name, 14)
	ln = ln + preparePhrase(qty, 5)
	ln = ln + preparePhrase(price, 9)
	ln = ln + preparePhrase(tPrice, 11)
	
	return ln
	
def preparePhrase (itm, l):
	itm = str(itm)
	return itm + ' '*(l-len(itm)) + '|'

#p = connectToPrinter()
#printReciept(p)
