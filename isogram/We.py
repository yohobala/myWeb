import math
import os

import shapefile


from PIL import Image, ImageDraw

class We():
  def world2screen(self,bbox, w, h, x, y):
    """转换地理空间坐标系到屏幕坐标"""
    minx, miny, maxx, maxy = bbox
    xdist = maxx - minx
    ydist = maxy - miny
    xratio = w/xdist
    yratio = h/ydist
    px = int(w - ((maxx - x) * xratio))
    py = int((maxy - y) * yratio)
    return (px, py)


  def gg(path,file):
    # 打开shapefile
    inShp = shapefile.Reader(path+file)
    iwidth = 600
    iheight = 400

    # 初始化 Image
    img = Image.new("RGB", (iwidth, iheight), (255, 255, 255))

    # 填充多边形
    draw = ImageDraw.Draw(img)

    # 获取人口和区域索引
    pop_index = None
    area_index = None

    # 绘制阴影
    for i, f in enumerate(inShp.fields):
        if f[0] == "POPULAT11":
            # Account for deletion flag
            pop_index = i - 1
        elif f[0] == "AREASQKM":
            area_index = i - 1

    # 绘制多边形
    for sr in inShp.shapeRecords():
        density = sr.record[pop_index] / sr.record[area_index]
        weight = min(math.sqrt(density / 80.0), 1.0) * 50
        R = int(205 - weight)
        G = int(215 - weight)
        B = int(245 - weight)
        pixels = []
        for x, y in sr.shape.points:
            """转换地理空间坐标系到屏幕坐标"""
            minx, miny, maxx, maxy = inShp.bbox
            xdist = maxx - minx
            ydist = maxy - miny
            xratio = iwidth / xdist
            yratio = iheight / ydist
            px = int(iwidth - ((maxx - x) * xratio))
            py = int((maxy - y) * yratio)
            pixels.append((px, py))
        draw.polygon(pixels, outline=(255, 255, 255), fill=(R, G, B))
    #img_path = path+file.split('.')[0]+'.jpg'
    img_path = os.path.dirname(os.getcwd())+'/webGIS/isogram/static/isogram/'+file.split('.')[0]+'.jpg'
    img.save(img_path)

    return img_path

