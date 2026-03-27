# AI大模型主题库

每个主题包含：序号、主题名、核心知识点、推荐深度。

## 主题列表

| 序号 | 主题 | 核心知识点 | 推荐深度 |
|------|------|-----------|---------|
| 1  | Transformer 架构原理 | Self-Attention；多头注意力；位置编码；Encoder-Decoder | 高 |
| 2  | Embedding 与向量数据库 | 文本向量化原理；余弦相似度；Milvus/pgvector 选型 | 高 |
| 3  | RAG 检索增强生成 | 分块策略；ANN 检索；Rerank；Prompt 组装；混合检索 | 高 |
| 4  | Prompt Engineering 进阶 | Zero-shot/Few-shot；CoT 思维链；ReAct；结构化输出 | 高 |
| 5  | Fine-tuning 微调原理 | 全参微调 vs LoRA；指令微调；数据准备；微调 vs RAG 选型 | 高 |
| 6  | LLM Agent 设计 | ReAct 框架；Tool Use；Memory 机制；多 Agent 协作 | 高 |
| 7  | Function Calling 原理与实践 | OpenAI Function Calling；JSON Schema 定义；调用链路 | 中 |
| 8  | LLM 推理优化 | KV Cache；量化（INT8/INT4）；FlashAttention；投机解码 | 高 |
| 9  | 大模型评估体系 | Benchmark（MMLU/HumanEval）；人工评估；G-Eval；RAG 评估 | 中 |
| 10 | 向量检索算法深度解析 | 暴力检索 vs ANN；HNSW 图算法；IVF 聚类；LSH | 高 |
| 11 | LangChain 核心组件 | Chain / Agent / Memory / Tool；与 LlamaIndex 对比 | 中 |
| 12 | 多模态模型原理 | CLIP 图文对齐；视觉 Tokenizer；GPT-4V；图生文/文生图 | 中 |
| 13 | 大模型幻觉问题与缓解 | 幻觉来源；RLHF；RAG 接地；自洽性采样；引用溯源 | 高 |
| 14 | 上下文窗口与长文档处理 | 位置编码外推；滑动窗口；检索优先；层次摘要 | 中 |
| 15 | RLHF 与对齐技术 | SFT → RM → PPO 流程；DPO 简化；Constitutional AI | 高 |
| 16 | 知识图谱与 LLM 融合 | GraphRAG；实体抽取；关系推理；KG 增强检索 | 中 |
| 17 | 代码大模型原理 | CodeX/DeepSeek-Coder；代码补全；单测生成；代码理解 | 中 |
| 18 | 推荐系统与大模型结合 | LLM 召回/排序；用户意图理解；Item Embedding | 高 |
| 19 | 大模型成本优化 | 模型蒸馏；缓存语义相似请求；Prompt 压缩；分级调用 | 高 |
| 20 | AI 安全与红队测试 | 越狱攻击；提示注入；内容安全过滤；对抗样本 | 中 |
| 21 | 流式输出与工程实践 | SSE/WebSocket；Token 流式传输；打字机效果实现 | 中 |
| 22 | 大模型应用架构设计 | 提示词管理；版本控制；A/B 测试；可观测性 | 高 |
| 23 | Stable Diffusion 原理 | 扩散模型；Latent Space；ControlNet；LoRA 应用 | 低 |
| 24 | 语音大模型 | Whisper ASR；TTS 合成；端到端语音对话 | 低 |
| 25 | MCP（Model Context Protocol） | MCP 规范；Tool/Resource/Prompt；Server 开发 | 中 |

## 使用说明

- `get_today_topic.py` 根据 `push-state.json` 中的 `ai.index` 取对应序号的主题
- 序号超出列表时，从头循环（index % len）
- 推荐深度说明：高 = 需要深入原理 + 工程实现；中 = 原理 + 示例；低 = 概念 + 对比
