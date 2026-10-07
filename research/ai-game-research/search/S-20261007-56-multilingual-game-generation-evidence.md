# 搜尋批次 S56：中日韓 AI 遊戲生成實例與一手任務證據

**日期／範圍：**2026-10-07；分別以日文、韓文、繁體／簡體中文查找近期生成遊戲及公開實際 run。避開 S47 搜尋、S55 coding-platform gallery 與通用英語 GitHub 搜尋。

## 研究問題與查重

開始前重讀研究根索引、精選候選、搜尋索引、G0267 等相近紀錄，並以 `manage.py lookup` 查「夜巡录」及 `Night-Patrol`（皆無既有命中）。目標是補足英語以外作者公開的可玩成品、原任務或執行流程；策展 prompt 集、教學與多輪建置僅按其證據價值收錄，不將「AI 做的」等同一次委託。

## 實際搜尋與查閱

| 實際 query／來源 | 核查結果與判斷 | 關聯紀錄 | 待查條件 |
|---|---|---|---|
| DuckDuckGo HTML：`生成AI ゲーム 制作 一発生成 Claude Code Codex 2026 ゲーム プレイ可能`；[Note：Codex 與 Claude Code 做 2D 橫向動作遊戲](https://note.com/finite_archive/n/nf1c8a7aa00c2) | 2026-09-13 的實作筆記比較兩種 coding agent 做簡單 2D 橫向動作遊戲；未提供可核對的具名原始 prompt／凍結 build／完整任務或獨立評測，規模也偏小。不列候選。| — | 若後續有 public source/build 及原始 session 再查。|
| DuckDuckGo HTML：`AI coding agent ゲーム 1プロンプト playable game 2026 生成`；[Note：AI 建置指南](https://note.com/ai_builders_lab/n/n7a16364d5352) | 通用建置教學列多種工具與提示方式，沒有可辨識的一次任務及交付 artifact。排除作成績證據。| — | 有具名 frozen run 再重查。|
| DuckDuckGo HTML：`AI 코딩 에이전트 게임 한 번 프롬프트 playable 게임 2026`；[Astra 一行提示詞遊戲案例整理](https://scv1218.tistory.com/347) | HTTP 200 可讀。文內指出「一行提示」實際常是完整長任務，且快速原型仍需人工確認可玩性、權利及效能；所列 kaiju、minecraft-like、3D browser prompt 範例沒有相應具名 run/build/session。列方法／提示彙編，不列成績。| — | 若引用一手作者 run／live artifact，再逐項確認。|
| DuckDuckGo HTML：`GPT 一次提示詞 生成 遊戲 Codex 可玩 2026 源碼 AI`；[Toolin：Codex 一個下午做完整遊戲](https://toolin.ai/blog/codex-build-complete-game-in-one-afternoon)；[GitHub repo](https://github.com/op7418/Night-Patrol)；[release](https://github.com/op7418/Night-Patrol/releases)；[README](https://github.com/op7418/Night-Patrol/blob/main/README.md)；[planning](https://github.com/op7418/Night-Patrol/blob/main/docs/PLANNING.md)；[roadmap](https://github.com/op7418/Night-Patrol/blob/main/docs/FIRST_ACT_DEMO_ROADMAP.md)；[implementation](https://github.com/op7418/Night-Patrol/blob/main/docs/IMPLEMENTATION_DETAILS.md) | 文章稱《夜巡录：荒庙篇》以 Codex 製作、約四至六小時；最初 prompt 僅是要做類似《Slay the Spire》的模糊起點，原型之後有多次人工補充與迭代，素材還使用 GPT-Image 2.0、Seedance、Suno。repo 和 v0.2.1-demo release 可查；文件描述卡牌、資源連攜、地圖／事件／商店與第一幕 Boss 流程。最終 build 因有人類 follow-up 而不符合 strict one-shot；exact Codex 型號、完整 prompt／transcript、frozen prototype 均未公開。新增 G0268 作可重跑題種子，不列 shortlist。| 新增 [G0268](../records/G0268.md) | 若公開 session／prototype snapshot／人類指示時間線，拆出首版與最終版本證據；不然維持多輪參照。|
| DuckDuckGo HTML：`AI coder 游戏 一次生成 可玩完整游戏 GPT Codex 2026`；CSDN 搜尋命中「AI全流程制作游戏教程分享：Codex + GPT Image 2.0，从0开始完成一个可试玩游戏（附完整思路）」；[知乎武俠 MMO](https://zhuanlan.zhihu.com/p/2045788868771832847) | CSDN 原頁回 HTTP 521，未保留可確認的 canonical URL；知乎回 403，均無法檢查原文內容，僅保留為未核搜尋命中；不將搜尋摘要／標題視為證據。| — | 頁面可讀 mirror、repo 或可玩版本出現後再查。|

## 結論與更新去向

- 日文、韓文與中文搜尋沒有帶來新的強 one-shot 候選，也沒有顯著提升既有強案例的證據。
- G0268 是明確多輪 Codex 協作、有限第一幕的可玩牌組 roguelike；保存它是為了完整交代值得重跑的公開任務線索與排除理由，不把它湊進一次交付成績。故 S54 後無增益方向累計 **2／至少 3**（S55、S56）。
- 未核搜尋命中：CSDN HTTP 521、知乎 HTTP 403；待可讀來源，不聲稱已排除內容本身。
- 已更新 G0268、候選摘要的「其他線索」、搜尋索引與研究日誌；不更動短名單。下一方向先重讀三份索引，再查**AI 專用遊戲生成／prompt-to-game 產品的公開 gallery 和實際輸出 provenance**，與 coding-agent SaaS showcase 分開，檢驗能否取得具名高系統任務、原始第一次輸入及 frozen playable build。
