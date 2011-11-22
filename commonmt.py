#coding:UTF-8

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
