# Universal Plotting Sheet example to test circular axis and to try out parameterization capabilties of axis.

import sys
import pyx
from pynomo.nomographer import Nomo_Axis
import math

#sys.path.insert(0, "..")

cc = pyx.canvas.canvas()

r = 6.0
def func_f_1(u): return r * math.sin(u / 180 * math.pi)
def func_g_1(u): return r * math.cos(u / 180 * math.pi)


txt_format_min = "$%2.0f $"  # "$%2.0f'$"
line_width = pyx.style.linewidth.thin

# generate compass circle
# with inner degree ticks
# and outer degree scale used to determine latitude width
#
axis_appear_circle = {'full_angle': True,
                      'axis_color': pyx.color.cmyk.OliveGreen,
                      'text_color': pyx.color.cmyk.OliveGreen,
                      'extra_angle': 90.0,
                      'text_format': "$%3.0f$",
                      'text_horizontal_align_center': True,
                      'grid_length_0': 1.0 / 4,
                      'grid_length_1': 1.0 / 4,
                      'grid_length_2': 1.0 / 4,
                      'grid_length_3': 0.8 / 4,
                      'grid_length_4': 0.5 / 4,
                      'text_size_0': pyx.text.size.tiny,
                      'text_size_1': pyx.text.size.tiny,
                      'text_size_2': pyx.text.size.tiny,
                      'text_size_3': pyx.text.size.tiny,
                      'text_size_4': pyx.text.size.tiny,
                      'text_distance_0': 1.2 / 4,
                      'text_distance_1': 1.2 / 4,
                      'text_distance_2': 1.2 / 4,
                      'text_distance_3': 1.2 / 4,
                      'text_distance_4': 1.2 / 4,
                      }
axis_appear_circle2 = {'full_angle': True,
                      'axis_color': pyx.color.cmyk.OliveGreen,
                      'text_color': pyx.color.cmyk.OliveGreen,
                      'extra_angle': -90.0,
                      'text_format': "$%3.0f$",
                      'text_horizontal_align_center': True,
                      'grid_length_0': 1.0 / 4,
                      'grid_length_1': 1.0 / 4,
                      'grid_length_2': 1.0 / 4,
                      'grid_length_3': 0.8 / 4,
                      'grid_length_4': 0.5 / 4,
                      'text_size_0': pyx.text.size.tiny,
                      'text_size_1': pyx.text.size.tiny,
                      'text_size_2': pyx.text.size.tiny,
                      'text_size_3': pyx.text.size.tiny,
                      'text_size_4': pyx.text.size.tiny,
                      'text_distance_0': 1.64 / 4,
                      'text_distance_1': 1.64 / 4,
                      'text_distance_2': 1.64 / 4,
                      'text_distance_3': 1.64 / 4,
                      'text_distance_4': 1.64 / 4,
                      }
# Nomo_Axis(func_f=func_f_1,
#                func_g=func_g_1, start=0.0, stop=359.9, turn=-1, title='',
#                canvas=cc, type='circular', tick_levels=5, tick_text_levels=3,
#                side='left', axis_appear=axis_appear_circle)
Nomo_Axis(func_f=func_f_1,
          func_g=func_g_1, start=0.0, stop=90.0, turn=1, title='',
          canvas=cc, type='circular', tick_levels=5, tick_text_levels=3,
          side='left', axis_appear=axis_appear_circle)
Nomo_Axis(func_f=func_f_1,
          func_g=func_g_1, start=270.0, stop=359.9, turn=1, title='',
          canvas=cc, type='circular', tick_levels=5, tick_text_levels=3,
          side='right', axis_appear=axis_appear_circle)
Nomo_Axis(func_f=func_f_1,
          func_g=func_g_1, start=90.1, stop=269.9, turn=1, title='',
          canvas=cc, type='circular', tick_levels=5, tick_text_levels=3,
          side='left', axis_appear=axis_appear_circle2)

