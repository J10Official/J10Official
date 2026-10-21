"""Render a seamless rotating Lorenz attractor; requires numpy and Pillow."""
from pathlib import Path
import math
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageChops

ROOT = Path(__file__).parent
W, H = 520, 280
BG = (13, 17, 23)

def velocity(p):
    x, y, z = p
    return np.array([10*(y-x), x*(28-z)-y, x*y-8*z/3])

p = np.array([0.1, 0.0, 0.0])
points = []
dt = .008
for n in range(10500):
    a = velocity(p)
    b = velocity(p+dt*a/2)
    c = velocity(p+dt*b/2)
    d = velocity(p+dt*c)
    p = p + dt*(a+2*b+2*c+d)/6
    if n > 1500 and n % 2 == 0:
        points.append(p.copy())
points = np.array(points)
points[:, 2] -= 25
colors = []
for i in range(len(points)):
    t = .5+.5*math.sin(i/len(points)*math.tau*2)
    colors.append(tuple(int(a*(1-t)+b*t) for a,b in zip((34,211,238),(167,139,250))))

frames = []
for frame in range(120):
    angle = math.tau*frame/120
    x = points[:,0]*math.cos(angle)+points[:,1]*math.sin(angle)
    depth = -points[:,0]*math.sin(angle)+points[:,1]*math.cos(angle)
    z = points[:,2]
    coords = np.column_stack([W/2+x*7.0, H/2-z*5.1])
    strokes = Image.new('RGB', (W,H))
    draw = ImageDraw.Draw(strokes)
    for i in np.argsort(depth[:-1]):
        shade = .28+.60*(depth[i]+30)/60
        color = tuple(min(255,int(v*shade)) for v in colors[i])
        draw.line([tuple(coords[i]),tuple(coords[i+1])],fill=color,width=1)
    glow = strokes.filter(ImageFilter.GaussianBlur(3))
    art = ImageChops.add(strokes,glow,scale=1)
    art = ImageChops.add(Image.new('RGB',(W,H),BG),art)
    # Bright tracers travel along the trajectory as the camera completes a turn.
    draw = ImageDraw.Draw(art)
    for j in range(10):
        k = (frame*len(points)//120+j*len(points)//10)%len(points)
        qx,qy=coords[k]
        draw.ellipse((qx-1.4,qy-1.4,qx+1.4,qy+1.4),fill=(220,248,255))
    frames.append(art)

palette = frames[0].quantize(colors=128)
indexed = [f.quantize(palette=palette,dither=Image.Dither.NONE) for f in frames]
indexed[0].save(ROOT/'attractor.gif',save_all=True,append_images=indexed[1:],duration=70,loop=0,optimize=True)
frames[0].save(ROOT/'attractor-preview.png')
print(f'{len(frames)} frames; {(ROOT / "attractor.gif").stat().st_size:,} bytes')

