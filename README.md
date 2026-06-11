# 🚀 surge-list

Oᴘᴛɪᴍɪᴢᴇᴅ ʀᴜʟᴇ sᴇᴛs ғᴏʀ **Sᴜʀɢᴇ**.

Lɪɢʜᴛᴡᴇɪɢʜᴛ • Fᴀsᴛ • Cᴏɴᴛɪɴᴜᴏᴜsʟʏ Uᴘᴅᴀᴛᴇᴅ

[![Stars](https://img.shields.io/github/stars/Jovanykoch/Loon?style=flat-square)](https://github.com/Jovanykoch/Loon/stargazers)
[![License](https://img.shields.io/github/license/Jovanykoch/Loon?style=flat-square)](LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/Jovanykoch/Loon?style=flat-square)](https://github.com/Jovanykoch/Loon/commits/main)

</div>

A ᴘᴇʀsᴏɴᴀʟ Sᴜʀɢᴇ ᴄᴏɴғɪɢᴜʀᴀᴛɪᴏɴ ᴀɴᴅ ʀᴜʟᴇ-sᴇᴛ ᴄᴏʟʟᴇᴄᴛɪᴏɴ ғᴏʀ ᴅᴀɪʟʏ ᴜsᴇ.

<div align="center">

---

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
| `adblock.list` | Rejection / blocking rule set. |

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
RULE-SET,https://jovanykoch.github.io/surge-list/lan.list,DIRECT
RULE-SET,https://jovanykoch.github.io/surge-list/openai.list,PROXY
RULE-SET,https://jovanykoch.github.io/surge-list/apple.list,DIRECT
RULE-SET,https://jovanykoch.github.io/surge-list/icloud.list,DIRECT
RULE-SET,https://jovanykoch.github.io/surge-list/edu.list,PROXY
RULE-SET,https://jovanykoch.github.io/surge-list/adblock.list,REJECT
RULE-SET,https://jovanykoch.github.io/surge-list/cn.list,DIRECT
RULE-SET,https://jovanykoch.github.io/surge-list/telegram.list,PROXY
RULE-SET,https://jovanykoch.github.io/surge-list/proxy.list,PROXY
GEOIP,CN,DIRECT
FINAL,DIRECT
```

Example policy groups:

```ini
[Proxy Group]
PROXY = select, HK, JP, SG, US, DIRECT
```

## Notes

- The built-in `Proxy` group in `surge-cn.conf` is intentionally minimal. Add your own proxy nodes, subscriptions, or external policy groups before using it as a complete profile.
- The default fallback rule is `FINAL,DIRECT`. Change it to `FINAL,Proxy` if you want unknown traffic to use the proxy by default.
- Rules are optimized for practical personal usage and may change over time.
- Review all rules before using them in a production or shared environment.

## Disclaimer

This repository is provided for personal learning and configuration reference only. Use it at your own discretion and comply with all applicable laws, regulations, service terms, and network policies in your region.
