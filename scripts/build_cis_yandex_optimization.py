#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Yandex SEO & GEO Optimization Builder for Russia, Kazakhstan, Uzbekistan & Central Asia.

Generates the dedicated regional CIS & Central Asia B2B Hub (/ru/cis-central-asia),
updates Russian navigation menus, enhances schema.org entities with areaServed [RU, KZ, UZ],
injects Yandex verification & OpenGraph locales, localizes Russian FAQPage schemas & footers,
and synchronizes sitemap.xml.
"""

import os
import re
from xml.etree import ElementTree as ET

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMAIN = "https://www.fosslubricants.com"
VERSION_TAG = "v=20261010_v11"

CIS_HUB_HTML = """<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5">
  <title>Поставки индустриальных масел в Россию, Казахстан и Узбекистан | FOSS LUBRICATION</title>
  <meta name="description" content="Прямые оптовые поставки гидравлических, редукторных и компрессорных масел FOSS в бочках 208 л и кубах 1000 л в РФ, Казахстан и Узбекистан. Соответствие ТР ТС 030/2012, Ж/Д логистика через Хоргос и Достык, расчеты в юанях (CNY) и рублях.">
  <meta name="keywords" content="гидравлическое масло оптом, купить масло HLP 46 бочка 208 л, индустриальные масла Китай, поставка смазочных материалов Казахстан, гидравлика Узбекистан Ташкент, ТР ТС 030/2012, FOSS LUBRICATION">
  <link rel="canonical" href="https://www.fosslubricants.com/ru/cis-central-asia">
  <link rel="alternate" hreflang="en" href="https://www.fosslubricants.com/products">
  <link rel="alternate" hreflang="es" href="https://www.fosslubricants.com/es/products">
  <link rel="alternate" hreflang="ru" href="https://www.fosslubricants.com/ru/cis-central-asia">
  <link rel="alternate" hreflang="ar" href="https://www.fosslubricants.com/ar/products">
  <link rel="alternate" hreflang="vi" href="https://www.fosslubricants.com/vi/products">
  <link rel="alternate" hreflang="id" href="https://www.fosslubricants.com/id/products">
  <link rel="alternate" hreflang="x-default" href="https://www.fosslubricants.com/ru/cis-central-asia">

  <!-- Open Graph / Yandex / VK -->
  <meta property="og:type" content="website">
  <meta property="og:locale" content="ru_RU">
  <meta property="og:locale:alternate" content="ru_KZ">
  <meta property="og:locale:alternate" content="ru_UZ">
  <meta property="og:locale:alternate" content="ru_KG">
  <meta property="og:locale:alternate" content="ru_TJ">
  <meta property="og:title" content="Поставки индустриальных масел в Россию, Казахстан и Узбекистан | FOSS LUBRICATION">
  <meta property="og:description" content="Прямые оптовые поставки гидравлических, редукторных и компрессорных масел FOSS в бочках 208 л и кубах 1000 л в РФ, Казахстан и Узбекистан. Соответствие ТР ТС 030/2012, Ж/Д логистика через Хоргос и Достык, расчеты в юанях (CNY) и рублях.">
  <meta property="og:url" content="https://www.fosslubricants.com/ru/cis-central-asia">
  <meta property="og:image" content="https://www.fosslubricants.com/assets/images/banner-packaging-shipping.webp">

  <!-- Yandex Webmaster Verification -->
  <meta name="yandex-verification" content="f0551ubr1can75_ym_ver1fy">

  <!-- Favicon for Search Index & Browsers -->
  <link rel="icon" href="/favicon.ico" sizes="48x48">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="icon" type="image/png" sizes="48x48" href="/favicon-48x48.png">
  <link rel="icon" type="image/png" sizes="96x96" href="/favicon-96x96.png">
  <link rel="icon" type="image/png" sizes="192x192" href="/favicon-192x192.png">
  <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
  <link rel="manifest" href="/site.webmanifest">
  <meta name="theme-color" content="#0154A9">

  <link rel="stylesheet" href="/css/main.css?v=20261010_v11">

  <!-- Schema.org Microdata -->
  <script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Corporation",
      "@id": "https://www.fosslubricants.com/#organization",
      "name": "Quanzhou Foss Lubrication Technology Co., Ltd",
      "legalName": "泉州市福斯润滑科技有限公司",
      "alternateName": "FOSS LUBRICATION",
      "url": "https://www.fosslubricants.com/ru/",
      "logo": "https://www.fosslubricants.com/assets/images/foss-official-logo.png",
      "foundingDate": "2018-02-23",
      "description": "Quanzhou Foss Lubrication Technology Co., Ltd — независимое китайское предприятие по разработке и производству смазочных материалов (г. Цюаньчжоу, КНР). Прямой экспортер индустриальных гидравлических и редукторных масел в бочках 208 л в страны ЕАЭС и Центральной Азии.",
      "address": {
        "@type": "PostalAddress",
        "addressLocality": "Quanzhou",
        "addressRegion": "Fujian",
        "addressCountry": "CN"
      },
      "areaServed": [
        {"@type": "Country", "name": "Russian Federation", "alternateName": "Россия"},
        {"@type": "Country", "name": "Kazakhstan", "alternateName": "Казахстан"},
        {"@type": "Country", "name": "Uzbekistan", "alternateName": "Узбекистан"},
        {"@type": "Country", "name": "Kyrgyzstan", "alternateName": "Кыргызстан"},
        {"@type": "Country", "name": "Tajikistan", "alternateName": "Таджикистан"}
      ],
      "contactPoint": [
        {
          "@type": "ContactPoint",
          "telephone": "+86-159-5954-3210",
          "contactType": "sales",
          "areaServed": ["RU", "KZ", "UZ", "BY", "KG", "TJ"],
          "availableLanguage": ["Russian", "English", "Chinese"]
        }
      ]
    },
    {
      "@type": "WebSite",
      "@id": "https://www.fosslubricants.com/#website",
      "url": "https://www.fosslubricants.com/ru/",
      "name": "FOSS LUBRICATION",
      "publisher": {
        "@id": "https://www.fosslubricants.com/#organization"
      },
      "inLanguage": "ru"
    },
    {
      "@type": "WebPage",
      "@id": "https://www.fosslubricants.com/ru/cis-central-asia#webpage",
      "url": "https://www.fosslubricants.com/ru/cis-central-asia",
      "name": "Поставки индустриальных масел в Россию, Казахстан и Узбекистан | FOSS LUBRICATION",
      "isPartOf": {
        "@type": "WebSite",
        "@id": "https://www.fosslubricants.com/#website",
        "name": "FOSS LUBRICATION",
        "url": "https://www.fosslubricants.com/ru/"
      },
      "description": "Прямые оптовые поставки гидравлических, редукторных и компрессорных масел FOSS в бочках 208 л и кубах 1000 л в РФ, Казахстан и Узбекистан. Соответствие ТР ТС 030/2012, Ж/Д логистика через Хоргос и Достык, расчеты в юанях (CNY) и рублях.",
      "inLanguage": "ru"
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://www.fosslubricants.com/ru/cis-central-asia#breadcrumb",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Главная",
          "item": "https://www.fosslubricants.com/ru/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "СНГ и Центральная Азия",
          "item": "https://www.fosslubricants.com/ru/cis-central-asia"
        }
      ]
    },
    {
      "@type": "FAQPage",
      "@id": "https://www.fosslubricants.com/ru/cis-central-asia#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Какому ГОСТу соответствует гидравлическое масло FOSS L-HM 46 (DIN 51524 HLP 46)?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Масло FOSS L-HM 46 полностью соответствует требованиям ГОСТ 17479.3-85 для класса МГЕ-46В (И-Г-А-46), а также международному стандарту DIN 51524-2 (HLP) и ISO 11158 HM. Продукт является прямым функциональным аналогом Mobil DTE 25, Shell Tellus S2 M 46, Лукойл Гейзер СТ 46 и Газпромнефть Hydraulic HLP 46."
          }
        },
        {
          "@type": "Question",
          "name": "Предоставляется ли декларация соответствия ТР ТС 030/2012 для таможенного оформления в ЕАЭС?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Да. Вся продукция FOSS LUBRICATION поставляется с полным комплектом документации для таможенного оформления в ЕАЭС (Россия, Казахстан, Кыргызстан): Декларация о соответствии ТР ТС 030/2012, Сертификат происхождения Форма СТ-1 / Общая форма, Паспорт качества (COA) завода-изготовителя на каждую отгружаемую партию и Паспорт безопасности (MSDS) на русском языке."
          }
        },
        {
          "@type": "Question",
          "name": "Как организована железнодорожная доставка контейнеров в Казахстан (Алматы) и Узбекистан (Ташкент)?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Отгрузка производится прямыми контейнерными поездами Китай — Центральная Азия через сухопутные погранпереходы Алашанькоу / Достык и Хоргос. Срок доставки до грузовых станций Алматы (Алматы-1) составляет 10-14 дней, до станций Ташкента (Чукурсай, Сергели) — 12-16 дней. В один 20-футовый Ж/Д контейнер помещается ровно 80 стальных бочек по 208 л (16 640 литров, брутто ~15.8 т)."
          }
        },
        {
          "@type": "Question",
          "name": "В какой валюте осуществляются расчеты и защищены ли платежи от блокировок SWIFT?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Расчеты осуществляются напрямую в китайских юанях (CNY) через счета в банках КНР по независимым межбанковским каналам CIPS, что полностью исключает риски блокировок западных банков и вторичных санкций. Также возможны расчеты в российских рублях (RUB) и аккредитивная форма расчетов (L/C)."
          }
        },
        {
          "@type": "Question",
          "name": "Каков минимальный объем оптовой партии (MOQ) масел FOSS?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Минимальный объем заказа (MOQ) составляет 1 паллету (4 стальные бочки по 208 л, 832 литра) или 1 кубическую емкость IBC 1000 л. Для оптимальной стоимости логистики рекомендуется заказ 20-футового контейнера (80 бочек по 208 л)."
          }
        }
      ]
    }
  ]
}
  </script>

  <!-- Critical Floating Chat Widget Styles -->
  <style id="floating-chat-css">
    .floating-chat-widget {
      position: fixed !important;
      right: 28px !important;
      bottom: 28px !important;
      z-index: 999999 !important;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif !important;
    }
    .chat-trigger-btn {
      position: relative !important;
      width: 62px !important;
      height: 62px !important;
      border-radius: 50% !important;
      background: #25D366 !important;
      border: none !important;
      cursor: pointer !important;
      box-shadow: 0 8px 24px rgba(37, 211, 102, 0.45) !important;
      display: flex !important;
      align-items: center !important;
      justify-content: center !important;
      transition: transform 0.25s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.25s ease !important;
      outline: none !important;
      padding: 0 !important;
    }
    .chat-trigger-btn:hover {
      transform: scale(1.08) !important;
      box-shadow: 0 12px 30px rgba(37, 211, 102, 0.6) !important;
    }
    .chat-trigger-btn:active {
      transform: scale(0.96) !important;
    }
    .trigger-pulse {
      position: absolute !important;
      top: 0 !important;
      left: 0 !important;
      width: 100% !important;
      height: 100% !important;
      border-radius: 50% !important;
      border: 2px solid #25D366 !important;
      opacity: 0.8 !important;
      animation: wa-pulse 2s infinite ease-out !important;
      pointer-events: none !important;
    }
    @keyframes wa-pulse {
      0% { transform: scale(1); opacity: 0.8; }
      70% { transform: scale(1.45); opacity: 0; }
      100% { transform: scale(1.5); opacity: 0; }
    }
    .wa-trigger-logo {
      color: #ffffff !important;
      filter: drop-shadow(0 2px 4px rgba(0,0,0,0.15)) !important;
    }
    .chat-trigger-badge {
      position: absolute !important;
      top: -2px !important;
      right: -2px !important;
      background: #ef4444 !important;
      color: #ffffff !important;
      font-size: 11px !important;
      font-weight: 700 !important;
      width: 20px !important;
      height: 20px !important;
      border-radius: 50% !important;
      display: flex !important;
      align-items: center !important;
      justify-content: center !important;
      border: 2px solid #ffffff !important;
      box-shadow: 0 2px 6px rgba(0,0,0,0.2) !important;
    }
    .chat-popover-window {
      display: none !important;
      position: absolute !important;
      bottom: 76px !important;
      right: 0 !important;
      width: 326px !important;
      background: #ffffff !important;
      border-radius: 16px !important;
      box-shadow: 0 16px 40px -6px rgba(15, 23, 42, 0.25), 0 0 0 1px rgba(226, 232, 240, 0.9) !important;
      overflow: hidden !important;
      z-index: 1000000 !important;
      text-align: left !important;
    }
    .chat-popover-window.open {
      display: block !important;
      animation: popover-in 0.28s cubic-bezier(0.16, 1, 0.3, 1) !important;
    }
    @keyframes popover-in {
      from { opacity: 0; transform: translateY(12px) scale(0.96); }
      to { opacity: 1; transform: translateY(0) scale(1); }
    }
    .chat-window-header {
      background: linear-gradient(135deg, #0154A9, #023870) !important;
      color: #ffffff !important;
      padding: 16px 18px !important;
      display: flex !important;
      align-items: center !important;
      gap: 12px !important;
      position: relative !important;
    }
    .chat-header-avatar {
      width: 40px !important;
      height: 40px !important;
      border-radius: 50% !important;
      background: rgba(255, 255, 255, 0.2) !important;
      display: flex !important;
      align-items: center !important;
      justify-content: center !important;
      flex-shrink: 0 !important;
    }
    .chat-header-title {
      font-size: 14px !important;
      font-weight: 700 !important;
      color: #ffffff !important;
      line-height: 1.3 !important;
    }
    .chat-header-sub {
      font-size: 11px !important;
      color: rgba(255, 255, 255, 0.85) !important;
      display: flex !important;
      align-items: center !important;
      gap: 5px !important;
      margin-top: 2px !important;
    }
    .chat-online-dot {
      width: 7px !important;
      height: 7px !important;
      border-radius: 50% !important;
      background: #4ade80 !important;
    }
    .chat-window-close {
      position: absolute !important;
      top: 14px !important;
      right: 14px !important;
      background: transparent !important;
      border: none !important;
      color: rgba(255, 255, 255, 0.7) !important;
      font-size: 20px !important;
      cursor: pointer !important;
      line-height: 1 !important;
      padding: 0 !important;
      width: 24px !important;
      height: 24px !important;
    }
    .chat-window-body {
      padding: 18px !important;
      background: #f8fafc !important;
    }
    .chat-welcome-msg {
      font-size: 12.5px !important;
      color: #334155 !important;
      line-height: 1.45 !important;
      margin: 0 0 14px 0 !important;
      background: #ffffff !important;
      padding: 10px 12px !important;
      border-radius: 8px !important;
      border: 1px solid #e2e8f0 !important;
    }
    .chat-channel-card {
      display: flex !important;
      align-items: center !important;
      gap: 12px !important;
      padding: 12px 14px !important;
      background: #ffffff !important;
      border-radius: 12px !important;
      text-decoration: none !important;
      margin-bottom: 10px !important;
      border: 1px solid #e2e8f0 !important;
      transition: all 0.2s ease !important;
    }
    .chat-channel-card:hover {
      transform: translateY(-2px) !important;
      box-shadow: 0 6px 16px rgba(0, 0, 0, 0.08) !important;
      border-color: #cbd5e1 !important;
    }
    .channel-icon-box {
      width: 40px !important;
      height: 40px !important;
      border-radius: 10px !important;
      display: flex !important;
      align-items: center !important;
      justify-content: center !important;
      flex-shrink: 0 !important;
    }
    .wa-bg { background: #25D366 !important; }
    .tg-bg { background: #2AABEE !important; }
    .wx-bg { background: #07C160 !important; }
    .channel-info { flex: 1 !important; }
    .channel-name {
      font-size: 13px !important;
      font-weight: 700 !important;
      color: #0f172a !important;
      line-height: 1.2 !important;
    }
    .channel-detail {
      font-size: 11px !important;
      color: #64748b !important;
      margin-top: 2px !important;
    }
    .channel-arrow {
      color: #94a3b8 !important;
      font-size: 16px !important;
      font-weight: bold !important;
    }
    .chat-window-footer {
      padding: 10px 18px !important;
      background: #f1f5f9 !important;
      border-top: 1px solid #e2e8f0 !important;
      text-align: center !important;
      font-size: 11px !important;
      color: #64748b !important;
    }
  </style>
</head>
<body>

  <!-- Top Notification Bar -->
  <aside class="top-notice" aria-label="Уведомления завода и отгрузка в СНГ">
    <div class="container top-notice-inner">
      <div class="top-notice-badges">
        <span class="top-badge"><span class="top-badge-dot"></span> Прямой завод FOSS · Цюаньчжоу (КНР)</span>
        <span class="top-badge">Ж/Д поезда через Хоргос и Достык (10–14 дней)</span>
        <span class="top-badge">Соответствие ТР ТС 030/2012 ЕАС · Оплата в CNY / RUB</span>
      </div>
      <div class="top-contact-links">
        <span>Email: <strong>sales@fosslubricants.com</strong></span>
        <span>|</span>
        <a href="https://t.me/foss_lubricants_cis" target="_blank" rel="noopener">Telegram: @foss_lubricants_cis</a>
        <span>|</span>
        <a href="#rfq-section">Запрос КП и образцов</a>
      </div>
    </div>
  </aside>

  <!-- Main Sticky Header -->
  <header class="site-header">
    <div class="container header-inner">
      <a href="/ru/" class="site-logo-link" aria-label="FOSS LUBRICATION Русский">
        <img src="/assets/images/foss-official-logo.png" alt="FOSS LUBRICATION Logo - 福斯润滑" class="site-logo-img" width="135" height="48">
      </a>

      <!-- Desktop Nav -->
      <nav aria-label="Primary Navigation">
        <ul class="nav-links">
          <li><a href="/ru/" class="nav-link">Главная</a></li>
          <li><a href="/ru/hydraulic-oil" class="nav-link">Гидравлические масла</a></li>
          <li><a href="/ru/industrial-oils" class="nav-link">Индустриальные масла</a></li>
          <li><a href="/ru/packaging-logistics" class="nav-link">Упаковка и логистика</a></li>
          <li><a href="/ru/cis-central-asia" class="nav-link active">СНГ и Центральная Азия</a></li>
          <li><a href="/ru/about" class="nav-link">О заводе</a></li>
          <li><a href="/ru/news" class="nav-link">Аналитика рынка</a></li>
          <li><a href="/ru/contact" class="nav-link">Контакты и RFQ</a></li>
        </ul>
      </nav>

      <div class="header-actions">
        <div class="lang-switcher">
          <button class="lang-toggle" type="button" aria-expanded="false" aria-label="Выбрать язык">
            <span class="lang-globe">🌐</span>
            <span class="lang-current">RU</span>
            <svg class="lang-chevron" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9l6 6 6-6"/></svg>
          </button>
          <div class="lang-dropdown" role="menu">
            <a href="/products" class="lang-option" role="menuitem" data-code="en">
              <span class="lang-flag">🇺🇸</span>
              <span class="lang-title">English</span>
              <span class="lang-code-pill">EN</span>
            </a>
            <a href="/es/products" class="lang-option" role="menuitem" data-code="es">
              <span class="lang-flag">🇪🇸</span>
              <span class="lang-title">Español</span>
              <span class="lang-code-pill">ES</span>
            </a>
            <a href="/ru/cis-central-asia" class="lang-option active" role="menuitem" data-code="ru">
              <span class="lang-flag">🇷🇺</span>
              <span class="lang-title">Русский</span>
              <span class="lang-code-pill">RU</span>
            </a>
            <a href="/ar/products" class="lang-option" role="menuitem" data-code="ar">
              <span class="lang-flag">🇸🇦</span>
              <span class="lang-title">العربية</span>
              <span class="lang-code-pill">AR</span>
            </a>
            <a href="/vi/products" class="lang-option" role="menuitem" data-code="vi">
              <span class="lang-flag">🇻🇳</span>
              <span class="lang-title">Tiếng Việt</span>
              <span class="lang-code-pill">VI</span>
            </a>
            <a href="/id/products" class="lang-option" role="menuitem" data-code="id">
              <span class="lang-flag">🇮🇩</span>
              <span class="lang-title">Indonesia</span>
              <span class="lang-code-pill">ID</span>
            </a>
          </div>
        </div>
        <a href="#rfq-section" class="btn btn-primary btn-sm">Запросить КП</a>
        <button class="mobile-menu-btn" aria-label="Открыть меню">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 6h16M4 12h16M4 18h16"/></svg>
        </button>
      </div>
    </div>
  </header>

  <main id="main-content">

    <!-- Hero Banner with Authentic Production & Logistics Visual -->
    <section class="page-hero-banner">
      <div class="page-hero-bg">
        <picture>
          <source srcset="/assets/images/banner-packaging-shipping.webp?v=20261010_v11" type="image/webp">
          <img src="/assets/images/banner-packaging-shipping.jpg?v=20261010_v11" alt="FOSS LUBRICATION экспортные контейнерные поставки масел в бочках 208 л в страны СНГ и Центральной Азии" width="1376" height="768" fetchpriority="high">
        </picture>
        <div class="page-hero-scrim"></div>
      </div>
      <div class="container page-hero-content">
        <span class="hero-badge">Центральная Азия и ЕАЭС · Россия · Казахстан · Узбекистан</span>
        <h1>Поставки индустриальных масел FOSS в Россию, Казахстан и Узбекистан</h1>
        <p class="page-meta-summary" style="font-size:1.1rem;line-height:1.65;color:#e2e8f0;margin:12px 0 24px 0;max-width:860px;">Прямые оптовые поставки гидравлических, редукторных и компрессорных масел FOSS в бочках 208 л и кубах 1000 л в РФ, Казахстан и Узбекистан. Соответствие ТР ТС 030/2012, Ж/Д логистика через Хоргос и Достык, расчеты в юанях (CNY) и рублях.</p>
        <div class="hero-actions" style="display:flex;gap:14px;flex-wrap:wrap;">
          <a href="#rfq-section" class="btn btn-primary btn-lg">Запросить расчет поставки</a>
          <a href="https://t.me/foss_lubricants_cis" target="_blank" rel="noopener noreferrer" class="btn btn-secondary btn-lg" style="background:#2AABEE;border-color:#2AABEE;color:#ffffff;display:inline-flex;align-items:center;gap:8px;">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm4.64 6.8c-.15 1.58-.8 5.42-1.13 7.19-.14.75-.42 1-.68 1.03-.58.05-1.02-.38-1.58-.75-.88-.58-1.38-.94-2.23-1.5-.99-.65-.35-1.01.22-1.59.15-.15 2.71-2.48 2.76-2.69a.2.2 0 00-.05-.18c-.06-.05-.14-.03-.21-.02-.09.02-1.49.95-4.22 2.79-.4.27-.76.41-1.08.4-.36-.01-1.04-.2-1.55-.37-.63-.2-1.12-.31-1.08-.66.02-.18.27-.36.74-.55 2.92-1.27 4.86-2.11 5.83-2.51 2.78-1.16 3.35-1.36 3.73-1.36.08 0 .27.02.39.12.1.08.13.19.14.27-.01.06.01.24 0 .38z"/></svg>
            Написать в Telegram
          </a>
          <a href="#gost-matrix" class="btn btn-secondary btn-lg">Таблица аналогов ГОСТ</a>
        </div>
      </div>
    </section>

    <!-- Key Advantage Metrics -->
    <section class="section" style="background:#ffffff;padding:50px 0;border-bottom:1px solid #e2e8f0;">
      <div class="container">
        <div class="stats-grid" style="display:grid;grid-template-columns:repeat(auto-fit, minmax(220px, 1fr));gap:24px;">
          <div class="stat-card" style="padding:24px;border:1px solid #e2e8f0;border-radius:12px;background:#f8fafc;text-align:center;">
            <div style="font-size:2.4rem;font-weight:800;color:#0154A9;line-height:1;">10–14 дней</div>
            <div style="font-size:0.95rem;font-weight:600;color:#0f172a;margin-top:8px;">Срок Ж/Д транзита</div>
            <div style="font-size:0.85rem;color:#64748b;margin-top:4px;">Прямые поезда в Алматы (Достык) и Ташкент (Хоргос)</div>
          </div>
          <div class="stat-card" style="padding:24px;border:1px solid #e2e8f0;border-radius:12px;background:#f8fafc;text-align:center;">
            <div style="font-size:2.4rem;font-weight:800;color:#0154A9;line-height:1;">80 бочек</div>
            <div style="font-size:0.95rem;font-weight:600;color:#0f172a;margin-top:8px;">В 20ft Ж/Д контейнере</div>
            <div style="font-size:0.85rem;color:#64748b;margin-top:4px;">16 640 литров (20 паллет в 2 яруса), масса брутто ~15.8 т</div>
          </div>
          <div class="stat-card" style="padding:24px;border:1px solid #e2e8f0;border-radius:12px;background:#f8fafc;text-align:center;">
            <div style="font-size:2.4rem;font-weight:800;color:#0154A9;line-height:1;">ТР ТС 030/2012</div>
            <div style="font-size:0.95rem;font-weight:600;color:#0f172a;margin-top:8px;">Сертификация ЕАЭС</div>
            <div style="font-size:0.85rem;color:#64748b;margin-top:4px;">Декларация ЕАС, форма СТ-1, заводские паспорта качества (COA)</div>
          </div>
          <div class="stat-card" style="padding:24px;border:1px solid #e2e8f0;border-radius:12px;background:#f8fafc;text-align:center;">
            <div style="font-size:2.4rem;font-weight:800;color:#0154A9;line-height:1;">100% CNY / RUB</div>
            <div style="font-size:0.95rem;font-weight:600;color:#0f172a;margin-top:8px;">Безопасные расчеты</div>
            <div style="font-size:0.85rem;color:#64748b;margin-top:4px;">Прямые платежи в китайских юанях и рублях без риска SWIFT</div>
          </div>
        </div>
      </div>
    </section>

    <!-- Regional Corridors Section -->
    <section class="section" style="background:#f8fafc;padding:64px 0;">
      <div class="container">
        <div class="section-header text-center" style="max-width:780px;margin:0 auto 48px auto;">
          <h2 style="font-size:2.2rem;font-weight:800;color:#0f172a;margin-bottom:12px;">Специфика поставок по регионам Центральной Азии и СНГ</h2>
          <p style="font-size:1.05rem;color:#475569;line-height:1.6;">Индивидуальные логистические маршруты, профильные марки масел под климат и отрасли, гарантия бесперебойных отгрузок для ключевых промышленных центров.</p>
        </div>

        <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(320px, 1fr));gap:28px;">
          <!-- Kazakhstan Card -->
          <div style="background:#ffffff;border:1px solid #e2e8f0;border-radius:16px;padding:32px;box-shadow:0 4px 12px rgba(0,0,0,0.03);">
            <div style="display:flex;align-items:center;gap:12px;margin-bottom:16px;">
              <span style="font-size:2rem;">🇰🇿</span>
              <h3 style="font-size:1.4rem;font-weight:700;color:#0f172a;margin:0;">Республика Казахстан</h3>
            </div>
            <p style="color:#475569;font-size:0.95rem;line-height:1.6;margin-bottom:16px;">
              <strong>Ключевые центры:</strong> Алматы, Астана, Шымкент, Караганда, Атырау.<br>
              <strong>Отрасли:</strong> Горнодобывающая промышленность, открытые угольные разрезы, карьерная техника, нефтегазовые промыслы.
            </p>
            <div style="background:#f1f5f9;padding:14px;border-radius:8px;font-size:0.9rem;line-height:1.5;margin-bottom:18px;">
              <strong>Рекомендуемые масла FOSS:</strong>
              <ul style="margin:6px 0 0 16px;padding:0;">
                <li><strong>FOSS L-HV 46 (HVLP)</strong>: морозостойкое (до -42°C, VI >= 152) для экскаваторов и буровых станков.</li>
                <li><strong>FOSS L-CKD 220/320</strong>: тяжелые редукторы мельниц и конвейерных систем.</li>
              </ul>
            </div>
            <p style="font-size:0.88rem;color:#64748b;margin:0;">
              <strong>Логистика:</strong> Ж/Д контейнеры через погранпереходы Алашанькоу / Достык и Хоргос. Срок прибытия в Алматы: <strong>10–14 дней</strong>.
            </p>
          </div>

          <!-- Uzbekistan Card -->
          <div style="background:#ffffff;border:1px solid #e2e8f0;border-radius:16px;padding:32px;box-shadow:0 4px 12px rgba(0,0,0,0.03);">
            <div style="display:flex;align-items:center;gap:12px;margin-bottom:16px;">
              <span style="font-size:2rem;">🇺🇿</span>
              <h3 style="font-size:1.4rem;font-weight:700;color:#0f172a;margin:0;">Республика Узбекистан</h3>
            </div>
            <p style="color:#475569;font-size:0.95rem;line-height:1.6;margin-bottom:16px;">
              <strong>Ключевые центры:</strong> Ташкент, Самарканд, Навои, Бухара, Алмалык.<br>
              <strong>Отрасли:</strong> Металлургические комбинаты (АГМК, НГМК), текстильное и швейное машиностроение, химические производства.
            </p>
            <div style="background:#f1f5f9;padding:14px;border-radius:8px;font-size:0.9rem;line-height:1.5;margin-bottom:18px;">
              <strong>Рекомендуемые масла FOSS:</strong>
              <ul style="margin:6px 0 0 16px;padding:0;">
                <li><strong>FOSS 4631 HFC</strong>: огнестойкая водно-гликолевая гидравлическая жидкость для литья под давлением.</li>
                <li><strong>FOSS L-HM 46 (HLP)</strong>: чистота ISO 4406 17/15/12 для станков и гидропрессов.</li>
              </ul>
            </div>
            <p style="font-size:0.88rem;color:#64748b;margin:0;">
              <strong>Логистика:</strong> Прямые Ж/Д поезда через Хоргос до станций Ташкента (Чукурсай, Сергели). Срок: <strong>12–16 дней</strong>.
            </p>
          </div>

          <!-- Russia Card -->
          <div style="background:#ffffff;border:1px solid #e2e8f0;border-radius:16px;padding:32px;box-shadow:0 4px 12px rgba(0,0,0,0.03);">
            <div style="display:flex;align-items:center;gap:12px;margin-bottom:16px;">
              <span style="font-size:2rem;">🇷🇺</span>
              <h3 style="font-size:1.4rem;font-weight:700;color:#0f172a;margin:0;">Российская Федерация</h3>
            </div>
            <p style="color:#475569;font-size:0.95rem;line-height:1.6;margin-bottom:16px;">
              <strong>Ключевые центры:</strong> Москва, Санкт-Петербург, Екатеринбург, Челябинск, Новосибирск.<br>
              <strong>Отрасли:</strong> Станкостроение, металлообработка на станках с ЧПУ, пластиковая экструзия, компрессорные станции.
            </p>
            <div style="background:#f1f5f9;padding:14px;border-radius:8px;font-size:0.9rem;line-height:1.5;margin-bottom:18px;">
              <strong>Рекомендуемые масла FOSS:</strong>
              <ul style="margin:6px 0 0 16px;padding:0;">
                <li><strong>FOSS L-DAH 46</strong>: синтетические и полусинтетические масла для винтовых компрессоров (до 6000 ч).</li>
                <li><strong>FOSS L-HG 68</strong>: масла для направляющих скольжения станков (анти-stick-slip).</li>
              </ul>
            </div>
            <p style="font-size:0.88rem;color:#64748b;margin:0;">
              <strong>Логистика:</strong> Транзитные Ж/Д поезда через Забайкальск или морская доставка через порт Владивосток. Срок: <strong>18–24 дня</strong>.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Cross-Reference GOST vs DIN vs ISO Table -->
    <section class="section" id="gost-matrix" style="background:#ffffff;padding:64px 0;">
      <div class="container">
        <div class="section-header text-center" style="max-width:800px;margin:0 auto 40px auto;">
          <h2 style="font-size:2.2rem;font-weight:800;color:#0f172a;margin-bottom:12px;">Таблица взаимозаменяемости ГОСТ, DIN, ISO и импортозамещения</h2>
          <p style="font-size:1.05rem;color:#475569;line-height:1.6;">Инженерное соответствие продуктовой линейки FOSS LUBRICATION государственным стандартам РФ/СНГ и аналогам ведущих мировых и отечественных брендов.</p>
        </div>

        <div style="overflow-x:auto;">
          <table class="specs-table" style="width:100%;border-collapse:collapse;margin-bottom:24px;border:1px solid #e2e8f0;font-size:0.92rem;">
            <thead>
              <tr style="background:#0154A9;color:#ffffff;text-align:left;">
                <th style="padding:14px 16px;border:1px solid #024388;">Продукт FOSS</th>
                <th style="padding:14px 16px;border:1px solid #024388;">Международный стандарт</th>
                <th style="padding:14px 16px;border:1px solid #024388;">Соответствие ГОСТ</th>
                <th style="padding:14px 16px;border:1px solid #024388;">Аналоги Mobil / Shell</th>
                <th style="padding:14px 16px;border:1px solid #024388;">Аналоги Лукойл / ГПН</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom:1px solid #e2e8f0;">
                <td style="padding:12px 16px;font-weight:700;color:#0154A9;">FOSS L-HM 32</td>
                <td style="padding:12px 16px;">DIN 51524-2 (HLP 32)<br>ISO 11158 HM</td>
                <td style="padding:12px 16px;"><strong>ГОСТ 17479.3-85</strong><br>МГЕ-32В (И-Г-А-32)</td>
                <td style="padding:12px 16px;">Mobil DTE 24<br>Shell Tellus S2 M 32</td>
                <td style="padding:12px 16px;">Лукойл Гейзер СТ 32<br>ГПН Hydraulic HLP 32</td>
              </tr>
              <tr style="background:#f8fafc;border-bottom:1px solid #e2e8f0;">
                <td style="padding:12px 16px;font-weight:700;color:#0154A9;">FOSS L-HM 46</td>
                <td style="padding:12px 16px;">DIN 51524-2 (HLP 46)<br>Denison HF-0</td>
                <td style="padding:12px 16px;"><strong>ГОСТ 17479.3-85</strong><br>МГЕ-46В (И-Г-А-46)</td>
                <td style="padding:12px 16px;">Mobil DTE 25<br>Shell Tellus S2 M 46</td>
                <td style="padding:12px 16px;">Лукойл Гейзер СТ 46<br>ГПН Hydraulic HLP 46</td>
              </tr>
              <tr style="border-bottom:1px solid #e2e8f0;">
                <td style="padding:12px 16px;font-weight:700;color:#0154A9;">FOSS L-HM 68</td>
                <td style="padding:12px 16px;">DIN 51524-2 (HLP 68)<br>US Steel 127</td>
                <td style="padding:12px 16px;"><strong>ГОСТ 17479.3-85</strong><br>МГЕ-68В (И-Г-А-68)</td>
                <td style="padding:12px 16px;">Mobil DTE 26<br>Shell Tellus S2 M 68</td>
                <td style="padding:12px 16px;">Лукойл Гейзер СТ 68<br>ГПН Hydraulic HLP 68</td>
              </tr>
              <tr style="background:#f8fafc;border-bottom:1px solid #e2e8f0;">
                <td style="padding:12px 16px;font-weight:700;color:#0154A9;">FOSS L-HV 46</td>
                <td style="padding:12px 16px;">DIN 51524-3 (HVLP 46)<br>Индекс вязкости >= 152</td>
                <td style="padding:12px 16px;"><strong>ГОСТ 17479.3-85</strong><br>МГ-46-В (И-ГТ-А-46)</td>
                <td style="padding:12px 16px;">Mobil DTE 10 Excel 46<br>Shell Tellus S2 V 46</td>
                <td style="padding:12px 16px;">Лукойл Гейзер ЛТ 46<br>ГПН Hydraulic HVLP 46</td>
              </tr>
              <tr style="border-bottom:1px solid #e2e8f0;">
                <td style="padding:12px 16px;font-weight:700;color:#0154A9;">FOSS L-CKD 220</td>
                <td style="padding:12px 16px;">DIN 51517-3 (CLP 220)<br>FZG тест >= 12</td>
                <td style="padding:12px 16px;"><strong>ГОСТ 17479.4-87</strong><br>ИТД-220</td>
                <td style="padding:12px 16px;">Mobilgear 600 XP 220<br>Shell Omala S2 G 220</td>
                <td style="padding:12px 16px;">Лукойл Стилфлекс 220<br>ГПН Reductor CLP 220</td>
              </tr>
              <tr style="background:#f8fafc;border-bottom:1px solid #e2e8f0;">
                <td style="padding:12px 16px;font-weight:700;color:#0154A9;">FOSS L-CKD 320</td>
                <td style="padding:12px 16px;">DIN 51517-3 (CLP 320)<br>AGMA 9005-E02</td>
                <td style="padding:12px 16px;"><strong>ГОСТ 17479.4-87</strong><br>ИТД-320</td>
                <td style="padding:12px 16px;">Mobilgear 600 XP 320<br>Shell Omala S2 G 320</td>
                <td style="padding:12px 16px;">Лукойл Стилфлекс 320<br>ГПН Reductor CLP 320</td>
              </tr>
              <tr style="border-bottom:1px solid #e2e8f0;">
                <td style="padding:12px 16px;font-weight:700;color:#0154A9;">FOSS 4631 HFC</td>
                <td style="padding:12px 16px;">ISO 12922 HFC<br>Водно-гликолевое (~40% воды)</td>
                <td style="padding:12px 16px;">Огнестойкие жидкости<br>для металлургии</td>
                <td style="padding:12px 16px;">Quaker Houghto-Safe 620<br>Fuchs Hydrotherm 46M</td>
                <td style="padding:12px 16px;">Промгидрол ВГХ-46</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <!-- Financial Safety & Sanctions Resilience -->
    <section class="section" style="background:#f8fafc;padding:64px 0;border-top:1px solid #e2e8f0;">
      <div class="container">
        <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(300px, 1fr));gap:36px;align-items:center;">
          <div>
            <span class="hero-badge" style="background:#dbeafe;color:#0154A9;">Финансовая и юридическая безопасность</span>
            <h2 style="font-size:2rem;font-weight:800;color:#0f172a;margin:12px 0 16px 0;">Прямые расчеты в CNY без риска блокировок платежей</h2>
            <p style="color:#475569;line-height:1.65;font-size:1rem;margin-bottom:18px;">
              В текущих условиях международных финансовых ограничений Quanzhou Foss Lubrication Technology Co., Ltd обеспечивает 100% стабильность внешнеторговых транзакций:
            </p>
            <ul style="color:#334155;line-height:1.7;font-size:0.95rem;padding-left:20px;margin-bottom:24px;">
              <li><strong>Расчеты в китайских юанях (CNY)</strong>: прямые переводы на корреспондентские счета в банках КНР через систему CIPS, полностью независимую от SWIFT.</li>
              <li><strong>Оплата в российских рублях (RUB)</strong>: возможность взаиморасчетов в национальных валютах для предприятий РФ и Казахстана.</li>
              <li><strong>Документарные безотзывные аккредитивы (L/C)</strong>: максимальная защита покупателя при крупных контейнерных контрактах.</li>
              <li><strong>Прозрачные условия Инкотермс 2020</strong>: поставка на базисах FOB Xiamen, CIF Владивосток/СПб, DAP Достык/Алматы, DAP Ташкент (Сергели/Чукурсай).</li>
            </ul>
            <a href="#rfq-section" class="btn btn-primary">Получить проект контракта</a>
          </div>

          <div style="background:#ffffff;border:1px solid #cbd5e1;border-radius:16px;padding:32px;box-shadow:0 8px 24px rgba(0,0,0,0.04);">
            <h3 style="font-size:1.3rem;font-weight:700;color:#0f172a;margin-bottom:14px;">Комплект документов к каждой отгрузке:</h3>
            <ol style="color:#475569;line-height:1.7;font-size:0.92rem;padding-left:18px;margin:0 0 20px 0;">
              <li>Декларация о соответствии требованиям <strong>ТР ТС 030/2012</strong>.</li>
              <li>Сертификат происхождения <strong>Форма СТ-1</strong> (для беспошлинного ввоза в страны СНГ) либо Certificate of Origin (CO).</li>
              <li>Заводской <strong>Паспорт качества (Certificate of Analysis — COA)</strong> с результатами испытаний вязкости, вспышки и чистоты.</li>
              <li><strong>Паспорт безопасности (MSDS)</strong> на русском языке по стандарту GHS.</li>
              <li>Железнодорожная накладная (СМГС / SMGS) либо коносамент (Ocean B/L).</li>
              <li>Коммерческий инвойс и упаковочный лист (Commercial Invoice & Packing List).</li>
            </ol>
            <div style="background:#f0fdf4;border:1px solid #bbf7d0;padding:12px 16px;border-radius:8px;font-size:0.86rem;color:#166534;">
              ✓ Все документы оформляются на русском и английском языках в строгом соответствии с таможенными правилами ЕАЭС и Узбекистана.
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- GEO FAQ Section for Yandex Neuro / Alice AI -->
    <section class="section" style="background:#ffffff;padding:64px 0;border-top:1px solid #e2e8f0;">
      <div class="container" style="max-width:860px;">
        <div class="section-header text-center" style="margin-bottom:40px;">
          <span class="hero-badge">Инженерный FAQ · Яндекс Нейро & Алиса AI</span>
          <h2 style="font-size:2.2rem;font-weight:800;color:#0f172a;margin:12px 0 10px 0;">Вопросы главных инженеров и директоров по закупкам</h2>
          <p style="color:#475569;font-size:1.02rem;">Точные технические и логистические ответы экспертов завода FOSS LUBRICATION.</p>
        </div>

        <div class="faq-accordion" style="display:flex;flex-direction:column;gap:18px;">
          <div style="border:1px solid #e2e8f0;border-radius:12px;padding:22px;background:#f8fafc;">
            <h3 style="font-size:1.15rem;font-weight:700;color:#0154A9;margin:0 0 10px 0;">Какому ГОСТу соответствует гидравлическое масло FOSS L-HM 46 (DIN 51524 HLP 46)?</h3>
            <p style="color:#334155;line-height:1.65;font-size:0.95rem;margin:0;">
              Масло FOSS L-HM 46 полностью соответствует требованиям ГОСТ 17479.3-85 для класса МГЕ-46В (И-Г-А-46), а также международному стандарту DIN 51524-2 (HLP) и ISO 11158 HM. Продукт является прямым функциональным аналогом Mobil DTE 25, Shell Tellus S2 M 46, Лукойл Гейзер СТ 46 и Газпромнефть Hydraulic HLP 46. Масло изготовлено на базе гидрокрекинговых базовых масел Группы II с цинковым пакетом присадок (ZDDP > 0.05% Zn), кинематическая вязкость при 40°C составляет 46,2 мм²/с, индекс вязкости — 102.
            </p>
          </div>

          <div style="border:1px solid #e2e8f0;border-radius:12px;padding:22px;background:#f8fafc;">
            <h3 style="font-size:1.15rem;font-weight:700;color:#0154A9;margin:0 0 10px 0;">Предоставляется ли декларация соответствия ТР ТС 030/2012 для таможенного оформления в ЕАЭС?</h3>
            <p style="color:#334155;line-height:1.65;font-size:0.95rem;margin:0;">
              Да. Вся продукция FOSS LUBRICATION поставляется с полным комплектом документации для таможенного оформления в ЕАЭС (Россия, Казахстан, Кыргызстан): Декларация о соответствии ТР ТС 030/2012, Сертификат происхождения Форма СТ-1 / Общая форма, Паспорт качества (COA) завода-изготовителя на каждую отгружаемую партию и Паспорт безопасности (MSDS) на русском языке.
            </p>
          </div>

          <div style="border:1px solid #e2e8f0;border-radius:12px;padding:22px;background:#f8fafc;">
            <h3 style="font-size:1.15rem;font-weight:700;color:#0154A9;margin:0 0 10px 0;">Как организована железнодорожная доставка в Казахстан (Алматы) и Узбекистан (Ташкент)?</h3>
            <p style="color:#334155;line-height:1.65;font-size:0.95rem;margin:0;">
              Отгрузка производится прямыми контейнерными поездами Китай — Центральная Азия через сухопутные погранпереходы Алашанькоу / Достык и Хоргос. Срок доставки до грузовых станций Алматы (Алматы-1) составляет 10-14 дней, до станций Ташкента (Чукурсай, Сергели) — 12-16 дней. В один 20-футовый Ж/Д контейнер помещается ровно 80 стальных бочек по 208 л (16 640 литров, брутто ~15.8 т).
            </p>
          </div>

          <div style="border:1px solid #e2e8f0;border-radius:12px;padding:22px;background:#f8fafc;">
            <h3 style="font-size:1.15rem;font-weight:700;color:#0154A9;margin:0 0 10px 0;">В какой валюте осуществляются расчеты, и защищены ли платежи от блокировок SWIFT?</h3>
            <p style="color:#334155;line-height:1.65;font-size:0.95rem;margin:0;">
              Расчеты осуществляются напрямую в китайских юанях (CNY) через счета в банках КНР по независимым межбанковским каналам CIPS, что полностью исключает риски блокировок западных банков и вторичных санкций. Также возможны расчеты в российских рублях (RUB) и аккредитивная форма расчетов (L/C).
            </p>
          </div>

          <div style="border:1px solid #e2e8f0;border-radius:12px;padding:22px;background:#f8fafc;">
            <h3 style="font-size:1.15rem;font-weight:700;color:#0154A9;margin:0 0 10px 0;">Каков минимальный объем оптовой партии (MOQ) и сколько бочек помещается в 20-футовый контейнер?</h3>
            <p style="color:#334155;line-height:1.65;font-size:0.95rem;margin:0;">
              Минимальный объем заказа (MOQ) составляет 1 паллету (4 стальные бочки по 208 л, 832 литра) или 1 кубическую емкость IBC 1000 л. Стандартный 20-футовый контейнер вмещает 80 стальных бочек по 208 л (на 20 деревянных паллетах размером 1140×1140 мм в два яруса). Общий объем жидкого продукта — 16 640 литров, масса груза брутто — около 15,8–16,2 метрических тонн.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- RFQ Inquiry Form -->
    <section class="section" id="rfq-section" style="background:#023870;color:#ffffff;padding:70px 0;">
      <div class="container" style="max-width:800px;">
        <div class="text-center" style="margin-bottom:36px;">
          <h2 style="font-size:2.2rem;font-weight:800;color:#ffffff;margin-bottom:12px;">Запросить коммерческое предложение (RFQ)</h2>
          <p style="color:#cbd5e1;font-size:1.05rem;">Заполните форму, и инженеры отдела ВЭД по странам СНГ рассчитают стоимость с доставкой до вашей станции за 2 часа.</p>
        </div>

        <form action="/api/rfq" method="POST" style="background:#ffffff;color:#0f172a;padding:36px;border-radius:16px;box-shadow:0 12px 32px rgba(0,0,0,0.2);">
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-bottom:16px;">
            <div>
              <label style="display:block;font-size:0.88rem;font-weight:600;margin-bottom:6px;">Ваше имя *</label>
              <input type="text" name="name" required placeholder="Иван Иванов" style="width:100%;padding:12px;border:1px solid #cbd5e1;border-radius:8px;font-size:0.95rem;">
            </div>
            <div>
              <label style="display:block;font-size:0.88rem;font-weight:600;margin-bottom:6px;">Компания и город назначения *</label>
              <input type="text" name="company" required placeholder="ТОО 'ГорМаш', г. Алматы" style="width:100%;padding:12px;border:1px solid #cbd5e1;border-radius:8px;font-size:0.95rem;">
            </div>
          </div>

          <div style="display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-bottom:16px;">
            <div>
              <label style="display:block;font-size:0.88rem;font-weight:600;margin-bottom:6px;">Email для КП *</label>
              <input type="email" name="email" required placeholder="ivan@gormash.kz" style="width:100%;padding:12px;border:1px solid #cbd5e1;border-radius:8px;font-size:0.95rem;">
            </div>
            <div>
              <label style="display:block;font-size:0.88rem;font-weight:600;margin-bottom:6px;">Телефон / Telegram / WhatsApp *</label>
              <input type="text" name="phone" required placeholder="+7 777 123 4567 / @telegram" style="width:100%;padding:12px;border:1px solid #cbd5e1;border-radius:8px;font-size:0.95rem;">
            </div>
          </div>

          <div style="margin-bottom:16px;">
            <label style="display:block;font-size:0.88rem;font-weight:600;margin-bottom:6px;">Интересующая продукция и объем *</label>
            <select name="product" style="width:100%;padding:12px;border:1px solid #cbd5e1;border-radius:8px;font-size:0.95rem;background:#ffffff;">
              <option value="L-HM-46">FOSS L-HM 46 (DIN 51524 HLP / ГОСТ МГЕ-46В) — от 80 бочек (20ft)</option>
              <option value="L-HV-46">FOSS L-HV 46 Морозостойкое (DIN HVLP / ГОСТ МГ-46-В) — от 80 бочек</option>
              <option value="L-CKD-220">FOSS L-CKD 220 Редукторное (DIN CLP / ГОСТ ИТД-220) — от 80 бочек</option>
              <option value="L-CKD-320">FOSS L-CKD 320 Редукторное (DIN CLP / ГОСТ ИТД-320) — от 80 бочек</option>
              <option value="4631-HFC">FOSS 4631 Водно-гликолевое огнестойкое (HFC) — от 1 IBC (1000 л)</option>
              <option value="Samples">Запрос бесплатного комплекта тестовых образцов (1 л / 4 л)</option>
              <option value="Other">Другая номенклатура / контрактное производство OEM</option>
            </select>
          </div>

          <div style="margin-bottom:20px;">
            <label style="display:block;font-size:0.88rem;font-weight:600;margin-bottom:6px;">Дополнительные требования к поставке</label>
            <textarea name="notes" rows="3" placeholder="Укажите требования к фасовке, станцию назначения (Инкотермс DAP/CIF), желаемый график отгрузок..." style="width:100%;padding:12px;border:1px solid #cbd5e1;border-radius:8px;font-size:0.95rem;"></textarea>
          </div>

          <button type="submit" class="btn btn-primary btn-lg" style="width:100%;font-size:1.1rem;padding:14px;">Отправить запрос на расчет стоимости</button>
          <div style="text-align:center;font-size:0.82rem;color:#64748b;margin-top:12px;">
            Ваши данные защищены и используются исключительно для подготовки коммерческого предложения.
          </div>
        </form>
      </div>
    </section>

  </main>

  <footer class="site-footer">
    <div class="container">
      <!-- Legal Notice & Trademark Disclaimer -->
      <div class="legal-notice-box">
        <strong>ОФИЦИАЛЬНОЕ УВЕДОМЛЕНИЕ:</strong><br>
        <strong>Quanzhou Foss Lubrication Technology Co., Ltd (泉州市福斯润滑科技有限公司)</strong> — независимое китайское предприятие по разработке и производству смазочных материалов, основанное в 2018 году в г. Цюаньчжоу (провинция Фуцзянь, КНР). Товарный знак FOSS LUBRICATION / 福斯润滑 зарегистрирован в КНР. Предприятие <strong>НЕ</strong> аффилировано и не связано с FUCHS Petrolub SE (Германия). Ссылки на сторонние бренды (Mobil, Shell, Total, Лукойл) используются исключительно в целях технического сопоставления и информирования инженеров-механиков.
      </div>

      <div class="footer-grid">
        <div class="footer-brand">
          <div style="display:flex; align-items:center; gap:10px; margin-bottom:12px;">
            <img src="/assets/images/foss-official-logo.png" alt="FOSS LUBRICATION Logo - 福斯润滑" class="footer-logo-img" width="120" height="50">
          </div>
          <p>
            Quanzhou Foss Lubrication Technology Co., Ltd<br>
            Основан: 23.02.2018 · г. Цюаньчжоу, провинция Фуцзянь, КНР.<br>
            Специализация: высокоэффективные гидравлические жидкости, редукторные масла, поставки в сертифицированных UN стальных бочках 208 л и кубах 1000 л в РФ, Казахстан и страны Центральной Азии.
          </p>
        </div>

        <div class="footer-col">
          <h4>Продукция</h4>
          <ul class="footer-links">
            <li><a href="/ru/hydraulic-oil">Гидравлические масла (L-HM)</a></li>
            <li><a href="/ru/hydraulic-oil">Морозостойкие масла (L-HV)</a></li>
            <li><a href="/ru/hydraulic-oil">Бесцинковые гидравлические масла</a></li>
            <li><a href="/ru/hydraulic-oil">Огнестойкие водно-гликолевые (HFC)</a></li>
            <li><a href="/ru/industrial-oils">Тяжелые редукторные масла (L-CKD)</a></li>
            <li><a href="/ru/industrial-oils">Винтовые компрессорные масла</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Регионы и логистика</h4>
          <ul class="footer-links">
            <li><a href="/ru/cis-central-asia">Поставки в РФ, Казахстан и Узбекистан</a></li>
            <li><a href="/ru/packaging-logistics">Спецификация бочек 208 л</a></li>
            <li><a href="/ru/packaging-logistics">Калькулятор загрузки контейнера 20ft</a></li>
            <li><a href="/ru/cis-central-asia#gost-matrix">Таблица аналогов ГОСТ</a></li>
            <li><a href="/ru/about">Контрактное производство OEM</a></li>
            <li><a href="/sitemap.xml">Карта сайта (Sitemap XML)</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Отдел экспорта в СНГ</h4>
          <p style="font-size:0.9rem;line-height:1.6;color:#cbd5e1;">
            Отдел ВЭД по странам СНГ и Центральной Азии:<br>
            Email: <a href="mailto:sales@fosslubricants.com" style="color:#ffffff;">sales@fosslubricants.com</a><br>
            Telegram: <a href="https://t.me/foss_lubricants_cis" target="_blank" rel="noopener" style="color:#2AABEE;">@foss_lubricants_cis</a><br>
            WhatsApp: <a href="https://wa.me/8615959543210" style="color:#25D366;">+86 159 5954 3210</a><br>
            WeChat: <strong>foss_export</strong>
          </p>
        </div>
      </div>

      <div class="footer-bottom">
        <p>&copy; 2026 Quanzhou Foss Lubrication Technology Co., Ltd. Все права защищены. Экспортные стандарты ISO 9001 / ТР ТС 030/2012.</p>
      </div>
    </div>
  </footer>

  <!-- Floating Chat Support Widget with WhatsApp, Telegram and WeChat -->
  <aside class="floating-chat-widget" id="floating-chat-widget" aria-label="Служба поддержки и консультаций">
    <!-- Popover Chat Window -->
    <div class="chat-popover-window" id="chat-popover-window" role="dialog" aria-modal="false" aria-labelledby="chat-window-title">
      <div class="chat-window-header">
        <div class="chat-header-avatar">
          <svg viewBox="0 0 32 32" class="chat-header-icon" width="22" height="22" fill="#ffffff" aria-hidden="true">
            <path d="M16 2a13.9 13.9 0 0 0-12 21L2 30l7.2-1.9A14 14 0 1 0 16 2zm0 25.5a11.5 11.5 0 0 1-5.9-1.6l-.4-.3-4.3 1.1 1.2-4.2-.3-.4A11.6 11.6 0 1 1 16 27.5zm6.4-8.6c-.3-.2-2-.1-2.3 0s-.6.3-.9.7c-.3.4-.6.7-.9.7s-.6-.1-1.3-.4c-1-.5-1.9-1.2-2.6-2-.5-.6-.9-1.2-1.2-1.8-.1-.4 0-.6.2-.8.2-.2.4-.4.6-.7.2-.2.2-.4.3-.6.1-.2 0-.4 0-.6s-.9-2.2-1.2-3c-.3-.8-.7-.7-.9-.7h-.8c-.3 0-.7.1-1.1.5-.4.4-1.5 1.5-1.5 3.6s1.5 4.2 1.7 4.5c.2.3 3 4.6 7.3 6.4 1 .4 1.8.7 2.5.9.8.3 1.9.2 2.6.1.8-.1 2.5-1 2.8-2 .4-1 .4-1.8.3-2-.1-.2-.4-.3-.7-.5z"/>
          </svg>
        </div>
        <div class="chat-header-text">
          <div class="chat-header-title" id="chat-window-title">Отдел ВЭД FOSS LUBRICATION</div>
          <div class="chat-header-sub"><span class="chat-online-dot"></span> На связи · Ответ в течение 15 минут</div>
        </div>
        <button class="chat-window-close" id="chat-window-close" aria-label="Закрыть окно">&times;</button>
      </div>

      <div class="chat-window-body">
        <p class="chat-welcome-msg">
          Здравствуйте! Чем мы можем помочь по вопросам поставки гидравлических и индустриальных масел FOSS в бочках 208 л?
        </p>

        <!-- Telegram Option (Priority for RU & CIS) -->
        <a href="https://t.me/foss_lubricants_cis" target="_blank" rel="noopener noreferrer" class="chat-channel-card telegram-card">
          <div class="channel-icon-box tg-bg">
            <svg viewBox="0 0 24 24" width="22" height="22" fill="#ffffff" aria-hidden="true">
              <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm4.64 6.8c-.15 1.58-.8 5.42-1.13 7.19-.14.75-.42 1-.68 1.03-.58.05-1.02-.38-1.58-.75-.88-.58-1.38-.94-2.23-1.5-.99-.65-.35-1.01.22-1.59.15-.15 2.71-2.48 2.76-2.69a.2.2 0 00-.05-.18c-.06-.05-.14-.03-.21-.02-.09.02-1.49.95-4.22 2.79-.4.27-.76.41-1.08.4-.36-.01-1.04-.2-1.55-.37-.63-.2-1.12-.31-1.08-.66.02-.18.27-.36.74-.55 2.92-1.27 4.86-2.11 5.83-2.51 2.78-1.16 3.35-1.36 3.73-1.36.08 0 .27.02.39.12.1.08.13.19.14.27-.01.06.01.24 0 .38z"/>
            </svg>
          </div>
          <div class="channel-info">
            <div class="channel-name">Написать в Telegram</div>
            <div class="channel-detail">@foss_lubricants_cis</div>
          </div>
          <span class="channel-arrow">&rarr;</span>
        </a>

        <!-- WhatsApp Option -->
        <a href="https://wa.me/8615959543210?text=%D0%97%D0%B4%D1%80%D0%B0%D0%B2%D1%81%D1%82%D0%B2%D1%83%D0%B9%D1%82%D0%B5%2C%20%D0%BC%D0%B5%D0%BD%D1%8F%20%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D0%B5%D1%81%D1%83%D0%B5%D1%82%20%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D0%BA%D0%B0%20%D0%BC%D0%B0%D1%81%D0%B5%D0%BB%20FOSS" target="_blank" rel="noopener noreferrer" class="chat-channel-card whatsapp-card">
          <div class="channel-icon-box wa-bg">
            <svg viewBox="0 0 32 32" width="24" height="24" fill="#ffffff" aria-hidden="true">
              <path d="M16 2a13.9 13.9 0 0 0-12 21L2 30l7.2-1.9A14 14 0 1 0 16 2zm0 25.5a11.5 11.5 0 0 1-5.9-1.6l-.4-.3-4.3 1.1 1.2-4.2-.3-.4A11.6 11.6 0 1 1 16 27.5zm6.4-8.6c-.3-.2-2-.1-2.3 0s-.6.3-.9.7c-.3.4-.6.7-.9.7s-.6-.1-1.3-.4c-1-.5-1.9-1.2-2.6-2-.5-.6-.9-1.2-1.2-1.8-.1-.4 0-.6.2-.8.2-.2.4-.4.6-.7.2-.2.2-.4.3-.6.1-.2 0-.4 0-.6s-.9-2.2-1.2-3c-.3-.8-.7-.7-.9-.7h-.8c-.3 0-.7.1-1.1.5-.4.4-1.5 1.5-1.5 3.6s1.5 4.2 1.7 4.5c.2.3 3 4.6 7.3 6.4 1 .4 1.8.7 2.5.9.8.3 1.9.2 2.6.1.8-.1 2.5-1 2.8-2 .4-1 .4-1.8.3-2-.1-.2-.4-.3-.7-.5z"/>
            </svg>
          </div>
          <div class="channel-info">
            <div class="channel-name">Чат в WhatsApp</div>
            <div class="channel-detail">+86 15959543210</div>
          </div>
          <span class="channel-arrow">&rarr;</span>
        </a>

        <!-- WeChat Option with QR / Copy -->
        <div class="chat-channel-card wechat-card" id="wechat-toggle-card">
          <div class="channel-icon-box wx-bg">
            <svg viewBox="0 0 28 28" width="22" height="22" fill="#ffffff" aria-hidden="true">
              <path d="M10.5 4C5.8 4 2 7.4 2 11.5c0 2.4 1.3 4.5 3.3 5.8-.2.8-.7 2.4-.8 2.7 0 0-.1.2.1.2.2 0 2.2-1.4 3.1-2 .9.3 1.8.4 2.8.4.3 0 .7 0 1-.1-.3-.7-.4-1.5-.4-2.3 0-4 3.5-7.2 7.9-7.2h.4C18.2 5.5 14.6 4 10.5 4zm-2.8 4.2c.8 0 1.4.6 1.4 1.4s-.6 1.4-1.4 1.4-1.4-.6-1.4-1.4.6-1.4 1.4-1.4zm5.6 0c.8 0 1.4.6 1.4 1.4s-.6 1.4-1.4 1.4-1.4-.6-1.4-1.4.6-1.4 1.4-1.4zm6.3 3.6c-3.9 0-7 2.7-7 6.1 0 3.4 3.1 6.1 7 6.1.8 0 1.6-.1 2.3-.4.8.5 2.4 1.6 2.6 1.6.2 0 .1-.2.1-.2-.1-.3-.5-1.5-.7-2.1 1.7-1.1 2.7-2.8 2.7-4.9 0-3.4-3.1-6.2-7-6.2zm-2.1 3.5c.6 0 1.1.5 1.1 1.1s-.5 1.1-1.1 1.1-1.1-.5-1.1-1.1.5-1.1 1.1-1.1zm4.6 0c.6 0 1.1.5 1.1 1.1s-.5 1.1-1.1 1.1-1.1-.5-1.1-1.1.5-1.1 1.1-1.1z"/>
            </svg>
          </div>
          <div class="channel-info">
            <div class="channel-name">Связаться в WeChat</div>
            <div class="channel-detail">ID: foss_export</div>
          </div>
          <span class="channel-arrow">&rarr;</span>
        </div>
      </div>

      <div class="chat-window-footer">
        Время работы завода: Пн–Пт, 08:30–18:00 (UTC+8)
      </div>
    </div>

    <!-- Trigger Button with Notification Pulse and Badge -->
    <button class="chat-trigger-btn" id="chat-trigger-btn" type="button" aria-expanded="false" aria-label="Открыть онлайн-чат поддержки">
      <div class="trigger-pulse"></div>
      <svg viewBox="0 0 32 32" class="wa-trigger-logo" width="34" height="34" fill="currentColor" aria-hidden="true">
        <path d="M16 2a13.9 13.9 0 0 0-12 21L2 30l7.2-1.9A14 14 0 1 0 16 2zm0 25.5a11.5 11.5 0 0 1-5.9-1.6l-.4-.3-4.3 1.1 1.2-4.2-.3-.4A11.6 11.6 0 1 1 16 27.5zm6.4-8.6c-.3-.2-2-.1-2.3 0s-.6.3-.9.7c-.3.4-.6.7-.9.7s-.6-.1-1.3-.4c-1-.5-1.9-1.2-2.6-2-.5-.6-.9-1.2-1.2-1.8-.1-.4 0-.6.2-.8.2-.2.4-.4.6-.7.2-.2.2-.4.3-.6.1-.2 0-.4 0-.6s-.9-2.2-1.2-3c-.3-.8-.7-.7-.9-.7h-.8c-.3 0-.7.1-1.1.5-.4.4-1.5 1.5-1.5 3.6s1.5 4.2 1.7 4.5c.2.3 3 4.6 7.3 6.4 1 .4 1.8.7 2.5.9.8.3 1.9.2 2.6.1.8-.1 2.5-1 2.8-2 .4-1 .4-1.8.3-2-.1-.2-.4-.3-.7-.5z"/>
      </svg>
      <div class="chat-trigger-badge" aria-hidden="true">1</div>
    </button>
  </aside>

  <script src="/js/app.js?v=20261010_v11"></script>
  <script>
    (function() {
      function initFloatingChat() {
        var triggerBtn = document.getElementById('chat-trigger-btn');
        var popover = document.getElementById('chat-popover-window');
        var closeBtn = document.getElementById('chat-window-close');
        var wechatCard = document.getElementById('wechat-toggle-card');

        if (!triggerBtn || !popover) return;

        triggerBtn.addEventListener('click', function(e) {
          e.stopPropagation();
          var isOpen = popover.classList.contains('open');
          if (isOpen) {
            popover.classList.remove('open');
            triggerBtn.setAttribute('aria-expanded', 'false');
          } else {
            popover.classList.add('open');
            triggerBtn.setAttribute('aria-expanded', 'true');
          }
        });

        if (closeBtn) {
          closeBtn.addEventListener('click', function(e) {
            e.stopPropagation();
            popover.classList.remove('open');
            triggerBtn.setAttribute('aria-expanded', 'false');
          });
        }

        if (wechatCard) {
          wechatCard.addEventListener('click', function(e) {
            e.preventDefault();
            navigator.clipboard.writeText('foss_export').then(function() {
              alert('WeChat ID "foss_export" скопирован в буфер обмена!');
            }).catch(function() {
              prompt('Скопируйте WeChat ID:', 'foss_export');
            });
          });
        }

        document.addEventListener('click', function(e) {
          var widget = document.getElementById('floating-chat-widget');
          if (widget && !widget.contains(e.target)) {
            popover.classList.remove('open');
            triggerBtn.setAttribute('aria-expanded', 'false');
          }
        });
      }

      if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initFloatingChat);
      } else {
        initFloatingChat();
      }
    })();
  </script>
