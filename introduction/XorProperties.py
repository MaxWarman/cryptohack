from crypty import *

KEY1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
KEY2xKEY1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
KEY2xKEY3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
FLAGxKEY1xKEY3xKEY2= "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

KEY1 = hexToBytes(KEY1)
KEY2 = xorBytes(KEY1, hexToBytes(KEY2xKEY1))
KEY3 = xorBytes(KEY2, hexToBytes(KEY2xKEY3))
FLAGxKEY1xKEY3xKEY2 = hexToBytes(FLAGxKEY1xKEY3xKEY2)

FLAG = xorBytes(FLAGxKEY1xKEY3xKEY2, KEY1)
FLAG = xorBytes(FLAG, KEY2)
FLAG = xorBytes(FLAG, KEY3)
FLAG = bytesToString(FLAG)

print(FLAG)

###
###	Flag: crypto{x0r_i5_ass0c1at1v3}
###