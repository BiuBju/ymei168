#coding:UTF-8

from django.http import HttpResponseRedirect,HttpResponse
from datetime import *

#全局打印，Debug专用，正式发布时清空此方法体
def gprint(str, decode="", encode=""):
    print "-------------start gprint-------------"
    if decode:
        print str.decode("utf8").encode("gbk")
    else:
        print str
    print "-------------end gprint-------------"

#判断字符串 stri 是否为空，为空返回 False，否则返回去掉空格的 stri
def gisempty(stri):
    if(stri==None or stri==""):
        return False
    stri=stri.strip()
    if(stri != ""):
        return stri
    else:
        return False

#验证码
def verifycode(request):
    import Image,ImageDraw,ImageFont,md5,cStringIO,random
    background = (random.randrange(230,255),random.randrange(230,255),random.randrange(230,255))
    line_color = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
    font_color = ['black','darkblue','darkred']
    img_width = 60
    img_height = 30
    font = ImageFont.truetype("wqy-microhei.ttc", 17) #开源字体
    #font=ImageFont.load_default() #默认字体好过没有，不能设置大小！

    im = Image.new('RGB',(img_width,img_height),background)
    draw = ImageDraw.Draw(im)
    mp = md5.new()
    mp_src = mp.update(str(datetime.now()))
    mp_src = mp.hexdigest()    
    rand_str = mp_src[0:4]

    #画干扰线
    for i in range(random.randrange(2,10)):
        xy = (random.randrange(0,img_width),random.randrange(0,img_height),
              random.randrange(0,img_width),random.randrange(0,img_height))
        draw.line(xy,fill=line_color,width=1)

    #写入验证码文字
    x = 2
    for i in rand_str:
        y = random.randrange(0,10)
        draw.text((x,y), i, font=font, fill=random.choice(font_color))
        x += 14
    del x
    del draw
    
    request.session['captcha'] = rand_str #增加到session
    gprint(rand_str)   
    buf = cStringIO.StringIO()
    im.save(buf, 'png')
    buf.closed
    return HttpResponse(buf.getvalue(),'image/png')
    
