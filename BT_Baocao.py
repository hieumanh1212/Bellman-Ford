import queue
class Graph:

    def __init__(self, SoDinh):
        self.n = SoDinh     #Gồm n Đỉnh
        self.DoThi = []     #Đồ thị
    #Add dữ liệu
    def addData(self, u, v, w):
        self.DoThi.append([u, v, w])    #Thêm dữ liệu vào đồ thị
    #Thật toán BellMan-Ford
    def BellmanFord(self, nguon):
        khoangcach = [float("Inf")] * self.n        #Khởi tạo khoảng cách từ nguồn đến các đỉnh còn lại bằng vô cùng
        khoangcach[nguon] = 0                       #Khởi tạo khoảng cách từ nguồn đến chính nó bằng 0
        par = [0]*(self.n+1)    #Cha
        for i in range(self.n-1):
            for u, v, w in self.DoThi:
                if khoangcach[u] != float("Inf") and khoangcach[u] + w < khoangcach[v]:
                    khoangcach[v] = khoangcach[u] + w
                    par[v] = u
        #Chu trình âm
        for u, v, w in self.DoThi:
            if khoangcach[u] != float("Inf") and khoangcach[u] + w < khoangcach[v]:
                print("Đồ thị chứa chu trình âm !")
                return
        for i in range(0,self.n):
            print("\nTừ đỉnh {0} đến đỉnh {1} là: {2} theo chu trình:".format(nguon, i, khoangcach[i]))
            if(khoangcach[i] != float("Inf")):
                self.duongdi(nguon, i, par)
    def duongdi(self, nguon, i, par):
        if nguon == i: print(nguon, end=" ")
        else:
            self.duongdi(nguon, par[i], par)
            print("-> %d"%(i), end="")
if __name__ == '__main__':
    n, m = map(int,input().split())
    g = Graph(n)
    for i in range (m):
        u,v,w = map(int, input().split())
        g.addData(u,v,w)

    g.BellmanFord(0)

'''
5 8
0 1 -1
0 2 4
1 2 3
1 3 2
1 4 2
3 2 5
3 1 1
4 3 -3
'''
