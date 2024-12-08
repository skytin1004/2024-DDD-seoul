# Co-op Translator를 사용하여 프로젝트 번역하기

**Co-op Translator**는 명령줄 인터페이스(CLI) 도구로, 프로젝트의 마크다운 파일과 이미지 파일을 여러 언어로 번역할 수 있도록 도와줍니다. 이 섹션에서는 도구 사용 방법, 다양한 CLI 옵션, 그리고 여러 사용 사례에 대한 예제를 설명합니다.

## CLI 옵션 개요

**Co-op Translator** CLI는 번역 프로세스를 사용자 맞춤형으로 설정할 수 있는 여러 옵션을 제공합니다:

- **`-l` (또는 `--language-codes`)**: 번역할 언어 코드의 공백으로 구분된 목록 (예: `"es fr de"`는 스페인어, 프랑스어, 독일어). 모든 지원 언어로 번역하려면 `"all"`를 사용하세요.
- **`-r` (또는 `--root-dir`)**: 프로젝트의 루트 디렉터리를 지정합니다 (기본값은 현재 디렉터리).
- **`-a` (또는 `--add`)**: 기존 번역을 삭제하지 않고 새로운 번역을 추가합니다 (기본 동작).
- **`-u` (또는 `--update`)**: 기존 번역을 삭제하고 다시 생성하여 번역을 업데이트합니다. **경고**: 현재 번역이 모두 삭제됩니다.
- **`-img` (또는 `--images`)**: 이미지 파일만 번역합니다.
- **`-md` (또는 `--markdown`)**: 마크다운 파일만 번역합니다.
- **`-chk` (또는 `--check`)**: 번역된 파일의 오류를 확인하고 필요 시 번역을 다시 시도합니다.
- **`-d` (또는 `--debug`)**: 디버그 모드를 활성화하여 자세한 로그를 기록합니다.

---

## 예제 시나리오 및 명령어

다음은 **Co-op Translator**의 일반적인 사용 사례와 해당 명령어입니다.

### 1. 기본 번역 (단일 언어)

프로젝트 전체(마크다운 파일 및 이미지)를 한 언어로 번역하려면, 예를 들어 한국어로 번역하려면 다음 명령어를 사용하세요:

```bash
translate -l "ko"
```

이 명령어는 모든 마크다운 및 이미지 파일을 한국어로 번역하며, 기존 번역을 삭제하지 않고 새로운 번역을 추가합니다.

