import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
            name="example-pkg-your-username",
            version="0.0.1",
            author="Example Author",
            author_email="author@example.com",
            description="A small example package",
            long_description=long_description,
            long_description_content_type="text/markdown",
            url="https://github.com/pypa/sampleproject",
            packages=setuptools.find_packages(),
            classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            ],
        )




"""
setup()需要几个论点。此示例包使用相对最小的集：

name是包的分发名称。只要包含字母，数字_和，就可以是任何名称-。它也不能在pypi.org上使用。请务必使用您的用户名更新此内容，因为这可确保您在上传程序包时不会遇到任何名称冲突。
version 是包版本看 PEP 440有关版本的更多详细信息。
author并author_email用于识别包的作者。
description 是一个简短的，一句话的包的总结。
long_description是包的详细说明。这显示在Python Package Index的包详细信息包中。在这种情况下，加载长描述README.md是一种常见模式。
long_description_content_type告诉索引什么类型的标记用于长描述。在这种情况下，它是Markdown。
url是项目主页的URL。对于许多项目，这只是一个指向GitHub，GitLab，Bitbucket或类似代码托管服务的链接。
packages是应包含在分发包中的所有Python 导入包的列表。我们可以使用 自动发现所有包和子包，而不是手动列出每个包。在这种情况下，包列表将是example_pkg，因为它是唯一存在的包。find_packages()
classifiers告诉索引并点一些关于你的包的其他元数据。在这种情况下，该软件包仅与Python 3兼容，根据MIT许可证进行许可，并且与操作系统无关。您应始终至少包含您的软件包所使用的Python版本，软件包可用的许可证以及您的软件包将使用的操作系统。有关分类器的完整列表，请参阅 https://pypi.org/classifiers/。
除了这里提到的还有很多。有关详细信息，请参阅 打包和分发项目。


"""







