from PIL import Image
im = Image.open('/workspace/screenshots/farm_scrolled.png').convert('RGB')
crops = {
 'zz_s1.png': (270, 190, 362, 258),
 'zz_s4.png': (212, 410, 318, 515),
 'zz_s5.png': (532, 475, 648, 585),
 'zz_sign.png': (695, 480, 875, 615),
}
for name,(l,t,r,b) in crops.items():
    c = im.crop((l,t,r,b))
    w,h = c.size
    s = min(8, max(4, 1000//max(w,h)))
    c = c.resize((w*s, h*s), Image.NEAREST)
    c.save('/workspace/screenshots/'+name)
    print(name, (l,t,r,b), 'scale', s, '->', c.size)