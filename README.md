# DRAGO - Distributed Reasoning Agent for Generative Operations

AI website engineering platform. Builds production-ready sites using theme/plugin ecosystems instead of generating thousands of lines of code.

## Mission

Turn "I need a dental clinic website" into: site architecture, theme selection, plugin mapping, hosting config, security hardening, SEO setup — without writing custom PHP/CSS unless unavoidable.

## Architecture

7-layer multi-agent system:
- Requirement Agent: business → required features
- Site Architect: pages, navigation, user journeys
- Theme Agent: theme scoring & selection
- Plugin Agent: requirement → vetted plugin mapping
- Deployment Agent: DNS, SSL, hosting, staging
- SEO Agent: schema, keywords, metadata, sitemap
- Security Agent: firewall, malware scan, backups, login protection

## Run

```bash
python drago.py --help
python drago.py build --brief "Dental clinic website"
```

## Code

```python
from agents.orchestrator import Orchestrator
from agents.deploy import SiteDeployer

plan = Orchestrator().run("Dental clinic website")
deploy = SiteDeployer(plan)
result = deploy.apply()
```

## Stack

- Python 3.11+
- Dependencies: see requirements.txt
