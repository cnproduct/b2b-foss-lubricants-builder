# 清爽无后缀 URL 架构与全站路由设计 (Clean Extensionless URL Routing)

在国际顶级 B2B 出海门户中，去除 `.html` 后缀是构建出版级国际品牌形象、提升 SEO 权重与防止恶意爬虫探查后端技术栈的关键工程标准。

---

## 一、 为什么必须彻底去掉 `.html` 后缀？

1. **国际品牌专业感 (Professionalism)**：
   - Apple、Tesla、ExxonMobil、Shell 等国际巨头的 URL 从不携带 `.html`。带 `.html` 给人强烈的“上世纪静态模板站”廉价感；
   - 清爽路径（如 `/hydraulic-oil`、`/news/middle-east-geopolitics`）更易于在商务邮件、RFQ 报价单及 WhatsApp 对话中复制传播。
2. **SEO 与权重集中 (Search Engine Optimization)**：
   - 彻底避免 `example.com/about` 与 `example.com/about.html` 产生两套 URL 导致的 Google 权重稀释与“重复内容惩罚（Duplicate Content Penalty）”；
   - 配合严格的 `rel="canonical"` 权威标签，确保搜索引擎爬虫将权威权重 100% 聚焦在无后缀标准地址上。
3. **架构可扩展性 (Future-Proof Architecture)**：
   - 未来无论是继续使用纯静态生成器、还是平滑迁移到 Node.js / Go / Headless CMS，外部链接无需重新 301 重定向，永久保全已有外链与权重。

---

## 二、 现代出海建站 Skill 标准规范沉淀

针对以后默认构建的所有 B2B 独立站，一律强制执行以下标准：

1. **站内 HTML 模板内部链接**：
   - 所有 `<a href="...">` 链接统一采用无后缀规范：
     ```html
     <!-- ✅ 正确写法 -->
     <a href="/about">About Factory</a>
     <a href="/hydraulic-oil">Hydraulic Oils</a>
     <a href="/news">Market Insights</a>
     <a href="/news/middle-east-geopolitics-oil-surge">Article</a>

     <!-- ❌ 禁止写法 -->
     <a href="/about.html">About Factory</a>
     <a href="/hydraulic-oil.html">Hydraulic Oils</a>
     ```
2. **Canonical 标签与 Schema 统一**：
   - 每个页面的 `<head>` 中必须明确标注权威地址：
     ```html
     <link rel="canonical" href="https://www.fosslubricants.com/hydraulic-oil">
     <meta property="og:url" content="https://www.fosslubricants.com/hydraulic-oil">
     ```
3. **Sitemap.xml 纯净输出**：
   - `sitemap.xml` 中收录的 `<loc>` 必须 100% 为无后缀规范 URL，不得夹杂任何 `.html`：
     ```xml
     <url>
       <loc>https://www.fosslubricants.com/hydraulic-oil</loc>
       <lastmod>2026-10-10</lastmod>
       <changefreq>weekly</changefreq>
       <priority>0.9</priority>
     </url>
     ```
4. **Nginx 核心配置文件实现规则**：
   ```nginx
   # 1. 拦截所有带 .html 的历史外链或直接访问，强制 301 永久重定向至无后缀 URL
   if ($request_uri ~ ^/(.*)\.html(\?.*)?$) {
       return 301 /$1$is_args$args;
   }

   # 2. 匹配无后缀 URL，在磁盘中透明寻找同名 .html 文件
   location / {
       try_files $uri $uri/ $uri.html =404;
   }
   ```
