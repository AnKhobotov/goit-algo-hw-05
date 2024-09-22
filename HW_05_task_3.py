from pathlib import Path
import sys
from collections import defaultdict

def parse_log_line(line: str) -> dict:
    
    line = line.split(" ")
    logs_dict = dict()
    
    for el in line:
        logs_dict["date"] = line[0]
        logs_dict["time"] = line[1]
        logs_dict["level"] = line[2]
        logs_dict["msg"] = " ".join(line[3:]).strip()
    
    return logs_dict

def load_logs(file_path: str) -> list:

    try:
        file_path = Path(file_path)
        logs_list = []
        with open(file_path, "r", encoding="utf-8", errors="string") as fh:
            while True:
                line = fh.readline()
                line = line.strip()
                if not line:
                    break
                logs_list.append(parse_log_line(line))
    except Exception as e:
        print(e, "Please, Check the path to file")
    finally:
        return logs_list




def filter_logs_by_level(logs: list, level: str) -> list:
    filtered_logs=[]
    for el in logs:
        if el.get('level') == level:
            el['level'] = '-'
            a = ' '.join(el.values())
            filtered_logs.append(a)
    return filtered_logs

from collections import defaultdict, Counter

def count_logs_by_level(logs: list) -> dict:

    counts = defaultdict(int)
    for el in logs:
        counts[el.get('level')] += 1
    return counts


def display_log_counts(counts: dict):
    riv="Рівень логування"
    qty="Кількість"
    print(f"{riv:<20}| {qty:<20}")
    print(f"-"*40)
    for key,value in counts.items():
        print(f'{key:<20}| {value:<20}')
    

def main():

   
    file_path, *level = sys.argv[1:3]    
    logs_list = load_logs(file_path)
    display_log_counts(count_logs_by_level(logs_list))
    if level:
        level = str(level[0]).upper()        
        print(f"Деталі логів для рівня '{level}': \n")
        a = filter_logs_by_level(logs_list, level)
        for i in a:
            print(f"{i}\n", sep=",")
        

if __name__=="__main__":
    main()
