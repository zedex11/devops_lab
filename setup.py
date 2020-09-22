from setuptools import setup, find_packages

setup(
    name="snapshot",
    packages=find_packages(),
    entry_points={
        "console_scripts":
            ["snapshot = monitor.snapshot:main"]
    },
    install_requires=[
        'psutil'
    ],
    version="0.1",
    author="Siarhei Hryshchanka",
    author_email="siarhei_hryshchanka@epam.com",
    description="Monitoring application",
    license="Free",
)
