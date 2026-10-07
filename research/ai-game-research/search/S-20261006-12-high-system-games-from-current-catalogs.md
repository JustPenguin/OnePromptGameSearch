# 搜尋批次 S-20261006-12：近期目錄中的高系統遊戲

**日期：**2026-10-06（台北時間）  
**研究問題：**在新近整理、有實際可玩 build 的模型遊戲集合中，能否找到公開完整委託規格、系統深度高而適合交給不同新模型重跑的獨特題型？

## 開始前查重

讀候選索引、精選候選及全項目 catalog；以 `DASH / DINNER`、`Crumb City`、`Elderwood Realms`、`Lumbridge` 搜本機 records/search/history。沒有同名紀錄。相近的 Last Courier、Pelican Bike、Kart Blitz 都是不同題材／來源，分開記錄；不併作同作。

## 搜尋及來源

| 實際 query／來源 | 發現和證據 | 判斷／後續條件 |
|---|---|---|
| `GPT-6 Astra one shot city delivery driving game exact prompt playable demo`；`site:agentgames.dev/play delivery game GPT-6 Astra prompt`；[AgentGames DASH / DINNER](https://agentgames.dev/play/dash-dinner) | GPT-6 Astra／Codex 標籤、作者 prompt 原文、browser playable build 和 Node.js tests 的平台說明。prompt 指定 3D 城市中第一人稱步行／騎車配送、計時訂單、記門禁碼、升級載具、疲勞與宿舍跨日恢復。另一份目錄核對記錄於 9/21 實際開過街道／踏板車並截圖，但只檢查到接受訂單，未完成取餐送達。 | 新增 G0209、納入重跑系統題備選。平台列出 prompt 和由 GPT-6 Astra 撰寫，未給完整 session／no-follow-up 證明、首版 hash、run 日期耗時或可見 QA 結果。畫面中的 3D／2D 相容分流、完整送貨和進度都需再由人實際檢視。 |
| `"Lumbridge" "Elderwood Realms" GPT-6 Astra one shot MMO`；[Elderwood closure page](https://elderwood-realms.rohannvarma.chatgpt.site/)；[獨立目錄的 screenshot provenance](https://github.com/MartinDelophy/awesome-gpt-6-astra/blob/main/assets/screenshots/lumbridge/SOURCE.md) | 一個曾公開上線的多人 browser RPG 原型，有真實當時 build 截圖和研究員訪客帳戶檢視；網站目前有正式關閉公告，說明收到 Jagex notice 後停站。作者 one-shot demo 陳述只關於一段 showcase，不能歸到整個多人遊戲；關閉公告說它在幾天內依到訪玩家逐步長成多人世界。 | 新增 G0210 並排除既有交付樣本；只保留「多人原創開放世界」重跑題材。不得使用原作名稱／角色當正式 benchmark，也不以此案例宣稱一次 prompt 做成 MMO。 |
| `site:github.com/MartinDelophy/awesome-gpt-6-astra delivery game prompt simulation`; repo 中 RPG／模擬類目 | 這個社群目錄標示 174 款遊戲，更新日為 2026-10-06；每款需連到直接遊玩頁，另附 creator attribution／verification 和真實截圖來源，但目錄明示收錄並非 benchmark 或官方 endorsement。抽查到高價值的 DASH/DINNER、同時核對已下架的 Elderwood；其他案例中有多輪迭代的作品，不符合原始任務條件。 | 可作發現入口，不把整份 gallery 收錄名單當合格樣本。後續按 exact prompt、first-run/live build、人工介入及高系統深度逐款篩選，不要重掃 174 款低深度遊戲。 |

## 本批結論

- **DASH / DINNER 值得留作重跑備選。**同一 brief 可測路線／步行駕駛／倒數／工作狀態／記憶與跨日經濟 progression，任務全文和 playable build 都公開。它比單一機制 arcade 題能揭露更多跨系統失誤，也形成獨特外送職涯題型。作者 run 不可當完整稽核的一次生成成績；但對你親自設計自己的統一 one-shot 實驗而言，公開 brief、成品和真實畫面可以當可重現參照。
- 美術沒有由使用者看過前不打「通過」。截圖只說明成品樣貌可查，不替代親自評估。
- **Elderwood Realms 不列入。**下線、後續玩家擴展與相似原作造成方法與可檢閱問題；保存可防止未來把「demo 一次生成」誤讀成「完整遊戲一次生成」。

## 重查條件

若 DASH / DINNER 作者公開無 follow-up 的原始 run、明確首版快照或完整系統測試，提升其現有證據等級；若用戶實際看過美術，更新「待檢」狀態。若同類在 GPT-6.1 Sol 或更近期模型上出現可追溯完整 build，保留同題 prompt 作新模型同 brief 重跑，不重查低價值手機遊戲 gallery。
