# S36 · 近期前沿模型遊戲生成實測與畫面證據

**日期：**2026-10-07　**研究方向：**追查近期 GPT-6 Astra 遊戲輸出，優先確認原始任務／影片實玩、模型比較與一次委託證據；同時查重已知候選

## 研究問題與先前查重

先讀研究索引、精選候選、搜尋索引及 S34。已知最新來源包括 GPT-6 Astra 社群 prompt repo、Hollowflux 等官方多輪成果，以及 THE NINTH BELL、Kart Blitz、OneShotGTA 等已登錄案例。這輪聚焦較新的 Astra 社群遊戲輸出和影片中多題實測，避免重複列出已有作品；查重確認 Street Heat 為 G0216 且缺原始 prompt／build，Tidal Rush 尚未收錄。

## 實際搜尋與查閱

| query／網址 | 結果與證據 | 關聯固定編號 | 後續／重查條件 |
|---|---|---|---|
| `"Tidal Rush" "eight racers" GPT-6 Astra browser game`；`"Tidal Rush" "three laps" GPT-6 game prompt`；`"Tidal Rush" RESONANCE SCIENCE browser racing GPT-6 Astra playable demo`；`"Tidal Rush" browser kart racing game GPT-6 Astra playable` | 找到 TIDAL RUSH — Paradise GP 的可玩 ChatGPT Sites build，遊戲內顯示三圈、八位賽車手、漂移／道具、結果頁與再賽。OpenAI 官方 Astra 發布頁直接連到該互動作品並標註 Pietro Schirano；策展 repo 提供遊戲畫面及 access check。未找到逐字原始 prompt、完整 session／follow-up trace 或 source。它是官方歸因的短循環賽車輸出，可供使用者檢視畫面／物理，但不足以證明使用者只輸入一次或 AI 自主修正，也低於本輪長流程／跨系統上限主題。建立 G0250 作視覺／物理副測，不升為嚴格 one-shot 強候選。 | [G0250](../records/G0250.md) | 若 OpenAI／作者補出原 prompt、生成記錄、source／凍結版本，再更新一次委託證據。現有可玩 URL：[Tidal Rush](https://tidal-rush-paradise-gp.skirano.chatgpt.site/)；[OpenAI 官方發表頁](https://openai.com/index/gpt-6-astra/)。策展截圖來源：[SOURCE.md](https://github.com/MartinDelophy/awesome-gpt-6-astra/blob/main/assets/screenshots/tidal-rush/SOURCE.md)。 |
| `"Street Heat" GPT-6 Astra game drift physics near-miss bonuses playable`；`site:github.com Street Heat GPT-6 Astra game playable` | 查重命中 G0216。再次確認可找到的 Tripo prompt 為衍生重建文字，並非創作者原始任務；未找到原作者 build／成品來源。現有排除狀態成立，不重複建檔或升格。 | [G0216](../records/G0216.md) | 僅在有原作者 prompt／ build／trace 等直接證據時重查。 |
| `Brendan Jowett GPT-6 Astra INSANE building video games full test September 10 2026 Unreal Engine one prompt`；`site:youtube.com/watch "GPT-6 Astra Is INSANE For Building Video Games"`；`Brendan Jowett Astra GTA 6 Minecraft Counter-Strike game recreation prompt one prompt follow up source video September 2026`；`"GPT-6 Astra" "five games" game generation prompt video` | 先找到 2026-09-10 的五款複刻展示，創作者稱每款各由簡短提示產生；但只有影片／沒有原始任務與可查 build，不升格。向近期多題對照追查後找到 2026-09-24 Brendan Jowett 的 Opus 5.5 × GPT-6 Astra 五題 UE5 影片。 | 先前展示僅列本批；後續對照見 [B0049](../records/B0049.md) | 若創作者釋出五份 prompt／source／session，再按每題範圍補充。 |
| `site:youtube.com/watch "Rampart" "Apex Circuit" "Void Wing" "Colossus" Astra Brendan`；`"Rampart" "Apex Circuit" "Void Wing" "Dead Signal" "Colossus" "Brendan Jowett" prompts`；`"NEW Opus 5.5 vs GPT-6 Astra Building Video Games" prompt exact task download playable build`；`Brendan Jowett Rampart Apex Circuit Void Wing Colossus GPT-6 Astra GitHub` | 創作者 YouTube 影片與社群公告確認：同一組單次 prompts 對照 GPT-6 Astra／Opus 5.5，最高設定，C++／UE5，Blender 原生做資產，不用外部下載；實玩畫面及每題時間／成本面板皆在影片。五題為平台、競速、六軸空戰、生存 FPS、Boss 戰。影片說明／社群留言中有人詢問 prompt，但目前查到的作者回應請觀眾到影片下留言，沒有在頁面附上原 prompt。Post-Cutoff 提供逐段時間戳與數字表，但其內容明示為 Gemini 從影音生成摘要；統計資料故標成二手轉錄、不得視為獨立核實。沒有 public source/build、完整 trace 或穩定評分 rubric。 | 新增 [B0049](../records/B0049.md) | 若取得原 prompt／完整軌跡或 playable build 則提高證據級別；若只持續有宣傳剪輯而無可重現材料，維持影片參照。 |
| [創作者原始影片](https://www.youtube.com/watch?v=w4JMLjnY1xY)；[創作者社群公告](https://www.skool.com/brendan/new-opus-55-is-insane-for-building-video-games-full-test)；[Post-Cutoff 影音摘要](https://postcutoff.com/v/yt-brendan-jowett-new-opus-5-5-vs-gpt-6-astra-building-vid/) | 前兩個為創作者來源；第三個是以影音生成的旁證摘要，適合定位時間戳、不能取代原始 prompt／logs。它記載每題模型版本、短遊戲描述、時間／API 成本及影片片段。不能把影片評論／單次短實玩提升為盲測品質排行。 | [B0049](../records/B0049.md) | 以創作者新增 artifact 或 raw prompts 觸發更新。 |

## 結論與更新去向

- 新增 [B0049](../records/B0049.md)：近期多題模型對照影片，五種遊戲類型有實玩畫面與工時／成本呈現，值得使用者直接檢視；原始 prompts、session、source/build、盲評 rubric 未公開，因此只列「近期實測／畫面參照」，不稱為可完整重現正式 benchmark。
- 新增 [G0250](../records/G0250.md) Tidal Rush：OpenAI 官方模型頁連結的 GPT-6 Astra 互動賽車，有 playable build 與實際 gameplay 截圖；適合畫面／物理副測，但原始 prompt／session 未公開，故不升為上限主測或已核實一次交付。
- 9 月 10 日五款複刻短片也有影片輸出，但缺乏一次委託及自主修正證據，不新增候選；來源及重查條件保留於本批，避免重新搜尋。
- Street Heat 的舊排除理由經重查沒有改變。
- B0049 五款畫面尚待使用者按其美術標準檢視；新的作品不沿用 E0008 中對當時 review 頁的評語。

## 待查與下一方向

下一輪改查近期作者公開的 Astra／Opus 高複雜度遊戲源碼／首版截圖／自動 QA traces，特別是長流程 RPG、經營模擬或完整城市 sandbox；只收錄原作者或第一手模型頁能對應具體 build 的項目。若只有精華片段且找不到 prompt／freeze／artifact，保留排除理由，不提升為 one-shot 強候選。
