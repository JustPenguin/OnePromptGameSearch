# 搜尋批次 S-20261006-13：最新 AgentGames 模型輸出

**日期：**2026-10-06（台北時間）  
**研究問題：**AgentGames 新近可玩的 GPT-6.1 Sol／Claude Opus 5.5 輸出中，是否有高系統密度、公開 brief，並能直接作為當前模型一次委託測試的案例？

## 開始前查重

查了根索引、候選頁、目錄及 AgentGames 現有紀錄。已有 TETHER（G0152）、Crowd Rush（G0042）、PATCH（G0200）、DASH/DINNER（G0209）和多項 AgentGames 方法紀錄。本批只對新增名稱建檔，更新平台結果只在其既有記錄已不足以使用時觸發。

## 搜尋及查閱

| 實際 query／來源 | 查到什麼 | 判斷與限制 |
|---|---|---|
| `site:agentgames.dev/play "GPT-6.1 Sol" "game" prompt`、`site:agentgames.dev/play "GPT-6 Astra" "RPG" prompt game playable`；[Afterlight 作者頁](https://agentgames.dev/play/afterlight)、[playable build](https://play.agentgames.dev/g/g_5bDBTNoVMJLfPNeZ/index.html) | 新近 GPT-6.1 Sol／Codex desktop high run，日期 2026-10-01 UTC；作者 prompt、實際 9 場 roguelite、三角色、三個不同 boss、局內疊加強化、永久成長和 device save 都公開。約 41 分鐘。頁面列 4.78M 記錄 token（多數 cached）及 $1.52 text-token hypothetical estimate，非實際帳單。prompt 自由選題，具體要求自創完整 progression game、遊戲內程序圖像／合成音、行動控制和自主驗證。 | 新增 G0211，作為 GPT-6.1 Sol 新候選。沒原始 session/no-follow-up trace；遊戲頁不獨立證明人類從未追加。精美 key art 是遊戲設定插圖，gameplay 是程序 Canvas，需直接看實玩畫面後才知道美術是否合格。屬具 9 次遭遇的動作 roguelite，不是廣闊探索型長遊戲。 |
| `site:agentgames.dev/play "GPT-6 Astra" "simulation game" playable prompt`、`site:agentgames.dev/play delivery game GPT-6 Astra prompt`；重查既有 TETHER、DASH/DINNER | DASH/DINNER 於 S12 剛完成查核；TETHER 原已有 prompt、五區／18 upgrades、bot economy/difficulty run simulation、review agent／regression tests，明確標 provenance 未核。 | 不重複建項目。TETHER 仍是比 DASH/DINNER 更偏物理手感／長程 progression 的系統壓力副題；若需要這類測試，應讀 G0152。 |
| AgentGames newest feed；`site:agentgames.dev/play progression game prompt GPT-6.1 Sol` | BLOCKHEAD 2 的搜尋結果摘要與頁面現況模型名不一致。直接開 canonical 頁目前標 Claude Opus 5.5、18 min、270K tokens；prompt 要求把一款已存在的 BLOCKHEAD engine（單關、無盡 wave）擴為 12 關 campaign。VOIDLINE 是有 3D neon visual、phase shifting 與 combo 的 endless tunnel racer，prompt 僅要求此單一反射循環。 | 新增 G0212 保存 BLOCKHEAD 的既有 engine 限制和 SERP/model mismatch，排除 blank-start 上限樣本；它可用於「擴建既有專案」測試，不是從需求創作完整新遊戲。VOIDLINE 題目太窄且只有 endless score loop，不列候選，避免以建模美術代替遊戲系統深度。 |
| [AgentGames Afterlight GPT-6.1 Sol](https://agentgames.dev/play/afterlight)；[current Crowd Rush](https://agentgames.dev/play/crowd-rush) | Afterlight 頁明確公開 AI 選題 prompt；Crowd Rush 已在 G0042 記錄，其 prompt 有 explicit revision／保留現成 30 關架構，不能當 blank-start。 | Crowd Rush 延用既有 G0042 待核實判斷；不要將 revision 成品算作一次完整生成。 |

## 本批結論

- Afterlight 是本批最值得保存的最新模型輸出：清楚的自創 brief、直接 playable、九場 encounter 和跨 run progression，足以讓一則 prompt 同時暴露戰鬥、升級、boss、行動操作與存檔問題；作者還列了 Playwright 自主檢查要求。可作目前模型重跑備選，**但無人介入 provenance 尚未獨立確認、美術需使用者看 gameplay**。
- BLOCKHEAD 2 公開版本其實是基於現存專案擴建；SERP 過時摘要也將 model 標錯，故以 creator page 的 canonical data 為準並排除作 blank-start sample。
- TETHER 已由 G0152 保存，避免因近期目錄查詢再建重複項；其系統深度高，但作者未聲明無人類 follow-up。
- VOIDLINE 有實際 3D 成品，但單一 endless reaction loop 不符合「上限差距」主題，故不加入候選頁。

## 重查條件

取得 Afterlight 的完整原始對話、凍結版 build、作者 no-follow-up 說明，或後續 GPT-6.1 Sol 的同題新 build 時更新 G0211；若使用者檢查過畫面則補記視覺判斷。AgentGames 搜尋摘要與遊戲頁若再不一致，始終引用頁面內作者 model／prompt 標籤並將版本差異記入來源紀錄。
