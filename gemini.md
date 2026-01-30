# ♊ Gemini Protocol (Project Constitution)

## 1. Data Schemas

### Core Conversion Payload
```json
{
  "source_code": "String (Java/Selenium/TestNG Code)",
  "target_language": "String (Enum: 'typescript' | 'javascript')",
  "output_path": "String (Optional, Path to save file)",
  "conversion_result": {
    "status": "String (success | error)",
    "converted_code": "String (Playwright Code)",
    "logs": ["String (Warning/Info messages)"]
  }
}
```

## 2. Behavioral Rules
- **Protocol:** B.L.A.S.T.
- **Architecture:** A.N.T. (3-Layer)
- **Principle:** Deterministic logic over probabilistic guesses.
- **Conversion Philosophy:** Prioritize **readability** and idiomatic Playwright matches over strict 1:1 syntax translation.
- **Source:** UI Input is primary.
- **Output:** UI Display + File System write.

## 3. Architectural Invariants
- Logic changes update SOPs (`architecture/`) before Code.
- Data Schema must be defined before Tool creation.
- `tools/` contains atomic, deterministic Python scripts.

## 4. Maintenance Log
*No entries yet.*
