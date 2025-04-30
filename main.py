from nicegui import ui, app

@ui.page("/")
def index():
    def is_android():
        import platform
        return "android" in platform.uname().release

    if is_android():
        ui.label("Hello nice android world")
    else:
        ui.label("Hello World")

    storage = app.storage.user
    storage["foobar"] = storage.get("foobar", 0)

    def callback():
        storage["foobar"] += 1
        ui.label(f"yeah{'.'*storage['foobar']}")

    # ui.button("Really?", on_click=lambda: ui.label("yeah"))
    ui.button("Really?", on_click=callback)

ui.run(host='localhost', reload=False, show=False, storage_secret="foobar")
