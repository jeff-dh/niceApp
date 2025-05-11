##### An android / buildozer nicegui example

###### Build Apk

    python -m venv .venv
    source .venv/bin/activate
    pip install buildozer aio_process_pool setuptools cython==3.0.12
    buildozer android debug
    buildozer serve

    browse to <you-ip>:8000 with your phone and install the app
