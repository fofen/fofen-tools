# -*- encoding=utf8 -*-

__author__ = "佛分/2020-07-10"

# 这是单个群的程序
# 运行之前，请先手工进入微信群

from airtest.core.api import *
auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

def get_red_pakets(): # 实现抢红包
    msg_elements_list = poco(name="android.widget.RelativeLayout").children()  # 获取别人发的消息
    # 反转消息
    msg_lists = []
    for item in msg_elements_list:
        msg_lists.insert(0,item)

    for msg in msg_lists:   # 第一次循环出来的就是最后一个元素，也是最新的元素
        red_key_element = msg.offspring(name='com.tencent.mm:id/r8')  # 判断红包是否存在
        not_red_key = msg.offspring(name='com.tencent.mm:id/r0')      # 已领取的
       
        if red_key_element: # 有红包
            if not_red_key.exists() and not_red_key.get_text() == '已领取': # 如果已被领取
                continue
            else:
                print('有新红包了')
                msg.click()  # 点红包
                kai_elements = poco(name='com.tencent.mm:id/den')   # 开红包
                if kai_elements.exists():
                    kai_elements.click()
                keyevent('BACK')  # 返回
        else:      # 没有红包
            continue
   
while True:
        get_red_pakets()
        sleep(1)    # 每1秒检查一次
