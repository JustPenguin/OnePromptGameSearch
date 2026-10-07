# 搜尋批次：S-20261007-39-current-model-high-system-community-games

**日期／範圍：**2026-10-07。延續 S38，改查近期 GPT-6 Astra／GPT-6.1 Sol／Claude Opus 5.5 社群高系統遊戲展示與 casebook，從可玩 build、任務、run 流程及 source 追查哪些值得列為一次任務候選，並把大型成品與 one-shot 證據分開。

## 研究問題與先前查重

重讀索引、候選頁、search/index 與 S38，查重 [G0251 Reactor Town](../records/G0251.md)、G0242、G0056、G0195、G0206、G0143 及 GPT-6 Astra 個案。確認 AGI Soon、Astra Attack、Funkatron MMOARPG、Little Acre 均無既有項目；前兩者新建 [G0252](../records/G0252.md) 與 [G0253](../records/G0253.md)。

## 實際搜尋與查閱

| query／網址 | 結果與證據 | 關聯固定編號 | 後續／重查條件 |
|---|---|---|---|
| `GPT-6.1 Sol game tycoon simulation management game playable source 2026 AI built`；`GPT-6 Astra city builder management simulation game playable source code 2026 Codex`；`Claude Opus 5.5 AI built full management sim game autonomous coding game 2026 playable`；`AI generated browser game colony sim management game one prompt 2026 GPT-6 Astra` | 一般搜尋未找到近期 Sol／Astra／Opus 具有明確 one-task provenance 的大型城市或 colony sim 首版成績。出現模型官方說明、方法文章及作者展示，需逐項讀來源才能確認流程。 | G0056、G0242、G0251 | 有原 prompt、run archive、首版交件而非僅最終迭代版時重查。 |
| `"Codex built the game, Codex plays the game" "1.5 days"`；[AGI Soon 作者貼文](https://www.reddit.com/r/codex/comments/1woa554/codex_built_the_game_codex_plays_the_game_codex/)；[可玩站](https://agi.dpa.plus/) | 作者稱 GPT-6 Astra/Codex 與 Blender MCP 在 1.5 天完成完整遊戲；先做 deterministic headless simulation，bots 跑數千局，可 replay／diff，並開放 agent API。作者也指出 onboarding／UX 仍需人眼。貼文沒有原始任務、session、repo 或確切使用者 prompt 數；「entirely with Astra」不等於一則委託後無人介入。列高價值自主 QA 待核 [G0252](../records/G0252.md)，不當已核實 one-shot。 | G0252 | 追查作者後續分享之 prompt、repo、歷程和人類修改情況；若能核實單一起始任務，可能成為高價值自我測試主題。 |
| `Astra Attack GPT-6 Astra browser FPS multiplayer prompt Korea Sudden Attack`；[作者 DCInside v2 貼文](https://gall.dcinside.com/mgallery/board/view/?id=ai_utilize&no=58556)；[實際 build](https://scar-flame.vercel.app/)；[第三方逐項檢視](https://www.terapep.com/blog/astra-attack-ai-browser-fps-2026/) | 有多人 FPS build、房間／配對、倉庫 4v4 與另一張 5v5 地圖、槍械瞄具、經驗與持久排名、練習場及 PWA。作者原貼已明稱 v2；沒有原 prompt、session 或 repo，第三方觀察到資產匯入腳本／版本記錄並核對 build。這是高系統多人 FPS 成品參照，但不是已驗證 one-shot。新增 [G0253](../records/G0253.md)。 | G0253、G0206 | 若取得作者原始聊天或 v1 artifact，查明最初 brief、修改節點和首版功能範圍。可借題重跑，不能引用為通過成績。 |
| `"Opus 5.5 changed gaming forever" "36 versions" RPG`；[Funkatron MMOARPG 作者貼文](https://www.reddit.com/r/ClaudeAI/comments/1wvxdxh/opus_55_changed_gaming_forever_i_gave_it_15_years/) | 作者展示含 8 個職業／技能樹、城鎮／區域／港口、地城、採集釣魚、天氣晝夜、多人／交易／PVP 的 16,500 行單檔 browser ARPG；但直接說一週 36 個版本、先餵十多年既有 lore，自己持續玩並提出修改。排除其最終版作 one-shot 成績；高系統題材可供另寫 brief 參照。 | —（無既有項目；不另建立 one-shot 記錄） | 只有出現可獨立檢視的首次交件與 task history 才重查。 |
| `"Astra Attack" "FMKorea" 봄바다 game Astra`；[DCInside 早期射擊場貼文](https://gall.dcinside.com/mgallery/board/view/?id=aidevelop&no=2044) | 確認同作者 2026-09-07 已發布 SCAR-H 練習場，隔日發布 v2 多人 FPS；外部流程分析另記錄首發 v2、長期 Pro 用量與無 prompt／repo。沒有證據可分離為一則任務後的首版成果。 | G0253 | 不重查，除非作者公開首版／prompt／trajectory。 |
| `"AGI Soon" "agi.dpa.plus" game codex Astra Reddit`；[一手作者貼文](https://www.reddit.com/r/codex/comments/1woa554/codex_built_the_game_codex_plays_the_game_codex/) | 核實貼文連結確實指向可玩遊戲；未找到可下載 repo 或 task archive。作者敘述「1.5 天」只說工作跨度，不能換算成單次模型回合。 | G0252 | 首個原始對話或 source archive 公開後重查。 |
| `"Little Acre" pocket-world builder GPT-6 Astra prompt game`；[casebook 頁](https://github.com/zlxxlz1026/awesome-gpt-6-astra-casebook/blob/main/docs/categories/games.md)；[Ottermind 條目](https://ottermind.ai/explore/gpt-6-astra/little-acre) | 公開 prompt 僅一句「build a small interactive 3D world from scratch」，結果含駕駛、放置建物／樹木、日夜和匯出。作者報告用掉五小時額度 55%，有人回報 lag；未找到可獨立遊玩的 playable URL，且系統規模仍小。列低上限／來源待核線索，不建候選。 | —（未達建檔／候選標準） | 只有公開可玩 build、任務與完整 run provenance 時才升級記錄。 |
| `site:github.com/zlxxlz1026/awesome-gpt-6-astra-casebook games one prompt RPG simulation`；[casebook 20 games](https://github.com/zlxxlz1026/awesome-gpt-6-astra-casebook/blob/main/docs/categories/games.md) | 個案庫含 20 個 Astra games／simulations。強題目線索包括 Windhaven fantasy island（但用 Tripo P2 供應 assets，成果偏可走動場景）、Voidrunner 3D combat racer（作者報 25 分鐘單 prompt、車種／武器／AI 對手）、construction machinery puzzle（作者原始 seed 短，但 repo 有 13 commits 和大量迭代，不能算 one-shot）、Ghost of Tsushima-style world（無 playable download）、一行 surreal climbing prototype。沒有新的多系統長流程 one-shot 且同時具可玩 build、原始 run trace。 | G0143、G0237；其餘未登錄 | 對 Voidrunner／Windhaven 找作者原始 post、完整提示及可玩連結；若具備可玩 build，再作視覺／短程副測評估，不冒充長流程主測。 |

## 結論與更新去向

- 本批發現並記錄 AGI Soon（G0252）與 Astra Attack（G0253）；前者是有潛力的自動模擬／QA 案例，但 one-task 證據不足；後者是高密度多人 FPS 成品參照，但作者版本線明示 v2、無 prompt／session，故不作一次委託成績。
- Funkatron MMOARPG 系統規模高，但一週 36 版本及作者持續修改已明確超出一次任務證據範圍；只作題材參照，不列候選。
- Astra casebook 有值得再查的 3D 對戰／場景短題，但沒有發現比當前長流程主題更合適的完整高上限候選。精選摘要與檢閱頁不更新。
- 下一方向：逐項回查 casebook 原始 X／作者鏈結和高系統 brief；優先找可玩 build、原始任務及首版／版本歷程同時存在的項目，並追 Reactor Town／AGI Soon 的作者是否釋出 source 或 transcript。
