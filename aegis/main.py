import os
from dotenv import load_dotenv

load_dotenv()


def main():
    print("=" * 50)
    print("Aegis - All Weather Portfolio Agent")
    print("=" * 50)
    print(f"KIS API: {'configured' if os.getenv('KIS_APP_KEY') else 'not configured'}")
    print(f"DB connection: {os.getenv('DB_HOST', 'localhost')}:{os.getenv('DB_PORT', '5432')}")
    print("=" * 50)


if __name__ == "__main__":
    main()
