# 搜尋批次：遊戲美術偏好評估與近期任務基準

**日期／範圍：**2026-10-07。接續 S90 已補強現有遊戲畫面證據後，另查公開的人類美術／偏好評分方法與近期高畫面負荷的遊戲生成題庫。目標是找能幫使用者直接檢視作品的 rubric、具體任務或生成 gameplay captures；不以 benchmark 分數代替使用者對單一作品的美術判斷。

## 研究問題與先前查重

先讀研究索引、候選摘要、搜尋索引、S89、S90，以及既有 [M0025 Code2Games](../records/M0025.md)、[M0029 AVR-Eval](../records/M0029.md)、[B0058 GameGoBench](../records/B0058.md)、[G0296 MoxRide](../records/G0296.md)、[G0297 MIDWAY 1942](../records/G0297.md)。以 `manage.py lookup` 查 `GameCode4D`、`Code2Games`、`VideoAesBench`、`Aesthetic Assessment`；Code2Games 已有 M0025，避免重建同一 benchmark；VideoAesBench 與遊戲圖像 aesthetics 名稱尚未入帳，建立 M0030 方法紀錄。

## 實際搜尋與查閱

| 實際 query／來源 | 查看內容與結果 | 收錄／排除理由及待核 |
|---|---|---|
| arXiv API exact query：`all:"video game" AND all:aesthetic AND all:evaluation`；結果 ID `2101.11700, 2110.11744` | 查到 `Multi-Modal Aesthetic Assessment for MObile Gaming Image` 及 aesthetic preference modeling 論文。前者是遊戲 screenshot aesthetics 的直接方法；目前公開摘要／索引資料未能核出可下載全量遊戲圖像、標註者 roster、原始 preference labels 或可重跑 dataset card。後者是通用視覺偏好方法，不是遊戲成品生成 benchmark。 | 新增 [M0030](../records/M0030.md) 作方法線索；不宣稱資料集已公開、不用模型分數代替人類評價。待找到完整資料與標註規格時再重查。 |
| arXiv API exact query：`all:game AND all:"visual appeal" AND all:benchmark` | 結果包含 [GameGo](https://arxiv.org/abs/2610.06910)、[Code2Games](https://arxiv.org/abs/2610.05033)、[Recursive Game Creator](https://arxiv.org/abs/2610.08621) 等。已入帳題目去重；GameTileNet 2507.02941 是低解析 tiles 的語意資料，不測最終遊戲美術；GameVibe / `Do VLMs understand human engagement in games` 2603.18480 測玩家 engagement，不是美術偏好。 | GameGo 已有 B0058/S79；Code2Games 已有 M0025/S23，本批讀它的 artifact 與人類評量細節；其餘題意不符者保留排除理由。 |
| [Code2Games paper](https://arxiv.org/abs/2610.05033)、[HTML paper](https://arxiv.org/html/2610.05033)、[官方 GitHub](https://github.com/AIGeeksGroup/Code2Games)、[官方網站](https://aigeeksgroup.github.io/Code2Games/)、[GameCode4D HF dataset](https://huggingface.co/datasets/AIGeeksGroup/GameCode4D) | 論文 2026-10-04 提交；10 類、20 個 prompts，各含兩版本；FPS、monster hunt、racing、skiing、temple run、TPS、水下、飛行、AC-style 與 block-world。每題需配對 Code2Worlds `.blend` base scene；pipeline 使用 Blender、UE5／驗證、Hunyuan3D、DashScope 與 animated humanoid FBX，並可在最多五次內部修復迭代完成。官方 code 與 HF 發布存在；HF 有 18 個 2–4.8 GB `.blend` scenes 和 task README，非空白專案完整遊戲資料集。paper 將 visual quality、interactive fidelity、multimodal artifacts、playable-game quality 分開。 | 更新既有 M0025，不另建候選：這是高價值 3D 題庫與方法，不是空白起始的完整遊戲 one-shot benchmark；目前公開套件仍需外部資產／API，重跑成本較高，公開生成完整 playable package 未核實。 |
| Code2Games paper §§ human evaluation／Figure 6–25；下載並查看 `FPS`, `racing`, `underwater` 48-frame macro keyframe sheets | 15 位評分者盲評隨機化 gameplay videos，分開評核心玩法、內容深度、功能性視覺與 `Art and presentation`；同作品兩個片段放不同區塊。作者報 Code2Games+Opus 5 人類總分 77.5、Art 57.0；+GPT-5.6 Sol 總分 75.5、Art 54.3。代表性的 48-frame sheets 可看出場景、HUD、攻擊／移動順序，但縮圖不夠判斷細緻材質、模型或完整美術品質。 | 對 M0025 增補：它提供一種把 art/presentation 與 gameplay/content/functionality 分開的人類 rubric。數字只屬論文研究 aggregate，不是使用者美術 verdict、3A 標準或單款作品成績。 |
| [VideoAesBench paper](https://arxiv.org/abs/2601.21915)、[GitHub](https://github.com/michaelliyunhao/VideoAesBench)、[HF dataset tree](https://huggingface.co/api/datasets/michaelliyunhao/VideoAesBench/tree/main?recursive=true) | 1,641 videos／1,804 QA，列有 game videos；維度涉及構圖、視覺元素與結構、景別／景深、主體、光線、色調、創意、情緒、主題、溝通與興趣。HF tree 顯示 `videoaesbench_qa.jsonl`、補充 PDF 和 `final_video_released.zip`，但不把影片 QA 當人類成品 preference ranking。 | 收進 M0030 作影片美學 QA 方法參考；不是生成遊戲 benchmark，不能裁定 playable quality、長期互動一致性或 AI 對藝術資產的歸因。 |
| Crossref/arXiv supplementary queries：`game generation human aesthetic preference benchmark`、`gameplay visual quality human rating art presentation`、`"aesthetic" "game generation" preference dataset` | 結果多為既有 GameGo、Code2Games、V-GameGym、通用影片 aesthetics、遊戲 engagement 或低解析 tile semantics；沒有找到新的近期完整遊戲輸出或具原始人類偏好 labels 的公開資料集。既有 AVR-Eval 對照 M0029：作者明言自動 judge 未直接在人類偏好上驗證；AVR-Agent 是多輪生成。 | 沒有用弱命中湊成遊戲候選；交叉彙整到 M0030，並保留尚待查的正式 preference dataset 問題。 |

## 結論、更新與搜尋計數

- 美術更相關的方法材料已入帳：M0030 記錄遊戲 screenshot aesthetics 與 VideoAesBench 的 rubric 線索；M0025 增加 Code2Games 的 15 人 blind review、分軸量表與代表性 gameplay frames。它們可幫忙設計檢視欄位，不能替代使用者判斷。
- 沒有找到新的公開完整遊戲 one-shot 強候選，也沒有補強 MoxRide／MIDWAY 以外的具名生成 case；Code2Games 的人類評分是新 benchmark/method evidence，不把它寫成 3A-ready 成品。
- S90 曾因 G0296 的來源端 gameplay screenshots 顯著補證而把 no-gain 計數重設為 0。S91 是第一個不同的後續方向，未找到新強遊戲候選／新 case 證據：**1／至少 3 個無增益方向**。研究繼續。
- 下一個不同方向：查近期可玩遊戲的 human playtest／art direction judging 活動與獨立評測資料庫，尋找有原始作品畫面、具體評分軸、模型／任務歸屬的最新高視覺成果；先按 catalog/index 去重，不能重做 S79/S85 的 benchmark roster sweep。

<!-- record-meta: {"id":"S-20261007-91","type":"search","updated":"2026-10-07"} -->
