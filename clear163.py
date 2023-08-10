'''
Description: 
Author: jiangsheng
Date: 2023-08-10 10:01:37
LastEditors: jiangsheng
LastEditTime: 2023-08-10 10:21:12
'''
import imaplib
import tqdm
# 邮箱配置
email = "maotanxiong@163.com"
password= "FTGAVZFOTINYROSS"
imap_server = "imap.163.com"
from imapclient import IMAPClient

# 连接到IMAP服务器
server = IMAPClient("imap.163.com", ssl=True, port=993)
server.login(email,password)

# 设置IMAP客户端的标识信息
server.id_({"name": "IMAPClient", "version": "2.1.0"})

# 选择收件箱文件夹
server.select_folder('INBOX')

# 获取收件箱中的所有邮件的UID
uids = server.search()

# 删除每个邮件
for uid in tqdm.tqdm(uids):
    server.delete_messages(uid)

# 提交更改并关闭连接
server.expunge()
server.logout()