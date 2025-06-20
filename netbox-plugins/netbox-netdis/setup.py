from setuptools import find_packages, setup

setup(
    name="netbox-netdis",
    version="0.1",
    description="Network Hardware Discovery Plugin for NetBox",
    install_requires=[],  # add dependencies to requirements-prod.txt
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
