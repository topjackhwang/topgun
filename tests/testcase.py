#!/usr/bin/env python
import urllib
import urllib2
import base64
import json

authKey = base64.b64encode("username:password")
headers = {"Content-Type":"application/json", "Authorization":"Basic " + authKey}
data = { "param":"value"}

#
# define different URL strings of test cases
#
url_case1 = "http://localhost:8080/fib/1"
url_case2 = "http://localhost:8080/fib/5"
url_case3 = "http://localhost:8080/fib/21"
url_case4 = "http://localhost:8080/fib/-3"
url_case5 = "http://localhost:8080/fib/abcd"

def testcase1():
    request = urllib2.Request(url_case1)
 
    for key,value in headers.items():
        request.add_header(key,value)
 
    response = urllib2.urlopen(request)
 
    res_str = response.read()
#    print res_str
    #
    # if the response result is as expected, it's passed
    #
    if res_str == '0 ':
	print 'Test Case 1: PASSED'

def testcase2():
    request = urllib2.Request(url_case2)

    for key,value in headers.items():
        request.add_header(key,value)

    response = urllib2.urlopen(request)

    res_str = response.read()
#    print res_str
    if res_str == '0 1 1 2 3 ':
        print 'Test Case 2: PASSED'

def testcase3():
    request = urllib2.Request(url_case3)

    for key,value in headers.items():
        request.add_header(key,value)

    response = urllib2.urlopen(request)

    res_str = response.read()
#    print res_str

    #
    # parse error code from response
    #
    j_str = json.loads(res_str)
#    print j_str['err_code']

    #
    # check if the returned error code is as expected
    #
    if j_str['err_code'] == -2:
        print 'Test Case 3: PASSED'

def testcase4():
    request = urllib2.Request(url_case4)

    for key,value in headers.items():
        request.add_header(key,value)

    response = urllib2.urlopen(request)

    res_str = response.read()
#    print res_str

    j_str = json.loads(res_str)
#    print j_str['err_code']

    if j_str['err_code'] == -3:
        print 'Test Case 4: PASSED'

def testcase5():
    request = urllib2.Request(url_case5)

    for key,value in headers.items():
        request.add_header(key,value)

    response = urllib2.urlopen(request)

    res_str = response.read()
#    print res_str

    j_str = json.loads(res_str)
#    print j_str['err_code']

    if j_str['err_code'] == -1:
        print 'Test Case 5: PASSED'

#
# execute all test case sub-functions
#
testcase1()
testcase2()
testcase3()
testcase4()
testcase5()
