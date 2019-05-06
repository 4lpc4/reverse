# -*- coding: UTF-8 -*-	
#任何需要符号执行的程序都要先建立一个angr工程
#factory.entry_state():返回入口点函数的值
#factory.simgr():创造一个simulation manage对象，可以收集内存，寄存器等相关信息
#explore():执行程序到相应的find位置，并且将找到的路径值放到一个list中去
#如果没有找到符合条件的路径，则打印错误
import angr
import datetime

def main():
	p = angr.Project("bbvvmm")   #创建一个Angr工程
	state = p.factory.entry_state(add_options=angr.options.unicorn)  #获取入口函数
	sm = p.factory.simgr(state)  #在入口准备开始符号执行
	sm.explore(find=0x00406B24)  #遍历可能的路径并找到成功的那条路径
	return sm.found[0].posix.dumps(0).strip(b'\0\n')  #返回当前状态输入 dumps(1)表示输入

if __name__ == '__main__':
	start_time = datetime.datetime.now()
	print(main())
	end_time = datetime.datetime.now()
	print((end_time-start_time).seconds)

