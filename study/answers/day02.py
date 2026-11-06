from pathlib import Path
from langchain_community.document_loaders import UnstructuredMarkdownLoader

# day02.py 位于 study/answers；往上两层是仓库根目录
repo_root = Path(__file__).resolve().parents[2]
path = repo_root / "data/C1/markdown/easy-rl-chapter1.md"

docs = UnstructuredMarkdownLoader(str(path)).load()

print("文档数量：", len(docs))
print("对象类型：", type(docs[0]))
print("正文前100字：", docs[0].page_content[:100])
print("元数据：", docs[0].metadata)