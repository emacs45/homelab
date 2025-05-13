# 🏡 Homelab

Welcome to my Homelab!
This repository contains a minimal, secure, and extensible self-hosted setup using:

- ✅ **Pi-hole** – DNS server and ad/tracker blocker
- 🔒 **Traefik** – Reverse proxy with automatic HTTPS via Let's Encrypt (DNS-01 challenge)
- ⚙️ Fully containerized using **Docker Compose**

------------------------------------------------------------

## 📦 Services Included

Service   | Description                   | Access
----------|-------------------------------|----------------------------------------------
Pi-hole   | DNS & network-wide ad blocker | https://pihole.yourdomain.tld
Traefik   | Reverse proxy + TLS manager   | (optional: https://traefik.yourdomain.tld)

------------------------------------------------------------

## 📁 Project Structure
```
homelab/
├── traefik/
│   ├── traefik.yml              -> Traefik configuration
│   ├── docker-compose.yml       -> Traefik stack definition
│   └── acme.json                -> Certificate storage (ignored)
├── pihole/
│   ├── docker-compose.yml       -> Pi-hole with Traefik labels
│   ├── dnsmasq.d/               -> Custom DNS config files (optional)
│   └── etc-pihole/              -> Pi-hole persistent data
└── .gitignore
```
------------------------------------------------------------

## 🌐 Domain & TLS Setup

- DNS and TLS are managed via Cloudflare DNS API and Let's Encrypt (DNS-01 challenge)
- Set your public subdomains (e.g. pihole.yourdomain.tld) to point to your homelab's IP
- Add your Cloudflare token and email to traefik/.env:

  ```
  CF_API_EMAIL=you@example.com
  CLOUDFLARE_DNS_API_TOKEN=your_token
  ```

------------------------------------------------------------

## 🔐 Access & Security

- All services are accessible via HTTPS only (handled by Traefik)
- Pi-hole is protected with a web UI password via environment variable
- The Traefik dashboard is disabled by default — enable with care

------------------------------------------------------------

## 📝 Recommended Adlist for Pi-hole

Currently using [this](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/pro.txt)

Thanks to [Hagezi](https://github.com/hagezi)

------------------------------------------------------------

## 🚀 Usage
```
# Start Traefik

cd traefik && docker compose up -d

# Start Pi-hole
cd ../pihole && docker compose up -d
```

------------------------------------------------------------

## 📌 Notes

- Don't forget to create acme.json with ```chmod 600``` before starting Traefik
- Make sure both services are on the same Docker network (traefik)

------------------------------------------------------------

## 🧪 Tested On

- Ubuntu 24.04.2 LTS (Proxmox VM)
- Docker Compose v2
- Fritzbox 7xx series as router
- IPv6 disabled in LAN to avoid DNS bypassing

------------------------------------------------------------

## ✅ Todo (Optional Ideas)

- Add monitoring with Grafana/Prometheus
- Enable Traefik dashboard with auth middleware
- ~~Add redirect from / to /admin for Pi-hole~~ (done)

------------------------------------------------------------

## 📬 License

MIT – Use, modify, share. Contributions welcome!