# -*- coding: utf-8 -*-
"""
	基于贪心算法的旅行商问题解法Python源码
	#贪心算法的思想是：每次都选择当前最优的解，也就是每次都选择当前最短的路径，直到所有的城市都被遍历过一次，然后再回到起点。
	#本问题中贪心算法用于在回溯法中求解下界，在分支限界法中求解上界
	Author:	Greatpan
	Date:	2018.9.30
"""

import math 
import time
from MyFuncTool import GetData,ResultShow,draw #导入自定义函数

def GreedyMethond(CityNum,Dist):
	"""
	函数名：GreedyMethond(CityNum,Dist)
	函数功能：	贪心策略算法核心
		输入	1 	CityNum：城市数量
			2	Dist：城市间距离矩阵
		输出	1 Cumulative_Path：最优路径长
			2 Already_Visited_City：最优路径
	其他说明：无
	"""
	Already_Visited_City=[]					#Already_Visited_City:已经遍历过的城市
	Cumulative_Path=0						#Cumulative_Path:目前所走城市的累积路径长
	Already_Visited_City.append(0)			#从城市0出发						

	for i in range(1,CityNum):  
		Cur_Min_Dist=math.inf				#Cur_Min_Dist：当前最小距离
		for j in range(1,CityNum):			#寻找下一个距离最短的城市
			if j not in Already_Visited_City and (Dist[Already_Visited_City[i-1]][j] < Cur_Min_Dist): #如果城市j未经历过且距离最短，则更新
				Cur_Min_City = j;			#Cur_Min_City:代表离当前城市距离最小的未经历的城市
				Cur_Min_Dist=Dist[Already_Visited_City[i - 1]][j]; #更新当前最小距离，即从当前城市到下一个城市的距离
 
		Already_Visited_City.append(Cur_Min_City) #将下一个距离最短的城市添加到已经遍历过的城市中
		Cumulative_Path+=Cur_Min_Dist #将当前最小距离添加到累积路径中，即从出发城市到当前城市的距离
	Cumulative_Path+=Dist[0][Cur_Min_City]	#将从最后一个城市回到出发城市的距离
	Already_Visited_City.append(0) #将出发城市添加到已经遍历过的城市中
	return Cumulative_Path,Already_Visited_City #返回最优路径长和最优路径

##############################程序入口#########################################
if __name__ == "__main__":
	Position,CityNum,Dist = GetData("./data/TSP25cities.tsp")

	start = time.clock()				#程序计时开始
	Min_Path,BestPath=GreedyMethond(CityNum,Dist)	#调用贪心算法
	end = time.clock()					#程序计时结束

	print()
	ResultShow(Min_Path,BestPath,CityNum,"贪心算法")
	print("程序的运行时间是：%s"%(end-start))
	draw(BestPath,Position,"Greedy Methond")
"""
结果：
贪心法求得最短旅行商经过所有城市回到原城市的最短路径为：
0->9->8->5->3->2->1->7->4->6->0
总路径长为：10464.1834865

程序的运行时间是：0.000508957
"""
