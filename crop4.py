from PIL import Image, ImageDraw
im = Image.open('/workspace/screenshots/farm_scrolled.png').convert('RGB')
# scene bottom at page 596 -> pixel 545; draw a red line there on a copy
im2 = im.copy()
d = ImageDraw.Draw(im2)
d.line([(0,545),(1280,545)], fill=(255,0,0), width=2)
im2.save('/workspace/screenshots/with_scenebottom_line.png')
for name,l,t,r,b in [('cc_s4.png',225,415,305,515),('cc_s5.png',548,478,628,578),('cc_s1.png',275,195,355,255)]:
    c = im.crop((l,t,r,b))
    w,h = c.size
    s = min(9, max(4, 1100//max(w,h)))
    c = c.resize((w*s, h*s), Image.NEAREST)
    c.save('/workspace/screenshots/'+name)
    print(name, (l,t,r,b), 'scale', s, '->', c.size)