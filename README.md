# parquet_experiment_for_aws_s3

0. 사용법 및 기능
- parquetStarter.sh로 시작
- AWS S3에 저장된 parquet 파일의 URI를 입력하면 다운로드 후 변수 df에 dataframe 형태로 저장
- 이후 python cli 활성화되고 거기서 각종 테스트 가능
끝.

1. 실험용 목적
- 파이썬 환경에서 parquet, pandas 익숙해지기 위한 parquet viewer, tester
- dataframe 관련 syntax가 항상 미묘하게 헷갈린다.
- 그 때 마다 구글검색이나 breakpoint()걸어서 테스트해보기 귀찮다.

2. 업무용 목적
- S3의 parquet 파일을 빠르게 조회
- parquet 파일 하나 보기 위해 Jupyter를 켜고싶지 않다.
- 별도창으로 가볍게 열어보고 싶다.
- 간단한 디버깅이나 유닛테스트를 하기 위해 breakpoint()대신 활용

3. 기타
- 초스피드 개발
- 향후 GUI 기반 실행파일로 만들고 싶다.
- 하지만 실험용, 업무용으로 빠르게 사용하기 위한 것이므로 일단 보류
- 그 시간에 차라리 상용툴을 사는게 낫다.

4. 요구사항 및 초스피드 세팅
- Ubuntu에서 개발
- Windows에서 사용하려면, 다음과 같은 수정 필요
  - parquetStarter.sh => parquetStarter.cmd
  - parquetViewer.py에서 import readline 삭제
- 공통
  * python3
    - awswrangler
    - pandas
    - awscli 설치 후 aws congifure 에서 인증설정 되어있어야 함

