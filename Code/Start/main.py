import pygame           #导入库

pygame.init()           #初始化

#定义变量
w = 900
h = 600
name = "SCP基金会"

def main(w,h,name):         #主函数
  w = (w,h)
  screen = pygame.display.set_mode(w)       #创建窗口
  pygame.display.set_caption(n)             #窗口标题
  #检测是否退出
  while True():
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
        pygame.quit()
        break
