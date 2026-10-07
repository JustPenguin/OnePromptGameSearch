# 搜尋批次 S-20261006-11：近期 one-shot 遊戲新線索

**日期：**2026-10-06（台北時間）  
**問題：**近期的新模型遊戲展示中，是否有帶真實成品畫面、具一定遊戲系統深度的案例；它們能否作為一次輸入後只驗收 AI 最終交件的評測證據？

## 開始前查重

查索引、精選候選、全目錄、search/index 及 S10；搜尋 `Survive the Sprint`、`endjineers`、作者網域，沒有舊紀錄。以 G0208 記錄，避免之後重複查同文／同 build。

## 搜尋與查閱

| 實際 query／來源 | 查到什麼 | 判斷／重查條件 |
|---|---|---|
| `"GPT-6.1 Sol" game build one prompt playable game October 2026`; `"Claude Opus 5.5" game "one prompt" playable build 2026`; `"one-shot" AI generated game playable demo GPT-6 Astra September October 2026 game build`; `site:github.com game GPT-6.1 Sol Codex game playable one shot` | 找到 endjin 於 2026-10-06 發表的 [Survive the Sprint](https://endjin.com/blog/introducing-survive-the-sprint)：Claude Opus 5.5 Max，作者稱一則 prompt 產生大部分首版，現有[可玩版](https://endjin.com/survive-the-sprint)、人物 sprite、遊戲 GIF 和宣傳影片。作品三段 survivor-like 戰役、三位 boss、11 個角色，含武器演化／perk／synergy／成就。 | 文章明說從 playable first version 後，經「fair bit of back and forth」加入角色特殊技、更多內容、效能改進、平衡、bug 修復和測試。沒有凍結首版或 prompt transcript；公開美術及成品不能歸功於 one-shot。新增 G0208，待核實，不列精選。首版原始檔／影片若公開則重查。 |
| `"GPT-6.1 Sol" game build one prompt playable game October 2026`；[Game Bench 相關近期結果](https://game-bench.piccini.app/) | 導回既有 Game Bench（B0009）及 Single HTML Game Bench（G0137/B0036）等已記案例，沒有比 S10 roster 更新的高深度新 run。 | 依 B0009／B0036／G0137 留存；不另建重複項目。 |
| `"Claude Opus 5.5" game "one prompt" playable build 2026`；[PowerHub Sonnet 5.5 vs Opus 5.5 kart test](https://powerhub.dev/blog/sonnet-opus-5-5-kart-game-test)；社群結果 | PowerHub 9/30 報導 9/29 創作者影片，一 prompt、各一次，Sonnet 5.5 約 58:24／411K tokens、Opus 5.5 約 79 分鐘／428K tokens；影片可看到兩款 3D kart 遊玩。PowerHub 自己只查看自動轉錄與兩處影片片段、沒有親自玩 build。 | 舊台帳已有 G0123，同文補證後改為方法參考／不列候選：缺 exact prompt、努力設定、下載成品、完整對話和獨立 playtest，題型又與證據更足的 Kart Blitz 重複。只可參考「首輪後修改也應計入總成本」的方法建議，不可當模型比較結果。 |
| `"Claude Opus 5.5" game "one prompt" playable build 2026`；社群結果 | 命中先前已收錄的 Kart Blitz（G0080）、若干只有單句自述但缺 task transcript 的短 demo，以及有明確中途回饋的案例。 | 不新增較弱或已知重複例。若作者後續補出 exact original prompt、原始 build、實際模型 trace，再逐案重查。 |

## 本批結論

Survive the Sprint 值得保存，因為它是當日新發布、可直接遊玩的 multi-stage survivor-like，有真實成品圖像和具體原始版本敘述。但文章展示的是多輪人類協作後的成品，而使用者要比較的是不受途中人類干預的最後 AI 交付；故它不是一個有效的 one-shot benchmark sample。現階段不以美術／完成度作候選推薦，也不把迭代版成果當作原始 run 證據。PowerHub 卡丁車比較同樣不升候選：題材重疊但公開證據不如已核 Kart Blitz，文章作者也沒實玩 build。

其餘結果屬先前項目，避免重覆整理。持續研究方向：追 10 月更新的 GPT-6.1 Sol／Opus 5.5 高系統深度可玩輸出，但先要求能識別原始任務、prompt 後 frozen artifact 或可稽核 trace；若只有成品展演，留在參考層。
