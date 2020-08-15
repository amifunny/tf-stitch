import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tf-stitch", 
    version="1.2.1",
    author="Hemant Singh",
    keywords=["Deep learning" , "tensorflow" , "tf2.0" ,"keras",
             "Boilerplate" , "Starter Code" , "Starter Pieces" , "Quick Work" , "Productivity"],
    description="Quick Starter Code with different specifications stitched together in tensorflow 2.0 .",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/amifunny/tf-stitch/",
    maintainer="amifunny",
    entry_points={
        'console_scripts':[
            'tf-stitch=tf_stitch.__main__:main'
        ]
    },
    include_package_data=True,
    packages=setuptools.find_packages(),
    package_data={
        'tf_stitch':['templates/*/*.py','template.json']
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]

)