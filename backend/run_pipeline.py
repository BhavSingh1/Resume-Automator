# run_pipeline.py
import sys
import traceback
from .app.pipelines.application_pipelines import run_application_pipeline


def main():
    try:
        print("🚀 Starting application pipeline...\n")
        run_application_pipeline()
        print("\n✅ Pipeline completed successfully")

    except KeyboardInterrupt:
        print("\n⛔ Pipeline interrupted by user")
        sys.exit(130)

    except Exception as e:
        print("\n❌ Pipeline failed")
        print(f"Error: {e}\n")
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
