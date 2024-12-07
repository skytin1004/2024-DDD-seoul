# Azure 리소스 설정 가이드

이 가이드는 Co-op Translator를 사용하기 위해 필요한 Azure 리소스를 설정하는 단계를 안내합니다. Azure Computer Vision 리소스와 Azure OpenAI 리소스를 생성하여 패키지에 필요한 번역 기능을 제공합니다.

### Azure 계정 만들기

Azure 계정이 아직 없으면 하나 만들어야 합니다.

1. **[Azure 가입](https://azure.microsoft.com/free/) 페이지로 이동합니다.**
2. **무료로 Azure 체험하기** 또는 **종량제**를 선택합니다.
3. **화면의 지시에 따라** 계정을 만듭니다.
   - 개인 정보 및 연락처 정보를 제공합니다.
   - **인증:** 신용카드나 전화번호를 사용하여 신원을 인증해야 합니다.

### Azure Computer Vision 리소스 생성

1. [Azure 포털](https://portal.azure.com/)에 로그인합니다.

1. 포털 페이지 상단의 **검색창**에 *computer vision*을 입력하고 나타나는 옵션 중 **Computer vision**을 선택합니다.

    ![Type computervision.](../../../translated_images/type-computervision.53c5d62331dd354ee612410f6365a6ecb5b2245cf56adc85c42b67f87639acbd.ko.png)

1. 탐색 메뉴에서 **+ 생성**을 선택합니다.

    ![Select create.](../../../translated_images/create-computervision.4af3f8309deac22c0f927b99c901afb5676345d520a026b5132ccd3eaad23c20.ko.png)

1. 다음 작업을 수행합니다:

    - Azure **구독**을 선택합니다.
    - 사용할 **리소스 그룹**을 선택합니다 (필요 시 새로 만듭니다).
    - 사용할 **지역**을 선택합니다.
    - **이름**을 입력합니다. 고유한 값이어야 합니다.
    - 사용할 **가격 책정 계층**을 선택합니다.

    ![Fill computer vision.](../../../translated_images/fill-computervision.41df3ec7184fba682a1b71482438ce8ed4ab800b62261ff36c09c5f4d76a1f1a.ko.png)

1. **검토 + 생성**을 선택합니다.

1. **생성**을 선택합니다.

### Azure OpenAI 리소스 생성

1. 포털 페이지 상단의 **검색창**에 *azure openai*를 입력하고 나타나는 옵션 중 **Azure OpenAI**를 선택합니다.

    ![Type Azure OpenAI.](../../../translated_images/type-azure-openai.c4498b10e42cd469c63c4a0dfc770d902af6e013fd3ec464c665b1b7abaf0b82.ko.png)

1. 탐색 메뉴에서 **+ 생성**을 선택합니다.

    ![Create Azure OpenAI.](../../../translated_images/create-azure-openai.07b88dd4b12c4faf758fc7c4eba9cfad32545bde73ddbd9b851f1ce47ab85a8b.ko.png)

1. 다음 작업을 수행합니다:

    - Azure **구독**을 선택합니다.
    - 사용할 **리소스 그룹**을 선택합니다 (필요 시 새로 만듭니다).
    - 사용할 **지역**을 선택합니다.
    - **이름**을 입력합니다. 고유한 값이어야 합니다.
    - 사용할 **가격 책정 계층**을 선택합니다.

    ![Fill Azure OpenAI.](../../../translated_images/fill-azureopenai.5974b1d8669c77babe536ee1dbfd4fa52f37f101bd717fa3a14be656137ecdf1.ko.png)

1. **다음**을 선택하여 **네트워크** 페이지로 이동합니다.

1. 사용할 네트워크 보안 **유형**을 선택합니다.

    ![Select a network security Type.](../../../translated_images/select-azureopenai-security-type.ba07acc6850ffcb1c4e84b6e2bbc046bfc7c60fb0dc51d7958ac83220f90f4e9.ko.png)

1. **다음**을 선택하여 **태그** 페이지로 이동합니다.

1. **다음**을 선택하여 **검토 + 제출** 페이지로 이동합니다.

1. **생성**을 선택합니다.

    ![Select Create.](../../../translated_images/create-azure-openai-complete.bb085da609fd5b6fda0d20dacaacfcabf245733b70804ef12bf961cb9278c204.ko.png)

### Azure OpenAI 모델 배포

1. 생성한 Azure OpenAI 리소스로 이동합니다.

1. 탐색 메뉴에서 **Azure OpenAI Studio로 이동**을 선택합니다.

    ![Select Go to Azure OpenAI Studio from the navigation menu.](../../../translated_images/go-to-azureopenai-studio.d3b1046f1dac14e0f9656eaf76cd37bd52d862c6172858bc4ac2148a69b5a752.ko.png)

1. Azure OpenAI Studio에서 왼쪽 탭의 **배포**를 선택합니다.
1. 탐색 메뉴에서 **+ 모델 배포**를 선택합니다.
1. 탐색 메뉴에서 **기본 모델 배포**를 선택하여 새 **gpt-4o** 배포를 만듭니다.

    ![Select Deployments.](../../../translated_images/deploy-aoai.a3ba46ef4f458fe1b379bf3e7a1e477e0491dbca5dfdaa43e71e555646fed341.ko.png)

1. 다음 작업을 수행합니다:

    - **모델 선택** 페이지에서 **gpt-4o**를 선택합니다.
    - **확인**을 선택하여 **모델 gpt-4o 배포** 페이지로 이동합니다.
    - **모델 gpt-4o 배포** 페이지에서 **배포 이름**을 입력합니다. 고유한 값이어야 합니다. 예를 들어, **gpt-4o**.
    - **모델 gpt-4o 배포** 페이지에서 사용할 **배포 유형**을 선택합니다.

    ![Create model.](../../../translated_images/create-4o.ec82f901305121716caa773d5e77f906263ef9ed42aae4146134f83cc7dbeb40.ko.png)

1. **배포**를 선택합니다.

**면책 조항**:
이 문서는 기계 기반 AI 번역 서비스를 사용하여 번역되었습니다. 우리는 정확성을 위해 노력하지만, 자동 번역에는 오류나 부정확성이 포함될 수 있음을 유의하시기 바랍니다. 원본 문서의 원어를 권위 있는 자료로 간주해야 합니다. 중요한 정보에 대해서는 전문적인 인간 번역을 권장합니다. 이 번역을 사용하여 발생하는 오해나 오역에 대해 당사는 책임을 지지 않습니다.