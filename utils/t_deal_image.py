from PIL import Image
import pytesseract

# 识别简单的验证码,不需要分割

im = Image.open('/Users/alpha/Desktop/7039.jpg')

# 'L'表示灰度,'1'表示二值图模式
imgry = im.convert('L')
# imgry.show()

threshold = 140
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

out = imgry.point(table, '1')


# out.show()

# text = pytesseract.image_to_string(out)
# print(text)

# import tesserocr
# text = tesserocr.image_to_text(out)
# print(text)


def binarizing(img, threshold):
    """传入image对象进行灰度/二值处理"""
    img = img.convert('L')  # 转灰度
    pixdata = img.load()  # 得到某个像素点的RGB元祖,而不是单一值了
    print(pixdata)
    w, h = img.size
    print(w, h)
    # 遍历所有像素,大于阈值的为黑色
    for y in range(h):
        for x in range(w):
            if pixdata[x, y] < threshold:
                pixdata[x, y] = 0
            else:
                pixdata[x, y] = 255
    return img


# imgry = binarizing(im, 140)
# imgry.show()


def depoint(img):
    """传入二值化后的图片进行降噪"""
    pixdata = img.load()
    w, h = img.zise
    for y in range(1, h - 1):  # 8邻域算法
        for x in range(1, w - 1):
            count = 0
            if pixdata[x, y - 1] > 245:  # 上
                count = count + 1
            if pixdata[x, y + 1] > 245:  # 下
                count = count + 1
            if pixdata[x - 1, y] > 245:  # 左
                count = count + 1
            if pixdata[x + 1, y] > 245:  # 右
                count = count + 1
            if pixdata[x - 1, y - 1] > 245:  # 左上
                count = count + 1
            if pixdata[x - 1, y + 1] > 245:  # 左下
                count = count + 1
            if pixdata[x + 1, y - 1] > 245:  # 右上
                count = count + 1
            if pixdata[x + 1, y + 1] > 245:  # 右下
                count = count + 1
            if count > 4:
                pixdata[x, y] = 255
    return img


def vertical(img):
    """传入二值化后的图片进行垂直投影"""
    pixdata = img.load()
    w, h = img.size()
    ver_list = []
    # 开始投影
    for x in range(w):
        black = 0
        for y in range(h):
            if pixdata[x, y] == 0:
                black += 1
        ver_list.append(black)
    # 判断边界
    l, r = 0, 0
    flag = False
    cuts = []
    for i, count in enumerate(ver_list):
        # 阈值这里为0
        if flag is False and count > 0:
            l = i
            flag = True
        if flag and count == 0:
            r = i - 1
            flag = False
            cuts.append((l, r))
        return cuts
