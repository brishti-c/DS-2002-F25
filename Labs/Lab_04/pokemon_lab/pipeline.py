#!/usr/bin/env python3

import sys
import update_portfolio
import generate_summary


# -----------------------------
# Function 1: run_production_pipeline
# -----------------------------
def run_production_pipeline():
    # Starting message
    print("Starting full production pipeline...", file=sys.stderr)

    # ETL Step
    print("Running ETL process (update_portfolio)...", file=sys.stderr)
    update_portfolio.main()

    # Reporting Step
    print("Running reporting process (generate_summary)...", file=sys.stderr)
    generate_summary.main()

    # Completion message
    print("Production pipeline completed successfully.", file=sys.stderr)


# -----------------------------
# Main Block
# -----------------------------
if __name__ == "__main__":
    run_production_pipeline()
