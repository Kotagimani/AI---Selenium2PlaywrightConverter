# 🏗️ System Design: Converter App

## 1. Stack
- **Frontend:** Vanilla HTML5, CSS (Modern/Dark Mode), JavaScript (ES6).
- **Backend:** Python FastAPI (acting as the "Bridge" between UI and `tools/`).
- **Core Logic:** Python Scripts in `tools/`.

## 2. Component Diagram

```
[Browser UI]  <--HTTP JSON-->  [FastAPI Server]  <--Import-->  [tools/converter.py]
     |                                 |
  Input: Java                       Output: File Write
  Output: TS                        (.tmp/ or user-defined)
```

## 3. API Endpoints

### `POST /api/convert`
- **Payload:**
  ```json
  {
    "source_code": "String",
    "output_dir": "String (Optional)"
  }
  ```
- **Response:**
  ```json
  {
    "status": "success",
    "converted_code": "String",
    "file_written": "Path (or null)"
  }
  ```

## 4. Directory Structure
```
root/
├── tools/
│   ├── converter.py      # The Logic Engine
│   └── text_utils.py     # Helpers
├── backend/
│   └── server.py         # FastAPI App
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── app.js
└── ...
```
