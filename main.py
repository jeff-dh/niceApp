from nicegui import ui, app

def is_android():
    import platform
    return "android" in platform.uname().release

@ui.page("/")
def index():
    if is_android():
        ui.label("Hello nice android world")

    storage = app.storage.user
    storage["foobar"] = storage.get("foobar", 0)

    def callback():
        storage["foobar"] += 1
        ui.label(f"yeah{'.'*storage['foobar']}")

    ui.button("Really?", on_click=callback)

ui.run(host='localhost', reload=False, show=False, storage_secret="foobar")
