# 搜尋批次：近期 coding agent 的公開遊戲 repo 與實機畫面

**日期／範圍：**2026-10-07。第三個與 S91/S92 不同的方向：以公開 GitHub repo search 掃描 2026-08-01 以來的 GPT-6/Codex/Claude Code 遊戲開發 repo，再查命中項的 README、commit history、原始 art direction、實機 screenshot 與任務 provenance。目標是找近期有來源可查的 playable artifact；只納入證據實際支持的結論。

## 研究問題與先前查重

先讀研究索引、候選摘要、搜尋索引及 S91/S92；在 repo lookup 中查 `Generational Survival Australia`、`GameForge AI`。沒有既有對應記錄。這是作者 repository／firsthand project search，與前兩批的 arXiv 人類偏好量表、玩家共創研究方向不同。

## 實際搜尋與查閱

| 實際 query／來源 | 查看內容與結果 | 納入／排除理由 |
|---|---|---|
| GitHub REST repository search `q="GPT-6 game generation created:>2026-08-01"`, sort updated desc, 10 results | 一筆 repo：[`Shane-Currie/Generational_Survival_Australia`](https://github.com/Shane-Currie/Generational_Survival_Australia)，description 稱 GPT-6 + Godot；repo created 2026-09-09。 | 進一步查 README、art direction、changelog、樹狀檔案、commit API、gameplay screenshots；建立 [G0298](../records/G0298.md) 為排除的近期 AI-assisted project，而非 one-shot 候選。 |
| 同 repo `GET /contents`、`GET /git/trees/main?recursive=1`、`GET /commits?per_page=5`；讀 raw `README.md`、`ART_DIRECTION.md`、`CHANGELOG.md` | Source 提供 Godot 4 game、2D walking/driving、交通燈與 NPC、map UI、地圖／車流工具及多個 geometry/runtime verification 文件。README 稱有 3,458 building footprints、4,009 address points；ART_DIRECTION 說美術依使用者的原始地圖 screenshot 並由 repo 作者畫 original art。GitHub history 只有初始 v1.3 prototype commit 及 README 更新；沒有 prompt、agent transcript、精確模型 snapshot 或 zero-intervention trace。Changelog 條目描述多個按日期／stage 的開發更動。 | 是高密度 2D map/traffic systems 實作，但完整 repo 與兩次 commit 不等於一次 prompt。可能有多輪 GPT-assisted development 與人工方向；不把作者 GPT-6 attribution 擴寫成單次生成。 |
| 下載並直接查看 [`preview.png`](https://github.com/Shane-Currie/Generational_Survival_Australia/blob/main/assets/towns/central_wodonga/previews/preview.png)（384×216）、[`overview.png`](https://github.com/Shane-Currie/Generational_Survival_Australia/blob/main/assets/towns/central_wodonga/previews/overview.png)、[`driving_camera_preview.png`](https://github.com/Shane-Currie/Generational_Survival_Australia/blob/main/assets/towns/central_wodonga/previews/driving_camera_preview.png) | preview 顯示頂視角道路、像素人物、樹與水塔；overview 是地圖視野。它不是高細節 3D／接近 3A 內容；多個靜態圖和 task/session 不同時缺席，不可從 repo README 的系統規格推定遊戲 art 或可玩品質。 | 僅存 source screenshot links 作畫面／任務參考；研究者不代替使用者評美術。因不符合本輪高美術方向且 one-shot 證據缺，G0298 狀態明確寫「使用者美術未評」。 |
| GitHub REST repository search `q="Codex generated game demo created:>2026-08-01"`；`q="Claude Code game generation 3D created:>2026-08-01"` | Codex 查詢 0 項；Claude Code 只命中 [`YuskiAlizer/gameforge-ai`](https://github.com/YuskiAlizer/gameforge-ai)。讀其 repo tree、README、commit API；10/05 建立且只有一個 commit。README 自稱可組合 Claude Code、Hunyuan3D、Unreal、Story/Gameplay/Code/Asset/QA agents，需在本機安裝多套工具。 | 這是生成工具／軟體 repo，不是可查的具名遊戲成品或 playable output；沒有預製 game artifact、原始任務或模型 run。保留在批次排除項，不建立作品候選或 catalog record。 |
| GitHub REST repository search `q="AI agent one shot game created:>2026-08-01"` | 0 repository results。 | 記錄 query 無命中；不聲稱 GitHub 以外不存在相關成果。 |

## 結論、計數與下一步

- 收錄 G0298 為來源可查的近期 GPT-6-assisted 2D Godot project 排除紀錄：系統建置量大，但缺 initial task/session/無介入證據，畫面是簡潔 pixel map，也不是本輪目標的 high-art 成品。GameForge AI 是生成工具，無可評作品；Codex repo query 無結果。
- 沒有新強 one-shot 候選、沒有新高美術生成成品，也沒有提升既有 case 的一手證據。S90 後第三個彼此不同無增益方向：**3／至少 3**；這完成最低回看數，不代表研究已完整。近期實際生成案例和主要基準仍需持續覆查，研究 goal 保持進行中。
- 下一方向：回到高端 3D playable work，查近期 AI game generation／coding model 的官方來源 repo、作者具名 demo 與完整 gameplay captures；逐個和 C0027、C0013、B0055 去重，優先追 prompt/session/frozen build，不重新掃一般 GitHub repo 關鍵詞。

<!-- record-meta: {"id":"S-20261007-93","type":"search","updated":"2026-10-07"} -->
