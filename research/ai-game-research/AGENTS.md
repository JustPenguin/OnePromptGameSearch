# 本研究資料的維護規則

先讀 README.md 與根目錄的 ai-game-one-shot-index.md。使用者定義為一次委託、途中不介入，AI 可自行修正，驗收最後交付。模型比較不是必要門檻。

- 詳細資料更新固定編號的 records/紀錄；開始搜尋前查名稱、別名與來源網址。具名但排除／待核實項目也保存。疑似同作不能直接合併。
- 新搜尋各自建立 search/批次，保存實際 query、來源、結果、無結果、排除與重查條件，雙向連結項目並更新 search/index.md。
- 不改寫 history/sections/、inventory-*.json 及遷移 manifest／名稱對照；它們是既有研究的追溯材料。
- 不手改 catalog.md、catalog.json、catalog.html；編輯紀錄後執行 tools/manage.py rebuild。編號不重排、不回收。
- 紀錄最上方 JSON 資料欄位與人類可讀判斷一致；sources 是對應該項目的來源，context_sources 僅供歷史脈絡查找，不能當直接證據。歷史推薦不自動當現行推薦。
- 重要推薦、證據等級或限制改變時，同步根目錄研究索引、精選候選及 HTML；記錄原因。未核實項目不可當成已確認一次交付成果。圖片來源需區分 AI 成品、原作及類型參考。
- 完成後執行 tools/manage.py validate；它驗證保存／映射完整性，不驗證遊戲品質。原封存台帳保留作備份，不追加新資料。
