import time
from typing import List, Dict


def solution(parentheses: List) -> bool:
    buffer = []
    item: Dict
    for item in parentheses:
        if item['status'] == 1:
            buffer.append(item)
        elif item['status'] == 0 and item['type'] == buffer[len(buffer) - 1]['type']:
            buffer.pop()
        else:
            return False
    return True


# Problem to match the parentheses to close each other.
if __name__ == '__main__':
    start_time = time.time()

    # {[]{()}}
    print("solution is: {}. All parentheses are ordered. ".format(solution([
        {"sign": "{", "type": 1, "status": 1},
        {"sign": "[", "type": 2, "status": 1},
        {"sign": "]", "type": 2, "status": 0},
        {"sign": "{", "type": 1, "status": 1},
        {"sign": "(", "type": 2, "status": 1},
        {"sign": ")", "type": 2, "status": 0},
        {"sign": "}", "type": 1, "status": 0},
        {"sign": "}", "type": 1, "status": 0}

    ])))
    end_time = time.time()
    print("Execution time: {} seconds".format((end_time - start_time)))
