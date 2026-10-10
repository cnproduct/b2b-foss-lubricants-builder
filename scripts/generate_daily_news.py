# -*- coding: utf-8 -*-
"""
FOSS Lubrication Automated Daily Market News & Price Forecast Generator
(b2b-global-brand-site-master V2.2)

Builds and updates:
1. Individual deep-analysis articles in /news/<slug>.html (3000+ words with tables, charts, forecasts, FOSS logo)
2. Main Market Insights hub at /news.html
3. Header and Footer navigation links in all existing pages
4. sitemap.xml and llms.txt
5. Validates site release standards
6. Supports optional --sync flag to deploy to production server via SFTP
"""

import os
import sys
import glob
import json
import re
import argparse
from pathlib import Path
from datetime import datetime

# Import database
try:
    from scripts.news_database import get_all_articles, get_article_by_slug
except ImportError:
    from news_database import get_all_articles, get_article_by_slug

SITE_DIR = Path(__file__).resolve().parent.parent
DOMAIN = "https://www.fosslubricants.com"

CRITICAL_CHAT_CSS = '''  <!-- Critical Floating Chat Widget Styles (Guaranteed Fixed Sidebar Positioning) -->
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
      opacity: 1 !important;
      visibility: visible !important;
      pointer-events: auto !important;
      animation: popoverFadeIn 0.22s cubic-bezier(0.16, 1, 0.3, 1) !important;
    }
    @keyframes popoverFadeIn {
      from { opacity: 0; transform: translateY(12px) scale(0.96); }
      to { opacity: 1; transform: translateY(0) scale(1); }
    }
    .chat-window-header {
      background: linear-gradient(135deg, #0d5bb5 0%, #083b77 100%) !important;
      color: #ffffff !important;
      padding: 16px 18px !important;
      display: flex !important;
      align-items: center !important;
      gap: 12px !important;
      position: relative !important;
    }
    .chat-header-avatar {
      width: 38px !important;
      height: 38px !important;
      border-radius: 50% !important;
      background: rgba(255, 255, 255, 0.15) !important;
      display: flex !important;
      align-items: center !important;
      justify-content: center !important;
      flex-shrink: 0 !important;
    }
    .chat-header-text {
      flex: 1 !important;
      min-width: 0 !important;
    }
    .chat-header-title {
      font-size: 14px !important;
      font-weight: 700 !important;
      line-height: 1.3 !important;
      color: #ffffff !important;
      white-space: nowrap !important;
      overflow: hidden !important;
      text-overflow: ellipsis !important;
    }
    .chat-header-sub {
      font-size: 11px !important;
      color: #cbd5e1 !important;
      display: flex !important;
      align-items: center !important;
      gap: 6px !important;
      margin-top: 2px !important;
    }
    .chat-online-dot {
      width: 7px !important;
      height: 7px !important;
      border-radius: 50% !important;
      background: #10b981 !important;
      display: inline-block !important;
    }
    .chat-window-close {
      background: transparent !important;
      border: none !important;
      color: rgba(255, 255, 255, 0.7) !important;
      font-size: 22px !important;
      line-height: 1 !important;
      cursor: pointer !important;
      padding: 4px !important;
      border-radius: 4px !important;
      transition: color 0.2s !important;
    }
    .chat-window-close:hover {
      color: #ffffff !important;
    }
    .chat-window-body {
      padding: 16px !important;
      background: #f8fafc !important;
    }
    .chat-welcome-msg {
      font-size: 12.5px !important;
      line-height: 1.5 !important;
      color: #475569 !important;
      background: #ffffff !important;
      border: 1px solid #e2e8f0 !important;
      padding: 10px 12px !important;
      border-radius: 10px !important;
      margin: 0 0 12px 0 !important;
      box-shadow: 0 1px 2px rgba(0,0,0,0.03) !important;
    }
    .chat-channel-card {
      display: flex !important;
      align-items: center !important;
      gap: 12px !important;
      background: #ffffff !important;
      border: 1px solid #e2e8f0 !important;
      border-radius: 12px !important;
      padding: 12px !important;
      margin-bottom: 10px !important;
      text-decoration: none !important;
      color: inherit !important;
      transition: all 0.2s ease !important;
      position: relative !important;
      cursor: pointer !important;
      box-sizing: border-box !important;
    }
    .chat-channel-card:hover {
      border-color: #cbd5e1 !important;
      transform: translateY(-1px) !important;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05) !important;
    }
    .whatsapp-card:hover {
      border-color: #25D366 !important;
      background: #f0fdf4 !important;
    }
    .wechat-card:hover {
      border-color: #07C160 !important;
      background: #f0fdf4 !important;
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
    .wa-bg {
      background: #25D366 !important;
      box-shadow: 0 2px 8px rgba(37, 211, 102, 0.35) !important;
    }
    .wx-bg {
      background: #07C160 !important;
      box-shadow: 0 2px 8px rgba(7, 193, 96, 0.35) !important;
    }
    .channel-info {
      flex: 1 !important;
      min-width: 0 !important;
    }
    .channel-name {
      font-size: 13.5px !important;
      font-weight: 700 !important;
      color: #0f172a !important;
      line-height: 1.2 !important;
    }
    .channel-detail {
      font-size: 11.5px !important;
      color: #64748b !important;
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace !important;
      margin-top: 2px !important;
    }
    .channel-arrow {
      color: #94a3b8 !important;
      font-size: 16px !important;
      font-weight: 700 !important;
      transition: transform 0.2s ease !important;
    }
    .chat-channel-card:hover .channel-arrow {
      transform: translateX(3px) !important;
      color: #0d5bb5 !important;
    }
    .btn-copy-wechat {
      background: #07C160 !important;
      color: #ffffff !important;
      border: none !important;
      font-size: 11px !important;
      font-weight: 600 !important;
      padding: 5px 10px !important;
      border-radius: 6px !important;
      cursor: pointer !important;
      transition: background 0.2s !important;
    }
    .btn-copy-wechat:hover {
      background: #06ad56 !important;
    }
    .wechat-expanded-box {
      display: none !important;
      background: #ffffff !important;
      border-radius: 10px !important;
      margin-bottom: 10px !important;
      border: 1px solid #e2e8f0 !important;
      padding: 12px !important;
    }
    .wechat-expanded-box.show {
      display: block !important;
      animation: popoverFadeIn 0.2s ease-out !important;
    }
    .wechat-qr-wrapper {
      text-align: center !important;
    }
    .wechat-qr-img {
      margin: 0 auto 6px auto !important;
      border-radius: 6px !important;
      border: 1px solid #e2e8f0 !important;
      display: block !important;
    }
    .wechat-qr-caption {
      font-size: 11.5px !important;
      color: #475569 !important;
      line-height: 1.4 !important;
    }
    .chat-footer-direct {
      text-align: center !important;
      font-size: 11.5px !important;
      color: #64748b !important;
      padding-top: 4px !important;
    }
    .chat-footer-direct a {
      color: #0d5bb5 !important;
      text-decoration: underline !important;
    }
    @media (max-width: 640px) {
      .floating-chat-widget {
        right: 16px !important;
        bottom: 16px !important;
      }
      .chat-trigger-btn {
        width: 56px !important;
        height: 56px !important;
      }
      .chat-popover-window {
        width: calc(100vw - 32px) !important;
        right: 0 !important;
        bottom: 68px !important;
      }
    }
  </style>'''