axis_appear_circle_extras = {'full_angle': False,
                            'axis_color': pyx.color.cmyk.OliveGreen,
                            'text_color': pyx.color.cmyk.OliveGreen,
                            'extra_angle': 0,  # -90.0,
                            'grid_length_1': 0,
                            'text_format': "$%3.0f$",
                            'text_horizontal_align_center': True,
                            'text_size_manual': pyx.text.size.tiny,
                            'text_horizontal_align_center': True,
                            'text_distance_1': 0.85 / 4,
                            'linewidth_main': line_width,
                            'linewidth_ticks': line_width,
                            'tick_linewidths': [line_width,
                                                line_width,
                                                line_width,
                                                line_width,
                                                line_width],
                            }
manual_axis_data_1 = {
    20.0: '70',
    30.0: '60',
    40.0: '50',
    50.0: '40',
    60.0: '30',
    70.0: '20',
    80.0: '10',
    100.0: '10',
    110.0: '20',
    120.0: '30',
    130.0: '40',
    140.0: '50',
    150.0: '60',
    160.0: '70',
}
Nomo_Axis(func_f=func_f_1,
          func_g=func_g_1, start=20.0, stop=160.0, turn=-1, title='',
          canvas=cc, type='manual line',
          side='right', manual_axis_data=manual_axis_data_1, axis_appear=axis_appear_circle_extras)

# generate vertical axis
# with ticks every 10 degrees
# three parts
axis_appear_vertical_axis_inner = {'full_angle': True,
                                  'extra_angle': 0.0,
                                  'axis_color': pyx.color.cmyk.OliveGreen,
                                  'text_color': pyx.color.cmyk.OliveGreen,
                                  'grid_length_0': 1.0 / 4,
                                  'grid_length_1': 1.0 / 4,
                                  'grid_length_2': 1.0 / 4,
                                  'grid_length_3': 0.8 / 4,
                                  'grid_length_4': 0.5 / 4,
                                  'text_format':  txt_format_min,
                                  # 'text_horizontal_align_center': True,
                                  'text_size_0': pyx.text.size.tiny,
                                  'text_size_1': pyx.text.size.tiny,
                                  'text_size_2': pyx.text.size.tiny,
                                  'text_size_3': pyx.text.size.tiny,
                                  'text_size_4': pyx.text.size.tiny,
                                  'text_distance_0': 1.2 / 4,
                                  'text_distance_1': 1.2 / 4,
                                  'text_distance_2': 1.2 / 4,
                                  'text_distance_3': 1.2 / 4,
                                  'text_distance_4': 1.2 / 4,
                                  }
o = 7
a = 0.2
t = 20.0
scale = 10
rs = r * scale
# pyx.unit.set(wscale=10)
# V_Axis_N_Above_Center_params
Nomo_Axis(func_f=lambda u: 0.0,
          func_g=lambda u: (rs + u)/scale, start=a, stop=t, turn=-1, title='',
          canvas=cc, type='circular', tick_levels=5, tick_text_levels=3,
          side='right', axis_appear=axis_appear_vertical_axis_inner)
# V_Axis_N_Center_params
Nomo_Axis(func_f=lambda u: 0.0,
          func_g=lambda u: (u)/scale, start=0.1, stop=rs - o, turn=-1, title='',
          canvas=cc, type='circular', tick_levels=5, tick_text_levels=3,
          side='right', axis_appear=axis_appear_vertical_axis_inner)
# V_Axis_S_Center_params
Nomo_Axis(func_f=lambda u: 0.0,
          func_g=lambda u: (- rs + u)/scale, start=0.1 + o, stop=rs - 0.1, turn=-1, title='',
          canvas=cc, type='circular', tick_levels=5, tick_text_levels=3,
          side='right', axis_appear=axis_appear_vertical_axis_inner)
