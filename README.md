# 프로젝트에 Azure AI Service를 적용하는 단계별 가이드

언어 모델이나 컴퓨터 비전 같은 AI 리소스를 프로젝트에 적용하고 싶으신가요?
Microsoft의 Azure AI Services는 다양한 AI 리소스를 쉽고 빠르게 활용할 수 있습니다.

이 가이드에서는 Azure 오픈소스 프로젝트 Co-op Translator의 제작 경험을 바탕으로 Azure AI Services를 프로젝트에 적용하는 단계별 방법을 배워보겠습니다.

## 워크샵 목표

- **Azure OpenAI**를 활용해 간단한 챗봇을 만들어 Azure AI Services의 기초를 익힙니다.
- **Co-op Translator**를 사용해서 텍스트와 이미지 번역 워크플로우를 자동화하는 실습을 진행합니다.
- **Azure Computer Vision**, **Azure OpenAI**가 Co-op Translator 프로젝트에 어떻게 적용되었는지 이해합니다.
- 프로젝트 제작 과정에서 겪었던 고민과 해결 방안을 공유합니다.

## 워크샵 사전 준비사항

- [GitHub 계정](https://github.com/join)  
- [Git 설치](https://git-scm.com/)  
- [Visual Studio Code 설치](https://code.visualstudio.com/) 및 [Python 확장](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Python 3.10 이상 설치](https://www.python.org/downloads/)  
- [pyenv 설치 (선택 사항)](https://github.com/pyenv/pyenv)

## 가이드

1. [Azure 리소스 생성하기](./translations/ko/getting_started/set-up-azure-resources.md)

2. [Package  설치하기](./translations/ko/getting_started/install-package.md)

3. [.env 파일 만들기](./translations/ko/getting_started/create-env-file.md)

4. [Azure OpenAI를 이용한 간단한 챗봇 구현 코드](./example/basic-chatbot.py)