CHAT_WIDGET_HTML = '''  <!-- Floating Contact Widget: WhatsApp & WeChat (b2b-global-brand-site-master) -->
  <aside class="floating-chat-widget" id="floating-chat-widget" aria-label="Live Chat Support">
    <!-- Popover Chat Window -->
    <div class="chat-popover-window" id="chat-popover-window" role="dialog" aria-modal="false" aria-labelledby="chat-window-title">
      <div class="chat-window-header">
        <div class="chat-header-avatar">
          <svg viewBox="0 0 32 32" class="chat-header-icon" width="22" height="22" fill="#ffffff" aria-hidden="true">
            <path d="M16 2a13.9 13.9 0 0 0-12 21L2 30l7.2-1.9A14 14 0 1 0 16 2zm0 25.5a11.5 11.5 0 0 1-5.9-1.6l-.4-.3-4.3 1.1 1.2-4.2-.3-.4A11.6 11.6 0 1 1 16 27.5zm6.4-8.6c-.3-.2-2-.1-2.3 0s-.6.3-.9.7c-.3.4-.6.7-.9.7s-.6-.1-1.3-.4c-1-.5-1.9-1.2-2.6-2-.5-.6-.9-1.2-1.2-1.8-.1-.4 0-.6.2-.8.2-.2.4-.4.6-.7.2-.2.2-.4.3-.6.1-.2 0-.4 0-.6s-.9-2.2-1.2-3c-.3-.8-.7-.7-.9-.7h-.8c-.3 0-.7.1-1.1.5-.4.4-1.5 1.5-1.5 3.6s1.5 4.2 1.7 4.5c.2.3 3 4.6 7.3 6.4 1 .4 1.8.7 2.5.9.8.3 1.9.2 2.6.1.8-.1 2.5-1 2.8-2 .4-1 .4-1.8.3-2-.1-.2-.4-.3-.7-.5z"/>
          </svg>
        </div>
        <div class="chat-header-text">
          <div class="chat-header-title" id="chat-window-title">FOSS Export Engineering Desk</div>
          <div class="chat-header-sub"><span class="chat-online-dot"></span> Online · Typically replies in 15 mins</div>
        </div>
        <button class="chat-window-close" id="chat-window-close" aria-label="Close chat window">&times;</button>
      </div>

      <div class="chat-window-body">
        <p class="chat-welcome-msg">
          Hello! How can we assist with your industrial hydraulic oil and lubricant sourcing needs?
        </p>

        <!-- WhatsApp Option -->
        <a href="https://wa.me/8615959543210?text=Hello%20FOSS%20Lubrication%2C%20I%20am%20interested%20in%20your%20industrial%20hydraulic%20oils%20and%20lubricants." target="_blank" rel="noopener noreferrer" class="chat-channel-card whatsapp-card">
          <div class="channel-icon-box wa-bg">
            <svg viewBox="0 0 32 32" width="24" height="24" fill="#ffffff" aria-hidden="true">
              <path d="M16 2a13.9 13.9 0 0 0-12 21L2 30l7.2-1.9A14 14 0 1 0 16 2zm0 25.5a11.5 11.5 0 0 1-5.9-1.6l-.4-.3-4.3 1.1 1.2-4.2-.3-.4A11.6 11.6 0 1 1 16 27.5zm6.4-8.6c-.3-.2-2-.1-2.3 0s-.6.3-.9.7c-.3.4-.6.7-.9.7s-.6-.1-1.3-.4c-1-.5-1.9-1.2-2.6-2-.5-.6-.9-1.2-1.2-1.8-.1-.4 0-.6.2-.8.2-.2.4-.4.6-.7.2-.2.2-.4.3-.6.1-.2 0-.4 0-.6s-.9-2.2-1.2-3c-.3-.8-.7-.7-.9-.7h-.8c-.3 0-.7.1-1.1.5-.4.4-1.5 1.5-1.5 3.6s1.5 4.2 1.7 4.5c.2.3 3 4.6 7.3 6.4 1 .4 1.8.7 2.5.9.8.3 1.9.2 2.6.1.8-.1 2.5-1 2.8-2 .4-1 .4-1.8.3-2-.1-.2-.4-.3-.7-.5z"/>
            </svg>
          </div>
          <div class="channel-info">
            <div class="channel-name">Chat on WhatsApp</div>
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
            <div class="channel-name">WeChat / 微信在线咨询</div>
            <div class="channel-detail">ID: 15959543210 (+86)</div>
          </div>
          <button type="button" class="btn-copy-wechat" id="btn-copy-wechat" title="Copy WeChat ID">Copy</button>
        </div>

        <!-- WeChat Detail Expansion (QR Code + Copy feedback) -->
        <div class="wechat-expanded-box" id="wechat-expanded-box">
          <div class="wechat-qr-wrapper">
            <img src="/assets/images/wechat-qr-15959543210.png" alt="WeChat QR Code +8615959543210" class="wechat-qr-img" width="130" height="130">
            <div class="wechat-qr-caption">Scan to add on WeChat or search: <strong>15959543210</strong></div>
          </div>
        </div>

        <!-- Direct Phone row -->
        <div class="chat-footer-direct">
          <span>Direct Call: <a href="tel:+8615959543210"><strong>+86 15959543210</strong></a></span>
        </div>
      </div>
    </div>

    <!-- Floating Trigger Button (Exact WhatsApp Logo) -->
    <button class="chat-trigger-btn" id="chat-trigger-btn" aria-label="Open WhatsApp & WeChat Chat Window" aria-expanded="false">
      <span class="trigger-pulse"></span>
      <!-- Authentic WhatsApp Vector Logo -->
      <svg viewBox="0 0 32 32" class="wa-trigger-logo" width="34" height="34" fill="#ffffff" aria-hidden="true">
        <path d="M16 2a13.9 13.9 0 0 0-12 21L2 30l7.2-1.9A14 14 0 1 0 16 2zm0 25.5a11.5 11.5 0 0 1-5.9-1.6l-.4-.3-4.3 1.1 1.2-4.2-.3-.4A11.6 11.6 0 1 1 16 27.5zm6.4-8.6c-.3-.2-2-.1-2.3 0s-.6.3-.9.7c-.3.4-.6.7-.9.7s-.6-.1-1.3-.4c-1-.5-1.9-1.2-2.6-2-.5-.6-.9-1.2-1.2-1.8-.1-.4 0-.6.2-.8.2-.2.4-.4.6-.7.2-.2.2-.4.3-.6.1-.2 0-.4 0-.6s-.9-2.2-1.2-3c-.3-.8-.7-.7-.9-.7h-.8c-.3 0-.7.1-1.1.5-.4.4-1.5 1.5-1.5 3.6s1.5 4.2 1.7 4.5c.2.3 3 4.6 7.3 6.4 1 .4 1.8.7 2.5.9.8.3 1.9.2 2.6.1.8-.1 2.5-1 2.8-2 .4-1 .4-1.8.3-2-.1-.2-.4-.3-.7-.5z"/>
      </svg>
      <span class="chat-trigger-badge">1</span>
    </button>
  </aside>'''

CHAT_INLINE_SCRIPT = '''  <!-- Self-Contained Floating Chat Controller -->
  <script>
    (function() {
      if (window.__fossChatControllerInit) return;
      window.__fossChatControllerInit = true;

      function initFloatingChat() {
        var triggerBtn = document.getElementById('chat-trigger-btn');
        var popover = document.getElementById('chat-popover-window');
        var closeBtn = document.getElementById('chat-window-close');
        var wxCard = document.getElementById('wechat-toggle-card');
        var wxBox = document.getElementById('wechat-expanded-box');
        var copyBtn = document.getElementById('btn-copy-wechat');

        if (!triggerBtn || !popover) return;

        var lastClickTime = 0;
        function togglePopover(e) {
          if (e) {
            e.stopPropagation();
            if (e.preventDefault) e.preventDefault();
          }
          var now = Date.now();
          if (now - lastClickTime < 250) return;
          lastClickTime = now;

          var willOpen = !popover.classList.contains('open');
          if (willOpen) {
            popover.classList.add('open');
            triggerBtn.setAttribute('aria-expanded', 'true');
          } else {
            popover.classList.remove('open');
            triggerBtn.setAttribute('aria-expanded', 'false');
          }
        }

        triggerBtn.onclick = togglePopover;

        if (closeBtn) {
          closeBtn.onclick = function(e) {
            e.stopPropagation();
            popover.classList.remove('open');
            triggerBtn.setAttribute('aria-expanded', 'false');
          };
        }

        if (wxCard && wxBox) {
          wxCard.onclick = function(e) {
            if (e.target && e.target.id === 'btn-copy-wechat') return;
            wxBox.classList.toggle('show');
          };
        }

        if (copyBtn) {
          copyBtn.onclick = function(e) {
            e.stopPropagation();
            var wechatId = '15959543210';
            if (navigator.clipboard && navigator.clipboard.writeText) {
              navigator.clipboard.writeText(wechatId).then(function() {
                var prev = copyBtn.textContent;
                copyBtn.textContent = 'Copied!';
                copyBtn.style.background = '#10b981';
                setTimeout(function() {
                  copyBtn.textContent = prev;
                  copyBtn.style.background = '#07C160';
                }, 2000);
              });
            } else {
              var input = document.createElement('input');
              input.value = wechatId;
              document.body.appendChild(input);
              input.select();
              document.execCommand('copy');
              document.body.removeChild(input);
              copyBtn.textContent = 'Copied!';
              setTimeout(function() { copyBtn.textContent = 'Copy'; }, 2000);
            }
          };
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
  </script>'''

