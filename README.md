# 🚀 surge-list

> Optimized Rule Sets for Surge

Lightweight • Fast • Continuously Updated

A personal Surge configuration and rule-set collection for daily use.

---

## Features

- Lightweight and optimized rule sets
- Designed for Surge users
- Daily-use focused routing strategy
- Continuous updates
- Easy subscription via GitHub Pages

---

## Files

| File | Description |
|------|-------------|
| `surge-cn.conf` | Main Surge configuration for China mainland environments |
| `openai.list` | AI-related services |
| `apple.list` | Apple ecosystem services |
| `icloud.list` | iCloud services |
| `edu.list` | Education and work-related services |
| `telegram.list` | Telegram traffic |
| `proxy.list` | General proxy rules |
| `cn.list` | China mainland direct rules |
| `adblock.list` | Ad blocking and rejection rules |

---

## Main Profile

### Configuration

```ini
[General]
[Replica]
[Proxy]
[Proxy Group]
[Rule]
[Host]
[URL Rewrite]
```

### Characteristics

- Public DNS and DoH endpoints
- IPv6 disabled by default
- Network Framework enabled
- Conservative routing strategy
- Suitable for China mainland users

---

## Rule Sets

```ini
RULE-SET,https://jovanykoch.github.io/surge-list/lan.list,DIRECT

RULE-SET,https://jovanykoch.github.io/surge-list/openai.list,PROXY

RULE-SET,https://jovanykoch.github.io/surge-list/apple.list,DIRECT

RULE-SET,https://jovanykoch.github.io/surge-list/icloud.list,DIRECT

RULE-SET,https://jovanykoch.github.io/surge-list/edu.list,PROXY

RULE-SET,https://jovanykoch.github.io/surge-list/adblock.list,REJECT

RULE-SET,https://jovanykoch.github.io/surge-list/cn.list,DIRECT

RULE-SET,https://jovanykoch.github.io/surge-list/telegram.list,PROXY

RULE-SET,https://jovanykoch.github.io/surge-list/proxy.list,PROXY
```

---

## Default Policy

| Traffic Type | Policy |
|-------------|---------|
| AI Services | Proxy |
| Apple Services | Direct |
| Education / Work | Proxy |
| Telegram | Proxy |
| China Mainland | Direct |
| Advertisements | Reject |
| Others | Proxy |

---

## Subscription

```text
https://jovanykoch.github.io/surge-list/
```

---

## License

Personal use only.