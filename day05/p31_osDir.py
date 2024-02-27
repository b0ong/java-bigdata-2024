# file: p32_osDir.py
# desc: 운영체제 디렉토리 확인

import os # OS에서 필요한 모듈

def search(dirName):
    try:
        fileNames = os.listdir(dirName) # 결과는 list
        for filename in fileNames:
            fullname = os.path.join(dirName, filename)  #str
            if os.path.isdir(fullname):
                search(fullname) # 재귀호출
            else:
                ext = os.path.splitext(fullname)[-1] # tuple의 제일 뒤의 값 srt
                if ext == '.py':    # 파이썬 파일만 출력 
                    with open(fullname, mode = 'r', encoding='utf-8') as fp: # with로 파일을 열면 close()필요없음
                        print(f'파일명: {fullname}, 라인수: {len(fp.readlines())}줄')
    except PermissionError as e:   # 접근제한이  없을때
        print('접근제한이 없습니다.', e.args)     
        
if __name__ == '__main__': # main entry
    search('/Users/hangugjin/Documents/source/java-bigdata-2024') #OS 드라이브 경로에서 \는 되도록 쓰지말것
    
    
    