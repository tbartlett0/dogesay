from setuptools import setup

setup(
    name             = "dogesay_web",
    packages         = ["dogesay_web"],
    version          = "1.0.0",
    description      = "Like cowsay but doge and on the web",
    url              = "https://github.com/tbartlett0/dogesay",
#    download_url     = "https://github.com/jinnovation/dogesay/tarball/1.0",
    author           = "Tim Bartlett",
    author_email     = "github@tim.bartletts.id.au",
    license          = "MIT",
    classifiers      = [
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Developers",
        "Topic :: Games/Entertainment",

        "License :: OSI Approved :: MIT License",
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3', 
    ],
    install_requires = ["bottle", "begins"],
    keywords         = "",

    entry_points     ={
        "console_scripts": [
            "dogesay-web =dogesay_web.script:main",
        ],
    },

    package_data     = {
        "dogesay_web": ["static/*.html"],
    },
)

