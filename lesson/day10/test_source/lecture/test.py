'''
특정 디렉터리에서 txt 파일만 읽기
 1. os.listdir() 이용 : 전체 읽기
 2. os.path.isfile(path) : 파일만 선정
 3. read() : txt 파일의 문장만 추출
'''

import os # dir or file path

print(os.getcwd())
txt_data = 'C:/workspace/python_basic/test/txt_data'

# 지정한 폴더의 목록(file or dir)을 하나씩 넘김
sub_dir = os.listdir(txt_data) # movie 파일 목록 반환
print("sub_dir :",sub_dir) # ['first', 'second']


def textPro(sub_dir): # ['first', 'second']
    first_txt = []  # first 디렉터리 텍스트 저장
    second_txt = []  # second 디렉터리 텍스트 저장

    # 디렉터리 구성
    for sdir in sub_dir : # ['first', 'second']
        dirname = txt_data + "/" + sdir
        print("dirname :", dirname)
        file_list = os.listdir(dirname)  # first dir 파일 목록 반환

        # 파일 구성
        for fname in file_list:
            file_path = dirname + '/' + fname # 디렉터리/파일 or 디렉터리

            # file 선택
            if os.path.isfile(file_path) :
                try :
                    file = open(file_path, 'r', encoding="UTF-8")
                    if sdir == 'first':
                        first_txt.append(file.read())
                    else :
                        second_txt.append(file.read())
                except Exception as e:
                    print('예외발생 :', e)
                finally:
                    file.close()
            else:
                print(f'{file_path}는 파일이 아니고 디렉터리이므로 제외함')

    return first_txt, second_txt

first_txt, second_txt = textPro(sub_dir) # ['first', 'second']
print('first_txt 길이 =', len(first_txt)) # first_tex 길이 = 10
print('second_txt 길이 =', len(second_txt)) # second_tex 길이 = 10

# 수집한 텍스트 내용
print(first_txt)
print(second_txt)

# list 결합
tot_texts = first_txt + second_txt
print('tot_texts 길이=', len(tot_texts)) # tot_texts 길이= 20

# 전체 텍스트 내용
print(tot_texts)
print(type(tot_texts)) # <class 'list'>
