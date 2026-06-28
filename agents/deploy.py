from __future__ import annotations


class SiteDeployer:
    def __init__(self, plan: dict):
        self.plan = plan

    def apply(self) -> dict:
        # ponytail: one-step deploy stub; real flow needs hosting credentials and env
        return {
            "status": "ok",
            "action": "deploy",
            "plan": self.plan,
        }
