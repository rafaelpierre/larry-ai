from setuptools import find_packages, setup
from pathlib import Path
import larry

PACKAGE_REQUIREMENTS = [
    "fastapi>=0.95.0,<1.0.0",
    "uvicorn[standard]==0.21.1",
    "jinja2",
    "click",
    "openai==0.28.1"
]

current_dir = Path(__file__).parent.parent
long_description = (current_dir / "README.md").read_text()

setup(
    name="larry-ai",
    packages=find_packages(),
    long_description = long_description,
    include_package_data=True,
    setup_requires=["setuptools", "wheel"],
    install_requires=PACKAGE_REQUIREMENTS,
    entry_points={"console_scripts": ["larry = larry.entrypoint:main"]},
    version="0.0.1",
    authors=["Rafael Pierre"],
)