from setuptools import find_packages, setup

version = "0.0.1"

setup(
    name="asgi_app",
    version=version,
    description="Starlette ASGI APP",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        "quart"
    ],
    entry_points={
        "console_scripts": [
            "app-serve = asgi_app.__main__:main"
        ],
    }
)
