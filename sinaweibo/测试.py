str = 'window.STK_15397003415462 && STK_15397003415462({"retcode":20000000,"msg":"succ","data":{"qrid":"2OTlbxfZ1AHBVWuRB6PCZoQr_8dQQOBUTBnFyY29kZQ..","image":"\/\/qr.weibo.cn\/inf\/gen?api_key=a0241ed0d922e7286303ea5818292a76&data=https%3A%2F%2Fpassport.weibo.cn%2Fsignin%2Fqrcode%2Fscan%3Fqr%3D2OTlbxfZ1AHBVWuRB6PCZoQr_8dQQOBUTBnFyY29kZQ..%26sinainternalbrowser%3Dtopnav%26showmenu%3D0&datetime=1539700341&deadline=0&level=M&logo=http%3A%2F%2Fimg.t.sinajs.cn%2Ft6%2Fstyle%2Fimages%2Findex%2Fweibo-logo.png&output_type=img&redirect=0&sign=a6f72da82629b2ddf465d34a284f3d2f&size=180&start_time=0&title=sso&type=url"}});'

import re

qrcode_qrid = re.search(r'"qrid":"(?P<qrid>(\w|..)*?)"', str)

# print(qrcode_qrid.group("qrid"))


from threading import Event

stoped = Event()
while not stoped.wait(3):
    print(1)