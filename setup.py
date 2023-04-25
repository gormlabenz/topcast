from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="topcast",
    version="0.1.5",
    author="Gorm Labenz",
    author_email="gorm@labenz.io",
    description="A Python package for Topcast",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gormlabenz/topcast",
    packages=find_packages(),
    license="MIT",
    keywords="topcast tts text-to-speech gcp google openai elevenlabs",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.7",
    install_requires=[
        "openai",
        "protobuf",
        "pydantic",
        "pydub",
        "elevenlabs",
        "google-cloud-texttospeech",
        "gTTS"
    ],
)
