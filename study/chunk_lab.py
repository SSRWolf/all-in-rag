"""D4/D5实验助手：不调用LLM；需要现有环境中的langchain_text_splitters。"""
import argparse
from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter

parser = argparse.ArgumentParser()
parser.add_argument('--size', type=int, default=500)
parser.add_argument('--overlap', type=int, default=50)
parser.add_argument('--file', type=Path, help='可选：自己的UTF-8文本文件')
args = parser.parse_args()
if args.size <= 0 or not 0 <= args.overlap < args.size:
    parser.error('需要 size > 0 且 0 <= overlap < size')
text = args.file.read_text(encoding='utf-8') if args.file else '\n\n'.join(
    f'第{i}节：RAG先从文档中查找相关证据，再根据证据生成回答。'
    '分块需要考虑上下文完整性。来源信息有助于核对回答。' * 5
    for i in range(1, 9))
chunks = RecursiveCharacterTextSplitter(chunk_size=args.size, chunk_overlap=args.overlap).split_text(text)
lengths = [len(c) for c in chunks]
print(f'size={args.size}, overlap={args.overlap}, 块数={len(chunks)}')
print(f'平均长度={sum(lengths)/len(lengths) if lengths else 0:.1f}, 最大长度={max(lengths, default=0)}')
for i, chunk in enumerate(chunks[:3], 1):
    print(f'\n块{i} ({len(chunk)}字符):\n{chunk}')
print('\n请解释：为什么实际块长、实际重叠不一定等于设置值？')
