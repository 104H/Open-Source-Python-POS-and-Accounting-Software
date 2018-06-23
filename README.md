# Open Source Python POS and Accounting Software

<h3>Description</h3>
<br />
<ol>
	<li>This software is written using Python 3 and powered by MySQL.</li>
	<li>It has so far been tested on Linux</li>
</ol>

<h3>Features</h3>
<br />
<h4>Point of Sale</h4>
<br />
<ol>
	<li>Functionality to query and add products by Barcode Number, Name and Code Name.</li>
	<li>Associate customer with each sale and purchase using their unique contact mobile phone number.</li>
	<li>Apply discount of individual products and the entire sale.</li>
	<li>Sale with cash (full payment), cheque (credit sale), purchase and return both sales and purchase.</li>
	<li>Update cash collected/paid against credit sales/purchase with cheque numbers.</li>
</ol>
<br />
<h4>Accounting</h4>
<br />
<ol>
	<li>Make <b>automated General Journal Entries</b> with each sale, purchase and returns of both. These entries are made in <u>Sale, Purchase, Cash, Accounts Recievable and Accounts Payable of Individual Customers.</u></li>
	<li>Make manual General Journal Entries</li>
	<li>Edit existing entries</li>
	<li>Display accounts of each Head of Account</li>
	<li>Maintain Accounts Recievable and Payable of each customer</li>
	<li>Create Control Account</li>
	<li>Create Income Statement</li>
	<li>All accounts mentioned above can be viewed for any date range</li>
</ol>
<br />
<h4>Future Plans</h4>
<br />
<ol>
	<li>Add ERP functionality to control access rights of employees</li>
	<li>Add Depreciation and Inventory Valuation</li>
	<li>Include BI Dashboard</li>
</ol>
<br />
<h3>Development and Technicalities</h3>
<br />
I have built this software using Python3. It uses <a href="https://github.com/PyMySQL/PyMySQL">PyMySQL</a> and <a href="https://wxpython.org/Phoenix/docs/html/index.html">WxPython</a>.
<br />
To understand the design start following the code starting from <a href="https://github.com/HH95/Open-Source-Python-POS-and-Accounting-Software/blob/master/mainInterface.py">mainInterface.py</a>.
