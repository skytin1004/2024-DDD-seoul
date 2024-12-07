# Co Op Translator에 기여하기

이 프로젝트는 기여와 제안을 환영합니다. 대부분의 기여는 Contributor License Agreement (CLA)에 동의해야 합니다. CLA는 당신이 기여할 권리가 있고, 실제로 그렇게 한다는 것을 선언하는 것입니다. 자세한 내용은 https://cla.opensource.microsoft.com을 참조하세요.

풀 리퀘스트를 제출하면, CLA 봇이 자동으로 CLA 제공이 필요한지 여부를 결정하고 PR에 적절하게 표시합니다 (예: 상태 확인, 댓글). 봇이 제공하는 지침을 따르기만 하면 됩니다. 이는 모든 리포지토리에 대해 한 번만 하면 됩니다.

## 개발 환경 설정

이 프로젝트의 개발 환경을 설정하려면 종속성 관리를 위해 Poetry를 사용하는 것이 좋습니다. 프로젝트 종속성 관리를 위해 `pyproject.toml`를 사용하므로 종속성을 설치하려면 Poetry를 사용해야 합니다.

### 가상 환경 생성

#### pip 사용

```bash
python -m venv .venv
```

#### Poetry 사용

```bash
poetry init
```

### 가상 환경 활성화

#### pip 및 Poetry 모두에 해당

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Poetry 사용

```bash
poetry shell
```

### 패키지 및 필요한 패키지 설치

#### Poetry 사용 (pyproject.toml에서)

```bash
poetry install
```

### 환경 변수

1. `.env` file in the root directory by copying the provided `.env.template` file.
1. Fill in the environment variables as guided.

> [!TIP]
>
> ### Additional development environment options
>
> In addition to running the project locally, you can also use GitHub Codespaces or VS Code Dev Containers for an alternative development environment setup.
>
> #### GitHub Codespaces
>
> You can run this samples virtually by using GitHub Codespaces and no additional settings or setup are required. 
>
> The button will open a web-based VS Code instance in your browser:
>
> 1. Open the template (this may take several minutes):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Running Locally using VS Code Dev Containers
>
> ⚠️ This option will only work if your Docker Desktop is allocated at least 16 GB of RAM. If you have less than 16 GB of RAM, you can try the [GitHub Codespaces option](../..) or [set it up locally](../..).
>
> A related option is VS Code Dev Containers, which will open the project in your local VS Code using the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Start Docker Desktop (install it if not already installed)
> 2. Open the project:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)

## Running Co Op Translator

To run Co Op Translator using Poetry in your environment, follow these steps:

1. Navigate to the directory where you want to perform translation tests or create a temporary folder for testing purposes.

2. Execute the following command. Replace `-l ko` with the language code you wish to translate into. The `-d` 플래그는 디버그 모드를 나타냅니다.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> 명령을 실행하기 전에 Poetry 환경이 활성화되어 있는지 (poetry shell) 확인하세요.

## 유지 관리자

### 커밋 메시지 및 병합 전략

프로젝트의 커밋 기록의 일관성과 명확성을 유지하기 위해 **Squash and Merge** 전략을 사용할 때 최종 커밋 메시지 형식을 따릅니다.

풀 리퀘스트 (PR)가 병합될 때, 개별 커밋은 하나의 커밋으로 합쳐집니다. 최종 커밋 메시지는 깨끗하고 일관된 기록을 유지하기 위해 아래 형식을 따라야 합니다.

#### 커밋 메시지 형식 (squash and merge용)

커밋 메시지에 다음 형식을 사용합니다:

```bash
<type>: <description> (#<PR number>)
```

- **type**: 커밋의 카테고리를 지정합니다. 다음과 같은 타입을 사용합니다:
  - `Docs`: For documentation updates.
  - `Build`: For changes to the build system or dependencies.
  - `Translator`: For changes affecting the translation logic or features.

- **description**: A concise summary of the change.
- **PR number**: The number of the pull request associated with the commit.

**Examples**:

- `Docs: 설치 지침을 명확하게 업데이트 (#50)`
- `Translator: 이미지 번역 처리 개선 (#60)`

> [!NOTE]
> Currently, the Docs, Translator, and Build prefixes are automatically added to PR titles based on the labels applied to the modified source code. As long as the correct label is applied, you typically don't need to manually update the PR title. You just need to verify that everything is correct and the prefix has been generated appropriately.

#### Merge strategy

We use **Squash and Merge** as our default strategy for pull requests. This strategy ensures that commit messages follow our format, even if individual commits don't.

**Reasons**:

- A clean, linear project history.
- Consistency in commit messages.
- Reduced noise from minor commits (e.g., "fix typo").

When merging, ensure the final commit message follows the commit message format described above.

**Example of Squash and Merge**
If a PR contains the following commits:

- `오타 수정`
- `README 업데이트`
- `형식 조정`

They should be squashed into:
`Docs: 문서 명확성 및 형식 개선 (#65)`

**면책 조항**:
이 문서는 기계 기반 AI 번역 서비스를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있지만, 자동 번역에는 오류나 부정확한 부분이 있을 수 있습니다. 원본 문서는 해당 언어로 작성된 원본을 권위 있는 자료로 간주해야 합니다. 중요한 정보에 대해서는 전문적인 인간 번역을 권장합니다. 이 번역을 사용함으로 인해 발생하는 오해나 잘못된 해석에 대해서는 책임을 지지 않습니다.