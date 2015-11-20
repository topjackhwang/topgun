#!/usr/bin/env python

#
# include neessaery libraries
#
import web
import xml.etree.ElementTree as ET

#
# parsing configuration file to retrieve user settings
# 
tree = ET.parse('conf/user_conf.xml')
root = tree.getroot()

#
# define accessing URL strings of web service
#
urls = (
    '/fib', 'show_help',
    '/fib/(.*)', 'run_fib'
)

app = web.application(urls, globals())

#
# sub-function of processing fibonacci sequences
#
def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)

#
# default value of boundary to allow processing of fibonacci sequences
#
limit = 5;

#
# retrieve  boundary value from user setting file
#
for child in root:
    if child.attrib['id'] == '1':
        if child.attrib['value'] != '':
	    tmp_var = child.attrib['value']
	    limit = int(tmp_var);

#
# display usage-howto statements
#
class show_help:
    def GET(self):
        return 'usage: http://<host>:<port>/fib/<number> eg: http://locahost:8080/fib/5'

#
# major class to process requests from client
#
class run_fib:
    def GET(self, str_no):
	output = '';

	#
	# error handling - if input parameter is not numeric
	#
	try:
	    int_no = int( str_no )
	except ValueError:
   	    return '{"err_code" : -1, "err_msg" : "The input parameter has to be numeric!!"}'

	#
	# error handling - if input parameter is larger than boundary limit
	#
	if int_no > limit:
		return '{"err_code" : -2, "err_msg" : "Current limit is set to ' + str(limit) + ', please input number less than it."}'
	#
	# error handling - if input parameter is negative value
	#
	if int_no < 0:
		return '{"err_code" : -3, "err_msg" : "The input number is negative, please input a positive number."}'

	for i in range(int_no):
	    output +=  str( fib(i) ) + ' '

	return output

#
# run main program
#
if __name__ == "__main__":
    app.run()
