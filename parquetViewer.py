# import sys
import os
import pdb
import awswrangler as wr
import pandas as pd

def read_parq(parq_path):
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


def write_uri():
    """S3 URI 입력"""
    uri = input('***Write S3 URI: ')
    return uri


def show_how_to_use():
    # TODO: how to use
    print('\n\n===============How to Use================')
    print('종료 : quit() or Ctrl+C')
    print('==========Command Example==========')
    print('df')
    print("pd.set_option('display.max_rows', None)")
    print("pd.set_option('display.max_columns', None)")
    print('df.dtypes')
    print("df['logtype']")
    print("df['logtype'].unique()")
    print("df.drop(columns=['logtype'])")
    print("df[df['logtype']=='name']")
    print('===================================')


if __name__ == '__main__':
    path = write_uri()
    df = read_parq(path)

    show_how_to_use()
    while True:
        cmd = input('(python_cli) ')
        os.system('clear')

        show_how_to_use()
        exec(f'print({cmd})')