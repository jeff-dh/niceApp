##### An android / buildozer nicegui example

###### Build Apk

    python -m venv .env
    source .env/bin/activate
    pip install buildozer,setuptools

    git clone https://github.com/jeff-dh/nicegui.git
    cd nicegui
    git checkout android
    cd ..

    git clone https://github.com/jeff-dh/niceApp.git
    cd niceApp
    ln -s ../nicegui/nicegui nicegui
    buildozer android debug
