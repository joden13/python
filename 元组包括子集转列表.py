# -*- coding: utf-8 -*-
#元组包括子集转列表


list1=((5501,(42432,4324234,432423,(6654654,65464,65464,(5435435,54353,['dsfsf','dsddf',('sfdsf','fdsfsdf'),'fdsfsd']))), u'\u5987\u4ea7\u79d1(\u57fa\u7840\u77e5\u8bc6)', 1, 0, u'', 35, u'\u5173\u4e8e\u75c5\u7406\u7f29\u590d\u73af\u7684\u7279\u5f81\u6b63\u786e\u7684\u662f\ue004', u'\u5b50\u5bab\u5448\u9ebb\u75f9\u72b6\u6001', u'\u968f\u5bab\u7f29\u9010\u6e10\u4e0a\u5347', u'\u5c5e\u5b50\u5bab\u808c\u8089\u7ec4\u7ec7\u529f\u80fd\u5f02\u5e38', u'\u7ee7\u53d1\u4e8e\u4e0d\u534f\u8c03\u7684\u5bab\u7f29\u8fc7\u5f3a', u'\u5b50\u5bab\u5e95\u90e8\u53ca\u4e0b\u6bb5\u808c\u7ec4\u7ec7\u5747\u88ab\u62c9\u957f\u53d8\u8584', u'', u'', u'', u'', u'', u'', u'', u'B', u'', None))
def tolist(e):
    new=[]
    changdu=len(e)
    for i in range(0,changdu):
        if isinstance(e[i], tuple):
            e[i]=list(e[i])
            new.append(e[i])
            tolist(e[i])
        elif isinstance(e[i], list):
            new.append(e[i])
            tolist(e[i])
        else:
            new.append(e[i])
            continue
    return new
#手动将元组先转换为列表再进行处理
list2=tolist(list(list1))
print list2
