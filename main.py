def monkey_patch_nicegui():
    import nicegui.run, aio_process_pool
    nicegui.run.ProcessPoolExecutor = aio_process_pool.Executor

    def patched_shutdown():
        assert nicegui.run.process_pool
        nicegui.run.process_pool.shutdown(wait=True, cancel_futures=True)
        nicegui.run.thread_pool.shutdown(wait=False, cancel_futures=True)

    nicegui.run.tear_down = patched_shutdown

monkey_patch_nicegui()

from nicegui import ui, app

@ui.page("/")
def index():
    ui.label("Hello World")

    def callback():
        ui.label(f"yeah")

    ui.button("Really?", on_click=callback)

ui.run(reload=False, show=False)
