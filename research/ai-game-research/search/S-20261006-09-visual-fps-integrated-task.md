# 搜尋批次 S-20261006-09：直接可玩的視覺與 FPS 跨段整合題

**日期：**2026-10-06（台北時間）  
**問題：**有沒有 GPT-6 Astra 的一次任務案例，同時能直接檢視高品質 3D 畫面，且作品不是純場景展示，而是接上一款有目標、可玩且可重啟的遊戲？

## 開始前查重

讀研究索引、候選名錄與搜尋批次 S07–S08。已有 G0201 Call of Duty-style FPS detailed brief，但原始測試有 follow-up passes，且沒有 playable demo；G0203 CrossFire 有 3D FPS build，但短 prompt 對 visuals／match objectives 未明確指定，作者流程證據有限；G0206 Smash Karts Arena 有最好的一次任務 trajectory 和多人系統，但只能看實玩影片／自行搭 server。查 exact title／作者／test page 後沒有同作項目，再新增 Shift Zero。

## 實際搜尋與查閱

| query／來源 | 結果與證據等級 | 更新與重查條件 |
|---|---|---|
| `"GPT-6 Astra" "one prompt" game playable 3D GitHub September 2026`、`"1 prompt 1 run" GPT-6 Astra playable FPS Three.js`、`GPT-6 Astra one prompt high quality 3D FPS game models playable demo September 2026`、`GPT-6 Astra test high-quality textures weapon assembly playable FPS one run Codex` | 找到 Adam Holter 的 Model test 頁：[GunBench: Rifle Assembly and Alien Factory FPS](https://adam.holter.com/tests/rifle-factory-alien-invasion/)，明確列 1 prompt／1 run、GPT-6 Astra、Codex high effort、2026-09-04。完整 prompt 要求 3D weapons scroll assembly showcase + reusable asset model + coherent FPS start / objectives / combat / restart / self-verification。Primary page 同時連至 playable output 和 video。 | 新增 [G0207](../records/G0207.md) 為強視覺／FPS 跨段候選。作者沒有公開 session trace／repo；如後續 release 源碼、完整 transcript、未剪原始錄影，更新證據級別。 |
| [原始 test page](https://adam.holter.com/tests/rifle-factory-alien-invasion/)；[Shift Zero playable](https://adam.holter.com/tests/runs/2026-09-04-gpt-6-astra-rifle-factory-alien-invasion/index.html)；[run video](https://adam.holter.com/tests/runs/2026-09-04-gpt-6-astra-rifle-factory-alien-invasion/published-x-2095986388663439614.mp4) | 直接開啟 playable page 的可訪問文字可確認兩款模型選擇、組件展示、工廠場景、crew evacuation、維持電力、三波破口、FPS controls、pause/restart；作者影音 source 可取用，但 web extractor 無法解碼 mp4。X 原帖因 403 無法獨立讀取。成品是實際 playable website，不是截圖；未通關，沒有被研究方或使用者正式美術評分。 | 檢閱 HTML 新增頁面 iframe，讓使用者直接評畫面與遊戲。視覺應分開記錄模型金屬／木質部件、燈光、組裝動畫、工廠 readability 及射擊中的視效；不把 brief 要求寫成已驗收事實。 |
| `"Astra Attack" "GPT-6 Astra" one prompt 4v4 browser FPS playable source`；[第三方檢視](https://www.terapep.com/blog/astra-attack-ai-browser-fps-2026/) | 發現高品質多人 4v4/5v5 FPS playable site，但來源分析發現這是 v2、多輪迭代，作者新增持續更新、多個開源地圖 ports、伺服器與修正，原作者沒有說 one-shot；不是一次任務成績。可作對照其 multiplayer operations 需要什麼，但不符合嚴格 protocol。 | 保留 S09 search log 的排除；若要未來做「協作開發上限」再取材，不重建候選。 |
| `"LAST SIGNAL" "GPT-6 Astra" playable game prompt source`、[作品調查](https://www.terapep.com/blog/gpt-6-astra-community-built-programs-2026/) | 搜到一個高可玩、3D wave survival shooter，第三方實際開過 build；出現十個版本／patch archive，作者公開文案有修 bug 調難度，非單次交付。沒有可核實 strict one-shot trace。 | strict one-shot 排除。可作給新模型重跑的題材，不列既有成績。 |
| `"Voidrunner" "anti-gravity" GPT-6 Astra @superalesha`、`"Make me the most insane" high-speed anti-gravity combat racer Astra gameplay video`；[prompt record](https://ottermind.ai/explore/gpt-6-astra/voidrunner) | 有完整 3D combat racer prompt：漂移／boost／武器拾取、三種車體、空中賽道、AI 對手與 neon shaders；作者稱單次約 25 分鐘，曾以本機 Blender。資料庫明示 demo 僅為 X video，沒有 source repo／play URL，無法讓使用者真正通關驗收。 | 保留為現有作品庫之來源線索；若找到 playable output 或 source 再查，不超過 Shift Zero 的直接成品優勢。 |

## 本批結論

- Shift Zero 是本批最好的「讓使用者直接判斷美術是否足夠精緻」候選：產品式 3D 模型組裝介紹不止一張靜態圖，往下可以真的進入 FPS 工廠防守，且 prompt 明確指定資產重用、操作、目標和重新開始。可直接開 playable page；記錄應顯示這是實際作品而非 AI 形容句。
- One-shot provenance 只由 test page 的「1 prompt／1 run」欄位和一次 GPT-6 Astra run entry 支持；沒有原始 trajectory、source repo 或第三方確認零 follow-up。比 G0206 多人主 session 的逐訊息證據弱，應在模型能力總結裡保留這層差異。
- 大量美術要求不是成品品質證據。本輪不預先給它美術過關，改為把實際 playable iframe 和 run 頁提供給使用者自己看。
- 明確排除 Astra Attack、LAST SIGNAL 作既有 strict one-shot 結果：有可玩 build 不等於 one-shot，有高人氣不等於完整記錄。

## 下一輪方向

沿「直接 playable + exact task + current model」找非槍戰候選：科幻逃脫／卡牌 roguelike／策略建造或 3D 探索型；優先找模型自動測試與公開 build/frozen first delivery 同時存在的作品。對 Opus 5.5、GPT-6.1 Sol 等仍保留 model/date/version 檢查，避免只因不同模型名稱就重複收錄既有遊戲。
