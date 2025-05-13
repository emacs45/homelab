# 🏡 Homelab

Welcome to my Homelab!
This repository contains a minimal, secure, and extensible self-hosted setup using:

- ✅ Pi-hole – DNS server and ad/tracker blocker
- 🔒 Traefik – Reverse proxy with automatic HTTPS via Let's Encrypt (DNS-01 challenge)
- 📊 Grafana + Prometheus – Monitoring stack
- 👤 Authentik – Self-hosted Identity Provider
- ⚙️ Fully containerized using Docker Compose

------------------------------------------------------------

## 📦 Services Included

Service     | Description                    | Access
------------|--------------------------------|----------------------------------------------
Pi-hole     | DNS & network-wide ad blocker  | https://pihole.yourdomain.tld
Traefik     | Reverse proxy + TLS manager    | (optional: https://traefik.yourdomain.tld)
Grafana     | Metrics & dashboards           | http://yourhost:3000
Prometheus  | Metrics collection             | http://yourhost:9090
Authentik   | SSO & auth provider            | http://yourhost:9000 or https://...:9443

------------------------------------------------------------

## 📁 Project Structure

```
homelab/
├── traefik/
│   ├── traefik.yml              -> Traefik configuration
│   └── docker-compose.yml       -> Traefik stack definition
│   └── acme.json                -> Certificate storage (ignored)
├── pihole/
│   ├── docker-compose.yml       -> Pi-hole with Traefik labels
│   ├── dnsmasq.d/               -> Custom DNS config files (optional)
│   └── etc-pihole/              -> Pi-hole persistent data
├── graf_prom/
│   ├── docker-compose.yml       -> Prometheus & Grafana stack
│   ├── prometheus/              -> Prometheus config
│   └── grafana/                 -> Grafana provisioning files
├── authentik/
│   ├── docker-compose.yml       -> Authentik setup incl. PostgreSQL/Redis
│   └── media/, certs/, ...      -> Persistent volumes
└── .gitignore
```
------------------------------------------------------------

## 🌐 Domain & TLS Setup

- DNS and TLS are managed via Cloudflare DNS API and Let's Encrypt (DNS-01 challenge)
- Set your public subdomains (e.g. pihole.yourdomain.tld) to point to your homelab's IP
- Add your Cloudflare token and email to traefik/.env

------------------------------------------------------------

## 🔐 Access & Security

- All services are accessible via HTTPS only (handled by Traefik)
- Pi-hole is protected with a web UI password via environment variable
- Authentik can be used to protect dashboards (Grafana, Homepage, etc.)
- The Traefik dashboard is disabled by default — enable with care

------------------------------------------------------------

## 📝 Recommended Adlist for Pi-hole

Currently using [this](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/pro.txt)

Thanks to [Hagezi](https://github.com/hagezi)

------------------------------------------------------------

## 📌 Notes

- Don't forget to create acme.json with `chmod 600` before starting Traefik
- Make sure all services are on the shared Docker network `traefik`
- API keys (Pi-hole, Proxmox, etc.) are injected via environment vars

------------------------------------------------------------

## 🧪 Tested On

- Ubuntu 24.04.2 LTS (Proxmox VM)
- Docker Compose v2
- Fritzbox 7xx series as router
- IPv6 disabled in LAN to avoid DNS bypassing

------------------------------------------------------------

## ✅ Todo (Optional Ideas)

- ~~Grafana/Prometheus Monitoring~~ (done)
- ~~Authentik Integration~~ (done)
- ~~Pi-hole redirect to /admin~~ (done)
- Add homepage dashboard (e.g. gethomepage.dev)
- Setup backup for persistent volumes
- Install OpenLDAP and integrate with Authentik
- Configure Grafana and Prometheus dashboards
- Consider migrating to k3s for orchestration in the future

------------------------------------------------------------

## 📬 License

MIT – Use, modify, share. Contributions welcome!