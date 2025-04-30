from setuptools import setup, find_packages

setup(
    name="AldiTalk",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "Flask",
        "flask-cors",
        "python-dotenv",
        "requests",
        "azure-cognitiveservices-speech",
        "openai",
        "transformers",
        "torch",
        "numpy",
        "sounddevice",
        "scipy",
        "pydub",  
        "soundfile", 
        "ffmpeg"
    ],
    author="Habib, Jin Bin, Alex, Min",
    author_email="minmyrios@gmail.com",
    description="A speech-to-text and text-to-text translation system with text-to-speech capabilities using Azure.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/minmyrios/AldiTalk",  # Currently not published
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Proprietary (Closed-Source) License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.12.8',
    include_package_data=True,  
)