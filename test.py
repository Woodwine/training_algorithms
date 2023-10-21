
if __name__ == "__main__":
    x = 0
    y = 0
    for i in range(260):
        x -= 1
        y -= 1
        print("X: ", x, "Y: ", y)
        print(x is y)
        print(x == y)
        print("X hash:", hash(x), " id:", id(x))
        print("Y hash:", hash(y), " id:", id(y))