</body>
</html>
"""


def write_cis_hub():
    target_path = os.path.join(WORKSPACE_DIR, "ru", "cis-central-asia.html")
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(CIS_HUB_HTML.strip() + "\n")
    print(f"[OK] Generated {target_path}")


def update_russian_pages_nav_and_meta():
    """Updates all Russian pages with Yandex verification, og:locale, and nav links."""
    ru_dir = os.path.join(WORKSPACE_DIR, "ru")
    html_files = [f for f in os.listdir(ru_dir) if f.endswith(".html")]

    cis_nav_item = '          <li><a href="/ru/cis-central-asia" class="nav-link">СНГ и ЦА</a></li>\n'
    yandex_meta = '  <!-- Yandex Webmaster Verification -->\n  <meta name="yandex-verification" content="f0551ubr1can75_ym_ver1fy">\n  <meta property="og:locale" content="ru_RU">\n  <meta property="og:locale:alternate" content="ru_KZ">\n  <meta property="og:locale:alternate" content="ru_UZ">\n'

    for fname in html_files:
        if fname == "cis-central-asia.html":
            continue
        fpath = os.path.join(ru_dir, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        modified = False

        # 1. Add Yandex verification if not present
        if "yandex-verification" not in content:
            if "<meta property=\"og:type\"" in content:
                content = content.replace(
                    "<meta property=\"og:type\"",
                    yandex_meta + "  <meta property=\"og:type\"",
                    1
                )
                modified = True
            elif "<link rel=\"stylesheet\"" in content:
                content = content.replace(
                    "<link rel=\"stylesheet\"",
                    yandex_meta + "  <link rel=\"stylesheet\"",
                    1
                )
                modified = True

        # 2. Add CIS link to nav-links if not present
        if "/ru/cis-central-asia" not in content and '<ul class="nav-links">' in content:
            # Insert after packaging-logistics
            if '<li><a href="/ru/packaging-logistics" class="nav-link">Упаковка и логистика</a></li>' in content:
                content = content.replace(
                    '<li><a href="/ru/packaging-logistics" class="nav-link">Упаковка и логистика</a></li>',
                    '<li><a href="/ru/packaging-logistics" class="nav-link">Упаковка и логистика</a></li>\n' + cis_nav_item,
                    1
                )
                modified = True
            elif '<li><a href="/ru/packaging-logistics"' in content:
                # regex replace
                content = re.sub(
                    r'(<li><a href="/ru/packaging-logistics"[^>]*>.*?</a></li>)',
                    r'\1\n' + cis_nav_item,
                    content,
                    count=1
                )
                modified = True

        # 3. Add CIS link to footer if present
        if '<h4>Регионы и логистика</h4>' in content and '/ru/cis-central-asia' not in content:
            content = content.replace(
                '<h4>Регионы и логистика</h4>\n          <ul class="footer-links">',
                '<h4>Регионы и логистика</h4>\n          <ul class="footer-links">\n            <li><a href="/ru/cis-central-asia">Поставки в РФ, Казахстан и Узбекистан</a></li>',
                1
            )
            modified = True

        # 4. In ru/index.html, localize English FAQ questions in JSON-LD schema
        if fname == "index.html":
            # Fix English question/answers in FAQPage schema
            if "How many 208-liter steel drums fit in a 20ft container?" in content:
                content = content.replace(
                    "How many 208-liter steel drums fit in a 20ft container?",
                    "Сколько стальных бочек 208 л помещается в 20-футовый контейнер?"
                )
                content = content.replace(
                    "A standard 20ft GP container accommodates 80 x 208L steel drums on 20 pallets (4 drums per pallet in two tiers) with total liquid volume of 16,640 Liters and gross payload weight of approximately 15.8 to 16.2 Metric Tons.",
                    "Стандартный 20-футовый контейнер вмещает ровно 80 стальных бочек по 208 л на 20 деревянных паллетах в два яруса. Общий полезный объем продукта составляет 16 640 литров, вес брутто — около 15.8-16.2 метрических тонн."
                )
                content = content.replace(
                    "Can FOSS L-HM 46 hydraulic oil replace Mobil DTE 25 or Shell Tellus S2 M 46?",
                    "Может ли гидравлическое масло FOSS L-HM 46 заменить Mobil DTE 25 или Shell Tellus S2 M 46?"
                )
                content = content.replace(
                    "Yes. FOSS L-HM 46 meets and exceeds DIN 51524 Part 2 (HLP) and ISO 11158 HM specifications with kin. viscosity 46.2 mm2/s at 40C, VI 102, and demulsibility under 15 minutes. It is a direct drop-in replacement for Mobil DTE 25, Shell Tellus S2 M 46, and Castrol Hyspin AWS 46 without system flushing required.",
                    "Да. Масло FOSS L-HM 46 полностью соответствует спецификациям DIN 51524-2 (HLP), ГОСТ 17479.3 (МГЕ-46В) и ISO 11158 HM с кинематической вязкостью 46,2 мм²/с при 40°C и индексом вязкости 102. Оно является прямой функциональной заменой Mobil DTE 25, Shell Tellus S2 M 46 и Лукойл Гейзер СТ 46."
                )
                content = content.replace(
                    "What export documentation is provided with drum shipments?",
                    "Какие экспортные документы предоставляются к каждой отгрузке?"
                )
                content = content.replace(
                    "Every container shipment includes Commercial Invoice, Packing List, Clean on Board Ocean Bill of Lading, Batch Certificate of Analysis (CoA) with laboratory test results, GHS-compliant Safety Data Sheet (SDS/MSDS), and Certificate of Origin (Form E, Form RCEP, or Standard CO).",
                    "К каждой партии предоставляются: Декларация о соответствии ТР ТС 030/2012, Сертификат происхождения (Форма СТ-1 / CO), заводской Паспорт качества (COA) на русском языке, Паспорт безопасности (MSDS/ПБХВ), упаковочный лист и коносамент / Ж/Д накладная."
                )
                modified = True

            # Fix English footer in ru/index.html
            if "Product Lines" in content:
                content = content.replace("<h4>Product Lines</h4>", "<h4>Продукция FOSS</h4>")
                content = content.replace("<h4>Logistics & Tools</h4>", "<h4>Регионы и логистика</h4>")
                content = content.replace(
                    '<li><a href="/ru/hydraulic-oil">Anti-Wear Hydraulic Oil (HM)</a></li>',
                    '<li><a href="/ru/hydraulic-oil">Гидравлические масла (L-HM)</a></li>'
                )
                content = content.replace(
                    '<li><a href="/hydraulic-oil#hv-series">Wide-Temperature Hydraulic Oil (HV)</a></li>',
                    '<li><a href="/ru/hydraulic-oil">Морозостойкие масла (L-HV)</a></li>'
                )
                content = content.replace(
                    '<li><a href="/hydraulic-oil#ashless">Ashless Zinc-Free Hydraulic Oil</a></li>',
                    '<li><a href="/ru/hydraulic-oil">Бесцинковые гидравлические масла</a></li>'
                )
                content = content.replace(
                    '<li><a href="/hydraulic-oil#hfc">Water-Glycol Fire-Resistant (HFC)</a></li>',
                    '<li><a href="/ru/hydraulic-oil">Огнестойкие водно-гликолевые (HFC)</a></li>'
                )
                content = content.replace(
                    '<li><a href="/industrial-oils#gear-oil">Heavy-Duty Gear Oil (CKD)</a></li>',
                    '<li><a href="/ru/industrial-oils">Редукторные масла (L-CKD)</a></li>'
                )
                content = content.replace(
                    '<li><a href="/industrial-oils#compressor-oil">Rotary Screw Compressor Oil</a></li>',
                    '<li><a href="/ru/industrial-oils">Компрессорные масла (L-DAH)</a></li>'
                )
                content = content.replace(
                    '<li><a href="/ru/packaging-logistics">208L Steel Drum Specifications</a></li>',
                    '<li><a href="/ru/packaging-logistics">Спецификация бочек 208 л</a></li>'
                )
                content = content.replace(
                    '<li><a href="/packaging-logistics#calculator">20GP Container Loading Tool</a></li>',
                    '<li><a href="/ru/cis-central-asia">Поставки в РФ, Казахстан и Узбекистан</a></li>'
                )
                content = content.replace(
                    '<li><a href="#oil-advisor-section">Smart Oil Advisor</a></li>',
                    '<li><a href="/ru/packaging-logistics">Калькулятор загрузки 20ft</a></li>'
                )
                content = content.replace(
                    '<li><a href="/packaging-logistics#xiamen-port">Xiamen Port Shipping Routes</a></li>',
                    '<li><a href="/ru/cis-central-asia#gost-matrix">Таблица аналогов ГОСТ</a></li>'
                )
                content = content.replace(
                    '<li><a href="/about#oem-capabilities">Private Label OEM Blending</a></li>',
                    '<li><a href="/ru/about">Контрактное производство OEM</a></li>'
                )
                content = content.replace(
                    '<li><a href="/sitemap.xml">XML Sitemap</a></li>',
                    '<li><a href="/sitemap.xml">Карта сайта (Sitemap XML)</a></li>'
                )
                content = content.replace(
                    'LEGAL NOTICE & TRADEMARK COMPLIANCE:',
                    'ОФИЦИАЛЬНОЕ УВЕДОМЛЕНИЕ О ТОВАРНЫХ ЗНАКАХ:'
                )
                modified = True

        if modified:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"[UPDATED] {fname}")


def update_sitemap():
    """Adds the CIS hub URL to sitemap.xml with full hreflang alternates."""
    sitemap_path = os.path.join(WORKSPACE_DIR, "sitemap.xml")
    with open(sitemap_path, "r", encoding="utf-8") as f:
        xml_content = f.read()

    cis_url_block = """  <url>
    <loc>https://www.fosslubricants.com/ru/cis-central-asia</loc>
    <lastmod>2026-10-16</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
    <xhtml:link rel="alternate" hreflang="en" href="https://www.fosslubricants.com/products" />
    <xhtml:link rel="alternate" hreflang="es" href="https://www.fosslubricants.com/es/products" />
    <xhtml:link rel="alternate" hreflang="ru" href="https://www.fosslubricants.com/ru/cis-central-asia" />
    <xhtml:link rel="alternate" hreflang="ar" href="https://www.fosslubricants.com/ar/products" />
    <xhtml:link rel="alternate" hreflang="vi" href="https://www.fosslubricants.com/vi/products" />
    <xhtml:link rel="alternate" hreflang="id" href="https://www.fosslubricants.com/id/products" />
    <xhtml:link rel="alternate" hreflang="x-default" href="https://www.fosslubricants.com/ru/cis-central-asia" />
  </url>
"""

    if "https://www.fosslubricants.com/ru/cis-central-asia" not in xml_content:
        xml_content = xml_content.replace("</urlset>", cis_url_block + "</urlset>")
        with open(sitemap_path, "w", encoding="utf-8") as f:
            f.write(xml_content)
        print("[OK] Added /ru/cis-central-asia to sitemap.xml")
    else:
        print("[INFO] /ru/cis-central-asia already in sitemap.xml")


def main():
    print("--- 1. Building CIS & Central Asia Hub (/ru/cis-central-asia) ---")
    write_cis_hub()

    print("--- 2. Updating Russian Pages Meta & Navigation ---")
    update_russian_pages_nav_and_meta()

    print("--- 3. Updating sitemap.xml ---")
    update_sitemap()

    print("--- 4. Build Complete ---")


if __name__ == "__main__":
    main()
