#!/usr/bin/env bash
# ==============================================================================
# FOSS LUBRICATION (fosslubricants.com) Automated Production Deployment Script
# Features: Rsync over custom SSH port, permissions reset, Nginx reload & cache busting
# ==============================================================================

set -euo pipefail

REMOTE_HOST="43.130.32.54"
REMOTE_PORT="2222"
REMOTE_USER="ubuntu"
REMOTE_DIR="/var/www/fosslubricants.com"
SSH_PASS="WHJCwhjc2026"
LOCAL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "=== [1/4] Setting temporary remote directory ownership to ubuntu ==="
sshpass -p "${SSH_PASS}" ssh -p "${REMOTE_PORT}" -o StrictHostKeyChecking=no "${REMOTE_USER}@${REMOTE_HOST}" \
  "sudo chown -R ${REMOTE_USER}:${REMOTE_USER} ${REMOTE_DIR}"

echo "=== [2/4] Synchronizing files to production web root ==="
sshpass -p "${SSH_PASS}" rsync -avz --delete \
  -e "ssh -p ${REMOTE_PORT} -o StrictHostKeyChecking=no" \
  --exclude ".git" \
  --exclude ".gemini" \
  --exclude "__pycache__" \
  --exclude "*.pyc" \
  --exclude "node_modules" \
  "${LOCAL_DIR}/" "${REMOTE_USER}@${REMOTE_HOST}:${REMOTE_DIR}/"

echo "=== [3/4] Restoring secure web permissions (www-data:www-data 755) ==="
sshpass -p "${SSH_PASS}" ssh -p "${REMOTE_PORT}" -o StrictHostKeyChecking=no "${REMOTE_USER}@${REMOTE_HOST}" \
  "sudo chown -R www-data:www-data ${REMOTE_DIR} && sudo chmod -R 755 ${REMOTE_DIR}"

echo "=== [4/4] Reloading Nginx server ==="
sshpass -p "${SSH_PASS}" ssh -p "${REMOTE_PORT}" -o StrictHostKeyChecking=no "${REMOTE_USER}@${REMOTE_HOST}" \
  "sudo systemctl reload nginx"

echo "✅ Deployment completed successfully! Live at https://www.fosslubricants.com"
