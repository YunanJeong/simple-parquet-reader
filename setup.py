# setup.py는 프로젝트의 테스트, 빌드, 배포에 필요한 정보를 가진다.
# setuptools라는 널리 쓰이는 패키지에 의존한다.
# setuptools 외에도 배포방법은 여럿 있다.
"""
setup.py vs. requirements.txt
둘 다 패키지에 필요한 dependency 목록을 표기한다.

setup.py는 일반적으로 PyPI에서 다운받는 것들을 명시
requirements.txt는 PyPI 외에 다운 경로를 지정할 수 있다. (ex. private한 환경, 사내 내부망 등)
또한, 패키지를 '설치'할 때 필요한 dependency가 추가로 있을 수 있는데, 이들을 setup.py에 표기할 수도 있다.(ex. wheel)
"""

import os
from setuptools import setup

with open(os.path.join('pyparq-reader', 'version.py'), 'rt') as f:
    version = f.readline().strip()
    version = version.split('=')[1].strip()
    version = version.strip("'")
setup(
    name='pyparq-reader',
    version=version,
    author='njhgle@gmail.com',
    pythonrequires='>=3.7',
    install_requires=[
        'wheel'
    ]
)
