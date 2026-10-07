# 搜尋批次：Historical Flight 發布歷史與美術素材來源追查

**日期／範圍：**2026-10-07。承接 S82 指明的 G0289 待查線索，查作者 GitHub public repo 的建立／提交／release 時序、被省略的 production files、素材清單與公開作者帳號。目的在區分「可玩的近期高完成度視覺作品」和「可歸因於模型的一次生成輸出」；不重做 S82 的一般 repo discovery。

## 實際查詢與檢視來源

| 查詢／來源 | 實際查看與結果 | 判斷 |
|---|---|---|
| GitHub REST API `GET /repos/itsleon21/historical-flight-contribute`、`GET /repos/itsleon21/historical-flight-contribute/commits?per_page=100`、`GET /repos/itsleon21/historical-flight-contribute/releases`、`GET /repos/itsleon21/historical-flight-contribute/branches` | repo 的 `created_at` 為 2026-10-01 04:33Z。`main` 上可見五個 commits：13:24 初始化受限 contribution repo；13:30 發佈 audited optimization source；16:35 發佈 playable Pages；16:47 修正 Pages assets；21:23 加雙語 guide/gallery。API 沒有 release，只有 main branch。 | 這組歷史只能還原對外發布包，第一個 commit 本身已是 restricted contribution repository；它不是完整遊戲的 build chronology，不能證明模型生成何時發生或是否一次完成。 |
| `git clone https://github.com/itsleon21/historical-flight-contribute.git`；檢視 `README.en.md`、`WITHHELD_FILES.json`、`CONTRIBUTING.md`、`docs/publication/AUDIT.md` | README 稱這是 reviewed browser runtime edition；完整 production project、original source models 和中間製作檔不公開。`WITHHELD_FILES.json` 列 12 個 withheld source modules，以及 `public/audio`、`public/assets`、`public/geodata`，並說所有聲音／美術／地理製作 scripts 不公開。README 把現行 repo 稱為 “a little game made by gpt-6 astra”，但沒有原始任務或 session。 | GPT-6 Astra 仍只是作者 attribution。公開 source contribution bundle 不能獨立 build 完整遊戲，無法檢查生成時工具、人工介入和凍結交件。 |
| repo `ASSETS.md`、`ASSET_POLICY.md`、`CREDITS.md`、`site/assets/manifest.json`、運行時 license files；`docs/publication/AUDIT.md` | manifest 登記 42 項實際交付資產。文件將 Kenney Nature Kit、Poly Haven 法線、Farmland 等第三方資產、IGN/BAN 地理資料，與受限使用的原創飛機／儀表／場景／農田圖集分開。地理資料日期 2026-09-22；原創 144 秒配樂使用 CC0 樂器採樣但整體編曲／混音受限；28 段僚機語音為 Kokoro v1.0 bm_george 合成。 | 素材來源可細分，提升 G0289 的作品／資產證據；卻無法確定各自由人或模型製作。遊戲高完成度視覺不能直接當作 Astra 原創美術能力證明。 |
| GitHub Users API `GET /users/itsleon21`、`GET /users/itsleon21/repos?per_page=100` | 公開 profile 無 bio、外部首頁或 Twitter 欄位，列出的公開 repo 只有此 contribution repo。 | 本方向未找到能把 public contribution repo 接回完整 production source、初始 prompt 或 session 的公開連結。沒有把「沒有搜到」升格成全網不存在。 |

## 結果

- 補強 G0289 的資產與發布歷史：公開版不是完整 production project，發布 commits 不是原始模型工作歷程；保留 3D flight visual/task reference，仍排除 strict one-shot 成績。
- 新資料揭露第三方素材、公開地理資料和受限原創素材分層，卻沒有原創資產的製作紀錄或 AI/人工歸屬。故這是**顯著補強作品美術素材 provenance**，不是新強候選，也不能把素材精緻度歸給 GPT-6 Astra。
- 目前 no-gain 方向計數自 S83 重設為 **0／至少 3**。需在後續至少三個彼此不同的新方向中，均沒有新強候選且沒有顯著補強案例，方可重新考慮告一段落；仍有其他未查線索時繼續研究。
- 下一方向：查近期公開 3D game generation benchmark 的實際 gameplay artifact 是否可對回具體模型／任務版本／原始輸出，特別是 2026 年第三季後的 UE5／browser 3D 建置；不重複 S81 的 release roster 概覽。
