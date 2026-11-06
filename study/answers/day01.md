# D1 标注第一章的五个处理阶段

## 回忆答案
先加载文档，得到正文和数据，再把参考文本分块，再将每一块变成embedding,针对用户问题找到文档中最相似的文本块，将文本块合并并用换行符分隔各个块，形成最终的上下文信息给大语言模型参考，最后将检索到的上下文与用户问题结合，给大语言模型生成回答

## 代码路径与运行命令
### 加载文档
```python
markdown_path = "../../data/C1/markdown/easy-rl-chapter1.md"
loader = TextLoader(markdown_path)
docs = loader.load()
```
### 文本分块
```python
text_splitter = RecursiveCharacterTextSplitter()
texts = text_splitter.split_documents(docs)
```
### 向量化与存储
```python
embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-zh-v1.5",
    model_kwargs={'device': 'cpu'},
    encode_kwargs={'normalize_embeddings': True}
)
vectorstore = InMemoryVectorStore(embeddings)
vectorstore.add_documents(texts)
```
### 检索及准备上下文
```python
retrieved_docs = vectorstore.similarity_search(question, k=3)
docs_content = "\n\n".join(doc.page_content for doc in retrieved_docs)
```
### 生成回答
```python
answer = llm.invoke(prompt.format(question=question, context=docs_content))
print(answer)
```

## 实际结果
### 问题1：文中举了哪些例子
1.  **DeepMind研发的走路的智能体**：例如像人一样的智能体学习在曲折道路上行走时举手保持平衡。
2.  **机械臂抓取**：利用分布式系统训练多个机械臂，学习适用于不同形状物体的统一抓取算法。
3.  **选择餐馆**：利用（去熟悉的餐馆）与探索（尝试新餐馆）。
4.  **做广告**：利用（最优策略）与探索（新策略）。
5.  **挖油**：利用（在已知地方挖油）与探索（在新地方挖油）。
6.  **玩游戏**：利用（如《街头霸王》中蹲在角落出脚的策略）与探索（尝试新招式如“大招”）。
7.  **象棋选手**：在棋局结束时得到正奖励（赢）或负奖励（输）。
{'token_usage': {'completion_tokens': 1334, 'prompt_tokens': 820, 'total_tokens': 2154, 'completion_tokens_details': {'accepted_prediction_tokens': None, 'audio_tokens': None, 'reasoning_tokens': 1127, 'rejected_prediction_tokens': None}, 'prompt_tokens_details': {'audio_tokens': None, 'cached_tokens': 2}}, 'model_name': 'glm-4.7-flash', 'system_fingerprint': None, 'id': '20261106145849e52ee95f6f994838', 'service_tier': None, 'finish_reason': 'stop', 'logprobs': None}
### 问题2：机器学习有哪些方法
根据提供的上下文，机器学习的方法主要包括**强化学习**（Reinforcement Learning）。

文中提到的具体方法和实例包括：
1.  **强化学习**：文中将其定义为理论与实践相结合的机器学习分支。
2.  **深度强化学习**：结合了深度学习，采用端到端训练的方式。
3.  **标准强化学习**：文中将其作为对比对象与深度强化学习进行区分。
4.  **K-臂赌博机**：作为强化学习中的具体模型示例。
5.  具体的应用实现，如**DeepMind 走路的智能体**和**机械臂抓取**。
{'token_usage': {'completion_tokens': 1815, 'prompt_tokens': 689, 'total_tokens': 2504, 'completion_tokens_details': {'accepted_prediction_tokens': None, 'audio_tokens': None, 'reasoning_tokens': 1669, 'rejected_prediction_tokens': None}, 'prompt_tokens_details': {'audio_tokens': None, 'cached_tokens': 2}}, 'model_name': 'glm-4.7-flash', 'system_fingerprint': None, 'id': '202611061502344ef6684852a345b1', 'service_tier': None, 'finish_reason': 'stop', 'logprobs': None}

## 输入、处理、输出
| 阶段 | 输入 | 处理 | 输出 |
|---|---|---|---|
| 加载文档 | Markdown 文件路径 | 加载文件正文 | `Document` 列表 `docs`，包含正文和元数据 |
| 文本分块 | `docs` | 按长度和重叠规则切分 | 文本块列表 `chunks` |
| 向量化与存储 | `chunks`、嵌入模型 | 将文本块转换为向量并存入向量库 | 可检索的 `vectorstore` |
| 检索与准备上下文 | 用户问题、`vectorstore` | 检索最相关的 3 个文本块并拼接 | 上下文字符串 `docs_content` |
| 生成回答 | 问题、上下文、提示词 | 调用大语言模型 | 消息对象 `answer`；回答正文是 `answer.content` |
## 错题与原因

- [ ] 运行出结果
- [ ] 能解释
- [ ] 换数据再做
