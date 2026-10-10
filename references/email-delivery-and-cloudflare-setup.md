# 客户询盘表单 100% 投递与 Cloudflare 防垃圾机制 (Email Delivery & Cloudflare Setup)

B2B 出海网站的核心转化终点是**表单询盘（RFQ）**。如果客户认真填写的技术参数表单因为垃圾邮件拦截、被黑客扫库发垃圾广告、或者邮件路由配置错误而丢失，将直接导致数十万美元的订单损失。

---

## 一、 询盘收件路由规范

- **官方指定业务主邮箱**：`sales@fosslubricants.com`
- **抄送与技术支持备份**：`technical@fosslubricants.com`
- **投递成功率硬指标**：**100% 送达**，严禁进入垃圾邮件箱（Spam Folder），严禁因服务器 IP 被拉黑而静默丢信。

---

## 二、 邮件防垃圾与安全投递三大支柱

### 1. 域名级邮件鉴权三剑客 (SPF, DKIM, DMARC)
在 Cloudflare DNS 面板中必须严格配置以下 DNS TXT 记录，防止全球邮件服务商（Google Workspace、Outlook、企业邮局）误判：

| 记录类型 | 主机记录 (Name) | 记录值 (Value) | 作用 |
| :--- | :--- | :--- | :--- |
| **SPF** | `@` | `v=spf1 include:_spf.mx.cloudflare.net ~all` (或对应企业邮局如腾讯企业邮/Zoho/Google) | 声明授权发送本域名邮件的真实服务器 IP |
| **DKIM** | `s1._domainkey` | `k=rsa; p=MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQ...` (由企业邮局生成公钥) | 对外发邮件进行数字加密签名，证明未经篡改 |
| **DMARC** | `_dmarc` | `v=DMARC1; p=quarantine; rua=mailto:dmarc-reports@fosslubricants.com; pct=100` | 建立投递反馈机制，严防钓鱼假冒发信 |

### 2. 前端无感防机器人与垃圾验证 (Cloudflare Turnstile)
传统 Google reCAPTCHA 经常弹出选斑马线、红绿灯，极度损害海外工程采购商的耐心。
- **改用 Cloudflare Turnstile**：完全静默无感验证（Invisible Smart Challenge），正常人类用户 0 毫秒通过，恶意刷信机器人直接在边缘节点阻断；
- **配置方式**：在 Cloudflare Dashboard -> Turnstile 创建 Site Key 与 Secret Key，前端仅需一行 JS 挂载：
  ```html
  <div class="cf-turnstile" data-sitekey="0x4AAAAAA..." data-theme="light"></div>
  ```

### 3. 表单后端投递通道双轨保障 (Dual-Pipeline Form Delivery)
为确保 100% 送达，表单提交采取双通道冗余机制：
- **通道 A：专用邮件 API（Resend / SendGrid / Postmark / Zoho SMTP）**：
  直接通过经严格白名单认证的事务型邮件通道发送至 `sales@fosslubricants.com`；
- **通道 B：飞书/企业微信/Telegram Webhook 实时通知**：
  每当有海外客户提交表单，除发送邮件外，即时向销售团队手机端推送一条 Webhook 报警卡片（包含客户姓名、公司、国家、采购型号、采购数量及 WhatsApp 手机号），实现 5 分钟内极速响应！