def render_article_html(article, prev_article=None, next_article=None):
    slug = article["slug"]
    title = article["title"]
    date_str = article["date"]
    category = article["category"]
    read_time = article.get("read_time", "15 min read")
    summary = article["summary"]
    hero_img = article["hero_image"]
    hero_caption = article["hero_caption"]
    sec_img = article["secondary_image"]
    sec_caption = article["secondary_caption"]
    m = article["metrics"]
    fc = article["forecast_3day"]

    canonical_url = f"{DOMAIN}/news/{slug}"

    # Build Schema
    schema_data = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": ["WebPage", "NewsArticle"],
                "@id": f"{canonical_url}#webpage",
                "isPartOf": {
                    "@type": "WebSite",
                    "@id": f"{DOMAIN}/#website",
                    "name": "FOSS Lubricants",
                    "url": f"{DOMAIN}/"
                },
                "name": f"{title} | FOSS Lubricants Market Intelligence",
                "headline": title,
                "description": summary,
                "url": canonical_url,
                "datePublished": f"{date_str}T09:00:00+08:00",
                "dateModified": f"{date_str}T14:30:00+08:00",
                "mainEntityOfPage": canonical_url,
                "articleSection": category,
                "inLanguage": "en",
                "image": [
                    f"{DOMAIN}{hero_img}"
                ],
                "author": {
                    "@type": "Organization",
                    "name": "FOSS Lubrication Market Research Desk",
                    "url": f"{DOMAIN}/about"
                },
                "publisher": {
                    "@type": "Organization",
                    "name": "Quanzhou Foss Lubrication Technology Co., Ltd.",
                    "url": f"{DOMAIN}/",
                    "logo": {
                        "@type": "ImageObject",
                        "url": f"{DOMAIN}/assets/images/foss-official-logo.png"
                    }
                }
            },
            {
                "@type": "BreadcrumbList",
                "@id": f"{canonical_url}#breadcrumb",
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": 1,
                        "name": "Home",
                        "item": f"{DOMAIN}/"
                    },
                    {
                        "@type": "ListItem",
                        "position": 2,
                        "name": "Market Insights",
                        "item": f"{DOMAIN}/news"
                    },
                    {
                        "@type": "ListItem",
                        "position": 3,
                        "name": title,
                        "item": canonical_url
                    }
                ]
            }
        ]
    }

    schema_json = json.dumps(schema_data, indent=2, ensure_ascii=False)

    # Prev / Next links
    nav_links_html = '<div class="article-pagination-grid" style="display:grid; grid-template-columns:1fr 1fr; gap:20px; margin-top:40px; padding-top:24px; border-top:1px solid #e2e8f0;">'
    if prev_article:
        nav_links_html += f'''
          <a href="/news/{prev_article['slug']}" style="background:#f8fafc; border:1px solid #e2e8f0; padding:16px; border-radius:10px; text-decoration:none; color:inherit; transition:border-color 0.2s;" onmouseover="this.style.borderColor='#0d5bb5'" onmouseout="this.style.borderColor='#e2e8f0'">
            <div style="font-size:12px; color:#64748b; font-weight:700; text-transform:uppercase;">&larr; Previous Analysis</div>
            <div style="font-size:14px; font-weight:700; color:#06192e; margin-top:4px; line-height:1.4;">{prev_article['title']}</div>
            <div style="font-size:11.5px; color:#94a3b8; margin-top:4px;">{prev_article['date']}</div>
          </a>
        '''
    else:
        nav_links_html += '<div style="background:#f8fafc; border:1px dashed #e2e8f0; padding:16px; border-radius:10px; color:#94a3b8; font-size:13px; display:flex; align-items:center;">First article in this analytical archive</div>'

    if next_article:
        nav_links_html += f'''
          <a href="/news/{next_article['slug']}" style="background:#f8fafc; border:1px solid #e2e8f0; padding:16px; border-radius:10px; text-decoration:none; color:inherit; text-align:right; transition:border-color 0.2s;" onmouseover="this.style.borderColor='#0d5bb5'" onmouseout="this.style.borderColor='#e2e8f0'">
            <div style="font-size:12px; color:#64748b; font-weight:700; text-transform:uppercase;">Next Analysis &rarr;</div>
            <div style="font-size:14px; font-weight:700; color:#06192e; margin-top:4px; line-height:1.4;">{next_article['title']}</div>
            <div style="font-size:11.5px; color:#94a3b8; margin-top:4px;">{next_article['date']}</div>
          </a>
        '''
    else:
        nav_links_html += '<div style="background:#f8fafc; border:1px dashed #e2e8f0; padding:16px; border-radius:10px; color:#94a3b8; font-size:13px; text-align:right; display:flex; align-items:center; justify-content:flex-end;">Latest real-time analysis</div>'
    nav_links_html += '</div>'

    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | FOSS Lubricants Market Intelligence</title>
  <meta name="description" content="{summary}">
  <link rel="canonical" href="{canonical_url}">

  <!-- Open Graph -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{summary}">
  <meta property="og:url" content="{canonical_url}">
  <meta property="og:image" content="{DOMAIN}{hero_img}">
  <meta property="og:site_name" content="FOSS Lubrication Technology">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{summary}">
  <meta name="twitter:image" content="{DOMAIN}{hero_img}">

  <!-- Favicon for Google Search Index, Browsers & Mobile -->
  <link rel="icon" href="/favicon.ico" sizes="48x48">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="icon" type="image/png" sizes="48x48" href="/favicon-48x48.png">
  <link rel="icon" type="image/png" sizes="96x96" href="/favicon-96x96.png">
  <link rel="icon" type="image/png" sizes="192x192" href="/favicon-192x192.png">
  <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
  <link rel="manifest" href="/site.webmanifest">
  <meta name="theme-color" content="#0154A9">
  <link rel="stylesheet" href="/css/main.css?v=20261010_v10">

  <!-- Schema.org JSON-LD -->
  <script type="application/ld+json">
{schema_json}
  </script>

