# 搜尋批次 S-20261006-07：高系統密度成品與一次委託 provenance

**日期：**2026-10-06（台北時間）  
**範圍：**從最近公開的原始碼、prompt、session 證據、實際可玩版中尋找近期模型與高挑戰題型；避免重複一般作品集搜尋。判斷時將「候選題目適合重跑」與「原作者案例已證明 strict one-shot」分開。

## 開始前查重

讀取研究根索引、精選候選、完整目錄、歷史索引及 S-20261006-06。G0193 已記 Fable Cities；G0117 已保存 Frontier Games 的 Pelican 線索；G0063 已完整記錄 Sonnet 5.5 Fortnite prompt；G0075 是僅有歷史提名、無原帖的 Happy Wheels Bottle Run，不能直接與新找到的 Happy Wheels 案例合併。Fusedown、CrossFire Transport Ship、QQ Speed 及 Happy Wheels Fable 5 Max 先查當前目錄與搜尋索引，確認無同名／相同作者來源後才新增或更新。

## 實際搜尋與查閱

| 實際 query／網址 | 查到什麼與限制 | 去向／重查條件 |
|---|---|---|
| `"Fusedown" "Fable 5.1" game`、`"Fusedown" multiplayer game Claude build GitHub`、`"FUSEDOWN" battle royale game Claude 50 players`、`"fusedown.io" "prompt" Claude battle royale full prompt`、`"50-player browser battle royale" prompt Claude Fable`、`"bombs, crates, a shrinking arena" "prompt" Claude`、`site:github.com "Fusedown" Claude Fable` | 找到作者 Reddit 貼文，稱 Fable 5.1 依長 prompt 建立 50 人 bot 補位大逃殺、縮圈、物資強化、四分鐘回合、觸控及周邊網頁；貼文評論透露首版後收到玩法回饋並在多輪中修正，因此原案不符合無使用者介入。未找到原始 prompt、repo、完整對話或可驗收首版。當天直接開站曾回 521 Web Server Down，無法確認暫時可玩。 | 新增 [G0202](../records/G0202.md) 作為高系統密度重跑題來源；不列為 one-shot 成績。站點恢復、原始 message trace／source 公開時重查。 |
| [by_opus 原始 repo](https://github.com/chandan0000001/by_opus)；`"Claude Opus 5.5" one sentence single session games source prompt playable` | 新 repo 收錄三個 Opus 5.5 3D 遊戲：Pelican Bicycle、CrossFire: Transport Ship、QQ Speed。公開逐字單句 prompt、source、build 及作者的自動 QA 說明。README 聲稱一次 session、無人工改碼、無外部圖音素材；還列 320 秒 soak、headless input 與子代理 review。source 中能核對模組與遊戲結構，demo links 可直接開。找不到原始 session transcript，單次 session／QA細節仍是作者自述。 | 更新既有 [G0117](../records/G0117.md)；新增 [G0203](../records/G0203.md)、[G0204](../records/G0204.md)。作單句開放式 prompt 和中度複雜 3D 操控題的重跑參照；使用者美術驗收仍空白。若取得 session export、未編輯交付 hash 或獨立測試，再提升證據等級。 |
| [Fusedown 50-player post](https://www.reddit.com/r/ClaudeAI/comments/1w9t33d/asked_claude_fable_51_to_build_a_whole/)；[當前 demo](https://fusedown.io/) | 用 `Fusedown.io gameplay screenshot battle royale Mahir Taha`、`site:x.com fusedown.io browser battle royale Claude`、`site:github.com "Fusedown" Claude Fable` 等查圖／repo 未找到獨立成品錄影或來源碼。保存的貼文封面只是宣傳預覽，不當成遊戲畫面證據。 | 在 G0202 記錄缺證；不要把貼文封面誤當實際遊玩截圖。若作者補出錄影或 repo，再查。 |
| [Happy Wheels one-shot post](https://www.reddit.com/r/ClaudeAI/comments/1u29zj2/i_have_created_a_happy_wheels_replica_oneshot/)；`"Happy Wheels" "Fable 5" one-shot game Pogo` | 作者稱 Fable 5 Max／Max reasoning 用 `/goal` 執行約兩小時、耗掉 5 小時 Max x5 額度；單一 Pogo stickman 長關卡，首次完整通關約 25 分鐘。作者貼實玩影片，稱約 30 分鐘遊玩才找到角色傾斜可加速 bug。沒有原 prompt、source repo 或可持續遊玩的 build；物理與完成度評語是作者自評。 | 新增 [G0205](../records/G0205.md) 為物理專項副測，不併入舊 G0075。若找到 G0075 原帖證明同作，連結或合併需保留歷史編號。 |
| `2026 AI generated game one prompt autonomous game GitHub playable Claude Opus 5.5 game build`、`site:reddit.com/r/ClaudeAI "one prompt" game "playable" 2026`；[Poly Bridge run](https://www.reddit.com/r/ClaudeAI/comments/1w4ggam/i_tested_claudes_game_dev_capability_as_a/) | Poly Bridge 複刻具物理、材料、破壞、20+關和 475 個自動檢查的潛力；但發文者明確說週末期間偶爾傳「keep going／continue」，因此不是嚴格 one user request。留言說可放出完整 prompt，但這次查詢沒有找到 prompt 正文或 playable link。 | 嚴格測試排除；保留高難度物理橋樑／結構應力題型線索，等無追問 run 和 prompt／成品可查時再重看。 |
| [Aman 的 Fortnite-style prompt 收錄頁](https://jasonzhu.ai/en/prompts/claude-opus-5-5/2104779190277181699)；[Opus 5.5 showcase](https://github.com/theolundqvist/frontier-games) | 重遇 G0063 已有 445 字 Sonnet 5.5 Fortnite BR prompt 與約 2h54m 作者自述；本輪沒有新的 source／遊戲 build。作者已列槍戰、bot、建造、縮圈和小島，任務作為重跑 brief 的價值不因缺 model comparison 而下降。 | 不建立重複項目；保留現行 G0063，只有出現 source、可玩 build、QA 或更新模型 run 才補查。 |
| [Fable Cities 作者貼文](https://www.reddit.com/r/ClaudeCode/comments/1w4qziv/ok_this_is_wild_used_claude_fable_51_and_said/) | 複核 G0193 的成本與時長資訊：作者約報 14 代理、24 小時、US$203、297.7k input／1.9m output／118.2m cache-read／6.0m cache-write token；早期一小時影片只是三波 build 的第一波。仍屬作者自述，且 repo 本身另列視覺與效能失敗。 | 更新 G0193；作長時 multi-agent 題型對照，不與短 session 排名合併。 |
| [Descente 作者貼文](https://www.reddit.com/r/ClaudeAI/comments/1wqo6o5/i_gave_claude_a_detailed_game_spec_and_let_it/) | 近期搜尋命中：Opus 5.5 xhigh + Godot MCP，5h48／870k tokens、最多 800 敵人、200+ bot run。作者後續明確說他「asked him to make his bot more human」；也就是模型交付後又有使用者指示。既有 G0196 已記為 strict one-shot 排除。 | 只作方法／規格來源，不提升候選；確認既有排除適用。 |
| [Godot 3D chess roguelite](https://www.reddit.com/r/ClaudeAI/comments/1wp8uxb/i_gave_opus_55_four_reference_images_and_build/) | Opus 5.5 建立三幕 3D chess roguelite，9 場戰鬥、boss、18 relic、成長和搜尋型 AI；但作者坦白 first prompt + 4 張人工作參考圖後，還有燈光 feedback messages，且非嚴格 one prompt。 | 既有 Chainmate／圖片輸入研究脈絡可供重跑 brief；不作 strict one-shot 成績。 |

## 本批結論

- 找到兩個證據深度不同的方向。其一是「一句開放委託＋模型自行拓展」，by_opus repo 的三款可玩 3D 作品有原始 prompt、source、build 和 self-QA 敘述；其中 Pelican Bike 是物理／畫面／音效整合，CrossFire 是槍戰 bot 和地圖，QQ Speed 是四賽道漂移操控。其二是特定高挑戰玩法題：Fusedown 顯示大逃殺 multiplayer 系統的重跑 brief 潛力，但原 run 有回饋迭代；Happy Wheels 可作長關卡物理專項但缺 prompt/source/build；Poly Bridge 因作者偶爾要求繼續而 strict 排除。
- 本批沒有任何新成品由使用者確認美術通過。程序繪製、模組數、頁面自述都不等於美術驗收。
- 「one sentence」並非「小題目」：CrossFire、QQ Speed 和 Pelican 都是實際可玩、有多模組的 3D 成品；但相較固定且細密的 FALL LINE／Fable Cities brief，它們的自由度更大，評分應分開。建議比較至少分成：開放式創作題、固定規格跨系統題、物理專項題、長時自治題。
- 已更新 G0117、G0193 狀態／證據，新增 G0202–G0205；沒有把迭代展示冒稱為 strict one-shot。

## 下一輪

改以 source-verified 作品庫的逐個原始任務和 demo 核查為主，先從近期 Opus 5.5／GPT-6 Astra collection 中挑真正多系統、可玩、無明顯同作重複且具原始 prompt 的 3–5 件；不要把策展評分當品質證據，取得遊戲畫面後才評估是否有足夠視覺水準。再針對最近 frontier model 的作者原帖追查 prompt 與無人工介入證據。
