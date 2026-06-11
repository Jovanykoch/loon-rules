# Surge List

A personal Surge configuration and rule-set collection for daily use.

This repository provides a ready-to-edit Surge profile and several remote rule sets for routing traffic by category, including AI services, Apple services, Telegram, China mainland traffic, proxy traffic, work-related domains, and rejection rules.

## Files

| File | Description |
| --- | --- |
| `surge-cn.conf` | Main Surge configuration for China mainland network environments. |
| `openai.list` | Rule set for AI-related services. |
| `apple.list` | Rule set for Apple-related services. |
| `edu.list` | Rule set for work-related domains or services. |
| `telegram.list` | Rule set for Telegram traffic. |
| `proxy.list` | General proxy rule set. |
| `cn.list` | China mainland direct-connection rule set. |
| `reject` | Rejection / blocking rule set. |

## Main Profile

The main profile is:

```ini
surge-cn.conf
```

It includes the following major sections:

```ini
[General]
[Replica]
[Proxy]
[Proxy Group]
[Rule]
[Host]
[URL Rewrite]
```

The profile uses public DNS servers and DoH endpoints, disables IPv6 by default, enables `network-framework`, and provides a conservative routing strategy for China mainland usage.

## Rule Sets

The main profile references these remote rule sets:

```ini
RULE-SET,https://jovanykoch.github.io/surge-list/openai.list,PROXY
RULE-SET,https://jovanykoch.github.io/surge-list/apple.list,DIRECT
RULE-SET,https://jovanykoch.github.io/surge-list/icloud.list,DIRECT
RULE-SET,https://jovanykoch.github.io/surge-list/edu.list,PROXY
RULE-SET,https://jovanykoch.github.io/surge-list/adblock.list,REJECT
RULE-SET,https://jovanykoch.github.io/surge-list/cn.list,DIRECT
RULE-SET,https://jovanykoch.github.io/surge-list/telegram.list,PROXY
RULE-SET,https://jovanykoch.github.io/surge-list/proxy.list,PROXY

```

Default behavior:

| Traffic | Policy |
| --- | --- |
| AI services | `Proxy` |
| Apple services | `DIRECT` |
| Work-related services | `Proxy` |
| Telegram | `Proxy` |
| China mainland traffic | `DIRECT` |
| Rejected traffic | `REJECT` |
| GeoIP CN | `DIRECT` |
| Final fallback | `DIRECT` |

## Usage

### Use rule sets in your own profile

You can also use only the rule sets and bind them to your own policy groups:

```ini
[Rule]
RULE-SET,https://jkoch14.me/surge-list/openai.list,AI
RULE-SET,https://jkoch14.me/surge-list/apple.list,DIRECT
RULE-SET,https://jkoch14.me/surge-list/edu.list,Work
RULE-SET,https://jkoch14.me/surge-list/telegram.list,Telegram
RULE-SET,https://jkoch14.me/surge-list/proxy.list,Proxy
RULE-SET,https://jkoch14.me/surge-list/cn.list,DIRECT
RULE-SET,https://jkoch14.me/surge-list/reject,REJECT
GEOIP,CN,DIRECT
FINAL,DIRECT
```

Example policy groups:

```ini
[Proxy Group]
Proxy = select, HK, JP, SG, US, DIRECT
AI = select, US, SG, JP, Proxy
Telegram = select, SG, JP, HK, Proxy
Work = select, Proxy, DIRECT
```

## Notes

- The built-in `Proxy` group in `surge-cn.conf` is intentionally minimal. Add your own proxy nodes, subscriptions, or external policy groups before using it as a complete profile.
- The default fallback rule is `FINAL,DIRECT`. Change it to `FINAL,Proxy` if you want unknown traffic to use the proxy by default.
- Rules are optimized for practical personal usage and may change over time.
- Review all rules before using them in a production or shared environment.

## Disclaimer

This repository is provided for personal learning and configuration reference only. Use it at your own discretion and comply with all applicable laws, regulations, service terms, and network policies in your region.
