import datetime


def log(text) -> None:
    log = open("./_bank/log.txt","a",encoding="utf-8")
    log.write(f"\n[~] {datetime.datetime.now().strftime('%Y/%b/%d -- %H:%M:%S -- %f')} {text}")
    log.close()
    del log
