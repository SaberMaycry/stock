from PIL import Image

im = Image.open('F:\相册\塞尔达\四英杰.png')

# src_image.show()
# print(src_image)

rgb_pixels = list(im.getdata())
r_pixels = list(im.getdata(band=0))
g_pixels = list(im.getdata(band=1))
b_pixels = list(im.getdata(band=2))

print(rgb_pixels[:10])
print(r_pixels[:10])
print(g_pixels[:10])
print(b_pixels[:10])
