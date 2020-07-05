python setup.py sdist bdist_wheel
twine upload --repository-url https://pypi.backbone.sk dist/*
rm -rf build dist ludialudom.egg-info
