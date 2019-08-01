# 声明：
### 本项目为自学过程中的练手项目，不具有实际使用价值。
### 参考：轻量级办公平台Sandbox
#### 原Sandbox项目地址 https://github.com/RobbieHan/gistandard

# 本项目说明：
### 1.改写原项目的启动之后的界面呈现布局：
    原项目启动：
        ![image](https://github.com/RobbieHan/gistandard/blob/18ac4434490d3658b72a4a77ef6656ffad01beed/media/sandbox-image/001.jpg)
    
    本项目启动：
        ![image](https://github.com/ChenWeiyong/django_rbac/blob/master/images/pic-2.png)
    
    改写原因：
        原项目的逻辑是根据分配给用户的权限，从而前端动态显示相应的执行选项，但是后面项目扩展的功能多了，在页面的top端横向拓展，
        会导致页面不美观，甚至显示会出现问题！
        而本项目只是取消了top端的横向拓展，修改了前端获取选项的代码，改成了只在左边栏向下拓展，就避免了上述问题。
### 2.取消原项目的xadmin功能：
    由于是自学，一切从简，为避免不必要的问题出现，由于取消了xadmin，所以第一次登录的用户是没有任何权限的，所以也就什么都看不到：
    1.rbac_menu创建好url
        1	资产管理：修改	1		ADM-ASSET-UPDATE	/adm/asset/update	1
    
    2.rbac_role创建角色
        1	超管
        
    3.设置users_userprofile_roles（前提创建了用户）(绑定关系)
        1	1	1
    
    4.然后登录后台注册admin去绑定权限，这样就不用一个个输入了
    
    5.实在不懂，参考本项目的数据库的内容实现！


    
### 3.项目运行环境：
    python3.5
    Django==1.11.6
    
### 4.增加webssh功能：
    本项目集成了webssh功能，可以在本账号下获取！
    
### 5.另外说明：
    项目中很多创建的引用并没有实现什么功能只是当时测试使用的，后续可以直接在应用中拓写。

### 6.项目部分截图：
    ![image](https://github.com/ChenWeiyong/django_rbac/blob/master/images/pic-1.png)
    ![image](https://github.com/ChenWeiyong/django_rbac/blob/master/images/pic-2.png)
    ![image](https://github.com/ChenWeiyong/django_rbac/blob/master/images/pic-3.png)
    ![image](https://github.com/ChenWeiyong/django_rbac/blob/master/images/pic-4.png)
    ![image](https://github.com/ChenWeiyong/django_rbac/blob/master/images/pic-6.png)
    ![image](https://github.com/ChenWeiyong/django_rbac/blob/master/images/pic-7.png)
    ![image](https://github.com/ChenWeiyong/django_rbac/blob/master/images/pic1.png)
 
    