# V_Axis_S_Below_Center_params
Nomo_Axis(func_f=lambda u: 0.0,
          func_g=lambda u: (-rs - u)/scale, start=a, stop=t, turn=-1, title='',
          canvas=cc, type='circular', tick_levels=5, tick_text_levels=3,
          side='right', axis_appear=axis_appear_vertical_axis_inner)

# Center latitude line
#
rwidth = 6
grid_color = pyx.color.cmyk.OliveGreen
line_style = [grid_color, pyx.style.linewidth.thin]
line_style_grey = [pyx.color.cmyk.Grey, pyx.style.linewidth.thin]
axis_offset = 8.0
a = 0.2
b = 0.6
tick = 0.0
cc.stroke(pyx.path.line(-axis_offset - rwidth, tick, -r - a, tick), line_style)
cc.stroke(pyx.path.line(-r + b, tick, r - b, tick), line_style)
cc.stroke(pyx.path.line(r + a, tick, axis_offset + rwidth, tick), line_style)

# Some latitude lines
# at 1 degree and minus 1 degree etc.
lat_list_v = [-6.0, 6.0]
for tick in lat_list_v:
    #cc.stroke(pyx.path.line(-axis_offset, tick, axis_offset + rwidth, tick), line_style_grey)
    cc.stroke(pyx.path.line(-axis_offset - rwidth,
              tick, -b, tick), line_style_grey)
    cc.stroke(pyx.path.line(b, tick, axis_offset + rwidth, tick), line_style_grey)
lat_list_v = [-8.0, 8.0]
for tick in lat_list_v:
    cc.stroke(pyx.path.line(-axis_offset - rwidth,
              tick, -a, tick), line_style_grey)
    cc.stroke(pyx.path.line(b, tick, axis_offset + rwidth, tick), line_style_grey)

# Field of Longitudes to calc Latitude
axis_appear_long = {
    'axis_color': pyx.color.cmyk.OliveGreen,
    'extra_angle': 0.0,
}
x_offset = r
y_offset = -r+1
scale_y = 15.5
rad_list = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
for tick in rad_list:
    Nomo_Axis(func_f=lambda u: x_offset + r - ((r-tick) * math.cos(u / 180 * math.pi)),
              func_g=lambda u: y_offset + u/scale_y, start=0.0, stop=70.0, turn=-1, title='',
              canvas=cc, type='linear', tick_levels=0, tick_text_levels=0,
              side='left', axis_appear=axis_appear_long)
d = r / 30.0
rad_list = [d, 2*d, 3*d, 4*d]
for tick in rad_list:
    Nomo_Axis(func_f=lambda u: x_offset + r - ((r-5.0-tick) * math.cos(u / 180 * math.pi)),
              func_g=lambda u: y_offset + u/scale_y, start=0.0, stop=70.0, turn=-1, title='',
              canvas=cc, type='linear', tick_levels=0, tick_text_levels=0,
              side='left', axis_appear=axis_appear_long)
