import colorgram
import turtle

rgb_colors = []
colors = colorgram.extract('download.jpg', 84)
for i in colors:
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)

print(rgb_colors)