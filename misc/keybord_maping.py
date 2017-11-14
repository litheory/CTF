mappings = {0x04:"A", 0x05:"B", 0x06:"C", 0x07:"D", 0x08:"E", 0x09:"F", 0x0A:"G", 0x0B:"H", 0X0C:"I", 0X0D:"J", 0X0E:"K", 0X0F:"L", 
0X10:"M", 0X11:"N", 0X12:"O", 0X13:"P", 0X14:"Q", 0X15:"R", 0X16:"S", 0X17:"T", 0X18:"U", 0X19:"V", 0X1A:"W", 0X1B:"X", 0X1C:"Y", 
0X1D:"Z", 0X1E:"1", 0X1F:"2", 0X20:"3", 0X21:"4", 0X22:"5", 0X23:"6", 0X24:"7", 0X25:"8", 0X26:"9", 0X27:"0", 0X28:"\n", 0x2A:"[DEL]", 
0x2B:"[TAB]", 0x2C:"[SPACE]", 0x2D:"-", 0x2E:"=", 0x2F:"[", 0x30:"]", 0x31:"\\", 0x32:"~", 0x33:";", 0x34:"'", 0x36:",", 0x37:"."}
nums = []
keys = open('usbdata.txt')
for line in keys:
	if line[0]!='0' or line[1]!='0' or line[3]!='0' or line[4]!='0' or line[9]!='0' or line[10]!='0' or line[12]!='0' or line[13]!='0' or line[15]!='0' or line[16]!='0' or line[18]!='0' or line[19]!='0' or line[21]!='0' or line[22]!='0':
		continue
	nums.append(int(line[6:8],16))
keys.close()
output = ""
for n in nums:
	if n == 0:
		continue
	if n in mappings:
		output += mappings[n]
	else:
		output += '[unknown]'
print 'output :\n' + output
