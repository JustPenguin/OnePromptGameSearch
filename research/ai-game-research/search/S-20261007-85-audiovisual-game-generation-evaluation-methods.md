# 搜尋批次：錄影音畫評分與近期遊戲生成評測方法

**日期／範圍：**2026-10-07。沿 S84 所列新方向，查 arXiv 公開索引中近年 `game generation`／`text-to-game`／`interactive game generation` 與 benchmark/evaluation 相關新論文；優先確認是否公開實際 3D gameplay AVRs、任務、model/version 與 judge rubric。S81 的官方 benchmark roster 已覆查，本批改查錄影型評測方法與能否對回成品。

## 實際 query 與來源

| query／來源 | 結果及檢視 | 收錄／排除理由 |
|---|---|---|
| arXiv API `search_query=all:"game generation" AND (all:benchmark OR all:evaluation)&sortBy=submittedDate&max_results=30` | 最新結果包括 2026-10-02 GameGo、2026-09-18 GameASG、2026-08-22 GameXpert-Bench、2026-06-16 GameCraft-Bench、2026-05-27 GUI Agents for Continual Game Generation、2025-09 V-GameGym、2025-08 Multi-Agent Game Generation and Evaluation via Audio-Visual Recordings、2024-12 Playable Game Generation。先核對已入帳項目後聚焦 AVR 論文。 | GameGo、GameASG、GameXpert、GameCraft 和 V-GameGym 都已有 B/G records 與 S79/S81/S72 等查核，不複製 roster audit；AVR 方法與使用者獨立美術軸關係較近，延伸核對原文／實作。 |
| arXiv API `search_query=all:"text-to-game" AND (all:benchmark OR all:generated)&sortBy=submittedDate&max_results=30`；`all:"interactive game" AND all:generation&sortBy=submittedDate&max_results=30` | Learn2Play Bench 評估 LLM 在陌生遊戲環境學習，不是生成遊戲；S3Gym 是 agent 自我測試方法；World Craft／GameWAM／Magpie 是視覺世界模型，不是可交付 code-agent 遊戲。 | 排除為目前的完整遊戲生成能力主題，保留查詢及題意不合理由。 |
| [AVR 論文 HTML](https://arxiv.org/html/2508.00632)、[AVR-Eval/Agent repo](https://github.com/SamsungSAILMontreal/AVR-Eval-Agent)、[README](https://github.com/SamsungSAILMontreal/AVR-Eval-Agent/blob/main/README.md)、repo task CSV：`data/video_games.csv`、`video_games_hard.csv` | 核 rubric 將描述符合、視覺設計、音訊品質、行為正確、玩法品質及 AI player quality 分列；Qwen2.5-Omni-7B 做兩段描述／比較，Qwen3-32B 審查。論文報告 broken-choice 0.91%、wrong-type 6.47%，比較 9 個生成 platformer 與 5 個 human-made platformer 的自動勝率 67.78%；作者明說未直接在人類偏好上驗證。AVR-Agent 的五種實驗遊戲為 2D platformer、beat ’em up、bowling、solitaire、incremental，另五種動畫；使用約 5–20 次迭代、best-of-k 與 asset/feedback 條件。hard CSV 有 3D 平台、spaceship、fighting、ARPG description，但不是已證實由其框架生成的 build。 | 新增 [M0029](../records/M0029.md) 作分離視覺／玩法／錯誤的 A/B 評測方法參照；AVR-Agent 明確多輪，生成實驗規模不代表完整 AAA 交付，模型 judge 也不能代替使用者美術評價。 |
| repo API `GET /repos/SamsungSAILMontreal/AVR-Eval-Agent`、`/contents`、`/contents/data`、`/contents/experiments_paper`、`/contents/images` | repo 含評估／產生程式、五種 `video_games*.csv` 規格、實驗指令和 before-after / agent diagrams；README 所述要求 Linux/CUDA 12.6 左右、Qwen2.5-Omni-7B + Qwen3-32B，部分實驗另用多種閉源與開源 coding model。repo last pushed 2025-08-18。 | 有方法與部分題種可查，但沒有可直接把論文各輸出逐個對到原始 session/final source 的大型 frozen artifact gallery；不列新強候選或最新模型成果。 |
| arXiv API id lookup: `2508.00632, 2412.00887, 2608.21833, 2608.16196, 2604.18394, 2606.17861, 2605.28258, 2509.26161` | 另核 abstract 和重點限制。PlayGen 以自回歸 video-game diffusion 生成可玩遊戲 byte/frames，與 LLM coding-agent 的交付協定不同；UniGen 是零編碼多代理 3D Unity prototype，並非最新模型的可重建單次委託；其餘幾篇已收錄或主要測互動 AI agent。 | 不將遊戲影片生成或遊戲內代理能力誤計為 coding agent 一次交付成績。 |

## 結果與計數

- 沒有新強 one-shot 候選，也沒有足以顯著更新某個既有 case 的最新生成成績。新增 M0029 是**評測方法參照**：其 rubric 有用，但自動 A/B judge 未在人類 preference 直接驗證，AVR-Agent 多輪流程不符合 strict task。
- S83 後第 2 個彼此不同無增益搜尋方向：**2／至少 3**。現有線索仍有未完成的方向，故研究繼續。
- 下一方向：查近期真實 3D game benchmark 中 AI 畫面／工具輸出是否可由公開 evaluation trace 對回具名 frozen build 和可重跑任務；優先查看 OpenGameEval／PlaytestArena 的 release delta 與可見 outputs，不重複只查論文 roster。
