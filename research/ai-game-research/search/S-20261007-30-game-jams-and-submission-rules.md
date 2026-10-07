# S30｜AI Game Jam 規則與可核實提交物

**日期：**2026-10-07（台北時間）  
**研究問題：**公開 AI game jam 是否要求一次輸入、無人中途干預，或至少保留原始 build／互動方式？活動評審和作品能否成為高品質線索？  
**先前查重：**讀過 S29 設定的活動／browser-game jam 方向及 E0003 Jamference 紀錄。本輪重讀活動原始規則和提交頁，不把「使用 AI」等同「AI 單次完成」。

## 實際搜尋

- `AI game jam 2026 rules prompt generated game one prompt agent coding game jam submissions`
- `2026 browser game jam AI generated games Claude Code GPT game prompt session video`
- `AI game generation competition 2026 game jam rules human collaboration generative AI game entries`
- `site:itch.io/jam AI game jam 2026 game prompt coding agent`
- `"Jamference" "Cat and Robot" game submission`
- `site:itch.io "Jamference: AI Game Jam Hack 1" "Play in browser"`
- `site:itch.io/jam/jamference-ai-game-jam-hack-1/entries`

## 原始規則與活動狀態

| 活動 | 規則／材料 | 跟本任務的適用性 |
|---|---|---|
| Jamference: AI Game Jam Hack 1（E0003） | [官方 jam 頁](https://itch.io/jam/jamference-ai-game-jam-hack-1)、[主辦人公告](https://www.reddit.com/r/aigamedev/comments/1wvqfkq/the_ai_game_jam_has_started/)；主題 Cat and Robot、強制 restriction「所有輸入只能控制玩家移動」。10/02–10/09 為建置週，後續一週參賽者互玩互評 fun／AI use／polish；規則允許單 prompt 或整週製作，也允許 code／art／audio／agents 等任意 AI 工具，要求說明團隊分工。 | 是很好的**候選發現池**：它明確容許 single-prompt run，也有固定玩法限制和真實遊玩／整體 polish 評分；然而參賽者也可和人合作或用一週，提交規則沒有要求披露完整 prompt／session trace。目前（10/07）距提交截止約兩日，尚不能把分數或結果當已定稿。需待作品鎖版和互評結束，再按個別遊戲、prompt 與人類介入證據稽核。既有 E0003 更新，不另建活動項目。 |
| All Tools Allowed #2（Critics Arcade） | [活動／評分與提交清單](https://itch.io/jam/all-tools-allowed-2)：2026-09-11–14，23 entries、20 browser playable，參賽可混用 AI art/audio/coding agents／assets／人力；評 immersion／player experience／cohesion／theme。規則明言「obvious zero-effort single-prompt dumps may be removed」，鼓勵 craft／iteration。 | 雖然有高評分作品和 playable builds，賽制刻意排除／不鼓勵直接單 prompt dump，也沒有 run trace 要求；不適合作一次委託候選庫。只記作活動篩選的排除理由，不逐筆抄錄作品分數。 |
| Codex Game Jam 2026 | [官方 jam 規則及提交](https://itch.io/jam/codex-game-jam-2026)：72 小時後延長至一週、11 entries；主題「Human + AI, One Game」，主辦文字明言人可 steer vision、fix problems、add human input，並鼓勵公開流程。 | 明確是人機合作作品，不能把完成作品的美術／玩法結果歸因為使用者只輸入一次。排除作 strict one-shot run，但如參賽者自願公開單次 run 可獨立核對再納入。 |
| AI Browser Game Jam（Focaccai） | [官方規則／提交清單](https://itch.io/jam/ai-browser-game-jam)：2026-02-20–03-10，29 entries，鼓勵分享 prompts／tools／pipeline 但為 optional；browser playable 為主要目標。 | 可用來找可玩作品，但流程證據是選擇性提供，活動允許完整迭代；需要逐作品核原作者資料。未發現一款同時有高系統範圍、精確 run log 和可重現 one-shot 證據強過既有候選。 |
| Jamference 後續週期與其他 AI jams | Jamference 主辦公告稱之後每兩週開一輪；目前可確認的下一輪資料不完整。[Fully AI Game Jam](https://itch.io/jam/fully-ai)把人描述為 Architect／Prompt Engineer／Curator；[Gameotron Game Jam](https://itch.io/jam/gameotron-game-jam)以改造其 AI bot artifacts 為核心；[All Tools Allowed #2](https://itch.io/jam/all-tools-allowed-2)拒絕明顯的單 prompt dump。 | 只留可清楚辨認「一次使用者任務，AI 自己完成、測試修正」的活動 run。Fully AI／Gameotron 的協作定位和 All Tools Allowed 的規則目前不匹配；不追蹤它們的總排名。 |

## 個別作品線索

- **Robokitteh of SPLORR!!** 是 Jamference 活動作者頁上出現的 playable 作品線索（[作者 profile](https://itch.io/profile/thegrumpygamedev)）；目前找到的是 profile 對參加 jam 的關聯，尚無能核對它使用哪個模型、原始 prompt、run 次數或 AI／人力分工的提交說明。僅記為活動候選池線索，不建立遊戲紀錄、不推定單次完成或美術合格。
- 其他 Jamference 搜尋結果在 10/07 尚無足夠可索引的已完成提交物／完整證據；建置週未截止，這是時點限制而非「沒有其他參賽者」。
- AI Browser Game Jam、All Tools Allowed 與 Codex Game Jam 頁面有大量可玩遊戲，但賽制允許或期待長時間人機合作；活動總分不代表一次生成品質。沒有因分數高而升格項目。

## 研究結論與下一輪

公開 game jam 最有用的是提供一批可玩作品和人類遊玩回饋，不會自動提供零介入或一次 prompt 證明。S30 暫無新增強候選；E0003 Jamference 應待 10/09 截止、作品凍結和後續互評結果後，再用個別作者頁逐項查 prompt／工具／AI 自主程度。若有作者公開單次 session、凍結成果、可玩的成品和高完成度，它才可能成為好人選。活動參與人數／作品整體均分不能替代你的美術驗收。

- 更新 [E0003 Jamference](../records/E0003.md)，狀態保留為待作品鎖版後逐項查核的線索。
- 已有條件但不符合本任務者保留活動規則和排除理由；不為了湊項目數建入所有作品。

**下一輪不同方向：**回到高水準公開 browser-game / AI game jam 作品本身，挑一到兩個有可玩 build、任務規格和作者 run 記錄的參賽者深查；優先等 Jamference 鎖版後查一手投稿資料，再查 AI Browser Game Jam 的高完整度作品；排除明確多人／多週迭代。若來源沒有 session／人類輸入脈絡，即列為可借用 brief 或線索，不列已證實成績。
