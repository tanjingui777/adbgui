from PIL import Image
im = Image.open('/workspace/screenshots/farm_scrolled.png').convert('RGB')
crops = {
 'z_shield5.png': (530, 470, 650, 560),
 'z_shield4.png': (205, 405, 325, 495),
 'z_sign.png': (700, 470, 880, 600),
 'z_shield5_wide.png': (480, 460, 700, 633),
}
for name,(l,t,r,b) in crops.items():
    c = im.crop((l,t,r,b))
    w,h = c.size
    s = min(8, max(3, 1000//max(w,h)))
    c = c.resize((w*s, h*s), Image.NEAREST)
    c.save('/workspace/screenshots/'+name)
    print(name, (l,t,r,b), 'scale', s, '->', c.size)