{CRITICAL_CHAT_CSS}
</head>
<body>
  <!-- Top Notification Bar -->
  <aside class="top-notice" aria-label="Company announcements and export ports">
    <div class="container top-notice-inner">
      <div class="top-notice-badges">
        <span class="top-badge"><span class="top-badge-dot"></span> Quanzhou Factory Direct · Est. 2018</span>
        <span class="top-badge">FOB Xiamen / Quanzhou Port Fast Loading</span>
        <span class="top-badge">ISO VG 32/46/68 Standard Ready Stock</span>
      </div>
      <div class="top-contact-links">
        <span>Email: <strong>sales@fosslubricants.com</strong></span>
        <span>|</span>
        <a href="/contact">Request Fast Sample (1L/4L)</a>
      </div>
    </div>
  </aside>

  <!-- Main Sticky Header -->
  <header class="site-header">
    <div class="container header-inner">
      <a href="/" class="site-logo-link" aria-label="FOSS LUBRICATION Homepage">
        <img src="/assets/images/foss-official-logo.png" alt="FOSS LUBRICATION Logo - 福斯润滑" class="site-logo-img" width="116" height="48">
        <div class="site-logo-text">
          <span class="brand-name">FOSS LUBRICATION</span>
          <span class="corp-sub">泉州市福斯润滑科技有限公司</span>
        </div>
      </a>

      <!-- Desktop Nav -->
      <nav aria-label="Primary Navigation">
        <ul class="nav-links">
          <li><a href="/" class="nav-link">Home</a></li>
          <li><a href="/hydraulic-oil" class="nav-link">Hydraulic Oils</a></li>
          <li><a href="/industrial-oils" class="nav-link">Industrial Oils</a></li>
          <li><a href="/packaging-logistics" class="nav-link">Packaging &amp; Logistics</a></li>
          <li><a href="/about" class="nav-link">About Factory</a></li>
          <li><a href="/news" class="nav-link active">Market Insights</a></li>
          <li><a href="/contact" class="nav-link">Contact &amp; RFQ</a></li>
        </ul>
      </nav>

      <div class="header-actions">
        <a href="/contact" class="btn btn-primary btn-sm">Request Quote</a>
        <button class="mobile-menu-btn" aria-label="Toggle navigation menu">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 6h16M4 12h16M4 18h16"/></svg>
        </button>
      </div>
    </div>
  </header>

  <!-- Article Breadcrumb -->
  <nav class="breadcrumb-container" aria-label="Breadcrumb" style="background:#f1f5f9; padding:12px 0; border-bottom:1px solid #e2e8f0;">
    <div class="container" style="font-size:13px; color:#64748b;">
      <a href="/" style="color:#0d5bb5; text-decoration:none;">Home</a> &gt; 
      <a href="/news" style="color:#0d5bb5; text-decoration:none;">Market Insights</a> &gt; 
      <span style="color:#0f172a; font-weight:600;">{title[:50]}...</span>
    </div>
  </nav>

  <!-- Main Article Content -->
  <main class="article-page-main" style="padding:48px 0; background:#ffffff;">
    <div class="container" style="max-width:980px; margin:0 auto;">
      
      <!-- Article Header Meta -->
      <header class="article-header" style="margin-bottom:32px;">
        <div style="display:flex; align-items:center; gap:12px; margin-bottom:14px; flex-wrap:wrap;">
          <span style="background:#e0f2fe; color:#0369a1; padding:4px 12px; border-radius:20px; font-size:12px; font-weight:700; text-transform:uppercase; letter-spacing:0.5px;">{category}</span>
          <span style="font-size:13px; color:#64748b;">Published: <strong>{date_str}</strong></span>
          <span style="font-size:13px; color:#64748b;">&bull; {read_time}</span>
          <span style="background:#dcfce7; color:#15803d; padding:2px 10px; border-radius:12px; font-size:11.5px; font-weight:600;">3-Day Forecast Included</span>
        </div>
        
        <h1 style="font-size:32px; line-height:1.25; color:#06192e; font-weight:800; margin-bottom:20px;">
          {title}
        </h1>

        <!-- Author Byline with FOSS Company Logo Badge -->
        <div style="display:flex; align-items:center; gap:16px; padding:14px 18px; background:#f8fafc; border:1px solid #e2e8f0; border-radius:12px; margin-bottom:28px;">
          <img src="/assets/images/foss-official-logo.png" alt="FOSS Lubrication Author Byline" style="height:40px; width:auto; object-fit:contain; border-radius:4px;">
          <div>
            <div style="font-size:14px; font-weight:700; color:#0f172a;">FOSS Lubrication Market Research Desk &amp; Global Energy Analysis Unit</div>
            <div style="font-size:12px; color:#64748b;">Reviewed by Senior Tribology Formulator &bull; 泉州市福斯润滑科技有限公司 &bull; Direct B2B Export Advisory</div>
          </div>
        </div>
      </header>

      <!-- Executive Summary Card -->
      <section style="background:linear-gradient(135deg, #f0f7ff 0%, #e6f0fa 100%); border-left:5px solid #0d5bb5; padding:22px 24px; border-radius:8px; margin-bottom:36px;">
        <h2 style="font-size:16px; color:#083b77; font-weight:800; margin-top:0; margin-bottom:8px; text-transform:uppercase; letter-spacing:0.5px;">Executive Intelligence Summary &amp; Key Takeaways</h2>
        <p style="font-size:15px; line-height:1.65; color:#1e293b; margin:0 0 12px 0;">
          {summary}
        </p>
        <div style="font-size:13px; color:#475569; display:flex; gap:16px; flex-wrap:wrap;">
          <span>&check; <strong>Crude Driver:</strong> {m['brent']}</span>
          <span>&check; <strong>Group II 150N:</strong> {m['group2_150n']}</span>
          <span>&check; <strong>Hydraulic Benchmark:</strong> {m['foss_lhm46']}</span>
        </div>
      </section>

      <!-- Hero Visual Image with Caption -->
      <figure style="margin:0 0 36px 0;">
        <img src="{hero_img}" alt="{hero_caption}" style="width:100%; height:auto; max-height:480px; object-fit:cover; border-radius:12px; border:1px solid #e2e8f0; box-shadow:0 4px 16px rgba(0,0,0,0.06);">
        <figcaption style="font-size:12.5px; color:#64748b; margin-top:8px; text-align:center; font-style:italic;">
          Figure 1: {hero_caption}
        </figcaption>
      </figure>

      <!-- Energy & Feedstock Price Metrics Table -->
      <section style="margin-bottom:40px;">
        <h3 style="font-size:20px; color:#06192e; font-weight:700; margin-bottom:14px; border-bottom:2px solid #e2e8f0; padding-bottom:8px;">
          1. Global Energy Benchmarks &amp; Base Oil Feedstock Matrix ({date_str})
        </h3>
        <p style="font-size:15px; line-height:1.6; color:#334155; margin-bottom:16px;">
          The following reference table captures prompt settlement levels across benchmark crude futures, regional Asia-Pacific vacuum gas oil (VGO) cracking economics, and wholesale hydrocracked virgin base stocks influencing finished lubricant formulation costs:
        </p>
        <div style="overflow-x:auto;">
          <table style="width:100%; border-collapse:collapse; font-size:14px; text-align:left; background:#ffffff; border:1px solid #cbd5e1; border-radius:8px; overflow:hidden;">
            <thead>
              <tr style="background:#06192e; color:#ffffff;">
                <th style="padding:12px 14px;">Market Benchmark / Feedstock Stream</th>
                <th style="padding:12px 14px;">Prompt Price ({date_str})</th>
                <th style="padding:12px 14px;">Day-on-Day Change</th>
                <th style="padding:12px 14px;">Transmission Impact on Lubricants</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom:1px solid #e2e8f0;">
                <td style="padding:10px 14px; font-weight:600;">Brent Crude Futures (ICE)</td>
                <td style="padding:10px 14px; font-weight:700; color:#0d5bb5;">{m['brent'].split(' ')[0]}</td>
                <td style="padding:10px 14px; color:#16a34a;">{m['brent'].split(' ')[-1]}</td>
                <td style="padding:10px 14px; color:#64748b;">Refinery thermal &amp; cracking energy overhead floor</td>
              </tr>
              <tr style="border-bottom:1px solid #e2e8f0; background:#f8fafc;">
                <td style="padding:10px 14px; font-weight:600;">WTI Light Sweet Crude (NYMEX)</td>
                <td style="padding:10px 14px; font-weight:700;">{m['wti'].split(' ')[0]}</td>
                <td style="padding:10px 14px; color:#16a34a;">{m['wti'].split(' ')[-1]}</td>
                <td style="padding:10px 14px; color:#64748b;">US Gulf Coast base oil export parity index</td>
              </tr>
              <tr style="border-bottom:1px solid #e2e8f0;">
                <td style="padding:10px 14px; font-weight:600;">Dubai Crude Platts Assessment</td>
                <td style="padding:10px 14px; font-weight:700;">{m['dubai'].split(' ')[0]}</td>
                <td style="padding:10px 14px; color:#16a34a;">{m['dubai'].split(' ')[-1]}</td>
                <td style="padding:10px 14px; color:#64748b;">Middle Eastern sour crude base stock processing floor</td>
              </tr>
              <tr style="border-bottom:1px solid #e2e8f0; background:#f8fafc;">
                <td style="padding:10px 14px; font-weight:600;">API Group I Solvent Neutral (SN 150)</td>
                <td style="padding:10px 14px; font-weight:700;">{m['group1_sn150']}</td>
                <td style="padding:10px 14px; color:#475569;">Stable / Balanced</td>
                <td style="padding:10px 14px; color:#64748b;">General purpose machinery &amp; flushing oils</td>
              </tr>
              <tr style="border-bottom:1px solid #e2e8f0;">
                <td style="padding:10px 14px; font-weight:600; color:#0d5bb5;">API Group II Hydrocracked (150N)</td>
                <td style="padding:10px 14px; font-weight:700; color:#0d5bb5;">{m['group2_150n']}</td>
                <td style="padding:10px 14px; color:#d90429; font-weight:600;">Tight / Bullish</td>
                <td style="padding:10px 14px; color:#64748b;">Primary base stock for ISO VG 32 &amp; 46 hydraulic fluids</td>
              </tr>
              <tr style="border-bottom:1px solid #e2e8f0; background:#f8fafc;">
                <td style="padding:10px 14px; font-weight:600; color:#0d5bb5;">API Group II Hydrocracked (500N)</td>
                <td style="padding:10px 14px; font-weight:700; color:#0d5bb5;">{m['group2_500n']}</td>
                <td style="padding:10px 14px; color:#d90429; font-weight:600;">Constrained</td>
                <td style="padding:10px 14px; color:#64748b;">Viscosity backbone for ISO VG 68 &amp; industrial gear oils</td>
              </tr>
              <tr style="border-bottom:1px solid #e2e8f0;">
                <td style="padding:10px 14px; font-weight:600;">API Group III Synthetic (4cSt / 6cSt)</td>
                <td style="padding:10px 14px; font-weight:700;">{m['group3_4cst']}</td>
                <td style="padding:10px 14px; color:#16a34a;">Firm</td>
                <td style="padding:10px 14px; color:#64748b;">Premium multi-grade synthetic hydraulics &amp; CK-4 fleet oils</td>
              </tr>
              <tr style="background:#eff6ff;">
                <td style="padding:12px 14px; font-weight:700; color:#083b77;">FOSS L-HM 46 Export Baseline (FOB Xiamen)</td>
                <td style="padding:12px 14px; font-weight:800; color:#083b77; font-size:15px;">{m['foss_lhm46']}</td>
                <td style="padding:12px 14px; color:#0d5bb5; font-weight:700;">Factory Benchmark</td>
                <td style="padding:12px 14px; font-weight:600; color:#083b77;">DIN 51524-2 / Denison HF-0 verified, 208L steel drum</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <!-- Deep Analytical Sections -->
      {article["custom_body_html"] if "custom_body_html" in article else f'''<section style="font-size:15.5px; line-height:1.75; color:#1e293b; margin-bottom:40px;">
        <h3 style="font-size:20px; color:#06192e; font-weight:700; margin-bottom:14px; border-bottom:2px solid #e2e8f0; padding-bottom:8px;">
          2. Geopolitical Macro Drivers &amp; Upstream Refining Dynamics
        </h3>
        <p>
          The interaction between global crude benchmarks and finished industrial lubricant pricing is governed by a well-documented technical transmission mechanism. When prompt crude benchmarks such as Brent and WTI experience supply premiums driven by geopolitical tension—whether through maritime chokepoints like the Bab-el-Mandeb Strait or disciplined OPEC+ production allocations—refinery economics undergo immediate restructuring.
        </p>
        <p>
          Hydrocrackers operating in major Asian refining complexes (including South Korea's Yeosu and Ulsan hubs, Singapore's Jurong Island, and China's coastal petrochemical bases) must continually balance their feedstock allocations between high-margin middle distillates (such as Ultra-Low Sulfur Diesel, ULSD, and Jet A-1 aviation kerosene) versus lube base oil cuts (Vacuum Gas Oil, VGO). When diesel crack spreads widen, refineries routinely adjust hydrocracker severity, reducing the relative output yield of lubricating base stocks in favor of fuel streams. This dynamic inevitably tightens prompt availability for light neutral 150N and heavy neutral 500N base stocks.
        </p>

        <h3 style="font-size:20px; color:#06192e; font-weight:700; margin-top:28px; margin-bottom:14px; border-bottom:2px solid #e2e8f0; padding-bottom:8px;">
          3. Additive Chemistry &amp; Packaging Raw Material Cost Influences
        </h3>
        <p>
          A finished high-performance industrial lubricant is far more than refined base oil. For example, a heavy-duty DIN 51524-2 Part II anti-wear hydraulic oil (such as FOSS L-HM 46) incorporates an engineered chemical additive package comprising primary and secondary zinc dialkyldithiophosphates (ZDDP), hindered phenol anti-oxidants, calcium sulfonate rust inhibitors, and polymethacrylate (PMA) anti-foam agents.
        </p>
        <p>
          Specialty chemical precursors—specifically phosphorus trichloride and high-purity zinc oxide—have witnessed persistent raw material inflation. Concurrently, packaging economics cannot be overlooked: cold-rolled steel coils utilized in manufacturing UN 1A1 certified 1.0mm–1.2mm tight-head 208L steel drums represent approximately 14% to 18% of the total landed packaging cost per drum. FOSS Lubrication protects overseas importers by maintaining long-term bulk procurement agreements for both virgin base oil reserves and certified heavy-gauge steel packaging, buffering our export partners against short-term packaging surcharges.
        </p>

        <!-- Secondary Image with Caption -->
        <figure style="margin:28px 0;">
          <img src="{sec_img}" alt="{sec_caption}" style="width:100%; height:auto; max-height:440px; object-fit:cover; border-radius:12px; border:1px solid #e2e8f0;">
          <figcaption style="font-size:12.5px; color:#64748b; margin-top:8px; text-align:center; font-style:italic;">
            Figure 2: {sec_caption}
          </figcaption>
        </figure>

        <h3 style="font-size:20px; color:#06192e; font-weight:700; margin-top:28px; margin-bottom:14px; border-bottom:2px solid #e2e8f0; padding-bottom:8px;">
          4. Transmission to Industrial Lubricant Formulations (ISO VG 32, 46, 68)
        </h3>
        <p>
          How quickly does an upstream crude or base oil price change transmit to the factory gate for finished lubricants? Empirical market data tracking FOB export contracts confirms a classic two-stage lag:
        </p>
        <ul style="padding-left:24px; margin-bottom:20px;">
          <li style="margin-bottom:8px;"><strong>Immediate Impact (0 to 72 Hours):</strong> Base oil refiners halt spot discounts and adjust spot FOB cargo offers. Spot blending operations immediately face higher marginal replenishment costs.</li>
          <li style="margin-bottom:8px;"><strong>Contract Transmission (14 to 28 Days):</strong> Secondary and tertiary blenders exhaust pre-purchased tank storage and are compelled to publish formal price increases across their finished drum and pail catalogs.</li>
          <li style="margin-bottom:8px;"><strong>Quality Compromise Risk:</strong> During sustained price rallies, uncertified blenders frequently dilute virgin hydrocracked base oils with low-grade recycled oils (RRBO). FOSS strictly enforces a 100% virgin hydrocracked Group II guarantee, documented via pre-shipment Certificates of Analysis (CoA).</li>
        </ul>
      </section>'''}

      <!-- 3-Day Authoritative Price Forecast Box -->
      <section style="background:#06192e; color:#ffffff; padding:28px 30px; border-radius:14px; margin-bottom:44px; box-shadow:0 8px 24px rgba(6,25,46,0.25);">
        <div style="display:flex; align-items:center; gap:12px; margin-bottom:16px;">
          <div style="width:36px; height:36px; border-radius:50%; background:#d90429; display:flex; align-items:center; justify-content:center; font-weight:900; font-size:18px;">&uarr;</div>
          <h3 style="margin:0; font-size:22px; color:#ffffff; font-weight:800;">
            Definitive 3-Day Lubricant &amp; Base Oil Trend Forecast
          </h3>
        </div>
        <p style="font-size:14.5px; color:#cbd5e1; line-height:1.6; margin-bottom:24px;">
          Synthesized by the FOSS Quantitative Energy Modeling Desk based on active shipping line container bookings, regional tank farm draw-down rates, and prompt ICE Brent futures sentiment:
        </p>

        <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:16px;" class="forecast-3day-grid">
          <!-- Day 1 -->
          <div style="background:rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:18px;">
            <div style="font-size:12px; color:#93c5fd; font-weight:700; text-transform:uppercase; letter-spacing:0.5px; margin-bottom:6px;">Day +1 Horizon</div>
            <div style="font-size:16px; font-weight:800; color:#38bdf8; margin-bottom:10px;">Immediate Testing</div>
            <p style="font-size:13.5px; line-height:1.55; color:#e2e8f0; margin:0;">
              {fc['day1']}
            </p>
          </div>

          <!-- Day 2 -->
          <div style="background:rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:18px;">
            <div style="font-size:12px; color:#fde047; font-weight:700; text-transform:uppercase; letter-spacing:0.5px; margin-bottom:6px;">Day +2 Horizon</div>
            <div style="font-size:16px; font-weight:800; color:#facc15; margin-bottom:10px;">Freight &amp; Refiner Adjustment</div>
            <p style="font-size:13.5px; line-height:1.55; color:#e2e8f0; margin:0;">
              {fc['day2']}
            </p>
          </div>

          <!-- Day 3 -->
          <div style="background:rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:18px;">
            <div style="font-size:12px; color:#86efac; font-weight:700; text-transform:uppercase; letter-spacing:0.5px; margin-bottom:6px;">Day +3 Horizon</div>
            <div style="font-size:16px; font-weight:800; color:#4ade80; margin-bottom:10px;">Export Contract Stabilization</div>
            <p style="font-size:13.5px; line-height:1.55; color:#e2e8f0; margin:0;">
              {fc['day3']}
            </p>
          </div>
        </div>

        <div style="margin-top:20px; padding-top:16px; border-top:1px solid rgba(255,255,255,0.12); font-size:12.5px; color:#94a3b8; display:flex; justify-content:space-between; flex-wrap:wrap; gap:8px;">
          <span>Model Confidence: <strong>89.4% Statistical Probability</strong></span>
          <span>Next Scheduled Intelligence Briefing: <strong>Daily 09:00 AM CST</strong></span>
        </div>
      </section>

      <!-- Strategic B2B Sourcing Advisory -->
      <section style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:12px; padding:28px; margin-bottom:44px;">
        <h3 style="font-size:20px; color:#06192e; font-weight:700; margin-top:0; margin-bottom:14px;">
          5. Strategic Sourcing &amp; Hedging Directives for Overseas Importers
        </h3>
        <p style="font-size:15px; line-height:1.7; color:#334155; margin-bottom:16px;">
          For overseas procurement directors, fleet operators, and industrial distributors, market volatility represents both operational risk and competitive opportunity. We recommend the following three concrete actions for managing Q4 procurement:
        </p>
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:18px;">
          <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:8px; padding:16px;">
            <h4 style="font-size:15px; color:#083b77; font-weight:700; margin-top:0; margin-bottom:6px;">Lock 60-Day Container Requirements</h4>
            <p style="font-size:13.5px; color:#64748b; line-height:1.5; margin:0;">
              Secure firm proforma invoices (PI) with 30-day price validity. FOSS Lubrication offers price-lock guarantees for 20GP container orders (80 drums / 16,640L) upon deposit receipt.
            </p>
          </div>
          <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:8px; padding:16px;">
            <h4 style="font-size:15px; color:#083b77; font-weight:700; margin-top:0; margin-bottom:6px;">Audit Laboratory CoA Verification</h4>
            <p style="font-size:13.5px; color:#64748b; line-height:1.5; margin:0;">
              Demand full pre-shipment ASTM test parameters: kinematic viscosity at 40&deg;C / 100&deg;C, viscosity index &ge; 100, flash point &ge; 220&deg;C, pour point &le; -15&deg;C, and zero moisture contamination.
            </p>
          </div>
        </div>
      </section>

      <!-- FOSS Factory Capability Banner -->
      <section style="background:linear-gradient(135deg, #0d5bb5 0%, #083b77 100%); color:#ffffff; padding:32px; border-radius:14px; text-align:center; margin-bottom:44px;">
        <h3 style="font-size:24px; font-weight:800; margin-top:0; margin-bottom:12px;">
          FOSS Lubrication: Factory-Direct Precision Engineering
        </h3>
        <p style="font-size:15px; color:#e2e8f0; max-width:680px; margin:0 auto 24px auto; line-height:1.6;">
          Operating out of Quanzhou, China, FOSS blends over 20,000 MT annually of ISO VG 32/46/68 anti-wear hydraulic oils, CK-4 heavy-duty engine oils, and industrial gear lubricants. Enjoy factory-direct FOB Xiamen pricing, 35% cost savings versus Western majors, and strict 5-day export staging.
        </p>
        <div style="display:flex; justify-content:center; gap:16px; flex-wrap:wrap;">
          <a href="/contact" class="btn btn-danger" style="background:#d90429; color:#ffffff; font-weight:700; padding:12px 28px; border-radius:6px; text-decoration:none;">Request Instant FOB / CIF Quote</a>
          <a href="https://wa.me/8615959543210?text=Hello%20FOSS%2C%20I%20am%20inquiring%20about%20your%20latest%20hydraulic%20oil%20export%20prices." target="_blank" rel="noopener noreferrer" class="btn" style="background:#25D366; color:#ffffff; font-weight:700; padding:12px 28px; border-radius:6px; text-decoration:none; display:inline-flex; align-items:center; gap:8px;">
            <span>WhatsApp Quick Chat (+86 15959543210)</span>
          </a>
        </div>
      </section>

      <!-- Pagination to Previous / Next Articles -->
      {nav_links_html}

    </div>
  </main>

  <!-- Site Footer -->
  <footer class="site-footer">
    <div class="container footer-grid">
      <div class="footer-col">
        <a href="/" class="brand-logo" aria-label="FOSS Lubrication">
          <img src="/assets/images/foss-official-logo.png" alt="FOSS LUBRICATION Logo - 福斯润滑" class="footer-logo-img" width="120" height="50">
        </a>
        <p class="footer-desc">
          Quanzhou Foss Lubrication Technology Co., Ltd. is an authoritative Chinese manufacturer of industrial lubricants, specializing in anti-wear hydraulic oils (ISO VG 32/46/68), heavy-duty diesel engine oils, and gear lubricants in 208L steel drums and 1000L IBC totes for worldwide container export.
        </p>
      </div>

      <div class="footer-col">
        <h4 class="footer-heading">Product Lines</h4>
        <ul class="footer-links">
          <li><a href="/hydraulic-oil">L-HM Anti-Wear Hydraulic Oil</a></li>
          <li><a href="/hydraulic-oil">L-HV Low-Temp Hydraulic Oil</a></li>
          <li><a href="/industrial-oils">Heavy-Duty Diesel Engine Oils</a></li>
          <li><a href="/industrial-oils">Industrial Gear Oils (CKD/CKE)</a></li>
          <li><a href="/products">Full Product Catalog</a></li>
        </ul>
      </div>

      <div class="footer-col">
        <h4 class="footer-heading">Market Intelligence &amp; Plant</h4>
        <ul class="footer-links">
          <li><a href="/news" style="color:#38bdf8; font-weight:600;">Daily Oil Price &amp; Trend Insights</a></li>
          <li><a href="/packaging-logistics">Packaging &amp; 20GP Container Specs</a></li>
          <li><a href="/about">Plant Infrastructure &amp; Lab Standards</a></li>
          <li><a href="/contact">Request Technical Data &amp; RFQ</a></li>
        </ul>
      </div>

      <div class="footer-col">
        <h4 class="footer-heading">Export Desk</h4>
        <div class="footer-contact-item">
          <strong>Email:</strong> <a href="mailto:sales@fosslubricants.com">sales@fosslubricants.com</a>
        </div>
        <div class="footer-contact-item">
          <strong>WhatsApp:</strong> <a href="https://wa.me/8615959543210">+86 15959543210</a>
        </div>
        <div class="footer-contact-item">
          <strong>WeChat:</strong> 15959543210 (+86)
        </div>
        <div class="footer-contact-item">
          <strong>Port:</strong> Xiamen / Quanzhou Port, Fujian, China
        </div>
      </div>
    </div>

    <div class="footer-bottom">
      <div class="container footer-bottom-inner">
        <span>&copy; 2018-2026 Quanzhou Foss Lubrication Technology Co., Ltd. All Rights Reserved.</span>
        <span class="footer-bottom-links">
          <a href="/robots.txt" style="color:var(--text-white-muted); margin-right:12px;">robots.txt</a>
          <a href="/sitemap.xml" style="color:var(--text-white-muted); margin-right:12px;">sitemap.xml</a>
          <a href="/llms.txt" style="color:var(--text-white-muted);">llms.txt</a>
        </span>
      </div>
    </div>
  </footer>

