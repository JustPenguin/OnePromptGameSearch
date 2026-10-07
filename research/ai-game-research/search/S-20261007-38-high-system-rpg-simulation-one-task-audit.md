# 搜尋批次：S-20261007-38-high-system-rpg-simulation-one-task-audit

**日期／範圍：**2026-10-07。沿 S37「近期 3D 物理／自主 QA」之後，轉查高系統 RPG／模擬作品，尋找近期模型從單一使用者任務自主做到最終可玩成品的公開證據；同時找能展示任務規格與真實 build 的重跑種子。

## 研究問題與先前查重

重讀根目錄索引、候選摘要、搜尋索引及 S37。核對既有 [G0225 Hollowflux](../records/G0225.md)、[G0242 Phantasy Codex Adventure](../records/G0242.md)、[G0056 Fast Food Tycoon](../records/G0056.md)、[G0226 Void Explorer](../records/G0226.md)、官方 GPT-6 Astra game showcase，以及 [G0143 Slipstream](../records/G0143.md)。查重確認 Reactor Town、The Legend of Deller、MiniTown、Theme Park Builder 均無現存項目；Reactor Town 新增為 [G0251](../records/G0251.md)。

## 實際搜尋與查閱

| query／網址 | 結果與證據 | 關聯固定編號 | 後續／重查條件 |
|---|---|---|---|
| `GPT-6.1 Sol full RPG game generated autonomous playtest source one prompt 2026 game`；`GPT-6 Astra complete RPG simulation game generated single prompt source playable AI self playtest October 2026`；`Claude Opus 5.5 high effort full RPG game AI self playtest source task run transcript 2026` | 沒找到可核實的更新模型單任務長流程 RPG 首版交件及完整 session 的直接證據。搜尋導向官方展示、作者 case study 和社群貼文；不得把長期 goal／人工回饋誤標為 one-shot。 | G0225、G0242、G0056 | 新模型發布可玩的完整 RPG／模擬且提供初始任務、run trace 或未經人類 feedback 的首版時重查。 |
| `"I made a mobile game in a single day" GPT-6 Astra "SimCity" "Powder Toy"`；`"complete, installable APK" "meaningful tests" GPT-6 Astra mobile game`；[Reactor Town Reddit 原文](https://www.reddit.com/r/ChatGPT/comments/1wzjskb/i_made_a_mobile_game_in_a_single_day/) | 找到高系統密度 Android town／reactor simulation；作者描述需求電力、城市經濟與成長、熱／冷卻／蒸汽／電路／控制棒，並申報 APK、source、測試。作者也明言自己玩 build、傳截圖與具體回饋，後續持續精修；因此不符嚴格的一次委託成績。逐字原始 brief、APK/source URL、完整 trace、首輪凍結版未確認。 | G0251 | 作者公開 artifact／repo 和首輪 build 後，核實模型版本、日期、完整 prompt、人工介入前後差異及測試。 |
| `"The Legend of Deller" "GPT-6 ASTRA" Codex 842-message conversation archive source`；`The Legend of Deller GPT-6 Astra 842 messages 339 developer messages`；[PicoBerry case study](https://picoberry.ai/gpt-6-astra-game-development) | 有可玩 browser action RPG、source／外部 GLB 資產工作流描述及 demo。作者披露約 12 小時、跨 4 天、對話記錄 842 則（其中 339 則 developer）、多輪場景／戰鬥／美術修改、手動放置最終物件，且依賴 PicoBerry 生成角色資產。作品可作 agentic 3D RPG 案例，但公開成品不代表單次無人介入交件。 | —（查重無既有記錄；不建立候選） | 除非公開可分離的初始 prompt 與未受後續修改的 build，否則不需重查其 one-shot 資格。 |
| `site:agentgames.dev/play RPG simulation GPT-6.1 Sol 2026`；`site:github.com "Astra" "full RPG" "playable" "single prompt" game` | 未找到符合長流程系統複雜度且有完整一次任務證據的新候選。找到／交叉確認的線索多為窄循環、參考案例或缺少來源流程。 | G0242、G0211 | 以新的可玩模型 build、原始 prompt 或 run artifact 作觸發條件。 |
| `site:openai.com/index GPT-6 Astra game RPG simulation game build showcase`；`site:developers.openai.com/showcase GPT-6 Astra game RPG simulation game`；[OpenAI Games showcase](https://developers.openai.com/showcase/games?app_type=game&use_case=games) | 官方頁現列 MiniTown、Theme Park Builder、Phantasy Codex Adventure 等互動遊戲。MiniTown 初始城市模擬任務後有七個建置階段；Theme Park Builder 有六輪；Phantasy Codex Adventure 有 ongoing goal 與後續多階段擴建。前兩者是較小系統的 brief／迭代參考，Phantasy 已有 G0242；皆非已證明的一次使用者委託凍結成果。 | G0242 | 若能分離初始 build 並明確證明後續迭代全由模型自主完成，可作 agentic run，不改變原作非 one-shot 的判定。 |
| `site:developers.openai.com/showcase/minitown MiniTown GPT Codex city sim`；OpenAI [MiniTown](https://developers.openai.com/showcase/minitown)；[Theme Park Builder](https://developers.openai.com/showcase/theme-park-builder)；[Phantasy Codex Adventure](https://developers.openai.com/showcase/phantasy-codex-adventure) | MiniTown brief 包含住宅／商業／工業區、自動道路、通勤、建築成長、晝夜與查看居民，適合城市模擬任務設計；官方歷程呈現反覆 build。Theme Park Builder 以小型等角樂園管理為題，迭代六階段但範圍較小。Phantasy 已記錄為 GPT-5.6 Codex 長流程 RPG、多階段 Goal 成品參照，不重複建檔。 | G0242 | MiniTown 若有新模型空白起始、一個 prompt、停止時 build 及完整 trace，再評估升為 run 案例。 |
| `site:reddit.com "gpt6-astra-one-shot-games" Mosswing Melon Lab`；`GPT-6 Astra one shot game prompts 2026 Mosswing Melon Lab`；[公開 repo](https://github.com/Ayi1337/gpt6-astra-one-shot-games)；[prompt 說明](https://www.terapep.com/blog/gpt-6-astra-one-shot-game-prompts-2026/) | 找到兩款聲稱 one-shot 且有原始 prompt／單檔可玩成果：Mosswing 是 tap-to-flap 3D endless runner，prompt 明確要求一檔、可立即玩、原創角色／世界與完成感，repo 記約 21 分鐘 xhigh；Melon Lab 是半流體水果合併小遊戲，prompt 要求盡速完成。比空泛一行 prompt 可重現，但玩法循環短、內容範圍小，不足以測長流程／多系統上限。耗時與 one-shot 歷程來自作者存檔，不是獨立 trace。 | —（查重未命中；不納入高上限候選） | 可引用 Mosswing 的 prompt 寫法作短題對照；若作者公開長流程同等證據，再另行評估。 |

## 結論與更新去向

- 未找到新的、已公開可核實的近期模型長流程 RPG／模擬 one-shot 成績；不把迭代展示或窄 arcade 遊戲充作上限案例。
- Reactor Town 系統複雜度很有價值，保留作待查任務線索 [G0251](../records/G0251.md)，明確標記作者有人工回饋，暫不進候選／檢閱頁。
- The Legend of Deller 是高完成度 agentic RPG 案例，但 842 則對話、約 12 小時與人工介入不符合使用者的一次委託驗收定義；不新增紀錄，避免把 case study 重複包裝成 one-shot。
- MiniTown／Theme Park 是官方任務與迭代參照；Phantasy Codex Adventure 沿用 G0242。Mosswing／Melon Lab 是有 prompt 和 build 的真 one-shot 小遊戲例證，但難度不足，不升為高上限候選。
- 索引新增 S38；精選摘要與 HTML 不變，因本輪沒有符合入選門檻的新候選。
- 下一個具體查找方向：回訪 Reactor Town 發布者的 repo／APK／原始 trace；另查有公開完成 build 的當前模型大型模擬、開放世界 RPG 或管理遊戲，優先一手 task artifact 與實際 run archive。
