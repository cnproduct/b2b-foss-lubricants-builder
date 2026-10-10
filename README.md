# B2B Foss Lubricants Site Builder · 出海独立站全流程构建与优化 Skill

[![Skill Status](https://img.shields.io/badge/Agent%20Skill-Ready-success.svg)](#)
[![Live Site](https://img.shields.io/badge/Production%20Site-fosslubricants.com-blue.svg)](https://www.fosslubricants.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Validation](https://img.shields.io/badge/Site%20Validation-PASS%20(1535%20refs)-brightgreen.svg)](#)

> 本仓库完整沉淀并封装了 **泉州市福斯润滑科技有限公司（Quanzhou Foss Lubrication Technology Co., Ltd.）** 官方外贸出海独立站 **[fosslubricants.com](https://www.fosslubricants.com/)** 的全生命周期构建工程、深度优化细节与未来演进路线图。

---

## 🌟 核心工程特色与交付价值

1. **工业物理事实与不可动摇的标准硬锚定**：
   - 全面执行 **ASTM D445、DIN 51524 Part 2/3 (HLP/HVLP)、ISO 11158 HM、Parker Denison HF-0、Cincinnati Lamb P-68/P-69/P-70**；
   - 每批次随附独立盖章的 **Certificate of Analysis (CoA)** 与 24 个月留样封签追溯机制；
   - 提供 ExxonMobil（DTE 25）、Shell（Tellus S2 M 46）、Fuchs（Renolin B 46）的 **1:1 精确等效物理替换表**。
2. **重液体危险品包装与 20GP 集装箱物流测算引擎**：
   - 采用 **UN 1A1/Y1.4/150** 认证冷轧重型钢桶（1.0-1.2mm 钢卷板，自重 18.5-19.5kg，全容积 208L）；
   - 内置 **20GP Container Loading Calculator**：精准计算 80 桶打托（16,640L / 16.44MT 净毛重平衡），完美符合全球各大港口公路限重；
   - 距厦门国际集装箱港仅 95 公里，FOB 出口订单 7-10 天极速备货放行。
3. **清爽无后缀 URL 全站路由与 SEO 权重聚合**：
   - 彻底告别 `.html` 廉价后缀，全站 29 个页面、`<a href>` 内部链接、`<link rel="canonical">`、Schema 及 `sitemap.xml` 100% 采用无后缀规范；
   - Nginx 配置强制 301 重定向与透明 `try_files` 解析，杜绝重复内容惩罚。
4. **出版级工业前端交互与动效体系**：
   - **CSS Grid 重叠堆叠 Hero 轮播**：3 Slides 共用单网格单元，彻底根治传统定位切换引起的重排（Reflow）与布局抖动（Zero Layout Shift）；
   - **视口下潜关键数字递增 (Dynamic Count-Up)**：滚动触发 2018 年创立、80 桶打托、100% 留样、35%-45% 成本优势从 0 飞速累加动效；
   - **两翼向心聚拢动效**：标题自左向中、卡片自右向中滑入，赋予精密机械般的仪式感；
   - **工业实景图点击无损放大画廊 (Lightbox)**：支持全屏无损放大查验钢桶焊缝、油样色泽及实验室仪器；
   - **侧边栏悬浮多渠道即时沟通枢纽**：高对比度悬浮 WhatsApp 预填草稿呼起与 WeChat 一键复制官方微信卡片。
5. **每日 3,000+ 字全自动深度能源研报与 3 天未来走势预测引擎**：
   - 内置 20 篇高深度历史开篇研报库；
   - 每日通过 Antigravity Automation 自动追踪宏观地缘、OPEC+ 配额、加氢二类/三类基油裂解价差；
   - 独创 **3-Day Predictive Forecast** 模型，每日量化预判未来 3 天基础油出厂价与液压油调价区间；
   - 自动更新 HTML、自动刷新新闻索引并同步追加至 `sitemap.xml`。
6. **Google Imagen 3 工业视觉生图规范**：
   - **100% 中国员工面孔约束**：化验师、中控工程师、叉车师傅、业务经理全量替换为真实中国专业团队；
   - **双轨中英官方品牌标识规范**：所有设备、储罐、钢桶及标牌统一标注：上面英文 `FOSS LUBRICATION`、下面中文 `福斯润滑`。
7. **询盘表单 100% 投递与 Cloudflare 防垃圾机制**：
   - 官方直收邮箱：`sales@fosslubricants.com`；
   - 域名级 SPF、DKIM、DMARC 邮件鉴权，彻底杜绝进垃圾箱；
   - 接入 Cloudflare Turnstile 静默无感人机验证，0 毫秒放行真人采购商，彻底拦截垃圾爬虫；
   - 邮件 + 飞书/企微 Webhook 双通道实时告警。
8. **云端生产部署与 CDN 缓存穿透策略**：
   - 自动化 Rsync 增量推送、自动权限复位（`www-data:www-data 755`）与 Nginx 平滑重载；
   - 图片资源附加版本号 `?v=20261010_v10`，彻底击穿 Cloudflare 30 天静态边缘缓存。

---

## 📁 仓库目录结构

```text
b2b-foss-lubricants-builder/
├── SKILL.md                                 # Skill 主入口规范与全流程详细教程
├── README.md                                # 项目说明与 GitHub 说明文档
├── manifest.json                            # Skill 元数据与命令行配置
├── LICENSE                                  # MIT 开源许可证
├── .gitignore                               # Git 忽略配置
├── references/                              # 9 大核心深度方法论与设计规范
│   ├── benchmark-analysis-and-positioning.md# 巨头对标分析与差异化公式
│   ├── engineering-standards-and-coa.md     # ASTM/DIN/ISO 工业标准与批次 CoA 格式
│   ├── packaging-logistics-calculator.md    # 208L 钢桶规格与 20GP 集装箱配载工程
│   ├── clean-url-and-routing.md             # 清爽无后缀 URL 架构与 Nginx 配置
│   ├── interactive-ux-design-patterns.md    # Grid轮播、数字滚动、向心聚拢与悬浮窗
│   ├── imagen3-industrial-prompts.md        # 10 大场景工业生图 Prompt 与中国员工约束
│   ├── daily-news-automation-engine.md      # 每日 3000 字深度研报与 3 天走势预测引擎
│   ├── email-delivery-and-cloudflare-setup.md # 表单 100% 投递、SPF/DKIM 与 Turnstile 配置
│   └── future-optimization-roadmap.md       # 五大未来演进路线图 (多语言/海运费API/3D换色)
├── scripts/                                 # 核心自动化与运维脚本
│   ├── generate_daily_news.py               # 每日深度研报自动化编译生成器
│   ├── news_database.py                     # 20 篇高深度行业开篇分析数据库
│   ├── apply_interactive_enhancements.py    # 交互动效与 Lightbox 自动注入工具
│   ├── validate_site.py                     # 6 维静态网站完整性与 SEO 校验工具
│   └── deploy_production.sh                 # 自动化 Rsync、权限复位与 Nginx 重载脚本
└── examples/                                # 生产配置与标准化示例
    ├── nginx.fosslubricants.conf            # Nginx 生产环境无后缀路由与缓存配置
    ├── sitemap.sample.xml                   # 无后缀标准 Sitemap 示例
    └── schema-product-coa.json              # 工业油品与实测 CoA 结构化数据 Schema
```

---

## 🚀 常用运行命令 (Quickstart CLI)

```bash
# 1. 运行每日研报自动化编译
python3 scripts/generate_daily_news.py

# 2. 全站 6 维静态完整性与 SEO 审计 (测试 1535+ 内部引用与无后缀规范)
python3 scripts/validate_site.py . --release --domain https://www.fosslubricants.com

# 3. 一键部署更新至生产服务器并刷新 Nginx
bash scripts/deploy_production.sh
```

---

## 🔮 未来优化路线图 (Roadmap Summary)

| 阶段 | 核心模块 | 目标与交付成果 |
| :--- | :--- | :--- |
| **阶段 1** | **多语言全球本地化** | 扩展西语（`/es/`）、俄语（`/ru/`）、阿语（`/ar/`）、越语（`/vi/`）、印尼语（`/id/`）无后缀国际子目录 |
| **阶段 2** | **实时海运费与原油指数 API** | 对接海运集装箱即时运价，在线一键生成透明的 CIF/FOB 测算报告并导出正式 PI 发票草案 |
| **阶段 3** | **3D 钢桶在线定制打样器** | 基于 Three.js/WebGL 实现 208L 钢桶 360 度自由旋转、桶身烤漆换色、客户 Logo 在线贴牌预览 |
| **阶段 4** | **AI 润滑专家与即时选油 Agent**| 挂载机床工程润滑手册，在右下角悬浮窗秒级解答海天、卡特彼勒等设备原厂油品替代与参数咨询 |
| **阶段 5** | **Cloudflare Workers 边缘计算与 PWA**| 边缘节点 50ms 极速响应，支持手机离线查阅技术参数与检验报告 |

---

## 📄 许可证 (License)
本项目遵守 [MIT License](LICENSE)。欢迎自由引用、构建或二次开发。