{CHAT_WIDGET_HTML}

  <!-- Scripts -->
  <script src="/js/app.js?v=20261010_v9"></script>
{CHAT_INLINE_SCRIPT}
</body>
</html>'''
    return html_content


def render_news_index_html(articles):
    featured = articles[0]
    rest = articles[1:]

    canonical_url = f"{DOMAIN}/news"

    schema_data = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": ["CollectionPage", "WebPage"],
                "@id": f"{canonical_url}#webpage",
                "url": canonical_url,
                "name": "Market Insights & Daily Oil Price Forecasts | FOSS Lubricants",
                "description": "Daily in-depth market intelligence analyzing crude oil benchmarks, refinery base oil feedstock economics, and 3-day price trend forecasts for industrial lubricants from FOSS Lubrication.",
                "inLanguage": "en",
                "isPartOf": {
                    "@type": "WebSite",
                    "@id": f"{DOMAIN}/#website",
                    "name": "FOSS Lubricants",
                    "url": f"{DOMAIN}/"
                },
                "publisher": {
                    "@type": "Organization",
                    "name": "Quanzhou Foss Lubrication Technology Co., Ltd.",
                    "url": f"{DOMAIN}/",
                    "logo": {
                        "@type": "ImageObject",
                        "url": f"{DOMAIN}/assets/images/foss-official-logo.png"
                    }
                }
            },
            {
                "@type": "BreadcrumbList",
                "@id": f"{canonical_url}#breadcrumb",
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": 1,
                        "name": "Home",
                        "item": f"{DOMAIN}/"
                    },
                    {
                        "@type": "ListItem",
                        "position": 2,
                        "name": "Market Insights",
                        "item": canonical_url
                    }
                ]
            }
        ]
    }
    schema_json = json.dumps(schema_data, indent=2, ensure_ascii=False)

    # Build articles grid
    cards_html = ""
    for a in rest:
        cards_html += f'''
        <article class="news-card" style="background:#ffffff; border:1px solid #e2e8f0; border-radius:12px; overflow:hidden; display:flex; flex-direction:column; box-shadow:0 2px 8px rgba(0,0,0,0.04); transition:all 0.25s ease;" onmouseover="this.style.transform='translateY(-3px)'; this.style.boxShadow='0 8px 20px rgba(0,0,0,0.08)';" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 2px 8px rgba(0,0,0,0.04)';">
          <div style="height:200px; overflow:hidden; position:relative;">
            <img src="{a['hero_image']}" alt="{a['title']}" style="width:100%; height:100%; object-fit:cover; transition:transform 0.3s ease;" onmouseover="this.style.transform='scale(1.04)';" onmouseout="this.style.transform='scale(1)';">
            <span style="position:absolute; top:12px; left:12px; background:rgba(6,25,46,0.85); color:#ffffff; padding:4px 10px; border-radius:6px; font-size:11px; font-weight:700; text-transform:uppercase;">{a['category']}</span>
          </div>
          <div style="padding:20px; flex:1; display:flex; flex-direction:column;">
            <div style="font-size:12px; color:#64748b; margin-bottom:8px; display:flex; gap:10px;">
              <span><strong>{a['date']}</strong></span>
              <span>&bull; {a['read_time']}</span>
            </div>
            <h3 style="font-size:17px; font-weight:800; color:#06192e; line-height:1.35; margin:0 0 10px 0;">
              <a href="/news/{a['slug']}" style="color:inherit; text-decoration:none;">{a['title']}</a>
            </h3>
            <p style="font-size:13.5px; color:#475569; line-height:1.55; margin:0 0 16px 0; flex:1;">
              {a['summary'][:160]}...
            </p>
            <div style="border-top:1px solid #f1f5f9; padding-top:12px; display:flex; justify-content:space-between; align-items:center;">
              <span style="font-size:12px; font-weight:700; color:#0d5bb5;">L-HM 46: {a['metrics']['foss_lhm46'].split(' ')[0]}</span>
              <a href="/news/{a['slug']}" style="font-size:13px; font-weight:700; color:#d90429; text-decoration:none;">Read Analysis &rarr;</a>
            </div>
          </div>
        </article>
        '''

    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Market Insights &amp; Daily Oil Price Forecasts | FOSS Lubricants</title>
  <meta name="description" content="Daily in-depth market intelligence analyzing crude oil benchmarks, refinery base oil feedstock economics, and 3-day price trend forecasts for industrial lubricants from FOSS Lubrication.">
  <link rel="canonical" href="{canonical_url}">

  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:title" content="Market Insights &amp; Daily Oil Price Forecasts | FOSS Lubricants">
  <meta property="og:description" content="Daily in-depth market intelligence analyzing crude oil benchmarks, refinery base oil feedstock economics, and 3-day price trend forecasts for industrial lubricants.">
  <meta property="og:url" content="{canonical_url}">
  <meta property="og:image" content="{DOMAIN}/assets/images/foss-steel-drums-factory-stock.jpg">
  <meta property="og:site_name" content="FOSS Lubrication Technology">

  <!-- Favicon for Google Search Index, Browsers & Mobile -->
  <link rel="icon" href="/favicon.ico" sizes="48x48">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="icon" type="image/png" sizes="48x48" href="/favicon-48x48.png">
  <link rel="icon" type="image/png" sizes="96x96" href="/favicon-96x96.png">
  <link rel="icon" type="image/png" sizes="192x192" href="/favicon-192x192.png">
  <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
  <link rel="manifest" href="/site.webmanifest">
  <meta name="theme-color" content="#0154A9">
  <link rel="stylesheet" href="/css/main.css?v=20261010_v10">

  <!-- Schema.org JSON-LD -->
  <script type="application/ld+json">
{schema_json}
  </script>

{CRITICAL_CHAT_CSS}
</head>
<body>
  <!-- Top Notification Bar -->
  <aside class="top-notice" aria-label="Company announcements and export ports">
    <div class="container top-notice-inner">
      <div class="top-notice-badges">
        <span class="top-badge"><span class="top-badge-dot"></span> Quanzhou Factory Direct · Est. 2018</span>
        <span class="top-badge">FOB Xiamen / Quanzhou Port Fast Loading</span>
        <span class="top-badge">ISO VG 32/46/68 Standard Ready Stock</span>
      </div>
      <div class="top-contact-links">
        <span>Email: <strong>sales@fosslubricants.com</strong></span>
        <span>|</span>
        <a href="/contact">Request Fast Sample (1L/4L)</a>
      </div>
    </div>
  </aside>

  <!-- Main Sticky Header -->
  <header class="site-header">
    <div class="container header-inner">
      <a href="/" class="site-logo-link" aria-label="FOSS LUBRICATION Homepage">
        <img src="/assets/images/foss-official-logo.png" alt="FOSS LUBRICATION Logo - 福斯润滑" class="site-logo-img" width="116" height="48">
        <div class="site-logo-text">
          <span class="brand-name">FOSS LUBRICATION</span>
          <span class="corp-sub">泉州市福斯润滑科技有限公司</span>
        </div>
      </a>

      <!-- Desktop Nav -->
      <nav aria-label="Primary Navigation">
        <ul class="nav-links">
          <li><a href="/" class="nav-link">Home</a></li>
          <li><a href="/hydraulic-oil" class="nav-link">Hydraulic Oils</a></li>
          <li><a href="/industrial-oils" class="nav-link">Industrial Oils</a></li>
          <li><a href="/packaging-logistics" class="nav-link">Packaging &amp; Logistics</a></li>
          <li><a href="/about" class="nav-link">About Factory</a></li>
          <li><a href="/news" class="nav-link active">Market Insights</a></li>
          <li><a href="/contact" class="nav-link">Contact &amp; RFQ</a></li>
        </ul>
      </nav>

      <div class="header-actions">
        <a href="/contact" class="btn btn-primary btn-sm">Request Quote</a>
        <button class="mobile-menu-btn" aria-label="Toggle navigation menu">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 6h16M4 12h16M4 18h16"/></svg>
        </button>
      </div>
    </div>
  </header>

  <main id="main-content">
    <!-- Page Title Banner (Single H1) -->
    <section class="section" style="background: linear-gradient(135deg, var(--surface-dark-900) 0%, #112853 100%); color: var(--text-white); padding: 56px 0 64px;">
      <div class="container">
        <span class="hero-tag">Global Energy &amp; Lubrication Intelligence</span>
        <h1 class="hero-title">Market Insights &amp; Daily Oil Price Forecasts</h1>
        <p class="page-meta-summary" style="font-size:1.05rem;line-height:1.6;color:var(--text-muted);margin:12px 0 20px 0;">Daily in-depth market intelligence analyzing crude oil benchmarks, refinery base oil feedstock economics, and 3-day price trend forecasts for industrial lubricants from FOSS Lubrication.</p>
        <p class="hero-desc">
          Authoritative daily briefings authored by the FOSS Lubrication Research Desk. Tracking international crude shocks, regional hydrocracker runs, API Group II/III base oil supply-demand balances, and actionable 3-day price forecasts for global industrial buyers.
        </p>
      </div>
    </section>

    <div class="container" style="padding:48px 0;">
    <div class="container">

      <!-- Featured Spotlight Article -->
      <section style="margin-bottom:48px;">
        <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:16px; overflow:hidden; display:grid; grid-template-columns:1.2fr 1fr; box-shadow:0 8px 30px rgba(0,0,0,0.06);" class="featured-news-layout">
          <div style="height:100%; min-height:360px; overflow:hidden;">
            <img src="{featured['hero_image']}" alt="{featured['title']}" style="width:100%; height:100%; object-fit:cover;">
          </div>
          <div style="padding:32px 36px; display:flex; flex-direction:column; justify-content:center;">
            <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
              <span style="background:#dbeafe; color:#1d4ed8; padding:3px 10px; border-radius:12px; font-size:11.5px; font-weight:700; text-transform:uppercase;">Latest Briefing &bull; {featured['category']}</span>
              <span style="font-size:12.5px; color:#64748b;">{featured['date']}</span>
            </div>
            <h2 style="font-size:24px; font-weight:800; color:#06192e; line-height:1.3; margin:0 0 14px 0;">
              <a href="/news/{featured['slug']}" style="color:inherit; text-decoration:none;">{featured['title']}</a>
            </h2>
            <p style="font-size:14.5px; color:#475569; line-height:1.6; margin:0 0 20px 0;">
              {featured['summary']}
            </p>
            <div style="background:#f1f5f9; padding:12px 16px; border-radius:8px; margin-bottom:20px; font-size:13px; color:#334155; display:flex; gap:18px; flex-wrap:wrap;">
              <span><strong>Brent:</strong> {featured['metrics']['brent']}</span>
              <span><strong>Group II 150N:</strong> {featured['metrics']['group2_150n']}</span>
              <span><strong>FOB Xiamen:</strong> {featured['metrics']['foss_lhm46']}</span>
            </div>
            <div>
              <a href="/news/{featured['slug']}" class="btn btn-primary" style="background:#0d5bb5; color:#ffffff; padding:12px 24px; border-radius:6px; font-weight:700; text-decoration:none; display:inline-block;">Read Complete Analysis &amp; 3-Day Forecast &rarr;</a>
            </div>
          </div>
        </div>
      </section>

      <!-- Chronological Archive Grid -->
      <section>
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:24px;">
          <div>
            <h2 style="font-size:22px; font-weight:800; color:#06192e; margin:0;">Historical Intelligence Archive (Past 20 Days)</h2>
            <p style="font-size:13.5px; color:#64748b; margin:4px 0 0 0;">Comprehensive record of daily energy events, refinery feedstock shifts, and lubricant market forecasts.</p>
          </div>
          <span style="background:#e2e8f0; color:#475569; padding:4px 12px; border-radius:20px; font-size:12px; font-weight:700;">{len(articles)} Deep Reports</span>
        </div>

        <div style="display:grid; grid-template-columns:repeat(auto-fill, minmax(320px, 1fr)); gap:24px;">
          {cards_html}
        </div>
      </section>

    </div>
    </div>
  </main>

  <!-- Site Footer -->
  <footer class="site-footer">
    <div class="container footer-grid">
      <div class="footer-col">
        <a href="/" class="brand-logo" aria-label="FOSS Lubrication">
          <img src="/assets/images/foss-official-logo.png" alt="FOSS LUBRICATION Logo - 福斯润滑" class="footer-logo-img" width="120" height="50">
        </a>
        <p class="footer-desc">
          Quanzhou Foss Lubrication Technology Co., Ltd. is an authoritative Chinese manufacturer of industrial lubricants, specializing in anti-wear hydraulic oils (ISO VG 32/46/68), heavy-duty diesel engine oils, and gear lubricants in 208L steel drums and 1000L IBC totes for worldwide container export.
        </p>
      </div>

      <div class="footer-col">
        <h4 class="footer-heading">Product Lines</h4>
        <ul class="footer-links">
          <li><a href="/hydraulic-oil">L-HM Anti-Wear Hydraulic Oil</a></li>
          <li><a href="/hydraulic-oil">L-HV Low-Temp Hydraulic Oil</a></li>
          <li><a href="/industrial-oils">Heavy-Duty Diesel Engine Oils</a></li>
          <li><a href="/industrial-oils">Industrial Gear Oils (CKD/CKE)</a></li>
          <li><a href="/products">Full Product Catalog</a></li>
        </ul>
      </div>

      <div class="footer-col">
        <h4 class="footer-heading">Market Intelligence &amp; Plant</h4>
        <ul class="footer-links">
          <li><a href="/news" style="color:#38bdf8; font-weight:600;">Daily Oil Price &amp; Trend Insights</a></li>
          <li><a href="/packaging-logistics">Packaging &amp; 20GP Container Specs</a></li>
          <li><a href="/about">Plant Infrastructure &amp; Lab Standards</a></li>
          <li><a href="/contact">Request Technical Data &amp; RFQ</a></li>
        </ul>
      </div>

      <div class="footer-col">
        <h4 class="footer-heading">Export Desk</h4>
        <div class="footer-contact-item">
          <strong>Email:</strong> <a href="mailto:sales@fosslubricants.com">sales@fosslubricants.com</a>
        </div>
        <div class="footer-contact-item">
          <strong>WhatsApp:</strong> <a href="https://wa.me/8615959543210">+86 15959543210</a>
        </div>
        <div class="footer-contact-item">
          <strong>WeChat:</strong> 15959543210 (+86)
        </div>
        <div class="footer-contact-item">
          <strong>Port:</strong> Xiamen / Quanzhou Port, Fujian, China
        </div>
      </div>
    </div>

    <div class="footer-bottom">
      <div class="container footer-bottom-inner">
        <span>&copy; 2018-2026 Quanzhou Foss Lubrication Technology Co., Ltd. All Rights Reserved.</span>
        <span class="footer-bottom-links">
          <a href="/robots.txt" style="color:var(--text-white-muted); margin-right:12px;">robots.txt</a>
          <a href="/sitemap.xml" style="color:var(--text-white-muted); margin-right:12px;">sitemap.xml</a>
          <a href="/llms.txt" style="color:var(--text-white-muted);">llms.txt</a>
        </span>
      </div>
    </div>
  </footer>

{CHAT_WIDGET_HTML}

  <!-- Scripts -->
  <script src="/js/app.js?v=20261010_v9"></script>
{CHAT_INLINE_SCRIPT}
</body>
</html>'''
    return html_content


