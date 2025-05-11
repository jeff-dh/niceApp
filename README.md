##### An android / buildozer nicegui example

###### Build Apk

    python -m venv .venv
    source .venv/bin/activate
    pip install buildozer aio_process_pool setuptools cython==3.0.12
    buildozer android debug
    buildozer serve

    browse to <your-ip>:8000 with your phone and install the app

Notes:

- if you have issue compiling try removing the specific cython version (btw: buildozer==1.5.0)
- allow background activity for the app on your phone. Otherwise -- I assume -- the backend doesn't survive in the "background".
