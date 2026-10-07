# 搜尋批次 S42：近期模型高複雜度遊戲 run 與重跑題種子

**日期／範圍：**2026-10-07；追查近期 Opus 5.5、Sonnet 5.5、GPT-6.1 Sol 與 Gemini 4 Argon 的可用性、公開遊戲輸出、原 prompt、影片/build/session；補強使用者可直接檢視的高複雜度候選。

## 研究問題與先前查重

先前 S41 已記錄 Muse Spark 1.3 的四個案例，但該模型 2026-09-02 發布，至本批日期已非最新。查閱 [G0254–G0257](../catalog.html) 後，另查近期模型是否有原始任務和真實遊戲畫面。搜尋目標不是堆疊短小作品，而是找能形成完整遊玩循環、可用一份任務跨模型重跑的案例；同時把作者自述與可獨立核實的部分分開。

## 實際搜尋與查閱

| query／網址 | 結果與證據 | 關聯固定編號 | 後續／重查條件 |
|---|---|---|---|
| `site:jasonzhu.ai/en/prompts/claude-opus-5-5 battle royale Sonnet 5.5 Fortnite one prompt game September 2026`；[Fortnite-style game one-shot test](https://jasonzhu.ai/en/prompts/claude-opus-5-5/2104779190277181699) | 找到創作者原貼文的 curator mirror，附 445 字元原 prompt、約 42 秒遊戲錄影、2026-09-29 貼文日期；標示 Sonnet 5.5、約 2h54m。可看第三人稱角色、草地／城鎮、射擊 HUD。模型／單次生成／耗時是作者自述；沒有 source、可玩 build 或完整 trace。建立高複雜度重跑 seed，不計已驗證成績。 | [G0258](../records/G0258.md) | 若創作者公開 playable build、source 或 session export，再檢查 bot、建造、縮圈及勝負閉環是否真能工作。 |
| [原 X 貼文](https://x.com/mdaman010/status/2104779190277181699) 與[含 prompt 的回覆](https://x.com/mdaman010/status/2104779493974167949) | 核實 curator mirror 所附來源連結；原始社群頁面未作獨立 run 驗證。保留 curator mirror 供穩定閱讀，原貼文用來確認作者來源。 | [G0258](../records/G0258.md) | 若原貼文刪除／修改，保留 mirror 記錄並再次比對來源存檔。 |
| `site:anthropic.com Claude Sonnet 5.5 September 2026 announcement`；[Anthropic Sonnet 5.5 announcement](https://www.anthropic.com/claude-sonnet-5-5) | 官方資料顯示 Sonnet 5.5 於 2026-09-28 發布；因此比 S41 的 Muse Spark 1.3 更新。官方模型宣傳／能力頁不是遊戲 run 證據。 | [G0258](../records/G0258.md) | 每次正式重跑前再確認模型實際可選版本、介面及工具條件。 |
| `GPT-6.1 Sol release September 29 2026 official`；[OpenAI release index](https://openai.com/research/index/release/) | 官方索引記錄 GPT-6.1 Sol 於 2026-09-29 發布；本 query 未找到可核實的 GPT-6.1 Sol 高複雜度遊戲原 prompt、build 和 agent trace。 | — | 搜尋到完整原 prompt 加可玩輸出／影片時再建作品紀錄；只出現模型列表或簡單遊戲不列主題。 |
| `Gemini 4 Argon official trusted cyber defenders September 2026`；[Google official announcement](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/) | 官方說明只透過 Fairwind Program 向受信任資安防禦者逐步推出；截至本批未發現一般可重跑的公開遊戲案例。暫不列為可用於公開模型比較的候選。 | — | 一般使用者可取得、並出現可檢視遊戲 run 時再查。 |
| `2026 September October game built by Claude Opus 5.5 one prompt playable game prompt GitHub`；[awesome-opus-5.5-video](https://github.com/zhuyansen/awesome-opus-5.5-video) | 策展 repo 有大量影片線索；單有 gallery 數量不能證明一次委託，也不代表完整 playable build 或公平評分。本批只收錄有清楚原 prompt、畫面與來源連結的 Battle Royale 一例。 | [G0258](../records/G0258.md) | 逐項核對每個作品的原始 prompt、模型、影片/build、介入紀錄，不能把整庫概稱已驗證。 |
| `site:github.com "GPT-6.1 Sol" "game" one-shot playable prompt 2026`；`"GPT-6.1 Sol" one prompt game playable build October 2026` | 本次搜尋未得具備高複雜度、原 prompt、可玩 build 或遊戲錄影且流程可核的 GPT-6.1 Sol 新遊戲 run。跨系統 app 任務和一般模型公告不算遊戲案例。 | — | 維持待查；有新的官方模型展示或可回放 agent task 時再更新。 |
| `Anthropic announcement testers asked multiple Claude models make a game from one prompt September 2026`；`site:anthropic.com/news "one prompt" game Opus 5.5 game September 2026` | 找到 Sonnet 5.5 官方發布及模型資訊，但未找到官方發布的一次生成高複雜度遊戲基準／評分套件。 | — | 若官方公開跨模型固定任務或可重跑資料集，新增 benchmark 方式紀錄。 |

## 結論與更新去向

- 新增 [G0258](../records/G0258.md)：Sonnet 5.5 大逃殺原 brief／創作者自述 run。用途是高複雜度重跑題種子，並非已驗證 one-shot 成績；美術待使用者評價。
- 本批日期較新的可用候選模型包含 Sonnet 5.5 與 GPT-6.1 Sol；Google Gemini 4 Argon 尚只向受信任資安防禦者推出，故不把它當可公開重跑選項。
- 沒找到 GPT-6.1 Sol 的強遊戲 run；保留搜尋 query 與結果，避免下一批重做同樣搜尋。未新增簡單小遊戲充數。
- 下一步可在更近期的公開 run、agent harness 直接操作證據與同題跨模型可重跑性之間繼續找；Sonnet 5.5 Battle Royale 是目前本輪值得先檢視的高系統 seed。使用者未判定其美術。
