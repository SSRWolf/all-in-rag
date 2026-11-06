# D2 检查 Document

## 回忆答案
docs = UnstructuredMarkdownLoader(str(path)).load()
UnstructuredMarkdownLoader(str(path)) 创建加载器。
.load() 读取文件，并在加载器内部创建 Document 对象，返回包含这些对象的列表。
docs = ... 把这个列表赋给变量 docs。
一个document封装了一份文本及其相关信息，page_content保存正文，metadata保存来源等元数据

## 代码路径与运行命令
```python
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
```

## 实际结果
文档数量： 1
对象类型： <class 'langchain_core.documents.base.Document'>
正文前100字： 第1章 强化学习基础

1.1 强化学习概述

强化学习（reinforcement learning，RL）讨论的问题是智能体（agent）怎么在复杂、不确定的环境（environment）中最大化
元数据： {'source': '/workspaces/all-in-rag/data/C1/markdown/easy-rl-chapter1.md'}


## 输入、处理、输出
| 代码 | 含义 | 输出示例 |
|---|---|---|
| `len(docs)` | 列表里的文档对象数量 | `1` |
| `type(docs)` | `docs` 的类型 | `<class 'list'>` |
| `type(docs[0])` | 第一个元素的类型 | `<class 'langchain_core.documents.base.Document'>` |
| `docs[0].page_content` | 第一个文档的全部正文 | 实际加载的正文 |
| `docs[0].page_content[:100]` | 解析后正文的前 100 个字符，不是前100个词 | 前 100 个字符；不足则全部输出 |
| `docs[0].metadata` | 查看实际有哪些字段，尤其是来源source | `{'source': '文件路径'}` |
| `docs[1]` | 尝试访问第二个文档对象 | `IndexError`，因为只有一个对象 |

## 错题与原因
文档路径错误：
  File "/opt/conda/envs/all-in-rag/lib/python3.12/site-packages/unstructured/partition/md.py", line 58, in partition_md
    _, text = read_txt_file(filename=filename)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/conda/envs/all-in-rag/lib/python3.12/site-packages/unstructured/file_utils/encoding.py", line 123, in read_txt_file
    formatted_encoding, file_text = detect_file_encoding(filename)

- [ ] 运行出结果
- [ ] 能解释
- [ ] 换数据再做
