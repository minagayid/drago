import argparse
import sys


def build(brief: str) -> dict:
    """Run the full DRAGO build pipeline."""
    try:
        from agents.orchestrator import Orchestrator
        result = Orchestrator().run(brief)
        return result
    except Exception as e:
        # ponytail: stub until agents are implemented; keep CLI runnable
        return {
            "status": "not_implemented",
            "brief": brief,
            "error": f"{type(e).__name__}: {e}",
        }


def main(argv=None):
    argv = argv or sys.argv[1:]
    parser = argparse.ArgumentParser(prog="drago")
    sub = parser.add_subparsers(dest="command")

    build_parser = sub.add_parser("build")
    build_parser.add_argument("--brief", required=True)

    args = parser.parse_args(argv)
    if args.command == "build":
        result = build(args.brief)
        print(result)
    else:
        parser.print_help()
        raise SystemExit(1)


if __name__ == "__main__":
    main()
