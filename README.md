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

- 아래 단계별로 워크샵을 진행합니다. 각 단계별로 자기주도형 학습을 하며, 단계별 시작 전 진행자가 간단한 안내 후 시작합니다.

  | 순서                         | 제목                                           |
  |------------------------------|------------------------------------------------|
  | [STEP 00](./docs/step-00.md) | Azure 리소스 생성하기                             |
  | [STEP 01](./docs/step-01.md) | .env 파일 만들기     |
  | [STEP 02](./docs/step-02.md) | Package 설치하기                |
  | [STEP 03](./docs/step-03.md) | Co-op Translator을 이용해서 문서 번역해보기               |

## 실습 자료

- [.env 파일 템플릿](./example/.env.template)
- [Azure OpenAI를 이용한 간단한 챗봇 구현 코드](./example/basic-chatbot.py)
- [Azure OpenAI를 이용한 간단한 챗봇 구현 코드 (.env 이용 버전)](./example/basic-chatbot-env.py)
- [gitignore 파일](./example/.gitignore)
- [발표 자료](./docs/24-12-8-workshop.pdf)
- [Co-op Translator GitHub](https://github.com/Azure/co-op-translator)
