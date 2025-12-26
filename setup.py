from setuptools import find_packages, setup


__version__ = "2.0.0"


setup(
    name="stable_baselines3",
    version=__version__,
    description="PyTorch version of Stable Baselines, implementations of reinforcement learning algorithms.",
    author="Antonin Raffin",
    author_email="antonin.raffin@dlr.de",
    url="https://github.com/DLR-RM/stable-baselines3",
    license="MIT",
    keywords=(
        "reinforcement-learning-algorithms reinforcement-learning "
        "machine-learning gym openai stable baselines toolbox python"
    ),
    packages=[
            pkg for pkg in find_packages()
            if pkg.startswith("stable_baselines3")
        ],
    package_data={
        "stable_baselines3": ["py.typed", "version.txt"]
    },
    install_requires=[
        "gym>=0.17",
        "numpy",
        "torch>=1.4.0",
        "cloudpickle",
    ],
)
