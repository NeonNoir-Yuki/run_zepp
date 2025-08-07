from mainmod import XiaoMi
import random
import os


def random_number(run_start, run_end):
    '''随机步数'''
    if run_end not in "":
        run_data = random.uniform(int(run_start), int(run_end))
        run_data = '%.0f' % run_data
    elif run_start == '' and run_end == '':
        run_data = random.randint(10000,50000)
    else:
        run_data = run_start

    return run_data

if __name__ == "__main__":
    i = 1; user = []
    # 获取用户数据    
    while True:
        try: 
            get_data = os.environ['ACTION_RUNZEPP_DATA_'+str(i)]; line = get_data.splitlines()
            username = line[0]; password = line[1]
            i += 1
        except: break
        try: run_start = line[2]
        except: run_start = ''
        try: run_end = line[3]
        except: run_end = ''

        run_data = random_number(run_start,run_end)
        XiaoMi(username, password, run_data).main()
    print('已执行', i-1, '次')