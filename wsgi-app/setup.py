from setuptools import find_packages, setup

version = "0.0.1"

setup(
    name="wsgi_app",
    version=version,
    description="Flask WSGI APP",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        "flask",
    ],
    entry_points={
        "console_scripts": [
            "app-serve = wsgi_app.__main__:main"
        ],
    }
)
