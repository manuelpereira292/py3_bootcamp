widget_one = ''
widget_two = ''
widget_three = 'button'

widgets_exist = any([widget_one, widget_two, widget_three])
print(widgets_exist)

all_widgets_exist = all([widget_one, widget_two, widget_three])
print(all_widgets_exist)

new_condition = any([widgets_exist, all([widget_one, widget_two, widget_three])])
print(new_condition)