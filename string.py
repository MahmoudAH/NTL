def main():


if __name__ == '__main__':main()
#data = "welcome my dera"
##data(1)
 Traceback(most
 recent
 call
 last):
 File
 "<input>", line
 1, in < module >
 T ypeError: 'str'
 object is not callable
 len(data)
 15
 data[1]
  'e'
 data.upper()
 'WELCOME MY DERA'
data.lower()
'welcome my dera'
data.split()
['welcome', 'my', 'dera']
data.split(m)
Traceback(most
recent
call
last):
File
"<input>", line
1, in < module >
NameError: name
'm' is not defined
data.split('m')
['welco', 'e ', 'y dera']
x = data.split()
x
['welcome', 'my', 'dera']
y = "; ".join()
Traceback(most
recent
call
last):
File
"<input>", line
1, in < module >
TypeError: join()
takes
exactly
one
argument(0
given)
y = "; ".join(x)
y
'welcome; my; dera'
y = " ".join(x)
y
'welcome my dera'
data.find(m)
Traceback(most
recent
call
last):
File
"<input>", line
1, in < module >
NameError: name
'm' is not defined
data.find[m]
Traceback(most
recent
call
last):
File
"<input>", line
1, in < module >
NameError: name
'm' is not defined
data.find['m']
Traceback(most
recent
call
last):
File
"<input>", line
1, in < module >
TypeError: 'builtin_function_or_method'
object is not subscriptable
data.find['my']

data.find('my')
8
data.find('m')
5
data[5]
'm'
data[5:8]
'me '
data.capitalize()
'Welcome my dera'
num=52
num
52
"num is {}".format(num)
'num is 52'
"num is {}".format(52)
'num is 52'
"num is {}".format(50)
'num is 50'
"num is {} and y is {}".format(50,55)
'num is 50 and y is 55'
"num is {} and y is {}".format(num,55)
'num is 52 and y is 55'
