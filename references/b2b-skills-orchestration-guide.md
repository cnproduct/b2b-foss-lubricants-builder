# 外贸出海建站 Skills 协同使用全景指南与实战手册 (B2B Skills Orchestration Guide)

本项目在打造 `fosslubricants.com` 的过程中，调度并协同了多个专业的 Agent Skills。本指南详细说明每个 Skill 的职责分工、触发时机、Prompt 模板、前置事实依赖与产出标准，以便在后续任何工业 B2B 建站项目中无缝复用。

---

## 🧭 Skills 协同矩阵总览

| 阶段 | 核心调用 Skill | 核心职责与分工 | 关键输出成果物 |
| :--- | :--- | :--- | :--- |
| **1. 知识库与事实锚定** | `product-truth-builder`<br>`exporter-profile-skill` | 提取企业法律实体、厂房产能、地理口岸、ASTM/DIN 测试参数、封签留样政策，建立不可动摇的事实基底 | `BrandProfile`、产品事实库、物理测试指标公差表 |
| **2. 工业级视觉生成** | `antigravity-image-gen`<br>`brand-visual-director` | 结合工厂真实工况与 Google Imagen 3 工业摄影提示词，锁定 100% 中国员工面孔与双轨中英文 Logo 标牌 | 10 张 16:9 工业实景大图与优化后的 `.webp` 高清资产 |
| **3. 架构与无后缀路由** | `b2b-foss-lubricants-builder`<br>`b2b-global-brand-site-master` | 规划全站 29 核心页面、无 `.html` 路由架构、Sitemap、Robots、Nginx 301 重定向与静态缓存策略 | 纯净无后缀 URL 拓扑、`nginx.conf`、`sitemap.xml` |
| **4. 交互与出版级排版** | `layout-typography-auditor`<br>`interactive-ux-design` | CSS Grid 零跳动 Hero 轮播、数字滚动递增、向心聚拢、Lightbox 实景放大、固定悬浮联系组件 | 高转化响应式 CSS/JS、无重排交互体系 |
| **5. 自动化能源研报引擎** | `automation`<br>`daily-news-automation-engine` | 定时抓取地缘与原油变动，自动化撰写 3000+ 字专业研报与 3 天未来价格预测矩阵，自动编译挂载 | 21 篇深度行业研报、自动化更新工作流 |
| **6. 多语言本地化矩阵** | `b2b-foss-lubricants-builder`<br>`locale-market-adapter` | 挂载 6 语种专业摩擦学词库（ES/RU/AR/VI/ID），实现多语种无后缀子目录与阿语 RTL 排版 | 40 个国际子目录页面、`hreflang` 标签矩阵 |
| **7. 投递安全与生产发布** | `gcloud-auth` / `cloudflare`<br>`deploy_production.sh` | 域名 SPF/DKIM/DMARC 邮件鉴权、Cloudflare Turnstile 验证码、Rsync 增量部署与权限安全复位 | 100% 询盘送达、生产环境 Nginx 极速运行 |

---

## 🛠️ 各 Skill 具体使用流程与 Prompt 范式

### 1. `product-truth-builder`（产品事实库与标准锚定）
- **何时使用**：在开始编写任何 HTML 代码或生成文案之前，先建立企业技术真相。
- **输入事实**：
  - 生产企业名称、工厂成立年份、地理经纬度与港口距离；
  - 调配反应釜容积（如 15,000L）、年产能（如 10,000 吨）；
  - 核心执行标准（ASTM D445, DIN 51524 HLP, ISO 11158 HM, Parker Denison HF-0）；
  - 包装规格（UN 1A1 208L 钢桶，1.0-1.2mm 钢板，80 桶/20GP）。
- **执行 Prompt 示例**：
  ```markdown
  请使用 product-truth-builder 为泉州福斯润滑科技有限公司建立工业液压油与工业油产品事实库。
  锁定核心参数：
  - 基础油：100% 采用全新加氢 Group II/III 基础油，严禁使用再生油；
  - 46号液压油 40°C 动粘度严格锁定 46.2 mm²/s (ASTM D445)；
  - 破乳化时间 40-40-0 锁定 12 分钟 (ASTM D1401)；
  - 开杯闪点 ≥ 230°C (ASTM D92)；
  - 批次附带质检部盖章 CoA 报告，留样 24 个月。
  输出结构化的产品事实 Schema 与跨品牌等效替换矩阵。
  ```

### 2. `antigravity-image-gen`（Google Imagen 3 工业实景生成）
- **何时使用**：需要为 Banner、产品专页、车间实况生成高质感商业摄影图时。
- **硬性防翻车约束**：
  1. **必须包含中国员工**（Chinese personnel in workwear/lab coat）；
  2. **负向词必须加入**：`caucasian, western face, blonde hair, blue eyes, fake smiling, plastic CGI texture`；
  3. **品牌标牌必须双轨**：上面英文 `FOSS LUBRICATION`，下面中文 `福斯润滑`。
- **执行 Prompt 示例**：
  ```markdown
  使用 generate_image 工具生成一张 16:9 高清工业纪实摄影图：
  场景：现代石油理化实验室，一位专业的中国女分析化学师戴护目镜身穿白大褂，手持锥形瓶观察金黄色润滑油透明度。
  背景：Tamson 恒温粘度浴槽，墙面发光中英文标牌：FOSS LUBRICATION / 福斯润滑 / QUALITY CONTROL LABORATORY。
  参数：Aspect Ratio: 16:9, ImageName: "hero_lab_chinese".
  ```

### 3. `layout-typography-auditor`（排版防错与交互审计）
- **何时使用**：在 HTML/CSS 编写完成后，检查全屏响应式、单行文字折行、容器溢出及移动端排版。
- **核心检查项**：
  - 轮播图是否采用 CSS Grid 堆叠（防止高度跳动）；
  - 关键数字滚动递增是否具备 `IntersectionObserver` 节流；
  - 侧边栏悬浮沟通窗口（WhatsApp / WeChat）在各分辨率下是否被页脚遮挡，对比度是否达标（白色文字配绿色按钮，严禁白底白字）；
  - 阿拉伯语 (`/ar/`) 是否具备 `dir="rtl"` 并适配了向右对齐。

### 4. `automation`（每日研报无人值守定时发布）
- **何时使用**：需要按天或按周定时发布 3000+ 字专业国际时事分析与未来 3 天油价走势预测时。
- **工作流配置**：
  ```bash
  # 配置 Crontab 或 Antigravity schedule:
  # 每天凌晨 06:00 自动执行：
  0 6 * * * python3 /path/to/scripts/generate_daily_news.py && bash /path/to/scripts/deploy_production.sh
  ```

---

## 🛡️ 跨项目建站避坑黄金准则 (Golden Rules)

1. **绝对不要在生产环境使用 `.html` 内部链接**：以后的所有 B2B 网站，从第一行代码开始就强制采用无后缀路由（`/about`、`/hydraulic-oil`），并在 Nginx 中配置 301 强制重定向；
2. **严防 CDN 静态缓存陷阱**：大图更新后，务必在 HTML 中升级查询参数（如 `?v=20261010_v10`），否则 Cloudflare 会持续给海外客户返回 30 天前的旧图片；
3. **多语言必须挂载专业词库**：杜绝直接调用无上下文的翻译 API，必须以 `references/tribology-multilingual-dictionary.md` 等行业专业词库为锚点；
4. **询盘表单必须配置安全三件套**：SPF + DKIM + DMARC，并接入 Cloudflare Turnstile 静默防刷，确保客户询盘 100% 进销售收件箱。