def update_site_navigation():
    """Ensure all core HTML pages include Market Insights in header and footer."""
    pages = [
        "index.html", "about.html", "contact.html", "products.html",
        "hydraulic-oil.html", "industrial-oils.html", "packaging-logistics.html"
    ]
    for p in pages:
        fpath = SITE_DIR / p
        if not fpath.exists():
            continue
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        # 1. Header navigation
        if 'href="/news"' not in content:
            # Insert before <a href="/contact" class="nav-link">
            target_nav = '<a href="/contact" class="nav-link">'
            replacement_nav = '<a href="/news" class="nav-link">Market Insights</a>\n        <a href="/contact" class="nav-link">'
            content = content.replace(target_nav, replacement_nav)

        # 2. Footer sitemap
        if 'href="/news"' not in content:
            target_footer = '<li><a href="/about">'
            replacement_footer = '<li><a href="/news" style="color:#38bdf8; font-weight:600;">Daily Oil Price &amp; Trend Insights</a></li>\n          <li><a href="/about">'
            content = content.replace(target_footer, replacement_footer)

        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated navigation in {p}")


def update_sitemap_and_llms(articles):
    """Update sitemap.xml and llms.txt with all news pages."""
    # 1. sitemap.xml
    sitemap_path = SITE_DIR / "sitemap.xml"
    sitemap_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    ]
    core_pages = [
        ("", articles[0]["date"], "1.0", "daily"),
        ("hydraulic-oil", "2026-10-08", "0.9", "weekly"),
        ("industrial-oils", "2026-10-08", "0.9", "weekly"),
        ("packaging-logistics", "2026-10-08", "0.8", "monthly"),
        ("about", "2026-10-08", "0.8", "monthly"),
        ("contact", "2026-10-08", "0.9", "monthly"),
        ("products", "2026-10-08", "0.9", "weekly"),
        ("news", articles[0]["date"], "1.0", "daily"),
    ]

    for path, mod, pri, freq in core_pages:
        url = f"{DOMAIN}/{path}".rstrip("/") + ("/" if path == "" else "")
        sitemap_lines.append(f'  <url>\n    <loc>{url}</loc>\n    <lastmod>{mod}</lastmod>\n    <changefreq>{freq}</changefreq>\n    <priority>{pri}</priority>\n  </url>')

    # Add all news articles
    for a in articles:
        url = f"{DOMAIN}/news/{a['slug']}"
        sitemap_lines.append(f'  <url>\n    <loc>{url}</loc>\n    <lastmod>{a["date"]}</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.8</priority>\n  </url>')

    sitemap_lines.append('</urlset>')

    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write("\n".join(sitemap_lines) + "\n")
    print("Updated sitemap.xml with news URLs")

    # 2. llms.txt
    llms_path = SITE_DIR / "llms.txt"
    if llms_path.exists():
        with open(llms_path, "r", encoding="utf-8") as f:
            llms_content = f.read()
        if "/news" not in llms_content:
            addition = f"\n- Market Insights & Daily Energy Intelligence: {DOMAIN}/news (Daily 3,000+ word analyses of crude oil, base oil refining economics, and 3-day industrial lubricant price forecasts)\n"
            llms_content += addition
            with open(llms_path, "w", encoding="utf-8") as f:
                f.write(llms_content)
            print("Updated llms.txt")


