import py2app.recipes
import py2app.build_app

from setuptools import find_packages, setup

pkgs = find_packages(".")

class recipe_plugin(object):
    @staticmethod
    def check(py2app_cmd, modulegraph):
        local_packages = pkgs[:]
        local_packages += ['pygame']
        return {
            "packages": local_packages,
        }

py2app.recipes.my_recipe = recipe_plugin

APP = ['auto_gato.py']
DATA_FILES = []
OPTIONS = {}
OPTIONS.update(
    iconfile="icon.icns",
    plist=dict(CFBundleIdentifier='com.example.yourdomain.notmine')
)

setup(
    name="Tic Tac Toe",
    app=APP,
    data_files=DATA_FILES,
    include_package_data=True,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    packages=pkgs,
    package_data={}
)