> [!TIP]
>
> **Co-op Translator**에서 사용할 수 있는 언어 코드를 확인하고 싶으신가요? 자세한 내용은 저장소의 [지원 언어](https://github.com/Azure/co-op-translator#supported-languages) 섹션을 방문하세요.

#### Phi-3 CookBook 예제

**Phi-3 CookBook**에서는 기존 마크다운 파일과 이미지를 한국어로 번역하기 위해 다음 방법을 사용했습니다.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. 여러 언어로 번역하기

프로젝트를 여러 언어로 번역하려면 (예: 스페인어, 프랑스어, 독일어), 다음 명령어를 사용하세요:

```bash
translate -l "es fr de"
```

이 명령어는 프로젝트를 스페인어, 프랑스어, 독일어로 번역하며, 기존 번역을 덮어쓰지 않고 새로운 번역을 추가합니다.

#### Phi-3 CookBook 예제

**Phi-3 CookBook**에서 최신 커밋을 반영한 후, 새로 추가된 마크다운 파일과 이미지를 번역하기 위해 다음 방법을 사용했습니다.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> 일반적으로 한 번에 한 언어씩 번역하는 것이 권장되지만, 이와 같은 특정 변경 사항을 추가해야 하는 경우에는 여러 언어를 한 번에 번역하는 것이 효율적일 수 있습니다.

### 3. 루트 디렉터리 지정

기본적으로 번역기는 현재 작업 디렉터리를 사용합니다. 프로젝트가 다른 곳에 위치해 있다면, -r 옵션을 사용하여 루트 디렉터리를 지정하세요:

```bash
translate -l "es fr de" -r "./my_project"
```

이 명령어는 `./my_project` 디렉터리의 파일을 스페인어, 프랑스어, 독일어로 번역합니다.

### 4. 기존 번역을 삭제하지 않고 새로운 번역 추가

기본 동작은 기존 번역을 삭제하지 않고 새로운 번역을 추가하는 것입니다. `-a` 옵션을 명시적으로 지정하여 이를 확인할 수 있습니다:

```bash
translate -l "ko" -a
```

이 명령어는 기존 번역에 영향을 주지 않고 한국어로 새로운 번역을 추가합니다.

#### Phi-3 CookBook 예제

**Phi-3 CookBook**에서 *README.md* 번역을 업데이트하기 위해, 먼저 기존 *README.md* 번역을 삭제한 후, 다음 방법을 사용하여 업데이트된 내용을 번역했습니다.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

### 5. 번역 업데이트 (기존 번역 삭제)

기존 번역을 삭제하고 새로운 번역으로 교체하려면 `-u` 옵션을 사용하세요. 이 옵션은 지정된 언어의 기존 번역을 모두 삭제하고 다시 번역합니다.

```bash
translate -l "ko" -u
```

경고: 이 명령어는 기존 번역을 삭제하기 전에 확인을 요청합니다.

#### Phi-3 CookBook 예제

**Phi-3 CookBook**에서는 모든 스페인어 번역 파일을 업데이트하기 위해 다음 방법을 사용했습니다. 여러 마크다운 문서의 원본 내용에 큰 변화가 있을 때 이 방법을 사용하는 것이 좋습니다. 번역할 마크다운 파일이 몇 개만 있는 경우, 특정 파일을 수동으로 삭제한 후 `-a` 방법을 사용하여 업데이트된 번역을 추가하는 것이 더 효율적입니다.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 6. 이미지 파일만 번역하기

프로젝트의 이미지 파일만 번역하려면 `-img` 옵션을 사용하세요:

```bash
translate -l "ko" -img
```

이 명령어는 마크다운 파일에는 영향을 주지 않고 이미지 파일만 한국어로 번역합니다.

### 7. 마크다운 파일만 번역하기

프로젝트의 마크다운 파일만 번역하려면 `-md` 옵션을 사용하세요:

```bash
translate -l "ko" -md
```

### 8. 번역된 파일의 오류 확인

번역된 파일의 오류를 확인하고 필요 시 번역을 다시 시도하려면 `-chk` 옵션을 사용하세요:

```bash
translate -l "ko" -chk
```

이 명령어는 번역된 마크다운 파일을 스캔하고 오류가 있는 파일을 다시 번역합니다.

#### Phi-3 CookBook 예제

**Phi-3 CookBook**에서는 한국어 파일의 번역 오류를 확인하고, 오류가 있는 파일을 자동으로 다시 번역하기 위해 다음 방법을 사용했습니다.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

이 옵션은 번역 오류를 확인합니다. 현재는 원본 파일과 번역된 파일의 줄 바꿈 차이가 6개 이상인 경우 번역 오류로 간주됩니다. 향후에는 더 큰 유연성을 위해 이 기준을 개선할 계획입니다.

예를 들어, 이 방법은 누락된 부분이나 손상된 번역을 감지하는 데 유용하며, 해당 파일을 자동으로 다시 번역합니다.

그러나 이미 어떤 파일이 문제인지 알고 있다면, 해당 파일을 수동으로 삭제하고 `-a` 옵션을 사용하여 다시 번역하는 것이 더 효율적입니다.

### 9. 디버그 모드

문제 해결을 위해 자세한 로그를 기록하려면 `-d` 옵션을 사용하세요:

```bash
translate -l "ko" -d
```

이 명령어는 번역을 디버그 모드에서 실행하여 번역 과정에서 발생하는 문제를 식별하는 데 도움이 되는 추가 로그 정보를 제공합니다.

#### Phi-3 CookBook 예제

**Phi-3 CookBook**에서는 마크다운 파일에 많은 링크가 포함된 번역이 형식 오류를 일으키는 문제를 겪었습니다. 예를 들어, 번역이 깨지거나 줄 바꿈이 무시되는 경우가 있었습니다. 이 문제를 진단하기 위해 `-d` 옵션을 사용하여 번역 과정이 어떻게 작동하는지 확인했습니다.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 10. 모든 언어로 번역하기

프로젝트를 모든 지원 언어로 번역하려면 all 키워드를 사용하세요.

> [!WARNING]
> 모든 언어를 한 번에 번역하는 것은 프로젝트 크기에 따라 상당한 시간이 걸릴 수 있습니다. 예를 들어, **Phi-3 CookBook**을 스페인어로 번역하는 데 약 2시간이 걸렸습니다. 규모를 고려할 때, 한 사람이 20개 언어를 처리하는 것은 현실적이지 않습니다. 여러 기여자가 각자 한두 개의 언어를 관리하고 번역을 점진적으로 업데이트하는 것이 좋습니다.

```bash
translate -l "all"
```

이 명령어는 프로젝트를 모든 지원 언어로 번역합니다. 진행할 경우 프로젝트 크기에 따라 번역에 상당한 시간이 걸릴 수 있습니다.