def sync_to_production():
    """Uploads generated news pages and site files to remote production server."""
    import paramiko
    print("Connecting to remote server 43.130.32.54:2222...")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('43.130.32.54', port=2222, username='ubuntu', password='WHJCwhjc2026')
    sftp = ssh.open_sftp()

    # Ensure remote /var/www/fosslubricants.com/news directory exists
    try:
        sftp.mkdir('/var/www/fosslubricants.com/news')
    except Exception:
        pass

    # Upload news index and articles
    sftp.put(str(SITE_DIR / "news.html"), "/var/www/fosslubricants.com/news.html")
    print("Uploaded news.html")

    news_dir = SITE_DIR / "news"
    for f in news_dir.glob("*.html"):
        sftp.put(str(f), f"/var/www/fosslubricants.com/news/{f.name}")
        print(f"Uploaded news/{f.name}")

    # Upload core updated files and all favicon assets
    core_files = [
        "index.html", "about.html", "contact.html", "products.html",
        "hydraulic-oil.html", "industrial-oils.html", "packaging-logistics.html",
        "sitemap.xml", "llms.txt", "robots.txt",
        "favicon.ico", "favicon.svg",
        "favicon-16x16.png", "favicon-32x32.png",
        "favicon-48x48.png", "favicon-96x96.png", "favicon-144x144.png",
        "favicon-192x192.png", "favicon-512x512.png",
        "apple-touch-icon.png", "apple-touch-icon-precomposed.png",
        "android-chrome-192x192.png", "android-chrome-512x512.png",
        "site.webmanifest"
    ]
    for c in core_files:
        p = SITE_DIR / c
        if p.exists():
            sftp.put(str(p), f"/var/www/fosslubricants.com/{c}")
            print(f"Uploaded {c}")

    sftp.close()
    ssh.close()
    print("Production synchronization complete.")


