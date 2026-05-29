# Loon Rules

A comprehensive rule set repository for Loon proxy tool, supporting both overseas users returning to China and domestic users accessing international networks.

## Features

### Rule Set Types

- **Direct Rules** (`direct.list`) - Domestic websites and services with direct connection
- **Proxy Rules** (`proxy.list`) - International websites and services via proxy
- **Blocking Rules** (`reject.list`) - Block ads, trackers, and malicious websites
- **Apple Optimization** (`apple.list`) - Apple services optimization
- **Domestic Media** (`media-cn.list`) - Domestic streaming platforms and media services

### Use Cases

| Scenario | Direct | Proxy | Notes |
|----------|--------|-------|-------|
| **Overseas** | Domestic sites/apps | Google, Netflix, etc. | Accessing domestic services primarily |
| **Returning to China** | Domestic sites/apps | Google, YouTube, etc. | Accessing international networks primarily |

---

## Quick Start

### Configuration for Returning to China

```conf
[Rule]
RULE-SET,http://jkoch14.me/loon-rules/rules/direct.list,DIRECT
RULE-SET,http://jkoch14.me/loon-rules/rules/proxy.list,PROXY
RULE-SET,http://jkoch14.me/loon-rules/rules/reject.list,REJECT
RULE-SET,http://jkoch14.me/loon-rules/rules/apple.list,DIRECT

GEOIP,CN,DIRECT
FINAL,PROXY
```

---

## Rule Files

| File | Description | URL |
|------|-------------|-----|
| direct.list | Domestic direct connection domains | http://jkoch14.me/loon-rules/rules/direct.list |
| proxy.list | International proxy domains | http://jkoch14.me/loon-rules/rules/proxy.list |
| reject.list | Ad/malicious domain blocking | http://jkoch14.me/loon-rules/rules/reject.list |
| apple.list | Apple services | http://jkoch14.me/loon-rules/rules/apple.list |
| media-cn.list | Domestic streaming media | http://jkoch14.me/loon-rules/rules/media-cn.list |

---

## Rule Format

### Supported Rule Types

```
DOMAIN-SUFFIX,example.com          # Match all subdomains
DOMAIN,example.com                 # Exact domain match
DOMAIN-KEYWORD,keyword             # Match domains containing keyword
IP-CIDR,192.168.0.0/16             # Match IP ranges
GEOIP,CN                            # Match by geographic location
```

---

## Update Rules

### Automatic Updates

Set automatic updates in Loon configuration:

```conf
[Subscription]
interval=86400  # Update every 24 hours
```

### Manual Updates

1. Open Loon
2. Navigate to "Subscriptions" → "Manage"
3. Select the rule set and click "Update Now"

---

## FAQ

### Q: Some websites cannot be accessed?

**A:** Add custom rules with higher priority in your local config:

```conf
[Rule]
DOMAIN-SUFFIX,example.com,DIRECT  # or PROXY
RULE-SET,http://jkoch14.me/loon-rules/rules/direct.list,DIRECT
```

### Q: How to switch between overseas and returning-to-China modes?

**A:** Create two separate configuration files or use Loon's tag feature to quickly switch rule sets.

### Q: Rules loading too slowly?

**A:** Import only the necessary rule sets instead of all of them. Recommended priority:
1. Direct connection rules (DIRECT)
2. Proxy rules (PROXY)
3. Blocking rules (REJECT)

---

## Contributing

- Found an issue? [Submit an Issue](https://github.com/Jovanykoch/loon-rules/issues)
- Want to contribute? [Create a Pull Request](https://github.com/Jovanykoch/loon-rules/pulls)

---

## License

MIT License - Feel free to use and modify

---

**Last Updated:** 2026-05-29  
**Maintainer:** [Jovanykoch](https://github.com/Jovanykoch)
