from nicegui import ui
from nicegui.events import ValueChangeEventArguments

def show(event: ValueChangeEventArguments):
    name = type(event.sender).__name__
    ui.notify(f'{name}: {event.value}')

ui.button('Haz clic', on_click=lambda: ui.notify('Hiciste Clic'))
with ui.row():
    ui.checkbox('Wenas', on_change=show)
    ui.switch('Hola/Adios', on_change=show)
ui.radio(['Pais', 'Ciudad', 'Estado'], value='Pais', on_change=show).props('inline')
with ui.row():
    ui.input('Escribe algo', on_change=show)
    ui.select(['Dia', 'Mes'], value='Dia', on_change=show)
ui.link('Sigue viendo...', '/documentation').classes('mt-8')

ui.run()