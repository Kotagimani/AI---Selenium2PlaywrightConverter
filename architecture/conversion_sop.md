# 🌉 Architecture: Java to Playwright Conversion SOP

## 1. Goal
Translate Selenium Java (TestNG) code provided via UI into equivalent, readable Playwright TypeScript code.

## 2. Inputs & Outputs
- **Input:** Raw Java String containing TestNG annotations (`@Test`, `@BeforeClass`) and Selenium WebDriver commands (`driver.findElement`).
- **Output:** TypeScript String containing Playwright Test annotations (`test`, `test.beforeAll`) and Playwright Locator actions (`page.locator`).

## 3. Translation Strategy (Heuristic)

### A. Structure Mapping
| Java (TestNG) | Playwright (TS) |
| :--- | :--- |
| `public class Tests { ... }` | `test.describe('Tests', () => { ... });` |
| `@BeforeClass` | `test.beforeAll(async ({ browser }) => { ... });` |
| `@BeforeMethod` | `test.beforeEach(async ({ page }) => { ... });` |
| `@Test` | `test('test name', async ({ page }) => { ... });` |
| `@AfterClass` | `test.afterAll(async () => { ... });` |

### B. Locator Mapping
| Selenium Java | Playwright TS |
| :--- | :--- |
| `By.id("foo")` | `page.locator('#foo')` |
| `By.cssSelector(".bar")` | `page.locator('.bar')` |
| `By.xpath("//div")` | `page.locator('xpath=//div')` |
| `driver.findElement(...)` | DIRECT `page.locator(...)` mapping |

### C. Action Mapping
| Selenium Java | Playwright TS |
| :--- | :--- |
| `.click()` | `.click()` |
| `.sendKeys("text")` | `.fill("text")` |
| `.getText()` | `.textContent()` |
| `driver.get("url")` | `page.goto("url")` |
| `Assert.assertEquals(a, b)` | `expect(a).toEqual(b)` |

## 4. Edge Cases
- **Explicit Waits:** Selenium `WebDriverWait` should be converted to Playwright `expect` with auto-waiting or `page.waitForSelector`.
- **Drivers:** `WebDriver driver = new ChromeDriver();` logic should be removed as Playwright handles browser context differently (injected fixtures).