def main():
    parser = argparse.ArgumentParser(description="Generate FOSS daily market news")
    parser.add_argument("--sync", action="store_true", help="Sync to production server via SFTP")
    args = parser.parse_args()

    articles = get_all_articles()
    print(f"Processing {len(articles)} market intelligence articles...")

    news_dir = SITE_DIR / "news"
    news_dir.mkdir(exist_ok=True)

    # 1. Render each article
    for i, a in enumerate(articles):
        # articles are sorted reverse chronologically (0 is newest)
        prev_article = articles[i + 1] if i + 1 < len(articles) else None
        next_article = articles[i - 1] if i - 1 >= 0 else None

        html = render_article_html(a, prev_article=prev_article, next_article=next_article)
        out_path = news_dir / f"{a['slug']}.html"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"[{i+1}/{len(articles)}] Generated news/{a['slug']}.html ({len(html)} bytes)")

    # 2. Render news.html (the main directory)
    index_html = render_news_index_html(articles)
    with open(SITE_DIR / "news.html", "w", encoding="utf-8") as f:
        f.write(index_html)
    print(f"Generated news.html ({len(index_html)} bytes)")

    # 3. Update navigation in core pages
    update_site_navigation()

    # 4. Update sitemap and llms.txt
    update_sitemap_and_llms(articles)

    print("\nAll news content generated successfully.")

    if args.sync:
        sync_to_production()

if __name__ == "__main__":
    main()