axis_appear_longend = {
    'axis_color': pyx.color.cmyk.OliveGreen,
    'text_color': pyx.color.cmyk.OliveGreen,
    'extra_angle': 0.0,
    'grid_length_0': 0.0 / 4,
    'grid_length_1': 0.0 / 4,
    'grid_length_2': 0.0 / 4,
    'grid_length_3': 0.0 / 4,
    'grid_length_4': 0.0 / 4,
    'grid_length_5': 0.0 / 4,
    'text_size_0': pyx.text.size.tiny,
    'text_size_1': pyx.text.size.tiny,
    'text_size_3': pyx.text.size.tiny,
    'text_distance_0': 1.2 / 4,
    'text_distance_1': 1.2 / 4,
    'text_distance_2': 1.2 / 4,
    'text_distance_3': 1.2 / 4,
    'text_distance_4': 1.2 / 4,
    # 'text_horizontal_align_center': True,
    'text_format':  txt_format_min,
    'linewidth_main': line_width,
    'linewidth_ticks': line_width,
    'tick_linewidths': [line_width,
                        line_width,
                        line_width,
                        line_width,
                        line_width],
}
axis_appear_long0 = {
    'axis_color': pyx.color.cmyk.OliveGreen,
    'text_color': pyx.color.cmyk.OliveGreen,
    'extra_angle': 0.0,
    'grid_length_0': 0.0 / 4,
    'grid_length_1': 0.0 / 4,
    'grid_length_2': 0.0 / 4,
    'grid_length_3': 0.0 / 4,
    'grid_length_4': 0.0 / 4,
    'grid_length_5': 0.0 / 4,
    'text_size_0': pyx.text.size.tiny,
    'text_size_1': pyx.text.size.tiny,
    'text_size_3': pyx.text.size.tiny,
    'text_distance_0': 1.2 / 4,
    'text_distance_1': 1.2 / 4,
    'text_distance_2': 1.2 / 4,
    'text_distance_3': 1.2 / 4,
    'text_distance_4': 1.2 / 4,
    'text_horizontal_align_center': True,
    'text_format':  txt_format_min,
    'linewidth_main': line_width,
    'linewidth_ticks': line_width,
    'tick_linewidths': [line_width,
                        line_width,
                        line_width,
                        line_width,
                        line_width],
}
axis_appear_long1 = {
    'axis_color': pyx.color.cmyk.OliveGreen,
    'text_color': pyx.color.cmyk.OliveGreen,
    'extra_angle': 0.0,
    'grid_length_0': 1.1 / 4,
    'grid_length_1': 1.1 / 4,
    'grid_length_2': 1.1 / 4,
    'grid_length_3': 0.9 / 4,
    'grid_length_4': 0.7 / 4,
    'grid_length_5': 0.7 / 4,
    'text_size_0': pyx.text.size.tiny,
    'text_size_1': pyx.text.size.tiny,
    'text_size_3': pyx.text.size.tiny,
    'text_distance_0': 1.2 / 4,
    'text_distance_1': 1.2 / 4,
    'text_distance_2': 1.2 / 4,
    'text_distance_3': 1.2 / 4,
    'text_distance_4': 1.2 / 4,
    'text_format':  txt_format_min,
    'linewidth_main': line_width,
    'linewidth_ticks': line_width,
    'tick_linewidths': [line_width,
                        line_width,
                        line_width,
                        line_width,
                        line_width],
}
Nomo_Axis(func_f=lambda u: x_offset + r,
          func_g=lambda u: y_offset + u/scale_y, start=0.0, stop=70.0, turn=-1, title='',
          canvas=cc, type='circular', tick_levels=0, tick_text_levels=0,
          side='right', axis_appear=axis_appear_longend)
Nomo_Axis(func_f=lambda u: x_offset + r + 0.15,
          func_g=lambda u: y_offset + u/scale_y, start=0.0, stop=70.0, turn=-1, title='',
          canvas=cc, type='circular', tick_levels=5, tick_text_levels=3,
          side='right', axis_appear=axis_appear_long1)

line_style = [grid_color, pyx.style.linewidth.normal]
deg_list = [70.0, 60.0, 50.0, 40.0, 30.0, 20.0, 10.0]
for deg in deg_list:
    d = r * math.cos(deg / 180 * math.pi)
    start_x = x_offset + r - d
    y = y_offset + deg / scale_y
    cc.stroke(pyx.path.line(start_x, y, start_x + d, y), line_style)

Nomo_Axis(func_f=lambda u: x_offset + r * (u/60.0),
          func_g=lambda u: y_offset, start=0.0, stop=60.0, turn=-1, title='',
          canvas=cc, type='circular', tick_levels=0, tick_text_levels=3,
          side='left', axis_appear=axis_appear_long0)

# cc.writeEPSfile("ex_axis_circular_ups")
# cc.writeSVGfile("ex_axis_circular_ups")
cc.writePDFfile("ex_axis_circular_ups")
