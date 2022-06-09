from setuptools import find_packages, setup

with open("requirements.txt", "r") as f:
    install_requires = f.readlines()

setup(
    name="tf",
    version="0.0.1",
    description="This contains all of the files written for AWS terraform",
    author="Rooklyn Kline",
    author_email="rkline2@umbc.edu",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    package_data={'':['scripts/*']},
    include_package_data=True,
    install_requires=install_requires,
    entry_points = {
        'console_scripts':[
            'tf = tf.cli:main',
        ],
    },
    python_requires=">=3.7",
    extras_require={
        "dev": [
            "pytest==6.2.5",
            "wheel==0.37.0",
        ]
    },
)
