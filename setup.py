from setuptools import setup


def _get_requirements():
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()
    return requirements


setup(
    name='speechemotionrecognition',
    version='1.1',
    packages=['speechemotionrecognition'],
    install_requires=_get_requirements(),
    description='Package to do speech emotion recognition'
)
