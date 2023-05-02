# 简介
这个库中包含了几个简单的文件加密工具和数据渗漏工具：   
- cryptor.py: 利用AES和RSA的混合加密工具  
- smtp.py: 利用smtp邮件的数据渗漏工具  
- web.py: 利用web网站(Pastebin)的数据渗漏工具  
- ftp.py: 利用ftp的数据渗漏工具  
# 技术回顾
## pycryptodomex库
这是cryptor.py中主要依赖的库，该库可以使用各种加密算法进行加密，以及生成密钥等操作  
## ftplib和smtplib库
这两个库分别用于完成ftp渗漏和smtp渗漏。  
