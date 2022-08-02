# import sys
"""
* import readline 유무에 따라  input() 함수 동작에 영향미침.
https://stackoverflow.com/questions/45772230/arrow-keys-not-working-while-entering-data-for-input-function
* input()은 파이썬 기본 빌트인 함수
https://docs.python.org/3/library/functions.html#input

"""
import os
import readline
import awswrangler as wr
import pandas as pd


def get_local_parq(parq_path):
    df = 1
    return df


def get_s3_parq(parq_path):
    """parquet 파일 읽기 테스트

    Note:
        s3 버킷 링크로 parquet를 바로 가져와 읽을 수 있다.
        parquet 다룰 때 s3는 awswrangler, 일반적으로 pandas를 활용가능

    Args:
        parq_path (str): 's3://버킷명/경로/경로/~~~'
    """
    print('***Loading Parquet From : '+parq_path)
    df = wr.s3.read_parquet(
        path=parq_path
    )
    return df


def write_s3_uri():
    """S3 URI 입력"""
    uri = input('***Write S3 URI: ')
    return uri


def parse_cmd(input_):
    # TODO: max_rows, max_columns 값 입력으로 변경
    cmd = input_
    if cmd == '1':
        cmd = "pd.set_option('display.max_rows', None)"
    if cmd == '2':
        cmd = "pd.set_option('display.max_columns', None)"
    if cmd == '3':
        cmd = "pd.set_option('display.max_rows', 60)"
    if cmd == '4':
        cmd = "pd.set_option('display.max_columns', 0)"
    return cmd


def show_how_to_use():
    # TODO: TEXT 파일 따로 빼기
    print('\n===============How to Use================')
    print('종료 : quit() or Ctrl+C')
    print('==========Command Example==========')

    print("1: pd.set_option('display.max_rows', None)")
    print("2: pd.set_option('display.max_columns', None)")
    print("3: pd.set_option('display.max_rows', 60)")
    print("4: pd.set_option('display.max_columns', 0)")

    print('df')
    print('df.dtypes')
    print("df['logtype']")
    print("df['logtype'].unique()")
    print("df.drop(columns=['logtype'])")
    print("df[df['logtype']=='name']")
    print('=========================================\n')
