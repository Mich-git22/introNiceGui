from nicegui import ui

class Demo:
    def __init__(self):
        self.number = 1

demo = Demo()
v = ui.checkbox('visible', value=True)
with ui.column().bind_visibility_from(v, 'value'):
    ui.slider(min=0, max=6).bind_value(demo, 'number')
    ui.toggle({1: 'POO', 2: 'IO', 3: 'Sofware', 4:'Probabilidad',5:'Administración',6:'Estructura de datos'}).bind_value(demo, 'number')
    ui.number().bind_value(demo, 'number')

ui.run()