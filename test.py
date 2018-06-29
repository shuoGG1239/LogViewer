class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def x(self):
        return self.__x

    def y(self):
        return self.__y

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    def __repr__(self):
        return 'PointId:' + str(id(self)) + ' ;X_Id:' + str(id(self.__x)) + ' ;Y_Id:' + str(id(self.__y))


"""
Run Result:
    r1==> PointId:33393632 ;X_Id:1536014000 ;Y_Id:1536014032
    r2==> PointId:33393688 ;X_Id:1536014000 ;Y_Id:1536014032
    r3==> PointId:33393744 ;X_Id:1536014000 ;Y_Id:1536014032
    r1==> PointId:33393632 ;X_Id:1536014064 ;Y_Id:1536014032
    r2==> PointId:33393688 ;X_Id:1536014000 ;Y_Id:1536014032
    r3==> PointId:33393744 ;X_Id:1536014000 ;Y_Id:1536014032
"""

if __name__ == '__main__':
    r1 = Point(1, 2)
    r2 = Point(1, 2)
    r3 = Point(r1.x(), r1.y())
    print("r1==>", r1)
    print("r2==>", r2)
    print("r3==>", r3)
    r1.setX(3)
    print("r1==>", r1)
    print("r2==>", r2)
    print("r3==>", r3)
