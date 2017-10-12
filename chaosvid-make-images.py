#!/usr/bin/env pypy
from PIL import Image, ImageDraw, ImageFont
from math import exp,sin,cos
w = 1200; h = 800; g = 255                      # width,height,grayscale
n = 0.01                                        # population start value
re = 8.0                                        # max reproduction rate
sl = 7e6                                        # stabilisation loop size
t = 250                                         # frames
ttf = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
font_a = ImageFont.truetype(ttf, h / 30)
for f in xrange(t):
  c = 0.5 * f / t                               # constant in equ
  surface = [0] * h * w
  for x in xrange(w):                           # Step horiz coord
    sm = int(sl * (0.01 + x / w));              # Stabil loop size
    for s in range(sm):                         # Stabilization loop
      r = (x + 0.9 * s / sm) * re / w;          # Reproduction rate
      a = (s % 1000) * 1e-7;                    # Anti-metastable sawtooth
      n = r * exp(-((n-0.5) ** 2)) * (1.0+sin(n-c)) + a;  # Chaos equation
      y = int( (1 - n / 7.0) * (h - 1))         # Vertical coord
      surface[x + y * w] += 1                   # Inc grayscale at coord
  surface = [ g * g / (g + s) for s in surface] # Soft clip of grayscale
  img = Image.frombytes('L', (w,h), str(bytearray(surface)))
  draw = ImageDraw.Draw(img)
  txt = u"r exp(-(x-0.5)\u00B2)(1+sin(x-" + '%0.2f' % c + "))"
  draw.text((h/20, h/20), txt, "black", font=font_a)
  img.save('vid/chaos%04d.png' % f)
