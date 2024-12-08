# Co-op 번역기 패키지 설치하기

**Co-op Translator**는 프로젝트 내 모든 마크다운 파일과 이미지를 여러 언어로 번역하는 데 도움을 주기 위해 설계된 명령줄 인터페이스(CLI) 도구입니다. 이 튜토리얼은 번역기를 설정하고 다양한 사용 사례에 맞게 실행하는 방법을 안내합니다.

### 가상 환경 만들기

가상 환경은 `pip` 또는 `Poetry`을 사용하여 만들 수 있습니다. 터미널에서 다음 명령어 중 하나를 입력하세요.

#### pip 사용하기

```bash
python -m venv .venv
```

#### Poetry 사용하기

```bash
poetry init
```

### 가상 환경 활성화하기

가상 환경을 만든 후에는 이를 활성화해야 합니다. 운영 체제에 따라 단계가 다릅니다. 터미널에서 다음 명령어를 입력하세요.

#### pip 및 Poetry 모두에 해당

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Poetry 사용하기

1. 환경을 Poetry로 만들었다면, 터미널에서 다음 명령어를 입력하여 활성화하세요.

    ```bash
    poetry shell
    ```

### 패키지 및 필요한 패키지 설치하기

가상 환경이 설정되고 활성화되면 다음 단계는 필요한 종속성을 설치하는 것입니다.

#### pip 사용하기 (requirements.txt에서)

1. pip을 사용 중이라면, 터미널에서 다음 명령어를 입력하세요. `requirements.txt` 파일에 지정된 필수 패키지가 자동으로 설치됩니다:

    ```bash
    pip install -r requirements.txt
    ```

#### Poetry 사용하기 (pyproject.toml에서)

1. Poetry를 사용 중이라면, 터미널에서 다음 명령어를 입력하세요. `pyproject.toml` 파일에 지정된 필수 패키지가 자동으로 설치됩니다:

    ```bash
    poetry install
    ```
