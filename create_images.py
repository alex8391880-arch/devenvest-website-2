from PIL import Image, ImageDraw
import os

# Create assets directory if it doesn't exist
os.makedirs('assets', exist_ok=True)

# Project 1 - Clubhouse
img1 = Image.new('RGB', (600, 400), color='#0f172a')
draw = ImageDraw.Draw(img1)
# Draw a simple building shape
draw.rectangle([100, 150, 500, 350], outline='#f59e0b', width=3)
draw.rectangle([150, 200, 450, 300], outline='#f59e0b', width=2)
# Add windows
for i in range(3):
    for j in range(2):
        x = 180 + i * 80
        y = 220 + j * 50
        draw.rectangle([x, y, x+30, y+30], outline='#f59e0b', width=1)
img1.save('assets/project1.jpg')

# Project 2 - Varna complex
img2 = Image.new('RGB', (600, 400), color='#1e3a8a')
draw = ImageDraw.Draw(img2)
# Draw a modern building
draw.rectangle([80, 120, 520, 340], outline='#f59e0b', width=3)
draw.rectangle([90, 130, 510, 330], outline='#f59e0b', width=1)
# Grid of windows
for i in range(5):
    for j in range(4):
        x = 110 + i * 80
        y = 150 + j * 40
        draw.rectangle([x, y, x+25, y+25], fill='#64748b')
img2.save('assets/project2.jpg')

# Create founder placeholder
img3 = Image.new('RGB', (400, 500), color='#e2e8f0')
draw = ImageDraw.Draw(img3)
# Draw a simple profile shape
draw.ellipse([100, 50, 300, 250], fill='#94a3b8')
draw.rectangle([50, 250, 350, 500], fill='#cbd5e1')
img3.save('assets/founder2.jpg')

print('All images created successfully')
