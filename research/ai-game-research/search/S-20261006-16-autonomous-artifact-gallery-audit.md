# 搜尋批次 S-20261006-16：自主生成作品展示與完整任務交付追查

**日期：**2026-10-06（台北時間）  
**研究問題：**換到自主 Coding-agent 個人作品展與實測文章來源，找有新模型、清楚一次委託規格、具體遊戲成品與可核實交付條件的高挑戰任務；並避免漏掉舊目錄中只留待選名的項目。

## 查重

先查搜尋批次索引、全目錄與歷史段落。LLM Choice Experiments 尚無獨立目錄項目。AI Fire 的 Browser OS 及其 GTA／flight 子遊戲，舊資料已有[G0009–G0011](../catalog.html)及歷史來源，故更新原固定編號，不重複新增遊戲。

## 實際搜尋與查閱

| query／網址 | 結果與證據 | 關聯項目 | 判斷／重查條件 |
|---|---|---|---|
| "GPT-6.1 Sol" game "Codex" playable game prompt autonomous；site:billiem.uk/choice/ "GPT-6.1 Sol" games；[LLM Choice Experiments](https://billiem.uk/choice/) | 作品展自述收有 117 個 autonomous Codex artefact，但目前三個最新 GPT-6.1 Sol 條目（2026-10-01）是 sheet-cutting planner、fictional incident atlas、congestion model；不是遊戲。其 GPT-6 Astra／GPT-5.6 專項可見多款規則清楚的小型邏輯遊戲，但規模不符合此次上限篩選。沒有新的高複雜度遊戲候選。 | — | 當作自主交付的作品展示來源；下一次僅在出現新的 frontier-model game artifact 或發布 prompt／可玩成品時回查，避免重新掃整個舊作品清單。 |
| "GPT-6.1 Sol" browser games "one prompt" Codex October 2026；[AI Fire 10/01 GPT-6.1 Sol 實測](https://aiagentsflows.com/2026/10/01/🔥-i-tested-gpt-6-1-sol-inside-codex-on-3-hard-tasks-can-this-beat-claude-sonnet-5-5/) | 找到一段完整 one-prompt Browser OS 規格，要求至少五個互通 app、一款 GTA-style 城市沙盒、一款 3D checkpoint flight game，及自測修正；作者稱 Codex GPT-6.1 Sol 約 33m42s 完成並提供實際成品圖片。未見公開 source/build、可操作頁或 Codex trace。遊戲是 OS 內嵌子項，主測不是獨立遊戲生成。作者批評自身畫面不及 Sonnet 5.5 精緻。 | [G0009](../records/G0009.md)、[G0010](../records/G0010.md)、[G0011](../records/G0011.md) | 保留成跨系統一次委託的重跑 brief 參考，不列遊戲上限主測／playable 候選；之後若作者公開 build、錄影或 trace，再核實。已把舊待選紀錄補上直接來源及此用途判斷。 |
| "GPT-6.1 Sol Reasoning Effort Test 2 Builds same prompts Colosseum"；[SPECTRUM AI Labs 六種 reasoning 設定測試](https://spectrumailab.com/blog/gpt-6-1-sol-reasoning-effort-test-2026) | 作者以空白工作目錄、memory off，對六種 reasoning effort 各跑兩種相同任務：自我介紹網站與 Three.js Colosseum。公開 prompt、12 個 build、事件紀錄、耗時／token／程式碼盲審；但兩題都不是遊戲，故可供 harness 觀察，不是本研究的遊戲測試。 | — | 不轉為遊戲候選。若未來將同一隔離與凍結交付 protocol 用在遊戲任務，可借用流程細節。 |
| "GPT-6.1 Sol" "playable game" one prompt；[AI Agents Flows 10/01 三項測試](https://aiagentsflows.com/2026/10/01/🔥-i-tested-gpt-6-1-sol-inside-codex-on-3-hard-tasks-can-this-beat-claude-sonnet-5-5/) | 複核文章中的 Browser OS one-prompt 證據及輸出圖片；另一項 3D 室內重建及 robot arm simulation 均不是遊戲。該文系統任務和前項上位案例一致，不重複建第二次目錄紀錄。 | [G0009–G0011](../catalog.html) | 僅更新既有紀錄，避免將系統中的兩個遊戲誤計為兩個完整遊戲交付案例。 |

## 本輪結論

- 沒有新增符合遊戲專題、可檢閱完整交付與高挑戰度的新成品候選。
- AI Fire Browser OS 有重要的精確 one-shot prompt 和畫面，適合作為跨系統整合壓力任務的參照；然而缺公開 source／playable artifact，遊戲只是完整產品的一部分，故不升級為遊戲主測。
- 自主作品展與 reasoning-effort 程式實測沒有增加強候選；其「空工作目錄、事件日誌、盲審和凍結 build」可供重跑流程參考，沒有當遊戲表現證據。
- 已更新 G0009–G0011 的 direct sources、限制與現行用途，保留其原歷史段落；重建目錄後驗證 metadata 查找。

## 下一輪方向

1. 從新的模型作者／創作者發文尋找「自選題／低約束，但交付完整可玩遊戲」公開 run，優先追 Reddit、X／YouTube 和 demo 頁的首版建立記錄。
2. 找公開的 3D 角色／物理、策略管理或 RPG 大體量任務，逐作檢查是否只有 showcase 宣稱、是否已有可玩 build、prompt 是否改過。
3. 重新檢查 10/04 之後新增的作品與模型，不重做目前已查過的常規 GPT-6.1 Sol generic query。
