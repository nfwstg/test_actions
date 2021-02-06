from glob import glob
from os.path import basename
from os.path import splitext

from setuptools import setup
from setuptools import find_packages


def _requires_from_file(filename):
        return open(filename).read().splitlines()

setup(
        name="test_action",
        version="0.1.0",
        license="MIT",
        description="Test Git Actions",
        author="nfwstg@gmail.com",
        url="",
        packages=find_packages("src"),
        package_dir={"": "src"},
        py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
        include_package_data=True,
        zip_safe=False,
        install_requires=_requires_from_file('requirements.txt'),
        setup_requires=["pytest-runner"],
        tests_require=["pytest", "pytest-cov"],
        classifiers=[
                    'Development Status :: 3 - Alpha',
                    'Intended Audience :: Developers',
                    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
                    'Operating System :: OS Independent',
                ],
)

