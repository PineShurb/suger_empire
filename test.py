
import random

DIR_STOP = 0
DIR_UP = 1
DIR_DOWN = 2
DIR_LEFT = 3
DIR_RIGHT = 4

EARTH_UNREACHABLE = 1

class SugerEmpire:
    def __init__(self, xlen=100, ylen=100,sn=100,pop=10,sight=5):
        self.xlen = xlen # 设置环境的宽度
        self.ylen = ylen # 设置环境的高度
        self.earth = [[0 for _ in range(self.xlen)] for _ in range(self.ylen)]  # 地图 土地
        self.surger = [[0 for _ in range(self.xlen)] for _ in range(self.ylen)]  # 地图 糖
        self.sn = sn # 糖的数量
        self.pop = pop # 人口数量
        person = {"x":0,"y":0,"suger":0,"age":0,"live":False,"direction":DIR_STOP}
        self.persons = [person for _ in range(self.pop)] # 人口列表
        self.popmap = [[0 for _ in range(self.xlen)] for _ in range(self.ylen)]  # 地图 人口
        self.sight = sight # 视野
        view = [[0 for _ in range(self.sight*2+1)] for _ in range(self.sight*2+1)]  #视野
        popvi = {"earth":view,"suger":view,"pop":view}
        self.view_module = popvi
        # self.views = [popvi for _ in range(self.pop)] # 视野列表
        pass
    def step(self, *args, **kwargs):
        # 在这里实现step函数的逻辑
        pass

    def reset(self):
        # 在这里实现reset函数的逻辑
        self.surger = [[0 for _ in range(self.xlen)] for _ in range(self.ylen)]
        for i in range(self.sn):
            x = random.randint(0, self.xlen-1)
            y = random.randint(0, self.ylen-1)
            self.surger[x][y] += 9
        self.popmap = [[0 for _ in range(self.xlen)] for _ in range(self.ylen)]
        for i in range(self.pop):
            while True:
                x = random.randint(0, self.xlen-1)
                y = random.randint(0, self.ylen-1)
                if self.popmap[x][y] == 0:
                    self.popmap[x][y] = i
                    self.persons[i]["x"] = x
                    self.persons[i]["y"] = y
                    break
            self.persons[i]["live"] = True
        pass
    
    def check_pop(self):
        # 确定每个活人都在自己的位置
        for i in range(self.pop):
            if(self.persons[i]["live"]):
                x = self.persons[i]["x"]
                y = self.persons[i]["y"]
                if self.popmap[x][y] != i:
                    print("pop error:" + str(i) + " not in " + str(x) + " " + str(y))
        # 确定每个有人的位置都是活人
        for x in range(sec.xlen):
            for y in range(sec.ylen):
                if self.popmap[x][y] != 0:
                    pnum = self.popmap[x][y]
                    if(self.persons[pnum]["live"] != True):
                        print("pop error:" + str(pnum) + " not live in " + str(x) + " " + str(y))
        pass

    def render(self):
        # 在这里实现render函数的逻辑
        pass

    def close(self):
        # 在这里实现close函数的逻辑
        pass
    
    def sugermap(self):
        return self.surger
        pass
    
    def popmap(self):
        return self.popmap
    
    def getview(self,person):
        '''
        获取一个人的视野
        person: 序号
        '''
        if(person >= self.pop):
            return None
        x = self.persons[person]["x"]
        y = self.persons[person]["y"]
        view = self.view_module
        for i in range(-self.sight,self.sight+1):
            for j in range(-self.sight,self.sight+1):
                if x+i < 0 or x+i >= self.xlen or y+j < 0 or y+j >= self.ylen:
                    view["earth"][i+self.sight][j+self.sight] = EARTH_UNREACHABLE
                    view["suger"][i+self.sight][j+self.sight] = 0
                    view["pop"][i+self.sight][j+self.sight] = 0
                else:
                    view["earth"][i+self.sight][j+self.sight] = self.earth[x+i][y+j]
                    view["suger"][i+self.sight][j+self.sight] = self.surger[x+i][y+j]
                    view["pop"][i+self.sight][j+self.sight] = self.popmap[x+i][y+j]
        return view



MAP_WIDTH = 500
MAP_HEIGHT = 500
VIEW_WIDTH = 200
VIEW_HEIGHT = 200


print("first py file\n")

sec = SugerEmpire(50,50)

import tkinter as tk

def button_reset():
    text_box.insert(tk.END, "reset click\n")
    sec.reset()
    refresh_map()
    refresh_view()
    
def refresh_map():
    suger_map = sec.sugermap()
    pop_map = sec.popmap
    main_map.delete("all")  # Clear the canvas
    main_map.create_rectangle(0, 0, MAP_WIDTH, MAP_HEIGHT, fill="white")
    xbit = MAP_WIDTH / sec.xlen
    ybit = MAP_HEIGHT / sec.ylen
    for x in range(sec.xlen):
        for y in range(sec.ylen):
            suger_level = suger_map[x][y]
            if suger_level != 0:
                main_map.create_rectangle(x*xbit, y*ybit, (x+1)*xbit, (y+1)*ybit, fill="green")
            if pop_map[x][y] != 0:
                main_map.create_rectangle(x*xbit, y*ybit, (x+1)*xbit, (y+1)*ybit, fill="red")

def refresh_view():
    view_map.delete("all")  # Clear the canvas
    view_map.create_rectangle(0, 0, VIEW_WIDTH, VIEW_HEIGHT, fill="white")
    view = sec.getview(0)  # Get the view for person 0
    xbit = VIEW_WIDTH / (sec.sight * 2 + 1)
    ybit = VIEW_HEIGHT / (sec.sight * 2 + 1)
    for x in range(sec.sight * 2 + 1):
        for y in range(sec.sight * 2 + 1):
            earth = view["earth"][x][y]
            suger = view["suger"][x][y]
            pop = view["pop"][x][y]
            if earth == EARTH_UNREACHABLE:
                view_map.create_rectangle(x*xbit, y*ybit, (x+1)*xbit, (y+1)*ybit, fill="black")
            '''
            if pop != 0:
                view_map.create_rectangle(x * xbit, y * ybit, (x + 1) * xbit, (y + 1) * ybit, fill="red")
            '''
            if suger != 0:
                view_map.create_rectangle(x*xbit, y*ybit, (x+1)*xbit, (y+1)*ybit, fill="green")
                # view_map.create_text((x + 0.5) * xbit, (y + 0.5) * ybit, text=str(suger))
    pass


root = tk.Tk()
root.geometry("1200x600")  # 设置窗口大小为800x600
root.title("Suger Empire")

button = tk.Button(root, text="reset", command=button_reset)
button.place(x=10, y=10)

text_box = tk.Text(root, height=10, width=40)
text_box.place(x=10, y=40,width=180,height=80)

main_map = tk.Canvas(root, width=500, height=500, bg='white')
main_map.place(x=250, y=50)

view_map = tk.Canvas(root, width=200, height=200, bg='white')
view_map.place(x=800, y=150)

root.mainloop()

