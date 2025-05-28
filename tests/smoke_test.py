import jericho

def test_jericho_imports():
    print("[OK] Jericho imported successfully")

def test_zork_boots():
    try:
        env = jericho.FrotzEnv('zork1.z5')  # Ensure this file is in the right place
        obs, reward, done, info = env.reset()
        print("[OK] Zork launched. First observation:")
        print(obs[:120] + "...")
    except FileNotFoundError:
        print("[FAIL] zork1.z5 not found. Please make sure it's available in the working directory.")
        exit(1)
    except Exception as e:
        print(f"[FAIL] Unexpected error launching Zork: {e}")
        exit(1)

if __name__ == "__main__":
    test_jericho_imports()
    test_zork_boots()