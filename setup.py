import setuptools

setuptools.setup(
    name="saywhen",
    description="Send notifications when command line job finishes",
    version="0.0.1",
    author="Yunqing Gong",
    author_email="gongyq10@gmail.com",
    url="https://github.com/yunqing/saywhen",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=['saywhen'],
    package_data={
        'saywhen': [
            'audio/*'
            ]
        },
    include_package_data=True,
    scripts=['scripts/saywhen']
)
