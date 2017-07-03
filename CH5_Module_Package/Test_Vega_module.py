#! /usr/bin/env python3

#from Vega import *
'''
module心得:
    基本syntax:
    1.      import module_name
    2.      from module_name import object_name 這邊的object name 只是代表你有呼叫這個object 的權力
            而且呼叫方式以， object_name()的方式直接呼叫與(1.) 的呼叫方式不同
    觀念補充: 基本上 一個module 相當於一個 .py 檔， 這個.py檔內部有許多function （或是其他object） 可以提供我們呼叫
              另外在這個.py檔案內可以設定 __all__ 這個variable 儲存 [functionname, functionname2 , ...]作為以下（3）方式
              import 的方法 一次把執行權力都拉進來。這樣會有個 name collision 的風險
              此外 我們也有可能把fucntionname 這個object 所reference 的 function 給overwrite掉

    3.      from module_name import * 會把在__all__ 裡面所有的 object name 都 import近來
package心得：
    基本syntax:
    基本上觀念都跟module 一樣 ，只是 package 是以資料夾的方式存在，package 底下就是以 不同py 檔案所構成的 module
    1.      import package_name.modulename
    2.      from package_name import modulename
                    直接使用
    3.      至於 __all__ 這個variable 就擺在 __init__.py 這個檔案底下，作為initialize 的參考
    除此之外 pakcage底下可以再加個資料夾 形成 新的 subpackage ，呼叫方法 import packageName.subPackageName.module

--------------------- 以上方法都是 absolute import 也就是一般使用 系統路徑 來呼叫 module 的方式 -----------

問題是有時候我們自己建立的module 有時後會呼叫我們自己建立的同個 package 內的其他module 因此這類型的呼叫方式不能夠使用絕對路徑
而是使用相對路徑 ，以底下資料夾的架構來解釋
Graphic/
    module1.py
    module2.py
    __init__.py
    Vector/
        module_vec.py
        __init__.py
---------------------------------------
在這樣的配置狀態，module_vec.py 如果用絕對路徑去呼叫 module1.py 裡面的 object ，
變成以 import Graphic.module1 來使用 但是這種方式首先我們要先把 python呼叫的path 設定好，因此這種呼叫方式基本上
是以開發完成後，的呼叫作法。

如果是用 相對路徑的話，縱使我們有改變top directory 的名子也不會影響我們的設定，因此在開發 module如果要呼叫 同個package下的
其他module 時建議使用 相對路徑的方式去 import
範例： 假設我們目前這個檔案是上面敘述的 module_vec.py 檔
        import ..Graphic.module1 
        這們一來就可以使用 module1.py 檔案裡面的 object 了 !!



-------------------------------------------------------------------
如果想要讓其他的專案都可以 import 自己的module 這樣就得把 module 複製到以下資料夾
~/.local/lib/python3.5/site-packages
如果想要查看系統的 sitepackage 位置 可以先用以下指令
>>import site
site.getsitepackages()
['/usr/local/lib/python3.5/dist-packages', '/usr/lib/python3/dist-packages', '/usr/lib/python3.5/dist-packages']



# Test1
'''

'''

import Vega
Vega.goodbye.goodbye()

result:
Traceback (most recent call last):
      File "./Test_Vega_module.py", line 5, in <module>
          Vega.goodbye.goodbye()
          AttributeError: module 'Vega' has no attribute 'goodbye'
Report: Because Vega is Package not Module 
----------------------------There may be some other issue, it seems deem Vega as class

'''

#Test2
'''
import Vega.goodbye
import Vega.hello

result:
Traceback (most recent call last):
      File "./Test_Vega_module.py", line 13, in <module>
          hello.hello()
          NameError: name 'hello' is not defined
Report: Because we have to call Vega.goodbye.goodbye() to work
                                    module.object --------- Absolute calling

'''
#Test3
'''
import Vega.Multi
# Vega package , Multi module
Vega.Multi.second()

result: Successful




'''


#Test4
'''
from Vega.goodbye import goodbye
from Vega.hello import hello
result:
    Successful
'''


#Test5
'''
import Vega.goodbye

Vega.goodbye.goodbye()


result:
    Successful
'''



