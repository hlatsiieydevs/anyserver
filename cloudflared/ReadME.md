# Cloudflare Argo Tunnel/Zero Trust

This enables you to host web applications without needing to setup port fowarding and any of that complicated junk. For more details, visit Cloudflare Docs (link here).

To set up this service to work, we need to do three key things: 
1. Secure a domain name 
2. Give Cloudflare the ability to manage the DNS settings
3. Establish a connection between the server and Cloudflare




## Installing Cloudflared on Ubuntu via CLI
### 1. Add Cloudflare's GPG keys
```bash
sudo mkdir -p --mode=0755 /usr/share/keyrings
curl -fsSL https://pkg.cloudflare.com/cloudflare-main.gpg | sudo tee /usr/share/keyrings/cloudflare-main.gpg >/dev/null
```

### 2. Add Cloudflare's Repository
```bash
echo "deb [signed-by=/usr/share/keyrings/cloudflare-main.gpg] https://pkg.cloudflare.com/cloudflared $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/cloudflared.list
```

### 3. Update package list
```bash
sudo apt update
```

### 4. Install Cloudflared
```bash
sudo apt install cloudflared
```

### 5. Verify Installation
```bash
sudo cloudflared --version
```
