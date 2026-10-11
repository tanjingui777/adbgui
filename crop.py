from PIL import Image
im = Image.open('/workspace/screenshots/farm_scrolled.png').convert('RGB')
print('size', im.size)
crops = {
 'crop_shield5.png': (500, 450, 680, 585),
 'crop_sign.png': (680, 450, 890, 600),
 'crop_shields123.png': (250, 150, 650, 300),
}
for name,(l,t,r,b) in crops.items():
    c = im.crop((l,t,r,b))
    w,h = c.size
    s = min(8, max(2, 1000//max(w,h)))
    c = c.resize((w*s, h*s), Image.LANCZOS)
    c.save('/workspace/screenshots/'+name)
    print(name, (l,t,r,b), 'scale', s, '->', c.size)