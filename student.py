def stu_list(list):
    return print(list)

# 문제2. 아래 함수를 작성하여
# 학번과 이름을 표시하는 머리글을 출력하시오.
def stu_list_head():
    print("학번\t이름")

# 문제3. 아래 함수를 작성하여 딕셔너리로 부터 
# 학번과 이름을 분리하여 학급명렬표를 출력하시오.
def stu_list_fomatted(list):
    fotmatted_list = ""
    for key in list.keys():
        fotmatted_list+=f"{key}\t{list[key]}\n"
    return print(fotmatted_list)