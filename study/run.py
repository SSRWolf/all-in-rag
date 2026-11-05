"""每日题目和实际日期复习记录；仅使用 Python 标准库。"""
import argparse
import json
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TASKS = json.loads((ROOT / 'tasks.json').read_text(encoding='utf-8'))
parser = argparse.ArgumentParser()
parser.add_argument('day', type=int, nargs='?')
parser.add_argument('--done', action='store_true', help='已完成并自查后登记')
parser.add_argument('--reviews', action='store_true', help='显示今天到期的复习')
args = parser.parse_args()
state_path = ROOT / 'progress.json'
state = json.loads(state_path.read_text(encoding='utf-8')) if state_path.exists() else {}
today = date.today()
if args.reviews:
    for key, value in sorted(state.items(), key=lambda item: int(item[0])):
        elapsed = (today - date.fromisoformat(value)).days
        if elapsed in (1, 3, 7):
            print(f'复习 D{key}: {TASKS[int(key)-1]["title"]}，距完成 {elapsed} 天')
    print('只显示今日到期题；漏掉的复习可自行回看 progress.json。')
elif args.day is None or not 1 <= args.day <= len(TASKS):
    parser.error('请输入 1–70，或使用 --reviews')
else:
    task = TASKS[args.day - 1]
    print(f'D{args.day} / 第{task["week"]}周：{task["title"]}')
    print('阅读：', task['reading'])
    print('回忆题：', task['recall'])
    print('动手题与验收：', task['task'])
    print('解释题：', task['explain'])
    print('提示：先完成一个最小例子，再扩展；卡住30分钟记录报错。')
    folder = ROOT / 'answers'
    folder.mkdir(exist_ok=True)
    note = folder / f'day{args.day:02d}.md'
    if not note.exists():
        note.write_text(f'# D{args.day} {task["title"]}\n\n'
                        '## 回忆答案\n\n## 代码路径与运行命令\n\n'
                        '## 实际结果\n\n## 输入、处理、输出\n\n'
                        '## 错题与原因\n\n- [ ] 运行出结果\n- [ ] 能解释\n- [ ] 换数据再做\n', encoding='utf-8')
    print('作答文件：', note)
    if args.done:
        state.setdefault(str(args.day), today.isoformat())
        state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding='utf-8')
        print(f'已自评完成 {len(state)}/70 天。这是学习记录，不是自动判卷。')
        start = date.fromisoformat(state[str(args.day)])
        print('复习日期：', ', '.join(str(start + timedelta(days=n)) for n in (1, 3, 7)))
