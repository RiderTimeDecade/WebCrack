import datetime
from concurrent.futures import ThreadPoolExecutor
from typing import List

from crack.crack_task import CrackTask
from url_processor import read_urls_from_file
from thread_utils import ThreadSafeCounter

author_info = '''
+---------------------------------------------------+
| __          __  _      _____                _     |
| \ \        / / | |    / ____|              | |    |
|  \ \  /\  / /__| |__ | |     _ __ __ _  ___| | __ |
|   \ \/  \/ / _ \ '_ \| |    | '__/ _' |/ __| |/ / |
|    \  /\  /  __/ |_) | |____| | | (_| | (__|   <  |
|     \/  \/ \___|_.__/ \_____|_|  \__,_|\___|_|\_\ |
|                                                   |
|                 code by @yzddmr6                  |
|                  version: 2.2                     |
+---------------------------------------------------+
'''

def worker(counter: ThreadSafeCounter, url: str) -> None:
    """Process a single URL with thread-safe task numbering."""
    task_num = counter.increment()
    CrackTask().run(task_num, url)

def multi_thread_crack(url_list: List[str], max_workers: int = 50) -> None:
    """Process URLs using multiple threads."""
    all_num = len(url_list)
    print(f"总任务数: {all_num}")
    print(f"并发线程数: {max_workers}")
    
    counter = ThreadSafeCounter()
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        executor.map(lambda url: worker(counter, url), url_list)

def main():
    print(author_info)
    try:
        import conf.config
    except:
        print("加载配置文件失败！")
        return

    url_list = read_urls_from_file('url.txt')
    if not url_list:
        return

    start = datetime.datetime.now()
    multi_thread_crack(url_list)
    end = datetime.datetime.now()
    print(f'All processes done! Cost time: {str(end - start)}')

if __name__ == '__main__':
    main()