# 70天 RAG 学习练习包

适用：已跑过第一章、刚开始第二章；现有 all-in-rag Codespace。
每天60–90分钟，每周第7天用于复习或补进度。10周是基准；遇到服务部署或项目调试可延至12周。
每天：回忆5–10分钟、动手40–60分钟、解释与记录10分钟。不要以API结果不稳定判定自己学不会。

## 开始

将整个 study 文件夹复制到 /workspaces/all-in-rag/ 下。在Codespaces终端执行：

```bash
conda activate all-in-rag
cd /workspaces/all-in-rag
python study/run.py 1
```

这会展示题目，并创建 study/answers/day01.md。代码题自行创建同目录 day01.py，再用 python study/answers/day01.py 运行。
阅读路径相对于仓库根目录；tasks.json包含完整70天任务。查看题目与记录工具只用Python标准库。

```bash
python study/run.py 1 --done
python study/run.py --reviews
python study/run.py 2
```

只有完成题目并留下实际证据才使用 --done。重复登记不会修改首次完成日期。
复习按照实际完成后的1、3、7天计算，不要求补日历打卡。工具不会后台提醒，不会自动评价答案。

## 第一周实验

```bash
python study/chunk_lab.py --size 200 --overlap 50
python study/chunk_lab.py --size 500 --overlap 50
python study/chunk_lab.py --size 1000 --overlap 50
```

D4固定overlap比较size；D5固定size比较overlap=0/50/100。先预测，再运行，再解释。
可用 --file data/C1/markdown/easy-rl-chapter1.md 换成仓库真实资料。
实验需要现有langchain_text_splitters；缺包先检查当前Python环境，勿整体升级依赖。
这是观察工具，完整课程代码仍由你按题目编写；不是70份已经解好的答案。

## 时间与资源优化

- W1 第一章复习/第二章；W2–3 第三章；W4 第四章；W5 第五六章；W6 第八章；W7 第七章；W8 第九章；W9 第十章预留/自主项目；W10复习交付。
- 第十章在当前仓库目录中标注规划中，W9开始时再检查。没发布就用自己的学习笔记做项目。
- 同一实验固定文档、问题、模型与其他参数，一次只改一个变量。生成温度能设0时设0，但仍可能存在随机性。
- 从D13开始复用证据标注和问题集；同时保留一组未用于调参的问题作最终验收。
- 不把块越多、回答越长或复杂架构默认视为更好。记录失败例。
- OCR、多模态、Milvus、Neo4j先用小样本；卡住30分钟记录错误、依赖及尝试。可先做概念题，部署列为待补。
- 每周复习日重做一道错题；如果不能解释本周输入输出，就先补课再继续。
- 忙碌日完成一道回忆题即可；不追求连续打卡，不将此记为整天已完成。

## 保存到GitHub

截图中的Codespace存在未提交改动，请先检查 git status，保留原改动。
可以创建学习分支，然后仅暂存自己确认过的study文件：

```bash
git switch -c study/rag-course
git add study
git diff --cached --stat
git commit -m "Add RAG study exercises"
git push -u origin study/rag-course
```

若分支已存在，使用 git switch study/rag-course。提交前检查内容，不提交.env、密钥、私人资料或模型缓存。
练习包发布在 study/rag-course 分支。在现有 Codespace 中先执行 git fetch origin，再执行 git switch study/rag-course。若提示本地改动冲突，先保存并提交自己的改动后再切换；不要丢弃改动。
