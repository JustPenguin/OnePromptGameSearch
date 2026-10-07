# 搜尋批次：S-20261007-41-current-one-shot-model-game-runs

**日期／範圍：**2026-10-07。接續 S40，但本輪改查「近期前沿模型是否已有可直接重跑、可看實際遊戲畫面的單次生成案例」，優先官方 model/provider 內容與作者可玩的真實 output。目標是同時記錄 prompt、模型／effort、輸出、one-shot 證據品質、美術畫面及遊戲循環，避免把一次生成、自主修正及長任務等不同條件混成同一件事。

## 研究前查重

重讀根目錄研究索引、候選摘要與搜尋 INDEX；核對 S40、最新遊戲 records 至 G0253，並查名稱／同模型／同文章，以免重複建 Gemini 生存題、Meta Muse 題或官方展示。舊記錄 [G0100](../records/G0100.md) 已有 Fable 5.1《NEON WARDEN》，所以不重建。舊記錄 [G0066](../records/G0066.md) 是 Google 官方 Gemini Flash 城堡 demo 的線索，本輪只重新核對其目前缺少 prompt／成品的狀態。

## 搜尋字串與檢閱結果

| query／網址 | 結果、證據與界線 | 固定編號 | 後續／排除理由 |
|---|---|---|---|
| `site:blog.google Gemini 3.8 game built playable game prompt coding agent 2026`; `site:deepmind.google game generation Gemini playable game demo coding agent 2026`; `"Gemini 3.8" "game" "playable" prompt built 2026`; `Gemini game generation one prompt playable browser game Github 2026` | 找到 Google 2026-09-02 官方 Gemini 3.8 Flash 發布文章中的簡短城堡解謎遊戲展示；描述有「looping instruction」於 Antigravity 開發，沒有公開原 prompt、遊戲 build 或完整 run transcript。文章展示更像能力示例，不能核實為一次使用者委託。[官方來源](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/) | 既有 [G0066](../records/G0066.md) | 不重複建候選。若官方提供可玩原 build、初始任務或 session，重新評估。 |
| `site:mdaakibansari.com.np/articles "Muse Spark" game one shot playable`; `"Muse Spark 1.3" "game" playable prompt one-shot 2026` | 找到三篇同作者 hands-on output：3D roguelike DUNGEONFALL、破壞式 voxel sandbox、3D 開放世界 survival。三者均包含未編輯 prompt、文章內可玩 demo 和實際遊戲畫面；one-shot／模型 effort／零 follow-up 為該作者自述，未有 session export 供獨立審計。高上限遊戲候選以 DungeonFall 最平衡；開放世界生存作互補；voxel 缺玩法閉環降為技術副測。 | 新增 [G0255](../records/G0255.md)、[G0256](../records/G0256.md)、[G0257](../records/G0257.md) | 使用同原文 prompt 在當日最新可用模型重跑；核實 build、記錄 trace／自主 QA、凍結交件。作品美術一律等使用者看實際截圖評價。 |
| [DUNGEONFALL article](https://www.mdaakibansari.com.np/articles/meta-muse-spark-1-3-dungeon-crawler) | 任務要求一檔 3D roguelike、8–11 程序房間與 loop corridors、三階敵人、Boss／treasure vault、近戰、loot／stats、minimap、音效、死亡重開。作者列 Muse Spark 1.3 xhigh、736 行、1 prompt／無 follow-up。畫面與 live demo 在文章；作者也報告轉角追敵會卡牆、缺攻擊預備動畫及部分走廊裝飾。這是本批最值得重跑成「完整可玩遊戲」的任務，不是已獨立驗證成績。 | G0255 | 新模型重跑須保存完整 prompt、session、playthrough 和凍結 build。 |
| [Voxel article](https://www.mdaakibansari.com.np/articles/meta-muse-spark-1-3-voxel-sandbox) | 任務把效能規格寫得具體：64×40×64 地形、約六萬方塊、露出面剔除、分塊 buffer 更新、射線選取、第一人稱碰撞、挖掘／放置。作者列 658 行、Muse Spark 1.3 xhigh、單次／零修正。原頁有 prompt／demo／遊戲畫面；但材料無限、缺任務和勝負循環，故不升格完整遊戲主測。 | G0256 | 只作 WebGL／技術上限副測。 |
| [Open-world survival article](https://www.mdaakibansari.com.np/articles/meta-muse-spark-1-3-open-world-survival-game) | 任務要求程序生態區、採集和節點耗竭／重生、生命／飢餓／體力、六格 hotbar、合成／放置 preview、日夜照明、death／restart。作者列 Muse Spark 1.3 Standard／xhigh、793 行、單次、零後續、約 1,000×1,000 units。作者指出沒有敵對生物、音效或刷新後存檔；有畫面／live demo，但流程自述未獨立核實。 | G0257 | 高系統密度的 sandbox 重跑題；與 DungeonFall 對照探索／生存對戰鬥／Boss 循環。 |
| `site:dev.meta.ai/docs/cookbook/one-shot-game-dev`; `Meta Muse Spark 1.3 game built one prompt playable demo 2026` | Meta 官方 cookbook 公布 Muse Spark 1.3 + OpenCode、最高 reasoning effort、AGENTS.md、Kenney CC0 assets、完整任務 prompt／驗收條件及兩張自稱來自實際 one-shot run 的畫面；單 HTML 可玩 output，包含水域／木頭／車／警示列車／碰撞／高分存檔。Meta 於 2026-09-02 公布 1.3。供應商文章自我報告 generation result，沒有公開 HTML/session；並且開始前須準備 AGENTS.md 與資產，不能稱為裸空白專案只輸入一句 prompt。玩法循環短，適合畫面／方法校準，不列主測。 | 新增 [G0254](../records/G0254.md) | 同規格重跑可比較 AI 善用外部素材與一次任務的完整度；須記錄預置檔案、素材和模型設定。 |
| `site:phaser.io/news "Muse Spark 1.3" game agent`; Phaser [2026-09-22 model lineup](https://phaser.io/news/2026/09/opus-5-5-grok-4-7-and-muse-spark-1-3-in-the-phaser-game-agent) | Phaser Game Agent 公告 Opus 5.5、Grok 4.7、Muse Spark 1.3 sandbox；是近期可用平台線索，未附同一公開任務的 Muse one-shot prompt/build/session/成品比較。 | — | 只作模型時效與平台 roster 線索，不立新作品項目。 |

## 本批去向與結論

- 新增 G0254–G0257 四筆獨立記錄，分開官方配方和第三方自測報告，並記明 evidence limits。候選摘要、根索引、檢閱 HTML 已同步：推薦先看 DUNGEONFALL；開放世界 survival 作互補；Crossy Road 作實際畫面校準；Voxel 僅作效能副測。
- 本批最重要的材料價值是「可重用題目＋可看的模型實際 build」組合。沒把作者自稱 one-shot 當作已驗證紀錄；新模型重跑時要讓 AI 可自主 QA，而使用者不在中途補 prompt，最後交付版本才是驗收對象。
- Muse Spark 1.3 發布於 2026-09-02，至本批整理日不是市場最新型號。重跑前須查最新可取得的 coding-capable 模型及設定，不拿該模型的歷史輸出做最新能力結論。
- 本批沒有給新作品預先標記美術合格；DUNGEONFALL／生存題的實際截圖在原作者頁，Crossy Road 有供應商提供的原 run 截圖已放進檢閱頁。後續由使用者看成品畫面作美術驗收。
- 下輪避免只沿用同一作者文章；接續查 2026-09 之後的官方模型展示／獨立作者 run archives，找更近期模型的高系統 one-task build，尤其是原 prompt、run trace、自動測試和實際可玩凍結版同時公開的作品。另追查 Meta 官方 cookbook 的 output archive 或完整 session 是否有發布。
