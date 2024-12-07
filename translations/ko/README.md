![Logo](/imgs/logo.png)

# Co-op Translator: 단일 명령어로 프로젝트를 현지화하세요

_고급 LLM 기술과 Azure AI 서비스를 통해 프로젝트의 다국어 번역을 쉽게 자동화할 수 있습니다._

[![Python package](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![License: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![Downloads](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![Downloads](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)

[![GitHub contributors](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)
[![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=VS%20Code%20Dev%20Containers&message=Open&color=007ACC&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)

## 🌐 다국어 지원
| [영어](../en/README.md) | [프랑스어](../fr/README.md) | [스페인어](../es/README.md) | [독일어](../de/README.md) | [러시아어](../ru/README.md) | [아랍어](../ar/README.md) | [페르시아어 (파르시어)](../fa/README.md) | [우르두어](../ur/README.md) | [중국어 (간체)](../zh/README.md) | [중국어 (번체, 마카오)](../mo/README.md) | [중국어 (번체, 홍콩)](../hk/README.md) | [중국어 (번체, 대만)](../tw/README.md) | [일본어](../ja/README.md) | [한국어](./README.md) | [힌디어](../hi/README.md) | [벵골어](../bn/README.md) | [마라티어](../mr/README.md) | [네팔어](../ne/README.md) | [펀자브어 (구르무키어)](../pa/README.md) | [포르투갈어](../pt/README.md) | [이탈리아어](../it/README.md) | [폴란드어](../pl/README.md) | [터키어](../tr/README.md) | [그리스어](../el/README.md) | [태국어](../th/README.md) | [스웨덴어](../sv/README.md) | [덴마크어](../da/README.md) | [노르웨이어](../no/README.md) | [핀란드어](../fi/README.md) | [네덜란드어](../nl/README.md) | [히브리어](../he/README.md) | [베트남어](../vi/README.md) | [인도네시아어](../id/README.md) | [말레이어](../ms/README.md) | [타갈로그어 (필리핀어)](../tl/README.md) | [스와힐리어](../sw/README.md) | [헝가리어](../hu/README.md) | [체코어](../cs/README.md) | [슬로바키아어](../sk/README.md) | [루마니아어](../ro/README.md) | [불가리아어](../bg/README.md) | [세르비아어 (키릴 문자)](../sr/README.md) | [크로아티아어](../hr/README.md) | [슬로베니아어](../sl/README.md) |
> **Note:**
> These translations were automatically generated using the open-source [co-op-translator](https://github.com/Azure/co-op-translator) and may contain errors or inaccuracies. For critical information, it is recommended to refer to the original or consult a professional human translation. If you'd like to add or update a translation, please refer to the [co-op-translator](https://github.com/Azure/co-op-translator) repository, where you can easily contribute using simple commands.

## 목차

- [개요](../..)
- [왜 Co-op Translator를 선택해야 할까요?](../..)
- [주요 기능](../..)
- [작동 원리](../..)
- [Co-op Translator 시작하기](../..)
  - [사전 준비 사항](../..)
  - [빠른 설치](../..)
  - [Co-op Translator 사용 방법](../..)
- [사례 연구: 실제 프로젝트에서 Co-op Translator 적용하기](../..)
- [🌐다국어 지원 설정](../..)
- [지원 언어](../..)
- [새로운 언어 추가](../..)
- [저장소 구조](../..)
- [기여](../..)
- [행동 강령](../..)
- [책임 있는 AI](../..)
- [상표](../..)

## 개요

**Co-op Translator**는 고급 대형 언어 모델(LLM) 기술과 Azure AI 서비스를 사용하여 프로젝트의 다국어 번역을 자동화하도록 설계된 Python 패키지입니다. 이 프로젝트는 여러 언어로 콘텐츠를 번역하는 과정을 단순화하여 개발자가 쉽게 접근하고 효율적으로 사용할 수 있도록 합니다.

Co-op Translator를 워크플로에 통합하면 다양한 언어에 대한 번역 폴더를 자동으로 생성하고, Markdown 파일과 이미지를 손쉽게 번역할 수 있습니다.

여기 Co-op Translator가 번역을 구조화하고 프로젝트 내의 Markdown 파일과 이미지 내 텍스트를 번역하는 방법의 예시가 있습니다:

![Example](/imgs/translation-ex.png)

### 왜 Co-op Translator를 선택해야 할까요?

Markdown 파일 작업 시 전통적인 번역 도구로 어려움을 겪으셨나요? 많은 번역 엔진은 Markdown 구문을 보존하지 못해 번역 후 형식 문제를 수동으로 수정해야 합니다. 심지어 ChatGPT와 같은 고급 도구도 코드 블록을 오해하여 번역된 콘텐츠를 원래 구조를 유지하면서 복사하고 붙여넣기 어렵게 만듭니다.

**Co-op Translator**는 이러한 문제를 해결하도록 특별히 설계되었습니다. 단일 명령으로 프로젝트 내 모든 Markdown 파일과 이미지를 원하는 언어로 번역하면서 올바른 Markdown 구문을 보존할 수 있습니다.

Co-op Translator로 프로젝트의 Markdown 파일을 손쉽게 번역하세요!

### 주요 기능

- **자동 번역**: 프로젝트 파일의 텍스트를 여러 언어로 쉽게 번역합니다.
- **포괄적 적용 범위**: 프로젝트 디렉토리 내 모든 Markdown 파일과 이미지 내 텍스트를 번역합니다.
- **고급 LLM 기술**: 최첨단 언어 모델을 사용하여 고품질 번역을 제공합니다.
- **현지화 단순화**: 프로젝트를 국제 시장에 맞게 현지화하는 과정을 간소화합니다.
- **쉬운 통합**: 기존 프로젝트 설정과 원활하게 통합됩니다.

### 작동 원리

![Architecture](/imgs/architecture_241019.png)

이 과정은 프로젝트 폴더의 Markdown 및 이미지 파일에서 시작되며, **Azure AI Services**에 의해 처리됩니다:

- **Azure OpenAI**: Markdown 파일의 텍스트를 번역합니다.
- **Azure Computer Vision**: 이미지에서 텍스트를 추출한 후, Azure OpenAI가 번역합니다.

최종 번역된 Markdown 및 이미지 파일은 지정된 번역 폴더에 저장되어 여러 언어로 사용할 준비가 됩니다.

## Co-op Translator 시작하기

### 사전 준비 사항

- Azure Computer vision 리소스
- Azure OpenAI 리소스
- Python 3.10 이상

### 빠른 설치

#### pip를 통한 Co-op Translator 설치

```bash
pip install co-op-translator
```

#### poetry를 통한 Co-op Translator 설치

```bash
poetry add co-op-translator
```

### Co-op Translator 사용 방법

1. [시작하기 전에 Azure 리소스 설정](./getting_started/set-up-azure-resources.md)
1. [루트 디렉토리에 '.env' 파일 생성](./getting_started/create-env-file.md)
1. [Co-op Translator 패키지 설치](./getting_started/install-package.md)
1. [Co-op Translator를 사용하여 프로젝트 번역](./getting_started/translator-your-project.md)

### 사례 연구: 실제 프로젝트에서 Co-op Translator 적용하기

이 사례 연구는 Co-op Translator가 실제 프로젝트를 번역하는 데 어떻게 적용되었는지 보여줍니다. 번역 과정, 직면한 문제, 달성된 결과를 강조하여 유사한 프로젝트에 도구를 적용하는 데 유용한 참고 자료를 제공합니다.

1. [Phi-3 Cookbook 번역: 사례 연구](./getting_started/Phi-3Cookbook-translation-case.md)

## 🌐 다국어 지원 설정

번역 과정을 시작하기 전에 README에 문서의 번역된 버전으로 연결되는 표를 추가할 수 있습니다. Co-op Translator는 번역 과정 중 이러한 링크를 자동으로 조정하여 사용자가 다른 언어 버전 간에 원활하게 전환할 수 있도록 합니다.

예를 들어, 사용자가 한국어 README로 이동하면 번역된 페이지를 떠나지 않고도 스페인어나 일본어와 같은 다른 번역으로 쉽게 전환할 수 있습니다.

번역을 실행하기 전에 표가 어떻게 보여야 하는지에 대한 예시는 다음과 같습니다:

### 예시

```md
## 🌐 Multi-Language Support

> **Note:**
> These translations were automatically generated using the open-source [co-op-translator](https://github.com/Azure/co-op-translator) and may contain errors or inaccuracies. For critical information, it is recommended to refer to the original or consult a professional human translation. If you'd like to add or update a translation, please refer to the [co-op-translator](https://github.com/Azure/co-op-translator) repository, where you can easily contribute using simple commands.

| Language             | Code | Link to Translated README                               | Last Updated |
|----------------------|------|---------------------------------------------------------|--------------|
| Chinese (Simplified) | zh   | [Chinese Translation](../zh/README.md)      | 2024-10-04   |
| Chinese (Traditional)| tw   | [Chinese Translation](../tw/README.md)      | 2024-10-04   |
| French               | fr   | [French Translation](../fr/README.md)       | 2024-10-04   |
| Japanese             | ja   | [Japanese Translation](../ja/README.md)     | 2024-10-04   |
| Korean               | ko   | [Korean Translation](./README.md)       | 2024-10-04   |
| Spanish              | es   | [Spanish Translation](../es/README.md)      | 2024-10-04   |
```

### 간단한 예시

```md
## 🌐 Multi-Language Support

| [English](../en/README.md) | [French](../fr/README.md) | [Spanish](../es/README.md) | [German](../de/README.md) | [Russian](../ru/README.md) | [Arabic](../ar/README.md) | [Persian (Farsi)](../fa/README.md) | [Urdu](../ur/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Japanese](../ja/README.md) | [Korean](./README.md) | [Hindi](../hi/README.md) | [Bengali](../bn/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Portuguese](../pt/README.md) | [Italian](../it/README.md) | [Polish](../pl/README.md) | [Turkish](../tr/README.md) | [Greek](../el/README.md) | [Thai](../th/README.md) | [Swedish](../sv/README.md) | [Danish](../da/README.md) | [Norwegian](../no/README.md) | [Finnish](../fi/README.md) | [Dutch](../nl/README.md) | [Hebrew](../he/README.md) | [Vietnamese](../vi/README.md) | [Indonesian](../id/README.md) | [Malay](../ms/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Swahili](../sw/README.md) | [Hungarian](../hu/README.md) | [Czech](../cs/README.md) | [Slovak](../sk/README.md) | [Romanian](../ro/README.md) | [Bulgarian](../bg/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Croatian](../hr/README.md) | [Slovenian](../sl/README.md) |

> **Note:**
> These translations were automatically generated using the open-source [co-op-translator](https://github.com/Azure/co-op-translator) and may contain errors or inaccuracies. For critical information, it is recommended to refer to the original or consult a professional human translation. If you'd like to add or update a translation, please refer to the [co-op-translator](https://github.com/Azure/co-op-translator) repository, where you can easily contribute using simple commands.
```

## 지원 언어

아래 표는 **Co-op Translator**가 현재 지원하는 언어를 나열합니다. 여기에는 언어 코드, 언어 이름 및 각 언어와 관련된 알려진 문제가 포함됩니다. 새로운 언어 지원을 추가하려면 `font_language_mappings.yml` file located at `src/co_op_translator/fonts/` and submit a pull request after testing.

| Language Code | Language Name        | Font                              | RTL Support | Known Issues |
|---------------|----------------------|-----------------------------------|-------------|--------------|
| en            | English              | NotoSans-Medium.ttf               | No          | No           |
| fr            | French               | NotoSans-Medium.ttf               | No          | No           |
| es            | Spanish              | NotoSans-Medium.ttf               | No          | No           |
| de            | German               | NotoSans-Medium.ttf               | No          | No           |
| ru            | Russian              | NotoSans-Medium.ttf               | No          | No           |
| ar            | Arabic               | NotoSansArabic-Medium.ttf         | Yes         | Yes          |
| fa            | Persian (Farsi)      | NotoSansArabic-Medium.ttf         | Yes         | Yes          |
| ur            | Urdu                 | NotoSansArabic-Medium.ttf         | Yes         | Yes          |
| zh            | Chinese (Simplified) | NotoSansCJK-Medium.ttc            | No          | No           |
| mo            | Chinese (Traditional, Macau) | NotoSansCJK-Medium.ttc           | No          | No           |
| hk            | Chinese (Traditional, Hong Kong) | NotoSansCJK-Medium.ttc           | No          | No           |
| tw            | Chinese (Traditional, Taiwan) | NotoSansCJK-Medium.ttc           | No          | No           |
| ja            | Japanese             | NotoSansCJK-Medium.ttc            | No          | No           |
| ko            | Korean               | NotoSansCJK-Medium.ttc            | No          | No           |
| hi            | Hindi                | NotoSansDevanagari-Medium.ttf     | No          | No           |
| bn            | Bengali              | NotoSansBengali-Medium.ttf        | No          | No           |
| mr            | Marathi              | NotoSansDevanagari-Medium.ttf     | No          | No           |
| ne            | Nepali               | NotoSansDevanagari-Medium.ttf     | No          | No           |
| pa            | Punjabi (Gurmukhi)   | NotoSansGurmukhi-Medium.ttf       | No          | No           |
| pt            | Portuguese           | NotoSans-Medium.ttf               | No          | No           |
| it            | Italian              | NotoSans-Medium.ttf               | No          | No           |
| pl            | Polish               | NotoSans-Medium.ttf               | No          | No           |
| tr            | Turkish              | NotoSans-Medium.ttf               | No          | No           |
| el            | Greek                | NotoSans-Medium.ttf               | No          | No           |
| th            | Thai                 | NotoSansThai-Medium.ttf           | No          | No           |
| sv            | Swedish              | NotoSans-Medium.ttf               | No          | No           |
| da            | Danish               | NotoSans-Medium.ttf               | No          | No           |
| no            | Norwegian            | NotoSans-Medium.ttf               | No          | No           |
| fi            | Finnish              | NotoSans-Medium.ttf               | No          | No           |
| nl            | Dutch                | NotoSans-Medium.ttf               | No          | No           |
| he            | Hebrew               | NotoSansHebrew-Medium.ttf         | Yes         | No           |
| vi            | Vietnamese           | NotoSans-Medium.ttf               | No          | No           |
| id            | Indonesian           | NotoSans-Medium.ttf               | No          | No           |
| ms            | Malay                | NotoSans-Medium.ttf               | No          | No           |
| tl            | Tagalog (Filipino)   | NotoSans-Medium.ttf               | No          | No           |
| sw            | Swahili              | NotoSans-Medium.ttf               | No          | No           |
| hu            | Hungarian            | NotoSans-Medium.ttf               | No          | No           |
| cs            | Czech                | NotoSans-Medium.ttf               | No          | No           |
| sk            | Slovak               | NotoSans-Medium.ttf               | No          | No           |
| ro            | Romanian             | NotoSans-Medium.ttf               | No          | No           |
| bg            | Bulgarian            | NotoSans-Medium.ttf               | No          | No           |
| sr            | Serbian (Cyrillic)   | NotoSans-Medium.ttf               | No          | No           |
| hr            | Croatian             | NotoSans-Medium.ttf               | No          | No           |
| sl            | Slovenian            | NotoSans-Medium.ttf               | No          | No           |

### Adding a new language

To add support for a new language:

1. Go to [src/co_op_translator/fonts/font_language_mappings.yml](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/fonts/font_language_mappings.yml).
2. Add the language code, name, and appropriate font file name. Make sure to include the `rtl` attribute if the language is right-to-left.
3. If you need to use a new font, ensure that the font is free to use in open-source projects by checking its licensing and copyright terms. After verifying, add the font file to the `src/co_op_translator/fonts/` 디렉토리에 해당 언어 코드, 이름 및 적절한 글꼴을 추가하세요.
4. 새로운 언어가 제대로 지원되는지 로컬에서 테스트하세요.
5. 변경 사항을 포함한 Pull Request를 제출하고 PR 설명에 새로운 언어 추가를 명시하세요.

예시:

```yaml
new_lang:
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

## 저장소 구조

- **src/co_op_translator/**: 번역기 소스 코드.
- **getting_started/**: 시작하기 위한 가이드 및 튜토리얼.
- **imgs/**: 문서에 사용된 이미지.
- **tests/**: 프로젝트의 테스트 케이스.
- **data/**: 데이터 파일 포함.

## 기여

이 프로젝트는 기여와 제안을 환영합니다. Azure Co-op Translator에 기여하고 싶으신가요? Co-op Translator를 더 접근 가능하게 만드는 방법에 대한 가이드라인은 [CONTRIBUTING.md](./CONTRIBUTING.md)를 참조하세요.

## 기여자

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## 행동 강령

이 프로젝트는 [Microsoft 오픈 소스 행동 강령](https://opensource.microsoft.com/codeofconduct/)을 채택했습니다.
자세한 내용은 [행동 강령 FAQ](https://opensource.microsoft.com/codeofconduct/faq/)를 참조하세요.
추가 질문이나 의견이 있으시면 [opencode@microsoft.com](mailto:opencode@microsoft.com)으로 연락해 주세요.

## 책임 있는 AI

Microsoft는 고객이 AI 제품을 책임감 있게 사용할 수 있도록 돕고, 학습 내용을 공유하며, 투명성 노트 및 영향 평가 도구를 통해 신뢰 기반의 파트너십을 구축하는 데 전념하고 있습니다. 이러한 리소스의 대부분은 [https://aka.ms/RAI](https://aka.ms/RAI)에서 찾을 수 있습니다.
Microsoft의 책임 있는 AI 접근 방식은 공정성, 신뢰성 및 안전성, 프라이버시 및 보안, 포용성, 투명성, 책임이라는 AI 원칙에 기반을 두고 있습니다.

이 샘플에서 사용된 것과 같은 대규모 자연어, 이미지, 음성 모델은 불공정하거나 신뢰할 수 없거나 불쾌한 방식으로 작동할 수 있으며, 이로 인해 피해가 발생할 수 있습니다. 위험과 제한 사항에 대해 알고 싶다면 [Azure OpenAI 서비스 투명성 노트](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text)를 참조하세요.

이러한 위험을 완화하는 권장 방법은 유해한 행동을 감지하고 방지할 수 있는 안전 시스템을 아키텍처에 포함하는 것입니다. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview)는 독립적인 보호 계층을 제공하여 애플리케이션 및 서비스에서 사용자가 생성한 콘텐츠와 AI가 생성한 콘텐츠를 감지할 수 있습니다. Azure AI Content Safety에는 유해한 자료를 감지할 수 있는 텍스트 및 이미지 API가 포함되어 있습니다. 또한 다양한 모달리티에서 유해한 콘텐츠를 감지하는 샘플 코드를 보고 탐색하고 시도해 볼 수 있는 인터랙티브한 Content Safety Studio도 제공됩니다. 다음 [빠른 시작 문서](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest)를 통해 서비스에 요청하는 방법을 안내받을 수 있습니다.

또 다른 고려 사항은 전체 애플리케이션 성능입니다. 다중 모달 및 다중 모델 애플리케이션의 경우 성능이란 시스템이 예상대로 작동하고 유해한 출력을 생성하지 않는 것을 의미합니다. [생성 품질 및 위험 및 안전 메트릭](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in)을 사용하여 전체 애플리케이션의 성능을 평가하는 것이 중요합니다.

개발 환경에서 [prompt flow SDK](https://microsoft.github.io/promptflow/index.html)를 사용하여 AI 애플리케이션을 평가할 수 있습니다. 테스트 데이터 세트나 타겟을 제공하면 내장 평가자 또는 선택한 맞춤 평가자를 통해 생성 AI 애플리케이션의 생성물이 정량적으로 측정됩니다. 시스템 평가를 위해 prompt flow sdk를 시작하려면 [빠른 시작 가이드](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk)를 따르세요. 평가 실행을 완료하면 [Azure AI Studio에서 결과를 시각화할 수 있습니다](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## 상표

이 프로젝트에는 프로젝트, 제품 또는 서비스의 상표나 로고가 포함될 수 있습니다. Microsoft 상표나 로고의 허가된 사용은 [Microsoft의 상표 및 브랜드 가이드라인](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general)을 따라야 합니다.
이 프로젝트의 수정된 버전에서 Microsoft 상표나 로고를 사용하는 경우 혼동을 일으키거나 Microsoft 후원을 암시해서는 안 됩니다.
제3자의 상표나 로고 사용은 해당 제3자의 정책을 따릅니다.

**면책 조항**:
이 문서는 기계 기반 AI 번역 서비스를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하지만, 자동 번역에는 오류나 부정확성이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어가 권위 있는 자료로 간주되어야 합니다. 중요한 정보에 대해서는 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인한 오해나 오역에 대해서는 책임을 지지 않습니다.