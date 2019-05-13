import turtle 
myPen=turtle.Pen()
myPen.speed(0)


radius=int(input('请输入螺旋丸的大小：')) #  圆的半径
angle=int(input('请输入螺旋丸的旋转速度：'))#  旋转角度
density=int(input('请输入螺旋丸的能量密度：'))#  完成360度需要的次数


def pellet(radius,angle,density):
    
    #使用循环，旋转360度。
    for i in range(density):
        #画出一个自定义的圆
        myPen.circle(radius,angle)
        
        #不留痕迹的回到原点并且恢复初始角度。
        myPen.penup()
        myPen.goto(0,0)
        myPen.left(360-angle)
        myPen.pendown()
    
        #每次的旋转角度
        myPen.left(360/density)
    
    point_1=15
    #绘制中心圆    
    myPen.penup()
    myPen.goto(0,-point_1)
    myPen.pendown()
    myPen.circle(point_1,360)
    
    point_2=radius*2*math.sin((360-angle)/360*math.pi)
    print(point_2, math.sin((360-angle)/2), math.sin(60))
    #绘制外圆    
    myPen.penup()
    myPen.goto(0,-point_2)
    myPen.pendown()
    myPen.circle(point_2,360)


# 绘制螺旋丸
pellet(radius,angle,density)






