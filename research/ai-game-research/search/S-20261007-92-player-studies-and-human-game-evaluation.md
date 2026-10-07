# 搜尋批次：玩家研究與人類遊戲生成評估

**日期／範圍：**2026-10-07。延續 S91 的 art rubric search，本方向改查近期 arXiv 的玩家研究：辨認人類 study 是在評「最終 AI 交付成品」、玩家與 AI 共創過程，或 AI-native gameplay；只將可支援本研究評估設計的材料留下，不把共創／遊戲內 AI 研究冒充 autonomous code-agent output。

## 研究問題與先前查重

先讀研究索引、候選摘要、搜尋索引、S91，以及 [M0025](../records/M0025.md)、[M0029](../records/M0029.md)、[M0030](../records/M0030.md)。以 exact-title 和 arXiv ID 對照 catalog，`Lottery and Sprint Arcade`、`Pharos Night`、`AI game co-creation user study` 均未收錄；新增方法紀錄 [M0031](../records/M0031.md)，不建立遊戲候選。

## 實際搜尋與查閱

| exact arXiv API query／來源 | 結果 | 判斷與排除理由 |
|---|---|---|
| `all:"game generation" AND (all:"human evaluation" OR all:"user study" OR all:"human preference")` | 回傳 [Lottery and Sprint Arcade (2607.10711)](https://arxiv.org/abs/2607.10711)，以及 Moral Alignment for LLM Agents (2410.01639)、Abstract Art Generation (2012.00744)。查 2607.10711 原始摘要。 | Arcade paper 是自然語音 play-edit-feedback，玩家邊玩邊改約 100 個遊戲參數；study 評估 interaction experience/workload，非一次任務後的凍結遊戲成品。另兩篇題意不符，排除。 |
| `all:"AI-generated game" AND (all:visual OR all:aesthetic OR all:playability)` | arXiv API 回空集合。 | 這組字面查詢沒有命中；不把零結果解讀成全網沒有此類研究，另查相鄰術語。 |
| `all:"procedural game generation" AND all:human AND all:visual quality` | arXiv API 回空集合。 | 此組 exact field query 無命中，保留原 query 與結果。 |
| `all:"game creation" AND all:"user study"`；`all:"game designer" AND all:"generative AI" AND all:players`；`all:"interactive game generation" AND all:evaluation`；`all:"video game" AND all:"human preference" AND all:AI-generated` | 命中 [Lottery and Sprint (2307.00348)](https://arxiv.org/abs/2307.00348)、[Pharos Night (2608.12216)](https://arxiv.org/abs/2608.12216)、[Using Generative AI to Uncover What Drives Player Enjoyment in PC and VR Games (2508.16596)](https://arxiv.org/abs/2508.16596)、以及 Orak video-game agent benchmark (2506.03610)。逐一查前述論文摘要與 Orak 題意。 | 2307.00348 有 human design sprint 與 AutoGPT、後續 playability/enjoyment study，屬有使用者介入的 board-game authoring；Pharos Night 有 13 人小型遊玩研究，但它測 LLM 驅動卡牌／NPC 的 AI-native game experience，不是 coding agent 生成遊戲；2508.16596 以 Steam/Meta Quest review 分析玩家享受因素，不是 generated-build art review；Orak 測 LLM agents 玩既有遊戲，不測生成。相關但不符合範圍者記入 M0031。 |

## 結論與搜尋計數

- 玩家研究與人類評估出現在 AI-native game 和 AI-assisted design 領域，但本輪檢視的案例有玩家持續語音修改、設計衝刺、遊戲內 AI 或既有遊戲 review analysis；沒有一個是最新 coding agent 接收一次任務後自行完成高品質遊戲，再由人類按美術、可玩性與完整度分軸盲評的實例。
- 新增 M0031 方法脈絡；沒有新遊戲候選或既有 case 的成品證據提升。S90 後第二個不同無增益方向：**2／至少 3**。
- 下一方向：查 2026 年近期模型／agent 官方 coding showcase 的具名高視覺遊戲成品與原始作者 repo，鎖定原任務與 playtest evidence；同既有 C0013/C0027 去重，不將官方宣傳圖當 gameplay。

<!-- record-meta: {"id":"S-20261007-92","type":"search","updated":"2026-10-07"} -->
